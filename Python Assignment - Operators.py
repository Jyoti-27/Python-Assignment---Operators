#!/usr/bin/env python
# coding: utf-8

# - Q.1 Import a keyword library and print list of keywords along with total number of keywords.

# In[1]:


import keyword
print(keyword.kwlist)
print("Total number of keywords are :", len(keyword.kwlist)) 


# - Q.2. In Markdown State, Copy Python keywords image from Google Images and Paste it in your notebook

# ![image.png](attachment:image.png)

# - Q.3 Create two strings a and b with any integer values stored in it and perform Addition, Multiplication, Subtraction and a2   +b2

# In[4]:


a = 9
b = 5

print(a + b) # Addition
print(a * b) # Multiplication
print(a - b) # Subtraction
print(a ** 2 + b ** 2) # a2 + b2


# - Q.4 Use Boolean operators (==, !=, >, >=, <, <= ) , between a and b and Display output

# In[7]:


a = 25
b = 39
print(a == b, a != b, a > b, a >= b, a < b, a <= b)


# - Q.5 Create two strings x and y with any integer values stored in it and perform bitwise operations (&,^, | ,>>,<<)
# 

# In[9]:


x = 11
y = 22
print(x & y, x ^ y, x | y, x >> y, x << y)





