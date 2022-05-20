import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('datasets/shopify_data.csv')

shop_id_data = data.groupby("shop_id")
print(shop_id_data.head())

print(shop_id_data.shop_id.unique())
#for shop_id in data:
#    print(data[shop_id].unique())