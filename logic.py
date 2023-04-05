from abc import ABC, abstractmethod

class AbstractLogic(ABC):
    @abstractmethod
    def convert_list_to_dict(self, list_to_be_converted : list):
        pass

class Logic(AbstractLogic):
    def convert_list_to_dict(self, list_to_be_converted : list):
        new_dict = {list_to_be_converted[i]: list_to_be_converted[i+1] for i in range(0, len(list_to_be_converted), 2)}
        return new_dict
