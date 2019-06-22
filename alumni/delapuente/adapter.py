import os.path
import os

class FileSystem:

    def stat(self, item):
        return os.stat(item)

    def walk(self, dirname):
        return os.walk(dirname)

    def join(self, *parts):
        return os.path.join(*parts)


class DriveAPI:

    def get_items(self, path):
        ...

    def item_type(self, item):
        ...


class DriveFileSystem:

    def __init__(self):
        self._api = DriveAPI()


    def stat(self, item):
        return self._api.item_type(item)

    def walk(self, dirname):
        is_folder = self._api(dirname) == 'folder'
        if not is_folder:
            raise ValueError('the path must be a folder')

        while True:
            items = self._api.get_items(dirname)
            yield items
            dirs = self._getdirs(items)
            for dirname in dirs:


        return os.walk(dirname)

    def join(self, *parts):
        return  '/'.join(parts)