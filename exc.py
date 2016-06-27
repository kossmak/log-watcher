class AppError(Exception):
    message = 'An error occurred'

    def __init__(self, message=None, *args, **kw):
        super(AppError, self).__init__(*args, **kw)
        if message is not None:
            self.message = message
        elif args:
            self.message = args[0]


class PluginError(AppError):
    message = 'Plugin error'


class PluginImportingError(PluginError):
    pass


class PluginUnexpectedError(PluginError):
    pass


class PluginClassNameError(PluginError):
    pass
