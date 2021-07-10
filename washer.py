#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Abstraction Example


# In[55]:


class Washer:
    def __init__(self):
        self.name = """Model: Washer v1.0,\nDescription: This class allows to model
        a washer machine.\nAuthor: Norberto Moreno V."""
    
    def __str__(self):
        return self.name
    
    # User interface
    def wash(self, temperature):
        #self.temperature = temperature
        self._fill_tank(temperature)
        self._adding_soap()
        self._washing()
        self._spyn_dry()
    
    # Private Methods
    def _fill_tank(self, temperature):
        print('Filling the tank with water at: {}°'.format(temperature))
    
    def _adding_soap(self):
        print('Adding soap!')
    
    def _washing(self):
        print('Washing...')
    
    def _spyn_dry(self, speed=3600):
        print('Spyning dry at {} rpm´s'.format(speed))


# In[56]:


my_washer = Washer()


# In[57]:


print(my_washer)


# In[58]:


my_washer.wash(65.4)


# In[ ]:





# In[ ]:




