def helloManh(num_rep):
  """
  This function prints out "hello Manh" num_rep times
  """
  try:
    num_rep = int(num_rep)
    for i in range(num_rep):
      print("hello Manh")
  except:
    print("something is wrong with num_rep")
    print("but hello Manh :)")

    
num_rep = input("enter a number: ")
helloManh(num_rep)

# i am just a normal person
