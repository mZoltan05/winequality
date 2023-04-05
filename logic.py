from abc import ABC, abstractmethod

class AbstractLogic(ABC):
    @abstractmethod
    def convert_list_to_dict(self):
        pass

class Logic(AbstractLogic):
    def convert_list_to_dict(self):
        pass