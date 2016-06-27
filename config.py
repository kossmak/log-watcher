#!/usr/bin/env python
# -*- coding: utf-8 -*-

cfg = {
    'logfile': '/tmp/test.log',
    'workers': [
        {
            'name': 'w01',
            'class': 'Worker01',
            'watch': '/tmp/t01.log'
        },
        {
            'name': 'w02',
            # FIXME: по pep8 названия пакетов и модулей д/б с маленькой буквы
            # а название класса с большой, ага
            # тогда можно разделить параметр 'class' на module_path и class_name
            'class': 'Workers.Worker02',
            'watch': '/tmp/t02.log'
        },
        {
            'name': 'w03',
            'class': 'Workers.Worker02',
            'watch': '/tmp/t03.log'
        },
    ]
}
