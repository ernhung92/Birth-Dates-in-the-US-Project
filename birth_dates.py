
# coding: utf-8

# In[4]:


data = open("births.csv",'r').read()
print(data)


# In[5]:


data_list = data.split('\n')
data_list


# In[6]:


final_list = []
for row in data_list:
    comma_list = row.split(',')
    final_list.append(comma_list)
final_list


# In[7]:


day_counts = dict()
no_header_data_list = final_list[1:len(final_list)]
for row in no_header_data_list:
    day_of_week = row[3]
    births = int(row[4])
    
    if day_of_week in day_counts:
        day_counts[day_of_week] += 1
    else:
        day_counts[day_of_week] = 1

day_counts

