import timeit
def BINSEARCH(List,value):
    print(List)
    for i in range (len(List)):
        for j in range(i+1,len(List)):
            if List[i]>List[j]:
                List[i],List[j]=List[j],List[i]
                unsort=True
    if unsort ==True:
        print("you entered an unordered List")
    print("sorted List",List)
    start=0
    end=len(List)-1
    mid=int((start+end)/2)
    while start <=end and List[mid]!=value:
        if value < List[mid]:
            end=mid-1
        else:
            start=mid+1
        mid=int((start+end)/2)
    if List[mid]==value:
        pos=mid
        print("'",pos,"' is the index of the value=",value)
    else:
        pos=0
    if pos ==0:
        for q in List:
            if q>=List[mid]:
                List.insert(List.index(q),value)
                print("updated List",List)
                break
L=[]
x=int(input("declare no of elements in a list"))
while x:
    last=x
    y=int(input("enter element in the list"))
    L.append(y)
    x-=1
find=int(input("put a value you want to find in list"))
BINSEARCH(L,find)
print(timeit.timeit())
