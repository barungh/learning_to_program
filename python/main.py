divident = int(input("Enter the divident : "))
divider = int(input("Enter the divisor : "))

quotient = 0
remainder = 0

while divident > divider:
    quotient = quotient + 1
    divident = divident - divider
    remainder = divident

print(quotient, remainder)
