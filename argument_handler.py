import argparse
from logic import AbstractLogic

class InputArguments:

    def __init__(self, logic : AbstractLogic):
        self.__logic = logic
        self.arguments = self._get_input_arguments()

    def _get_input_arguments(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--features','-f', nargs='*',help='Features for model training, separated by whitespace. For example: citric_acid residual_sugar chlorides')
        parser.add_argument('--model_arguments','-a', nargs='*',help='Arguments of the model, separated by whitespace. For example: kernel rbf degree 3')

        parser.add_argument('--datasource_location','-d', type=str, help='Relative path of the datasource')
        parser.add_argument('--result_location','-r', type=str, help='Relative path where the result will be saved')
        parser.add_argument('--test_data_proportion','-t', type=float, help='It should be between 0.0 and 1.0 and represent the proportion of the dataset to include in the test split')

        arguments = {}
        for key,value in parser.parse_args()._get_kwargs():
            if value != None:
                arguments[key] = value

        if 'model_arguments' in arguments.keys():
            #['kernel', 'tbf', 'degree', '3', 'shrinking', 'True'] -> {'kernel': 'tbf', 'degree': 3,'shrinking': True}           
            arguments['model_arguments'] = self.__logic.convert_list_to_dict( arguments['model_arguments'] )

        return arguments