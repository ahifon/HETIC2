from flask import Flask, request
from json import loads
import numpy as np
from sklearn.linear_model import LinearRegression

with open('model.json', 'r') as f:
  content = f.read()
  model = loads(content)

predictor = LinearRegression(n_jobs=-1)
predictor.coef_ = np.array(model)
predictor.intercept_ = np.array([0])

app = Flask(__name__)

@app.route('/')
def hello_world():
    params = request.args.get('input') # "10,20,30"
    parameters = params.split(",")
    
    X = [[
      int(parameters[0]),
      int(parameters[1]),
      int(parameters[2])
    ]]
    outcome = predictor.predict(X=X)
    return str(outcome)


if __name__ == "__main__":
  app.run()