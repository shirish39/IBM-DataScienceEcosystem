#!/usr/bin/env python
# coding: utf-8

# # Exercise 1: Create a Jupyter Notebook

# # Exercise 2: Create markdown cell with title of the notebook

# # DataScienceEcosystem

# # Exercise 3 - Create a markdown cell for an introduction

# In this notebook, Data Science Tools and Ecosystem are summarized.

# ### Objectives:

# •	List popular languages that Data Scientists use.

# •	List commonly used libraries used by Data Scientists.

# •	Comment on Data Science tools.

# # Exercise 4 - Create a markdown cell to list data science languages

# Some of the popular languages that Data Scientists use are:

#     1.Python.
#     2.R.
#     3.SQL.
#     4.Java.
#     5.Julia.
#     6.Scala.
#     7.C/C++.
#     8.JavaScript.
# 	9.Apache Apark
# 	10.Hadoop
#     11.MangoDB
# 

# # Exercise 5 - Create a markdown cell to list data science libraries

# Some of the commonly used libraries used by Data Scientists include:

#     1.NumPy.
# 	2.Pandas.
# 	3.Matplotlib.
# 	4.Scikit-learn.
# 	4.Seaborn
# 	5.SciPy.
# 	6.TensorFlow
# 	7.PyTorch
# 	8.Statsmodels
# 	9.NLTK
# 	10.Scrapy

# # Exercise 6 - Create a markdown cell with a table of Data Science tools

# In[10]:


import pandas as pd

# Create a DataFrame with a single column
Data_Science_Tools = ['python', 'Apache Spark', 'Hadoop', 'SAS']  # Add your values here
df = pd.DataFrame(Data_Science_Tools, columns=['Data Science Tools'])

# Display the DataFrame
print(df)


# # Exercise 7 - Create a markdown cell introducing arithmetic expression examples

# ### Below are a few examples of evaluating arithmetic expressions in Python

# In[13]:


# Addition
result_addition = 2 + 3
print("Addition:", result_addition)
# Result: 5


# In[14]:


# Subtraction
result_subtraction = 12 - 4
print("Subtraction:", result_subtraction)
# Result: 8


# In[15]:


# Multiplication
result_multiplication = 5 * 7
print("Multiplication:", result_multiplication)
# Result: 35


# # Exercise 8 - Create a code cell to multiply and add numbers

# This a simple arithmetic expression to multiply then add integers.

# In[17]:


#This a simple arithmetic expression to multiply then add integers.
(3*4)+5
#Result: 17


# # Exercise 9 - Create a code cell to convert minutes to hours

# This will convert 200 minutes to hours by diving by 60

# In[19]:


#This will convert 200 minutes to hours by diving by 60
minutes_value = 200
hours_result = minutes_value / 60

# Display the result
print(f"{minutes_value} minutes is equal to {hours_result:.2f} hours.")


# # Exercise 10 - Insert a markdown cell to list Objectives

# Below the introduction cell created in Exercise 3, insert a new markdown cell to list the objectives that this notebook covered 
# (i.e. some of the key takeaways from the course). In this new cell start with an introductory line 
# titled: Objectives: in bold font. Then using an unordered list (bullets) indicate 3 to 5 items covered in this notebook, 
# such as List popular languages for Data Science.

# # Exercise 11 - Create a markdown cell to indicate the Author's name

# ## Author

# Shirish Macha
