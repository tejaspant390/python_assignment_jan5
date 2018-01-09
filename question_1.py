def divide(num):
    print(100/num)

num2 = int(input("Enter the number you want to divide 100 with:"))

try:
    divide(num2)

except:
    print("Zero Division is not allowed.")
else:
    print("The division is successful")

finally:
    divide(100)