'''Assignment 3

1) Practise
	Dictionary
	Tuple
	Set

2) Write a function for basic math operations like add multiply substract divide and use this in your program, take 2 number input from user.

3) Write a program to check Palindrome Number

The Number  which is equal to reverse number know as Palindrome Number.
 For example Number 12321 is a Palindrome Number, because 12321 is equal to its reverse Number 12321.

Steps for checking Palindrome number


1. Find reverse of the given number.
2. Compare that number with the reverse number.
3. If number and its reverse is equal then it is a Palindrome Number otherwise not.


'''




# ----------------------------------------------------------ANS:-1-----------------------------------------------------





def calculate(a, b, oper):
    if oper in ["add", "+"]:
        return a + b
    elif oper in ["subtract", "-"]:
        return a - b
    elif oper in ["multiply", "*"]:
        return a * b
    elif oper in ["divide", "/"]:
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero"
    else:
        return "Invalid operation"

x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

op = input("-------Enter Operation --------\n1). Add or +\n2). Subtract or -\n3). Multiply or *\n4). Divide or /\n: ")

result = calculate(x, y, op)
print("Result:", result)






# --------------------------------------------------------------- ANS:- 2---------------------------------------------------------------------





num = int(input("Enter a number: "))
reverse = int(str(num)[::-1])

if num == reverse:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")
