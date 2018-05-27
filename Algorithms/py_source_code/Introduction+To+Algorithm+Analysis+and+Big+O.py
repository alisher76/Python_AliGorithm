
# coding: utf-8

# # Introduction to Algorithm Analysis and Big O
# ---
# ###### Why analyze algorithms?
# Before we begin, let's clarify what an algorthim is. An algorithm is simply a procedure or formula for solving a problem. Some problems are famous enough that the algorithms have names, as well as some procedures being common enough that the algorithm associated with it also has a name. So now we have good question we need to answer:
# 
# How do analyze algorithms and how can we compare algorithms against each other?
# 
# Imagine if you and a friend both came up with functions to sum the numbers from 0 to N. How would you compare the functions and algorithms within the functions? Let's say you both cam up with these two seperate functions:
# 
# 

# In[5]:


# First function (Note the use of xrange since this is in Python 2)
def sum1(n):
    '''
    Take an input of n and return the sum of the numbers from 0 to n
    '''
    final_sum = 0
    for x in range(n+1): 
        final_sum += x
    
    return final_sum


# In[6]:


sum1(10)


# In[7]:


def sum2(n):
    """
    Take an input of n and return the sum of the numbers from 0 to n
    """
    return (n*(n+1))/2


# In[8]:


sum2(10)


# In[9]:


get_ipython().magic('timeit sum1(10)')


# In[10]:


get_ipython().magic('timeit sum2(10)')


# You'll notice both functions have the same result, but completely different algorithms. You'll note that the first function iteratively adds the numbers, while the second function makes use of:
# 
# # ∑i=0ni=n(n+1)2
# 
# So how can we objectively compare the algorithms? We could compare the amount of space they take in memory or we could also compare how much time it takes each function to run. We can use the built in %timeit magic function in jupyter to compare the time of the functions. The %timeit magic in Jupyter Notebooks will repeat the loop iteration a certain number of times and take the best result.
