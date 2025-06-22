''' 
Assignment 2 

1) Do practise of the session

2) In your last program where you find the total and percentage of a student's marks of 5 subject, find the grade of the student using conditional statement. Eg. grade 'A' if percentage is greator than or equals to 60, 'B' for  percentage is greator than or equals to 50 and less than 60,  'C' for  percentage is greator than or equals to 40 and less than 50,  'D' for  percentage is greator than or equals to 33 and less than 40, otherwise 'Fail'


3) Input a number from user and find its factorial using for loop


4) Create a billing program using list. Program should have options to 
1. Create Bill
2. Display Item Price and total bill amount
3. Display Total
4. Exit


5) Write a  Python program to find the smallest number in a list.
Write a  Python program to find the second greatest number in a list.
Write a  Python program to find the second smallest number in a list.

'''






# ans 1:-
'''
name = input("Enter student name: ")
student_class = input("Enter student class: ")

sub1 = float(input("Enter marks for Subject 1: "))
sub2 = float(input("Enter marks for Subject 2: "))
sub3 = float(input("Enter marks for Subject 3: "))
sub4 = float(input("Enter marks for Subject 4: "))
sub5 = float(input("Enter marks for Subject 5: "))

total = sub1 + sub2 + sub3 + sub4 + sub5
percentage = (total / 500) * 100

if percentage >= 60:
    grade = 'A'
elif percentage >= 50:
    grade = 'B'
elif percentage >= 40:
    grade = 'C'
elif percentage >= 33:
    grade = 'D'
else:
    grade = 'Fail'

print("\n--- Student Result ---")
print(f"Name      : {name}")
print(f"Class     : {student_class}")
print(f"Total     : {total}")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade     : {grade}")




# Ans :-2


num = int(input("Enter a number: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print("Factorial is:", fact)

  
  
  
  
# Ans:-3



items = []
prices = []

while True:
    print("\n1. Create Bill\n2. Display Item Price and Total\n3. Display Total\n4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter item name: ")
        price = float(input("Enter item price: "))
        items.append(name)
        prices.append(price)
    elif choice == '2':
        total = 0
        for i in range(len(items)):
            print(f"{items[i]}: ₹{prices[i]}")
            total += prices[i]
        print("Total Bill Amount: ₹", total)
    elif choice == '3':
        print("Total: ₹", sum(prices))
    elif choice == '4':
        break
    else:
        print("Invalid choice")


'''

# Ans:-3 


'''n = [10, 5, 3, 8, 2, 15, 7]'''
n = int(input("Enter the list"))
for i in range(1,11):
  print(n)
smallest = min(n)
print("Smallest number:", smallest)

sorted_num = sorted(n)
print(sorted_num)

second_greatest = sorted_num[-2]
print("Second greatest number:", second_greatest)

second_smallest = sorted_num[1]
print("Second smallest number:", second_smallest)
