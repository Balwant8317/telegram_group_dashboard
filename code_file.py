import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Example: Group Growth
plt.figure(figsize=(10, 5))
plt.plot(group_growth)
plt.xlabel("Days")
plt.ylabel("Number of New Members")
plt.title("Group Growth")
plt.savefig('static/group_growth.png') 
plt.close()

# Example: Active Members
plt.figure(figsize=(10, 5))
plt.plot(active_members)
plt.xlabel("Days")
plt.ylabel("Percentage of Active Members")
plt.title("Active Members")
plt.savefig('static/active_members.png')
plt.close()