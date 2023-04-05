import pandas as pd 
from sklearn.svm import SVR
from argument_handler import InputArguments


inputArguments = InputArguments()

print(inputArguments.arguments)

df = pd.read_csv('winequality.csv')
X = df.drop(columns='quality')
y = df['quality']

asd1 = 'degree'
asd2 = 3

model = SVR(**{asd1:asd2}) # 1 az 1be mehet bele a model_arguments
model.fit(X, y)
predictions = model.predict(X)
print()
print(predictions)
print()
