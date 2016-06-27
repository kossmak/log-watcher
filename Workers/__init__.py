#!/usr/bin/env python
# -*- coding: utf-8 -*-

import multiprocessing as mp


class WorkerBase(mp.Process):
    def __init__(self, info, log_queue, *args, **kw):
        super(WorkerBase, self).__init__(*args, **kw)
        self.name = info['name']
        self.filename = info['watch']
        self.log_queue = log_queue

    def send_message(self, text):
        msg = "{%s} %s" % (self.name, text)
        self.log_queue.put(msg)

    def run(self):
        self.send_message("run method not realized. Exiting.")
