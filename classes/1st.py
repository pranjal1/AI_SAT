import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cross_validation import train_test_split
from sklearn import linear_model, preprocessing

data = pd.read_csv('house_data.csv')

