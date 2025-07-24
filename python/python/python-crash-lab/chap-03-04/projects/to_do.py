tasks = []
print("Welcome to your To-Do List App!\nYour tasks:\n[Your list is currently empty.]")

tasks.append("python-crash-course")
tasks.append("Discrete maths")
tasks.append("grokking algorithms")
tasks.append("git pro")
tasks.append("Html and css by Duckett")
tasks.append("c absolute beginners")

print()

counter = 1
print("Your tasks for today:")
for task in tasks:
    print(str(counter) + "." + task)
    counter = counter + 1

print()
print(f"we done with {tasks.pop(1)}")

print()
print("Updated tasks:")

tasks.insert(1, "Number Theory")
counters = 1

for task in tasks:
    print(str(counters) + "." + task)
    counters = counters + 1
print("===========================================================")
print("\nThank you for using your To-Do List App.\nKeep building your habits!")