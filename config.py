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