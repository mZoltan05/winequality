import pandas as pd 
from sklearn.svm import SVR

from argument_handler import InputArgumentReader
from model_data_preparer import DataPreparer
from logic import Logic


inputArgumentReader = InputArgumentReader(Logic())
X_train, X_test, y_train, y_test = DataPreparer.get_prepared_data(inputArgumentReader.arguments)

if 'model_arguments' in inputArgumentReader.arguments.keys():
    model = SVR(**inputArgumentReader.arguments['model_arguments'])
else:
    model = SVR()
    
model.fit(X_train, y_train)
predictions = model.predict(X_test)
print()
#print(predictions)
print()
