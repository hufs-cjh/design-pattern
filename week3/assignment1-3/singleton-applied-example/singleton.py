from abc import ABCMeta


# metaclass for Singleton
class SingletonABCMeta(ABCMeta):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:

            # separate long line
            cls._instances[cls]\
                = super(SingletonABCMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
