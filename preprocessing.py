#numpy and pandas for data manipulation
import numpy as np
import pandas as pd

#sklearn preprocessing for dealing with categorical variables
from sklearn.preprocessing import LabelEncoder

#File system management
import os


app_train = pd.read_csv('data/application_train.csv')
print(app_train.shape)
app_train.head()
from sklearn.linear_model import LogisticRegression