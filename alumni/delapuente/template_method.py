

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
        yield from self._do_walk()

    def _do_walk(self, dirname):
        self._check_walkable(dirname)
        items = self._get_items(dirname)
        dirs = self._filter_walkables(items)

        if not dirs:
            yield items

        else:
            yield items
            for dir in dirs:
                yield self.walk(dir)

    def join(self, *parts):
        return  '/'.join(parts)

    def _check_walkable(self, dirname):
        is_folder = self._api(dirname) == 'folder'
        if not is_folder:
            raise ValueError('the path must be a folder')

    def _get_items(self, dirname):
        return self._api.get_items(dirname)

    def _filter_walkables(self, items):
        return filter(lambda i: self._api.item_type(i) == 'directory', items)