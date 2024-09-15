#exceptions
#ImportError: an import fails;

#IndexError: a list is indexed with an out-of-range number;

#NameError: an unknown variable is used
#SyntaxError: the code can't be parsed properly; 

#TypeError: a function is called on a value of an inappropriate type;

#ValueError: a function is called on a value of the correct type, but with an inappropriate value.

try:
    variable = 10
    print(variable + "hello")
    print(variable / 2)
except ZeroDivisionError:
    print("Divided by zero")
except (ValueError, TypeError):
    print("Error occurred")
    
    
try:
   print("Hello")
   print(1 / 0)
except ZeroDivisionError:
   print("Divided by zero")
finally:
   print("This code will run no matter what")

#You can raise exceptions by using the raise statement.  
#Exceptions can be raised with arguments that give detail about them.

name = "123"

raise NameError("Invalid name!")
try:

   num = 5 / 0

except:

   print("An error occurred")

   raise
