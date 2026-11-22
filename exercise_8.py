m1 = float(input("Enter scored marks of subject 1: "))
m2 = float(input("Enter scored marks of subject 2: "))
m3 = float(input("Enter scored marks of subject 3: "))
total_marks = float(input("Enter all subjects total marks: "))

total = m1 + m2 + m3
average = (total / total_marks) * 100

print("Total Marks scored =", total)
print("Perccentage Marks =", average)