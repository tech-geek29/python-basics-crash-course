
# coding: utf-8

# # Python Crash Course Exercises 
# 


# ## Exercises
# 
# Answer the questions or complete the tasks outlined in bold below, use the specific method described if applicable.

# ** What is 7 to the power of 4?**

# In[1]:

7**4


# ** Split this string:**
# 
#     s = "Hi there Sam!"
#     
# **into a list. **

# In[3]:

list("Hi there samm!")


# In[4]:

'Hi there dad!'.split(" ")


# ** Given the variables:**
# 
#     planet = "Earth"
#     diameter = 12742
# 
# ** Use .format() to print the following string: **
# 
#     The diameter of Earth is 12742 kilometers.

# In[1]:

planet = "Earth"
diameter = 12742


# In[2]:

print("The diameter of {} is {} kilometers.".format(planet,diameter))


# ** Given this nested list, use indexing to grab the word "hello" **

# In[6]:

lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]


# In[9]:

lst[3][1][2][0]


# ** Given this nested dictionary grab the word "hello". Be prepared, this will be annoying/tricky **

# In[11]:

d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}


# In[12]:

d['k1'][3]['tricky'][3]['target'][3]


# ** What is the main difference between a tuple and a list? **

# In[23]:

# Tuple is immutable


# ** Create a function that grabs the email website domain from a string in the form: **
# 
#     user@domain.com
#     
# **So for example, passing "user@domain.com" would return: domain.com**

# In[18]:

def domainGet(str):
    return str.split('@')[-1]


# In[19]:

domainGet('user@domain.com')


# ** Create a basic function that returns True if the word 'dog' is contained in the input string. Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization. **

# In[20]:

def findDog(str):
    return 'dog' in str


# In[21]:

findDog('Is there a dog here?')


# ** Create a function that counts the number of times the word "dog" occurs in a string. Again ignore edge cases. **

# In[5]:

def countDog(str):
    lst = str.split()
    count = 0
    for i in lst:
        if 'dog'== i:
            count = count+1
    return count


# In[6]:

countDog('This dog runs faster than the other dog dude!')


# ** Use lambda expressions and the filter() function to filter out words from a list that don't start with the letter 's'. For example:**
# 
#     seq = ['soup','dog','salad','cat','great']
# 
# **should be filtered down to:**
# 
#     ['soup','salad']

# In[8]:

seq = ['soup','dog','salad','cat','great']


# In[9]:

list(filter(lambda str: str[0]=='s', seq))


# ### Final Problem
# **You are driving a little too fast, and a police officer stops you. Write a function
#   to return one of 3 possible results: "No ticket", "Small ticket", or "Big Ticket". 
#   If your speed is 60 or less, the result is "No Ticket". If speed is between 61 
#   and 80 inclusive, the result is "Small Ticket". If speed is 81 or more, the result is "Big    Ticket". Unless it is your birthday (encoded as a boolean value in the parameters of the function) -- on your birthday, your speed can be 5 higher in all 
#   cases. **

# In[13]:

def caught_speeding(speed, is_birthday):
    
    if is_birthday:
        speeding = speed - 5
    else:
        speeding = speed
    
    if speeding > 80:
        return 'Big Ticket'
    elif speeding > 60:
        return 'Small Ticket'
    else:
        return 'No Ticket'


# In[14]:

caught_speeding(81,True)


# In[15]:

caught_speeding(81,False)


# # Great job!
