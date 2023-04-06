import argparse
from logic import AbstractLogic

class InputArgumentReader:
    def __init__(self, logic : AbstractLogic):
        self.__logic = logic
        self.arguments = self._get_input_arguments()

    def _get_input_arguments(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--features','-f', nargs='*',help='Features for model training, separated by whitespace. E.g. citric_acid residual_sugar chlorides')
        parser.add_argument('--model_arguments','-a', nargs='*',help='Arguments of the model, separated by whitespace. E.g. kernel rbf degree 3')

        parser.add_argument('--datasource_location','-d', type=str, help='Relative path of the datasource. E.g. ..\data\ ')
        parser.add_argument('--test_data_proportion','-t', type=float, help='It should be between 0.0 and 1.0 and represent the proportion of the dataset to include in the test split')
        parser.add_argument('--save_result_location','-sl', type=str, help='Relative path where the result will be saved. E.g. result\ ')
        parser.add_argument('--save_result','-s', type=str, help='If true,then the result will be saved.')

        arguments = {}
        for key,value in parser.parse_args()._get_kwargs():
            if value != None:
                arguments[key] = value

        return self.__format_arguments(arguments)
    
    def __format_arguments(self, input_arguments : dict):
        formatted_arguments = input_arguments
        if 'model_arguments' in input_arguments.keys():
            #['kernel', 'tbf', 'degree', '3', 'shrinking', 'True'] -> {'kernel': 'tbf', 'degree': 3,'shrinking': True}           
            formatted_arguments['model_arguments'] = self.__logic.convert_list_to_dict( input_arguments['model_arguments'] )

        if 'features' in input_arguments.keys():
            #['citric_acid', 'residual_sugar', 'chlorides'] -> ['citric acid', 'residual sugar', 'chlorides']
            formatted_arguments['features'] = list(map(lambda s: s.replace('_',' '), formatted_arguments['features']))

        return formatted_arguments
