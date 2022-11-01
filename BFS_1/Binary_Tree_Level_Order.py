# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#Time_Complexity: O(n)
#Space_Complexity:O(n)


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:    #Edge case
            return []
        q= deque()  #Initialize a queue
        q.append(root)  #Append the root inside queue
        result = [] #Initialize an empty result array

        while q:    #Continue till the queue is empty
            size = len(q)   #Initialize size as length of the queue
            temp = []   #Initialize a temporary array
            
            for _ in range(size):   #Continue till the size
                node = q.popleft()  #Pop the first element in the queue using popleft and store it in node
                temp.append(node.val)   #Append the value of the node into the temp

                if node.left:   #If the there is a left child then append it to the queue
                    q.append(node.left)
                    
                if node.right:  #If there is a right child then append it to the queue
                    q.append(node.right)
                    
            result.append(temp) #Append the temp array into the result array
        return result   #Return the result 