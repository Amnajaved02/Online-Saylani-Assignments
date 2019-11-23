val1=int(input("Enter a number:"))
val2=int(input("Enter a number:"))
operand=str(input("Enter operand:"))

if operand=="+":
    result=val1+val2
    print(result)
elif operand=="-":
    result=val1-val2
    print(result)
elif operand=="*":
    result=val1*val2
    print(result)
elif operand=="/":
    result=val1/val2
    print(result)
elif operand=="**":
    result=val1**2
    print(result)

list1=["amna",19,"javed"]
for i in list1:
    if type(i)==int:
        print(i)

dict={}
dict["name"]="amna"
print(dict)

list1=["amna",19,"javed","bla bla","javed","Amna Javed"]
for i in range(0,len(list1)):
    if list1[i] in list1[i+1:]:
        print (list1[i])
    print(list1[i],list1[i+1:])


dict1={'name':'Amna','address':'Maskan','occupation':'student'}
key=input("enter key :")
if key in dict1.keys():
    print("{} already exists".format(key))

    
dict1={1:'Amna',2:6,3:'student'}
sum=0
for i in dict1.keys():
    if type(i)==int:
        print(i)
        sum+=i
        if type(dict1[i])==int:
            print(dict1[i])
            sum+=i
print(sum)
