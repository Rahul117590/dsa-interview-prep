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
list_to_dict()



    



        
        

