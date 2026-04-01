import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("--- Day 16: NumPy Basics ---")
arr = np.array([10, 20, 30, 40, 50])
print(f"NumPy Array: {arr}")
print(f"Array Mean: {np.mean(arr)}, Array Sum: {np.sum(arr)}\n")

print("--- Day 17 & 18: Pandas & Mini Project 4 (Data Analysis) ---")
# Create a simple dataset and save to CSV
data = {
    'Name': ['Ali', 'Ayesha', 'Bilal', 'Zara', 'Omer'],
    'Age': [21, 22, 20, 23, 21],
    'AI_Score': [85, 92, 78, 88, 95]
}
df = pd.DataFrame(data)
df.to_csv('students_data.csv', index=False)
print(" Dataset saved to 'students_data.csv'")

# Read the CSV and analyze
df_read = pd.read_csv('students_data.csv')
print("\nDataset Preview:")
print(df_read.head())
print(f"\nAverage AI Score for the class: {df_read['AI_Score'].mean()}\n")

print("--- Day 19 & 20: Matplotlib & Mini Project 5 (Visualizations) ---")
print(" NOTE: Close each graph window to make the next one appear!")

# 1. Line Chart
plt.plot(df_read['Name'], df_read['AI_Score'], marker='o', color='blue')
plt.title('AI Scores (Line Chart)')
plt.xlabel('Students')
plt.ylabel('Scores')
plt.show() # TAKE SCREENSHOT 1

# 2. Bar Chart
plt.bar(df_read['Name'], df_read['Age'], color='orange')
plt.title('Student Ages (Bar Chart)')
plt.xlabel('Students')
plt.ylabel('Age')
plt.show() # TAKE SCREENSHOT 2

# 3. Pie Chart
plt.pie(df_read['AI_Score'], labels=df_read['Name'], autopct='%1.1f%%', colors=['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0'])
plt.title('AI Score Distribution (Pie Chart)')
plt.show() # TAKE SCREENSHOT 3