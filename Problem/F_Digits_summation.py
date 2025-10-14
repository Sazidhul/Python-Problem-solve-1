#Given two numbers N and M. Print the summation of their last digits
#input: Only one line containing two numbers 
#Output: Print the answer of the problem.
#Example:input: 13 12 Output: 5
#Note: First Example: last digit in the first number is 3 and last digit in the second number is 2.
#So the answer is: (3 + 2 = 5)
inp = input()

numbers = inp.split()

N = int(numbers[0]) #13
M = int(numbers[1]) #12

last_digit_of_N = N % 10
last_digit_of_M = M % 10

sum = last_digit_of_N + last_digit_of_M

print(sum)


