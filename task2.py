#! python3
"""
###### Task 2
Ask the user to enter in the prices of 5 items in dollars.cents (eg 10.34).  Find the total value of all items and then calculate the total price including 5% GST and 7% PST

Sample:
Enter in price of item #1: 10.25
Enter in price of item #2: 11.45
Enter in price of item #3: 13.85
Enter in price of item #4: 9.25
Enter in price of item #5: 10.25
Your subtotal is 55.05
Your GST is 2.75
Your PST is 3.85
Your total is 61.65
"""


total = 0.0
print("You will enter in 5 numbers and this program will find the sum.")
print()
for i in range(5):
    num = i + 1
    strNum = input(f"Enter in number {num}>")
    intNum=float(strNum)
    total=total+intNum
print(f"The total of your numbers is {total}")

GST=total*0.05
GST=round(GST,2)
print(f"Your GST is{GST}")
PST=total*0.07
PST=round(PST,2)
print(f"Your PST is {PST}")
subtotal=total+GST+PST
subtotal=round(subtotal,2)
print(f"Your total is {subtotal}")
