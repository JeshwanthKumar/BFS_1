"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
#Time_Complexity: O(n)
#Space_Complexity: O(n)

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:    #Edge case
            return []   #If the root is None then return an empty array
        result = [] #Initialize result as an empty array
        q = deque() #Initialize q using deque
        q.append(root)  #Append the root into the q
        
        while q:    #Continue untill the q is empty
            size = len(q)   #Size is the length of the  q
            level = []  #Initialize level as an empty array
            
            for _ in range(size):   #Continue till the size
                node = q.popleft()  #Pop the first element in the q using popleft and store it in node
                level.append(node.val)  #Append node.val in level
                
                for child in node.children: #For every children in the root append every child into the q
                    q.append(child)
                    
            result.append(level)    #Append the level into result
            
        return result   #Return result