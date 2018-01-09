def square(num):
    print( num**2)
def cube(num):
    print(num**3)

print("Select 1 for squaring \n 2 for cubing")
user=input("Enter choice: ")

choice = {
    "1": square,
    "2":cube
}
num =int(input("enter the number:"))

try:
    choice[user](num)

except ValueError:
    print("Enter valid integer")

else:
    print("calculation successful.")