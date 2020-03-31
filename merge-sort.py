#!/usr/bin/env python
# coding: utf-8

# In[24]:


def merge(arrA, arrB):
    i=0
    j=0
    k=0
    l=[]
#     for k in range(len(arrA)+len(arrB)):
    while k< len(arrA)+len(arrB):
     
        if i==len(arrA):
            l.extend(arrB[j:])
            k=k+len(arrB[j:])
        elif j==len(arrB):
            l.extend(arrA[i:])
            k=k+len(arrA[i:])
        elif arrA[i]<arrB[j]:
            l.append(arrA[i])
            k=k+1
            i=i+1
        else:
            l.append(arrB[j])
            k=k+1
            j=j+1
    return l


# In[25]:


merge([2,3,4],[1,2,3])


# In[36]:


def merge_sortify (arr):
    if len(arr)<2:
        return arr
    else:
        mid=int(len(arr)/2)
        m1=merge_sortify(arr[:mid])
        m2=merge_sortify(arr[mid:])
        return merge (m1,m2)


# In[37]:


merge_sortify([12,3,41,87,32,76,54,23,21])


# In[38]:


merge_sortify([9,2])


# In[ ]:





# In[ ]:




