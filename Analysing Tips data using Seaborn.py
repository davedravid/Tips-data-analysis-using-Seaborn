import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset('tips')

plt.figure(figsize=(8, 6))
sns.barplot(data=data, x='day', y='total_bill', palette='Blues_d', errorbar=None)
plt.title('Average Total Bill by Day', fontsize=16)
plt.xlabel('Day', fontsize=12)
plt.ylabel('Average Total Bill ($)', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

plt.figure(figsize=(8, 6))
sns.scatterplot(data=data, x='total_bill', y='tip', hue='day', style='time', s=100, palette='deep')
plt.title('Total Bill vs Tip by Day', fontsize=16)
plt.xlabel('Total Bill ($)', fontsize=12)
plt.ylabel('Tip ($)', fontsize=12)
plt.legend(title='Day')
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 6))
sns.boxplot(data=data, x='time', y='total_bill', hue='time', palette='Set2', dodge=False)
plt.title('Distribution of Total Bill by Time of Day', fontsize=16)
plt.xlabel('Time of Day', fontsize=12)
plt.ylabel('Total Bill ($)', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
