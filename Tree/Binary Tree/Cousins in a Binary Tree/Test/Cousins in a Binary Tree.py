# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isCousins(root: TreeNode, x: int, y: int) -> bool:
    if x == 1 or y == 1:
        return False

    data = []
    # Function to  print level order traversal of tree 
    def printLevelOrder(root): 
        h = height(root) 
        for i in range(1, h+1): 
            printGivenLevel(root, i)
        return data


    # Print nodes at a given level 
    def printGivenLevel(root , level): 
        if root is None: 
            data.append(root)
            #return
        elif level == 1: 
            data.append(root.val)
        elif level > 1 : 
            printGivenLevel(root.left , level-1) 
            printGivenLevel(root.right , level-1) 


    """ Compute the height of a tree--the number of nodes 
        along the longest path from the root node down to 
        the farthest leaf node 
    """
    def height(node): 
        if node is None: 
            return 0 
        else : 
            # Compute the height of each subtree  
            lheight = height(node.left) 
            rheight = height(node.right) 

            #Use the larger one 
            if lheight > rheight : 
                return lheight+1
            else: 
                return rheight+1

    data = [0]
    data.append(printLevelOrder(root))
    print(data)
    
    x_index = data.index(x)
    y_index = data.index(y)
    print(x_index)
    print(y_index)
    
    x_level = int((x_index)**(1/2))
    y_level = int((y_index)**(1/2))
    print(x_level)
    print(y_level)
    
    if x_level != y_level:
        return False
    else:
        return x_index//2 != y_index//2
        
        '''
        data.reverse()
        print(data)

        i = 0
        power = 1
        levels = [['-1' for i in range(1)] for j in range(len(data))]
        while i<len(data):
            print(data[i])
            if data[i] == x:
                x_loc = i
            if data[i] == y:
                y_loc = i
            if not levels[power-1]:
                levels[power-1] = i
            else:
                if levels[power-1][0] == '-1':
                    levels[power-1][0] = i
                else:
                    levels[power-1].append(i)
            if i == power:
                power = power*2
            i+=1
        print(levels)
        for level in levels:
            if x_loc in levels and y_loc in levels:
                return True
            elif x_loc in levels and y_loc not in levels:
                break
            elif y_loc in levels and x_loc not in levels:
                break
            else:
                pass
        return False
        '''

'''
#Test case #1: 
#Input: root = [1,2,3,4], x = 4, y = 3
#Output: false
tree_4 = TreeNode(4)
tree_3 = TreeNode(3)
tree_2 = TreeNode(2,tree_4)
tree_1 = TreeNode(1,tree_2,tree_3)
print(isCousins(tree_1,4,3))
'''
'''
#Test case #2: 
#Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
#Output: true
tree_5 = TreeNode(5)
tree_4 = TreeNode(4)
tree_3 = TreeNode(3,None,tree_5)
tree_2 = TreeNode(2,None,tree_4)
tree_1 = TreeNode(1,tree_2,tree_3)
print(isCousins(tree_1,5,4))
'''
'''
#Test case #3: 
#Input: root = [1,2,3,null,4], x = 2, y = 3
#Output: false
tree_4 = TreeNode(4)
tree_3 = TreeNode(3)
tree_2 = TreeNode(2,None,tree_4)
tree_1 = TreeNode(1,tree_2,tree_3)
print(isCousins(tree_1,2,3))
'''
'''
#Patched with check to see if root
#Test case #90:
#Input: root = [1,2,3,null,null,null,4,5], x = 1, y = 2
#output: false
tree_5 = TreeNode(5)
tree_4 = TreeNode(4)
tree_3 = TreeNode(3,None,tree_4)
tree_2 = TreeNode(2)
tree_1 = TreeNode(1,tree_2,tree_3)
print(isCousins(tree_1,1,2))
'''
'''
#Test case 96/104
#Input: root = [1,2,null,3,5,4,null,6], x = 5, y = 4
#Output: false
'''
tree_6 = TreeNode(6)
tree_5 = TreeNode(5)
tree_4 = TreeNode(4)
tree_3 = TreeNode(3,None,tree_4)
tree_2 = TreeNode(2)
tree_1 = TreeNode(1,tree_2)
print(isCousins(tree_1,1,2))
