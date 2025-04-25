import pickle
import numpy as np
from sklearn.datasets import load_iris

with open("app/model/model.pkl", "rb") as f:
    model = pickle.load(f)

# Label map
iris = load_iris()
target_names = iris.target_names

def predict(input_data: list):
    arr = np.array(input_data).reshape(1, -1)
    pred_idx = model.predict(arr)[0]
    return target_names[pred_idx]
