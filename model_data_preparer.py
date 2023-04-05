import pandas as pd
from sklearn.model_selection import train_test_split

class DataPreparer:
    @staticmethod
    def get_prepared_data(input_arguments: dict):
        
        if 'datasource_location' in input_arguments.keys():
            df = pd.read_csv(input_arguments['datasource_location'] + 'winequality.csv')
        else:
            df = pd.read_csv('winequality.csv')
        
        if 'features' in input_arguments.keys():
            X = df[input_arguments['features']]
        else:
            X = df.drop(columns='quality')
    
        y = df['quality']
        test_data_proportion = input_arguments['test_data_proportion'] if 0 < input_arguments['test_data_proportion'] < 1 else 0.2 

        return train_test_split(X, y, test_size= test_data_proportion , random_state= 1)
        
