from json import loads, dumps
from sklearn.linear_model import LinearRegression

with open('/data/input.data.json') as f:
  content = f.read()
  TRAIN_INPUT = loads(content)

with open('/data/output.data.json') as f:
  content = f.read()
  TRAIN_OUTPUT = loads(content)

predictor = LinearRegression(n_jobs=-1)

predictor.fit(X=TRAIN_INPUT, y=TRAIN_OUTPUT)

with open('model.json', 'w') as f:
  f.write(dumps(predictor.coef_.tolist()))