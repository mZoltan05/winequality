import pandas as pd
from sklearn.model_selection import train_test_split

class DataPreparer:
    @staticmethod
    def get_prepared_data(input_arguments: dict):

        df = pd.read_csv('winequality.csv')
        X = df.drop(columns='quality')
        y = df['quality']

        test_data_proportion = input_arguments['test_data_proportion'] if 0 < input_arguments['test_data_proportion'] < 1 else 0.2 
        return train_test_split(X, y, test_size= test_data_proportion , random_state= 1)
        
