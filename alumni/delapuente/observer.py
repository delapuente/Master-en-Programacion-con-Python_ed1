

class Observable:

    def __init__(self):
        self._observers = []

    def add_observer(self, handle):
        self._observers.append(handle)

    def click(self):
        self._notify()

    def _notify(self):
        for handle in self._observers:
            handle()

    def get_state(self):
        return self._clicked_events


class LazyObserver:
    def __init__(self, observable):
        self._observers = []
        self._observable = observable

    def add_observer(self, handle):
        self._observers.append(handle)

    def update(self):
        self._notify()

    def _notify(self):
        state = self._observable.get_state()
        for handle in self._observers:
            handle(state)


def log_click():
    print('click!')

def open_window():
    print('window open')

def do_business():
    print('cosas Nazis, Peter')

o = Observable()
o.add_observer(log_click)
o.add_observer(open_window)
o.add_observer(do_business)

o.click()

class Profile:

    ...




