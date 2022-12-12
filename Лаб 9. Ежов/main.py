import pandas as pd
import random
import matplotlib.pyplot as plt
import math as math

passengers = pd.read_csv('./titanic.csv')
#print(passengers)

a_s = passengers[(passengers["Age"] < 40) & (passengers["Age"] > 25) & (passengers["Sex"] == 'male')]
#print(a_s)
a_s = passengers[(passengers["Survived"] == 1) & (passengers["Pclass"] == 1) | (passengers["Sex"] == 'female') & (passengers["Age"] < 25)]
#print(a_s)

