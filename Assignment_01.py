# 1) Write a python program that takes in a student name, class. It should also take in five subject marks of the students and find the total mark and percentage. Display a result in such a way that their name, class,  and percentage are printed.

name =  input("Enter student name: ")
student_class =  input("Enter student class: ")

sub1 = float (input("Enter marks for Subject 1: "))
sub2 = float (input("Enter marks for Subject 2: "))
sub3 = float (input("Enter marks for Subject 3: "))
sub4 = float (input("Enter marks for Subject 4: "))
sub5 = float (input("Enter marks for Subject 5: "))

total = sub1 + sub2 + sub3 + sub4 + sub5
percentage = (total / 500) * 100

print("\n--- Student Result ---")
print(f"Name      : {name}")
print(f"Class     : {student_class}")
print(f"Total     : {total}")
print(f"Percentage: {percentage:.2f}%")


# 2) Input 2 strings concatinate them and store in another variable. then perform generally used string methods on it like

str1 =  input("Enter first string: ")
str2 =  input("Enter second string: ")

combined = str1 + str2

print("\n--- String Operations ---")
print("Concatenated String:", combined)
print("Length:", len(combined))
print("Uppercase:", combined.upper())
print("Lowercase:", combined.lower())
print("Title Case:", combined.title())

substr =  input("Enter a substring to find: ")
print(f"'{substr}' found at index:", combined.find(substr))

old =  input("Enter a substring to replace: ")
new =  input("Enter a new substring: ")
print("After Replacement:", combined.replace(old, new))

print("String 1:", str1, "String 2:", str2, sep=" & ", end=" ----\n")
