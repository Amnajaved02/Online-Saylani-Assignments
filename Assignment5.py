def factorial(num):
  assert num>0,"only positive numbers"
  factorial=1
  for i in range(1,num+1): 
    factorial = factorial * i 
  return factorial
user=int(input("Enter the number: "))
print(factorial(user))

def case(string):
  up=0
  low=0
  for x in string:
    if x.isupper():
      upper+=1
    elif x.islower():
      lower+=1
  return up,"letters are capital", low,"letters are small"

user=input("Enter string: ")
print(case(user))

def even(lis):
  for x in lis:
    if x %2==0:
      print (x,sep=',')

user=int(input("Enter the number of elements in list: "))
l=[]
while user:
  a=int(input("Enter the number: "))
  l.append(a)
  inp-=1
even(l)

def palindrome(palin):
  palin=palin.lower()
  z = palin[::-1]
  if z == palin:
      print ("This is a palindrome")
  else:
      print ("Not a palindrome")
user=input("Enter string: ")
palindrome(user)

def prime(num):
  if num > 1:  
   for i in range(2,num):  
       if (num % i) == 0:  
           print(num,"is not a prime number")  
           print(i,"times",num//i,"is",num)  
           break  
   else:  
       print(num,"is a prime number")  
          
  else:  
    print(num,"is not a prime number")
user=int(input("Enter the number: "))
print(prime(user))

def shop_list(*args):
  print (args)
shop_list("glasses","maggie","facewash","kiwi")
