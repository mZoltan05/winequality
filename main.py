import pandas as pd 
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split

from argument_handler import InputArgumentReader
from model_data_preparer import DataPreparer
from logic import Logic


inputArgumentReader = InputArgumentReader(Logic())
X_train, X_test, y_train, y_test = DataPreparer.get_prepared_data(inputArgumentReader.arguments)






asd1 = 'degree'
asd2 = 3

model = SVR(**{asd1:asd2}) # 1 az 1be mehet bele a model_arguments
model.fit(X_train, y_train)
predictions = model.predict(X_test)
print()
print(predictions)
print()
