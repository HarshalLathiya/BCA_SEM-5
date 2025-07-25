name = input("Enter student name: ")
rollno = input("Enter roll number: ")
j2ee = int(input("Enter J2EE marks: "))
python = int(input("Enter Python marks: "))
cs = int(input("Enter CS marks: "))

total = j2ee + python + cs
percentage = total / 3

print("\n--- Student Report ---")
print("Name:", name)
print("Roll No:", rollno)
print("Total Marks:", total)
print("Percentage:", percentage, "%")
