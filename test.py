def calculator():
  n = int(input("How many operations? "))
  lst = []
  lst.append((input("First Number? ")))  
  for i in range(n):
      operation = input("Operation (+ - * / **): ")
      if operation in "+-*/**":
        number = (input("Next Number? ")) 
        lst.append(number)
        expr = operation.join(map(str, lst[-2:]))    
        lst = [expr]
      else:
        print("Try Again")
        operation = input("Operation (+ - * /): ")

  print("Result:", eval(lst[0]))

while True:
  try:
      calculator()
  except Exception as e:
      print("Error:", e)
      print("Try Again")