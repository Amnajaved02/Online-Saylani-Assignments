'''1. Write a program which takes 5 inputs from user for different subject’s
marks, total it and generate mark sheet using grades ?'''

subjects=['Maths','Physics','Chemistry','Islamiat','English']
marks=[]
total_marks=0
for i in range(0,5):
    mark=int(input('Enter marks for {}:'.format(subjects[i])))
    total_marks+=mark
    marks.append(mark)
for j in range(0,5):
    print(subjects[j],":",marks[j])
print("total marks : {}".format(total_marks))

'''2. Write a program which take input from user and identify that the given
number is even or odd?'''
    
number=int(input('Enter a number:'))
if number%2==0:
    print('{} is even'.format(number))
else:
    print('{} is odd'.format(number))

'''3.Write a program which print the length of the list'''
subjects=['Maths','Physics','Chemistry','Islamiat','English']
print(len(subjects))

subjects=['Maths','Physics','Chemistry','Islamiat','English']
length=0
for i in subjects:
    length+=1
print(length)

'''4.Write a Python program to sum all the numeric items in a list?'''

nums=[1,2,3,4,5]
print(sum(nums))
total_sum=0
for i in nums:
    total_sum+=nums[i-1]
print(total_sum)

'''5.Write a Python program to get the largest number from a numeric list.'''

list1 = [10, 20, 4, 45, 99] 
list1.sort() 
print("Largest element is:", list1[-1]) 

'''6.write a program that prints out all the elements of the list that are
less than 5.'''
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in a:
    if i<5:
        print(i)
