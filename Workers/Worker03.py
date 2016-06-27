#!/usr/bin/env python
# -*- coding: utf-8 -*-

from . import WorkerBase


class Worker03(WorkerBase):
    # def __init__(self, info, log_queue, *args, **kw):
    #     super(Worker03, self).__init__(info, log_queue, *args, **kw)
    #     pass  # пустое переопределение конструктора можно опустить

    def run(self):
        for i in xrange(3):
            self.send_message("message num ")
