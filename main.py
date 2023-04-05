import pandas as pd 
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split

from argument_handler import InputArguments
from logic import Logic


inputArguments = InputArguments(Logic())
print(inputArguments.arguments)


df = pd.read_csv('winequality.csv')
X = df.drop(columns='quality')
y = df['quality']

test_data_proportion = inputArguments.arguments['test_data_proportion'] if 0 < inputArguments.arguments['test_data_proportion'] < 1 else 0.2 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= test_data_proportion , random_state= 1)

asd1 = 'degree'
asd2 = 3

model = SVR(**{asd1:asd2}) # 1 az 1be mehet bele a model_arguments
model.fit(X, y)
predictions = model.predict(X)
print()
print(predictions)
print()
