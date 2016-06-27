#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Queue
import importlib
import logging
import multiprocessing as mp
import pprint
import time

from config import cfg
import exc

log = logging.getLogger(__name__)

LOG_LEVEL = logging.DEBUG
MAIN_LOOP_SLEEP_TIME = 0.2


def init_logging():
    # https://docs.python.org/2/library/logging.html#logrecord-attributes
    formatter = logging.Formatter('[%(asctime)s] - %(name)s - %(levelname)s\n'
                                  '... by %(pathname)s:%(lineno)s `%(funcName)s()`:\n\n'
                                  '%(message)s\n'
                                  '------------\n')
    console = logging.StreamHandler()
    console.setFormatter(formatter)
    log.addHandler(console)
    log.setLevel(LOG_LEVEL)

init_logging()


def get_worker_class(name):
    try:
        # импортироваться повторно не будут: инфа 100%
        module = importlib.import_module(name)
    except ImportError as err:
        msg = str(err)  # просто не нашёлся модуль по указанному пути
        log.error(msg)
        # практика показывает, что райзить нужно только специализированные уникальные эксепшины,
        # которые однозначно адресуют строку в программе
        raise exc.PluginImportingError(msg)
    except Exception as err:
        # непрогнозируемые ошибки пишем подробнее для отладки
        log.exception('Unexcpected error during import {}'.format(name))
        raise exc.PluginUnexpectedError(str(err))

    try:
        # а здесь можно было завести строгое соглашение:
        # "имя класса-плагина-воркера" для импорта всегда одинаково
        # тогда можно будет обойтись без getattr
        class_name = name.rsplit('.', 1)[-1]
        worker_class = getattr(module, class_name)
    except AttributeError as e:
        msg = "can't load class [{}]: {}".format(name, e.message)
        log.error(msg)
        raise exc.PluginClassNameError(msg)
    return worker_class


def all_workers_are_dead(workers):
    for i in reversed(range(len(workers))):
        if not workers[i].is_alive():
            del(workers[i])
    return workers


def process_queue(queue):
    log.debug('entering into queue')
    try:
        while not queue.empty():
            msg = queue.get_nowait()
            log.debug('\t {}'.format(msg))
    except Queue.Empty:
        log.warn('!!!!!!!!! Queue.Empty')


def init_workers(queue):
    workers = []
    for worker_info in cfg['workers']:
        try:
            worker_class = get_worker_class(worker_info['class'])
        except exc.PluginError:
            log.error('Worker class {} skipped'.format(worker_info['class']))
            continue
        except KeyError:
            log.error('Invalid configuration:\n{}'.format(pprint.pformat(worker_info)))
            continue

        try:
            worker = worker_class(worker_info, queue)
            workers.append(worker)
            worker.start()
        except:
            log.exception('Something wrong with worker')
            continue
    return workers


def main():
    log.info('begin')

    queue = mp.Queue(0)
    workers = init_workers(queue)

    while not all_workers_are_dead(workers):
        log.debug('workers alive: {}'.format(len(workers)))
        process_queue(queue)
        time.sleep(MAIN_LOOP_SLEEP_TIME)

    log.info('end')


if __name__ == '__main__':
    main()
