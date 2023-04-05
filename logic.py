from abc import ABC, abstractmethod
import re

class AbstractLogic(ABC):
    @abstractmethod
    def convert_list_to_dict(self, list_to_be_converted : list):
        pass
    
    @abstractmethod
    def parse_string_to_type(self,str_to_be_parsed : str):
        pass

class Logic(AbstractLogic):
    def convert_list_to_dict(self, list_to_be_converted : list):
        new_dict = {list_to_be_converted[i]: list_to_be_converted[i+1] for i in range(0, len(list_to_be_converted), 2)}
        for key in new_dict.keys():
            new_dict[key] = self.parse_string_to_type(new_dict[key]) 
            
        return new_dict

    def parse_string_to_type(self, value : str):
        if re.match(r"^\d+$", value):
            return int(value)
        elif re.match(r"^\d+\.\d+$", value):
            return float(value)
        elif value.lower() in ("true", "false"):
            return bool(value)
        else:
            return value
    