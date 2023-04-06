import pandas as pd
from sklearn.model_selection import train_test_split

class DataPreparer:
    def __init__(self, input_arguments: dict):
        self._input_arguments = input_arguments
        self.prepared_data = self.__get_prepared_data()
        self.save_result = {'save_result': self.__get_save_result(), 'path': self.__get_result_location()}

    def __get_prepared_data(self):
        if 'datasource_location' in self._input_arguments.keys():
            df = pd.read_csv(self._input_arguments['datasource_location'] + 'winequality.csv')
        else:
            df = pd.read_csv('winequality.csv')
        
        if 'features' in self._input_arguments.keys():
            X = df[self._input_arguments['features']]
        else:
            X = df.drop(columns='quality')

        y = df['quality']
        if 'test_data_proportion' in self._input_arguments.keys():
            return train_test_split(X, y, test_size= self._input_arguments['test_data_proportion'] , random_state= 1)
        return train_test_split(X, y, test_size= 0.2 , random_state= 1) 
        
    def __get_result_location(self):
        if 'save_result_location' in self._input_arguments.keys():
            return self._input_arguments['save_result_location']
        return ''
    
    def __get_save_result(self):
        if 'save_result' in self._input_arguments.keys():
            return self._input_arguments['save_result'].lower() == 'true'
        return False