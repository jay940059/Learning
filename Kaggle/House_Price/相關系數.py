#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
x = np.random.randint(0,100,10)
y = 5*x
z = np.random.randint(0,100,10)
dataframe = pd.DataFrame({'x':x,'y':y,'z':z})


# 創建數據

# In[3]:


dataframe


# In[5]:


import matplotlib.pyplot as plt
import seaborn as sns
df = dataframe.corr() #計算相關係數
plt.subplots(figsize=(10,10)) #設置長寬尺寸大小
sns.heatmap(df, annot = True, vmax=1, square=True, cmap="Blues")
#1.資料 2.是否輸出熱力圖數值大小 3.最大值顯示 4.變成正方形 5.要甚麼顏色
plt.show()

