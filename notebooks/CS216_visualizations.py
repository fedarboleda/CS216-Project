#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[3]:


match=pd.read_csv("Fifa_world_cup_matches.csv")
match


# In[4]:


import pandas as pd
import matplotlib.pyplot as plt
match['possession team1'] = match['possession team1'].str.rstrip('%').astype('float') / 100.0
match['possession team2'] = match['possession team2'].str.rstrip('%').astype('float') / 100.0
descriptive_stats = match.describe()
avg_goals_team1 = match.groupby('team1')['number of goals team1'].mean().sort_values(ascending=False)
avg_goals_team2 = match.groupby('team2')['number of goals team2'].mean().sort_values(ascending=False)
avg_goals = pd.concat([avg_goals_team1, avg_goals_team2], axis=1).mean(axis=1).sort_values(ascending=False)
avg_goals.plot(kind='bar', figsize=(10, 5), color='skyblue')
plt.title('Average Goals Scored by Teams')
plt.ylabel('Average Goals')
plt.xlabel('Teams')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 5))
plt.scatter(match['possession team1'], match['number of goals team1'], color='blue', label='Team 1')
plt.scatter(match['possession team2'], match['number of goals team2'], color='red', label='Team 2')
plt.title('Relationship between Possession and Number of Goals')
plt.xlabel('Possession (%)')
plt.ylabel('Number of Goals')
plt.legend()
plt.tight_layout()
plt.show()


# In[ ]:




