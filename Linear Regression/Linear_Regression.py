
# coding: utf-8

# In[42]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[43]:


dataset=pd.read_csv('bikedata.csv')
x=dataset.iloc[:,1:2].values
y=dataset.iloc[:,2].values


# In[44]:


from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(x,y)
y_pred=regressor.predict(35)


# In[45]:


plt.scatter(x,y,color='red')
plt.plot(x,regressor.predict(x),color='blue')
plt.title('Linear Regression')
plt.xlabel('Number of hrs spent driving')
plt.ylabel('Risk score')
plt.show()


# In[46]:


y_pred


# In[41]:


dataset

