#! python3

"""
##### Problem 3
Have the user enter an integer that is smaller than 10
Find the sum of the series:
1 + 11 + 111 + 1111 + ....
for the n terms, where the nth term has n number of 1's

input:
int number that is smaller than 10

output:
the sum of the series is xxxx

example:
enter a number: 4
the sum of the series is 1234
"""

i=input("Enter an integer that is smaller than 10:")
i=int(i)

if i>=10:
    print("The number must be smaller than 10.")
else:
    total_sum=0
    term=0
for i in range (1, i+1):
    term = term*10+1
    total_sum+=term
print(f"The sum of the series is {total_sum}")