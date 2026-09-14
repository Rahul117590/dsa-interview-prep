# height of the binary tree max depth(Max_depth)--


# class Node: #define the class of that node
#     def __init__(self,key): # define construction
#         self.key=key
#         self.right=None
#         self.left=None
    
# def height_tree(a):
#     if (a==None):
#         return 0
#     else:
#         ldepth=height_tree(a.left)
#         rdepth=height_tree(a.right)

#         return 1 + max(ldepth,rdepth)


# # now define the node for the tree
# root=Node(1)
# root.left=Node(2)
# root.right=Node(4)
# root.left.right=Node(5)
# root.left.left=Node(5)
# root.right.right=Node(8)
# root.right.right.left=Node(9)

    
# print('max depth of tree is :',height_tree(root))







# min depth of the tree

# class Node:
#     def __init__(self,key): # this is the constructure of the data
#         self.key=key
#         self.right=None
#         self.left=None

# def min_depth(a):
#     if a is None:
#         return 0
#     else:
#         ldepth=min_depth(a.left)
#         rdepth=min_depth(a.right)
        
#         return 1 + min(ldepth,rdepth)

# # now define the node
# root=Node(4)
# root.left=Node(3)
# root.right=Node(6)
# root.right.left=Node(12)
# root.right.right=Node(43)
# root.right.right.left=Node(33)
# root.right.right.right=Node(40) 
# print('the minimun depth of the tree is :',min_depth(root))







# find the minimun difference between two elements of array
# arr=[5,32,45,4,12,18,25]  ans-1
'''
sort the array first
'''
# def min_diff_element(arr):
#     arr=sorted(arr)
#     size=len(arr)
#     min_diff=999*999
#     for i in range(0,size-1):
#         if(arr[i+1]-arr[i]<min_diff):
#             min_diff=arr[i+1]-arr[i]
#         return min_diff

# arr=[47,38,38,2,49,394,24]
# print(min_diff_element(arr))
