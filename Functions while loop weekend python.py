#!/usr/bin/env python
# coding: utf-8

# In[1]:


i=1
while(i<=5):
    print(i)
    i+=1


# In[2]:


i=1
while(i<=5):
    print(i)
    if i==3:
     break
    i+=1


# In[3]:


i=1
while(i<=5):
    i+=1
    if i==3:
     continue
    print(i)


# In[5]:


def funcexample():
    print("This is a sample function")
funcexample()


# In[6]:


def funcexample():
    print("This is a sample function")
print("testing")
funcexample()


# In[8]:


#one argument func
lastname="Krishna"
def funcexample(firstname):
    print(firstname+" "+lastname)
funcexample("Ajay")
    
    


# In[9]:


lastname="Krishna"
def funcexample(firstname):
    print(firstname+" "+lastname)
funcexample("Ajay")
funcexample("Baskar")
funcexample("dev")
    
    


# In[12]:


#Multiple argument func
lastname="Krishna"
def funcexample(firstname,city,phonenum):
    print(firstname+" "+lastname,city,phonenum)
funcexample("Ajay","Mumbai",12345)
funcexample("Baskar","chennai",56789)
funcexample("dev","Bangalore",78547)
    

    


# In[16]:


#Func with formatted string
lastname="Krishna"
def funcexample(firstname,city,phonenum):
    print(f"Hello ,{firstname.title()}"+" "+lastname,f"your city is {city.upper()}",f" and contact number is {phonenum}")
funcexample("ajay","Mumbai",12345)
funcexample("baskar","chennai",56789)
funcexample("dev","Bangalore",78547)
    
    


# In[17]:


lastname="Krishna"
def funcexample(firstname="Ravi",city,phonenum):
    print(f"Hello ,{firstname.title()}"+" "+lastname,f"your city is {city.upper()}",f" and contact number is {phonenum}")
funcexample("ajay","Mumbai",12345)
funcexample("baskar","chennai",56789)
funcexample("dev","Bangalore",78547)
funcexample("Delhi",35567)
    
    


# In[20]:


#Default argument
lastname="Krishna"
def funcexample(firstname="Ravi",city="Delhi",phonenum=35567):
    print(f"Hello ,{firstname.title()}"+" "+lastname,f"your city is {city.upper()}",f" and contact number is {phonenum}")
funcexample("ajay","Mumbai",12345)
funcexample("baskar","chennai",56789)
funcexample("dev","Bangalore",78547)
funcexample()
    
    


# In[21]:


#Positional arguments
def describe_pet(animal_type,pet_name):
    print(f"\n I have a {animal_type}")
    print(f"my {animal_type}'s name is {pet_name.title()}")
describe_pet('Husky','bruno')


# In[22]:


#Positional arguments
def describe_pet(animal_type,pet_name):
    print(f"\n I have a {animal_type}")
    print(f"my {animal_type}'s name is {pet_name.title()}")
describe_pet('Husky','bruno')
describe_pet(pet_name="pinku",animal_type="bomarian")


# In[26]:


#Tuple passed as arguments
def garden(*flower_name):
    print(f" Hi All we have {flower_name.title()} in our garden!")

garden("rose","sunflower","lily","jasmine")


# In[27]:


#Tuple passed as arguments
def garden(*flower_name):
    print(f" Hi All we have {flower_name} in our garden!")

garden("rose","sunflower","lily","jasmine")

