print("--- Day 8: String Operations ---")
text = "  NexaSecure Tech Internship  "
clean_text = text.strip()
print(f"Original: '{text}'")
print(f"Cleaned & Upper: '{clean_text.upper()}'\n")

print("--- Day 9: File Handling ---")
with open("internship_notes.txt", "w") as file:
    file.write("Learning Python & AI at NexaSecure!")

with open("internship_notes.txt", "r") as file:
    content = file.read()
print(f"File Content: {content}\n")

print("--- Day 10: Loops & List Comprehension ---")
numbers = [1, 2, 3, 4, 5]
squares = [num**2 for num in numbers]
print(f"Original numbers: {numbers}")
print(f"Squared numbers: {squares}\n")