# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#Time_Complexity: O(n)
#Space_Complexity: O(n)


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:    #Edge case
            return False    #If there is no root return False
        q = deque() #Initialize q using deque
        q.append(root)  #Append the root into the q
        
        while q:    #Continue until the q is empty
            size = len(q)   #Size is the lenght of q
            level = []  #Initialize level as an empty array
            
            for _ in range(size):   #Continue till the size
                node = q.popleft()  #Pop the first element in the q using popleft
                
                if node != None:    #If the node is not equal to None then append the node.val in level and append node.left and node.right into the q
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
                    
                else:   #Else append the node into the q
                    level.append(node)
                   
                
            if not(self.isPalindrome(level)):  #If the level is not palindrome then return False 
                return False
            
        return True #Else return True
                    
    def isPalindrome(self, li): #Palindrome function
        left = 0    #Initialize left as 0
        right = len(li)-1   #Initialize right pointer as lenght of list -1
        
        while left <=right: #Continue till left and right crosses 
            if li[left] != li[right]:   #If the list[left] is not equal to list[right] then return false
                return False
            
            left+=1 #Increment left by 1
            right-=1    #Decrement right by 1
            
        return True #Return True