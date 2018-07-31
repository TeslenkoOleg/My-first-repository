x= float(input('Enter 1-st number:'))
operation = input("Choose operatin:")
y = float(input('Enter 2-nd number:'))
result = None
def cul():

   if operation == "+":
    result = x+y
   elif operation == "-":
    result = x-y
   elif operation == "*":
    result = x*y
   elif operation == "/":
    result = x/y
   else:
    print("Error!!")

   print(result)


cul()



