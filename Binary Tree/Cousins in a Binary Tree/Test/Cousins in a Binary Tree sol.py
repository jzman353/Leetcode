def isSibling(root, a , b): 
  
    # Base Case 
    if root is None: 
        return 0
  
    return ((root.left == a and root.right == b) or 
            (root.left == b and root.right == a)or
            isSibling(root.left, a, b) or
            isSibling(root.right, a, b)) 
  
# Recursive function to find level of Node 'ptr' in  
# a binary tree 
def level(root, ptr, lev): 
      
    # Base Case  
    if root is None : 
        return 0 
    if root == ptr:  
        return lev 
  
    # Return level if Node is present in left subtree 
    l = level(root.left, ptr, lev+1) 
    if l != 0: 
        return l 
  
    # Else search in right subtree 
    return level(root.right, ptr, lev+1) 
  
  
# Returns 1 if a and b are cousins, otherwise 0 
def isCousin(root,a, b): 
      
    # 1. The two nodes should be on the same level in  
    # the binary tree 
    # The two nodes should not be siblings(means that  
    # they should not have the smae parent node 
  
    if ((level(root,a,1) == level(root, b, 1)) and 
            not (isSibling(root, a, b))): 
        return 1
    else: 
        return 0

'''
Input: [1,null,2,3,5,4,null,null,null,null,6], 5, 3
Output: false
'''