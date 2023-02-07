from abc import ABCMeta, abstractmethod


class WindowInterface(metaclass=ABCMeta):
    @abstractmethod
    def create_user_interface(self):
        pass


class WindowEntryInterface(metaclass=ABCMeta):
    @abstractmethod
    def get_user_credentials(self):
        pass
