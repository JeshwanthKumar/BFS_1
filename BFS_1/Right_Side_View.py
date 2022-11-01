# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#Time_Complexity: O(n)
#Space_Complexity: O(n)


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:    #Edge case
            return []   #If not root return empty list
        result = [] #Initialize result to an emoty array
        q = deque() #Initialize q using dequeue
        q.append(root)  #Append the root into the q
        
        while q:    #Continue till the q is empty
            size = len(q)   #Size is length of q
            for _ in range(size):   #Continue till the size
                node = q.popleft()  #Pop the first element in the queue using popleft and store it in node
                
                if node.left:   #If there is a left child then append it to the q
                    q.append(node.left)
                    
                    
                if node.right:  #If there is a right child then append it to the q
                    q.append(node.right)
                    
                    
            result.append(node.val) #Append the node.val into the result which will only append the right sided view of the tree
        return result   #Return result