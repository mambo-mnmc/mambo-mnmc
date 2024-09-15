while True:
	print("Hi", input("Enter your name using capital letters"))
	print("""please tell me what you want to calculate by indicating to me what you sort of arithmetic operator you want to use.""" 
	print(""" you may use the following to tell me: '+', '-', '/','Modu', and '*'""")
	print(""" to end or finish engaging me, please type 'Stop' """')
	user_input = input("Enter calculation type:  ")

   if user_input == "Stop":
      break
   elif user_input == "+":
      num1 = float(input("Enter a number"))
      num2 = float(input("Enter another number"))
      result = str(num1 + num2)
      print("The answer is " + result)
   elif user_input == "-":
      num1 = float(input("Enter a number"))
      num2 = float(input("Enter another number"))
      result = str(num1 - num2)
      print("The answer is " + result)
   elif user_input == "*":
      num1 = float(input("Enter a number"))
      num2 = float(input("Enter another number"))
      result = str(num1 * num2)
      print("The answer is " + result)
   elif user_input == "/":
   	num1 = float(input("Enter a number"))
   	numb= float(input("Enter another number"))
   	result = num1/numb
   	print("The answer is " + result)
   elif user_input == "Modu":
   	num1 = float(input("Enter a number"))
   	num2 = float(input("Enter another number"))
   	result = str(num1%num2)
   	print("The answer is " + int(result))
   else:
   	print("Unknown input")