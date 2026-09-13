# write a python program to find out the common latters between two strings
# NAINA    REENE

# def common_latter():
#     str1=input('enter the first input string:')
#     str2=input('enter the secong input string:')
#     s1=set(str1)
#     s2=set(str2)
#     result=s1 & s2  # and opertor find out the common latter between that set that are unique 
#     print(result)
  
# common_latter()

# write the python program to count the frequency of words apearing in a string
'''
ex- Sheena loves eating apple and mango. Her sister also loves eating apple and 
mango '''

# def freq_words():
#     str1=input('enter the input string :')
#     l1=str1.split()  # split word it split the whole sentense into the seperated words
#     d1={}

#     for i in l1:
#         if i not in d1.keys():
#             d1[i]=0
#         d1[i]=d1[i]+1

#     print(d1)
# freq_words()

# write the python program to convert two lists into a dicitionary 
#  and also for dictionary to tuple 
'''
list1=['Naina','Kimi','Sheena']
list2=[374838,838483,933839]'''

def list_to_dict():
    keys=['Naina','Kimi','Sheena']
    values=[374838,838483,933839]
    result=dict(zip(keys,values))# zip key word use to map the key to there value 
    print(result)

# def dict_to list():
# def dict_to_tuple():
#     li={'Naina': 374838, 'Kimi': 838483, 'Sheena': 933839}
#     for i in li.items():
#         print(i)

# dict_to_tuple()




# find the missing number no in the array
'''
1,2,4,5,6,7'''
# there are two method to solve this method so 

# summation method  and the xor method 
# def get_missing_summation(a):
#     n=a[-1]
#     sum1=0
#     total=n*(n+1)//2
#     sum1=sum(a)
#     print(total-sum1)
    
# a=[1,2,3,4,5,6,7,9]
# get_missing_summation(a)





# find out pairs with given sum value of an array
'''
arr=[3,5,16,7,14,8,9,18]
sum=17''' #firsted sorted the array  use duble pointer method

def twosum(arr,sum):
    arr.sort()
    left=0
    right=len(arr)-1
    while (left<=right):
        if(arr[left]+arr[right]>sum):
            right=right -1
        elif(arr[left]+arr[right]<sum):
            left=left+ 1
        elif(arr[left]+arr[right]==sum):
            print('value of pair are',arr[left],'&',arr[right])
            left=left +1
            right= right-1
    
arr=[5,7,4,3,9,8,19,21]
sum=17
twosum(arr,sum)











   




    



        
        

