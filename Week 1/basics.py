print("--- Day 2: Variables & Data Types ---")
role = "AI Intern NST"
duration_days = 30
print(f"Role: {role}, Duration: {duration_days} days\n")

print("--- Day 3: Control Flow (If-Else & Loops) ---")
for i in range(1, 4):
    if i % 2 == 0:
        print(f"Task {i} is Even")
    else:
        print(f"Task {i} is Odd")
print()

print("--- Day 4: Functions ---")
def complete_task(task_name):
    return f"Status: {task_name} Completed!"
print(complete_task("Day 4 Task") + "\n")

print("--- Day 5: Lists & Tuples ---")
skills_list = ["Python", "Machine Learning", "Data Science"]
data_tuple = (100, 200, 300)
print(f"List: {skills_list}\nTuple: {data_tuple}\n")

print("--- Day 6: Dictionaries & Sets ---")
info_dict = {"Company": "NexaSecure Tech", "Track": "Python & AI"}
unique_set = {1, 2, 3, 3, 2, 1}
print(f"Dict: {info_dict}\nSet: {unique_set}")