import pandas as pd 
from sklearn.svm import SVR

from argument_handler import InputArgumentReader
from model_data_preparer import DataPreparer
from prediction_display import PredictionDisplay
from logic import Logic


inputArgumentReader = InputArgumentReader(Logic())
dataPreparer = DataPreparer(inputArgumentReader.arguments)

X_train, X_test, y_train, y_test = dataPreparer.prepared_data

if 'model_arguments' in inputArgumentReader.arguments.keys():
    model = SVR(**inputArgumentReader.arguments['model_arguments'])
else:
    model = SVR()


model.fit(X_train, y_train)
predictions = model.predict(X_test)

PredictionDisplay.plot_result(predictions, y_test, dataPreparer.save_result)