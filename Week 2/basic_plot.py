import matplotlib.pyplot as plt

print("--- Day 12: Basic Data Visualization ---")
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
hours_coded = [2, 3, 5, 4, 6]

plt.plot(days, hours_coded, marker='o', color='green', linestyle='dashed')
plt.title('Coding Hours During Internship')
plt.xlabel('Days of the Week')
plt.ylabel('Hours Coded')
plt.grid(True)

print("Opening graph window... close the graph window to end the script.")
plt.show()