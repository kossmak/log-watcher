#!/usr/bin/env python

from config import cfg
import multiprocessing as mp
import Queue
import time
import importlib
import sys

def get_worker_class(name):
    try:
        if name in sys.modules:
            module = sys.modules[name]
        else:
            module = importlib.import_module(name)
        worker_class = getattr(module, name.rsplit('.', 1)[-1])
    except Exception as e:
        raise NameError("can't load class [%s]: %s" % (name, e.message))
    return worker_class

def all_workers_is_dead(workers):
    for i in reversed(range(len(workers))):
        if not workers[i].is_alive():
            del(workers[i])
    return len(workers) == 0

def process_queue(queue):
    try:
        while not queue.empty():
            msg = queue.get_nowait()
            print "\t %s" % msg
    except(Queue.Empty):
        print "!!!!!!!!! Queue.Empty"

def main():
    print "begin"
    queue = mp.Queue(0)
    workers = []
    for worker_info in cfg['workers']:
        worker_class = get_worker_class(worker_info['class'])
        worker = worker_class(worker_info, queue)
        workers.append(worker)
        worker.start()
    while True:
        print "workers alive: %d" % len(workers)
        process_queue(queue)
        if all_workers_is_dead(workers):
            break
        time.sleep(.2)
    print "end"

if __name__ == '__main__':
    main()