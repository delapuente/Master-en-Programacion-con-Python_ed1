
class FileSystem:
    """
    This is a singleton:

    >>> r = FileSystem()
    >>> s = FileSystem()
    >>> assert r is s
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(FileSystem, *args, **kwargs)

        return cls._instance


if __name__ == '__main__':
    import doctest
    doctest.testmod()
