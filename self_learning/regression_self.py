#this contains code that is filtered down version of what is in jupyter notebook test1
#only necessary codes here, visualization part is in jupyter notebook

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

#this function splits a dataset into training and testing dataset
def split_train_test(data, test_ratio):
    shuffled_indices = np.random.RandomState(42).permutation(len(data))
    test_set_size = int(len(data) * test_ratio)
    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]


#step1: read the csv file
X = pd.read_csv('./datasets/housing/housing.csv')

#step2: perform data visualization like hist plots (look jupyter notebook)

#step3: division into testing and training set (20%~80% split)
#this method is flawed as if the dataset is updated, there will be completely new training and testing data for every update.
#this should be avoided.
#----> train_set, test_set = split_train_test(housing, 0.2)

#so, we use this approach, where everything is already handled
train_set, test_set = train_test_split(housing, test_size=0.2, random_state=42)


