import random

from sqlalchemy import true
random.seed(113)

# Инициализация и заполение массива рандомными числами
A = []
for i in range(10):
    A.append(random.randint(1, 50))
A.sort()
print("Исходный массив", A)


class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def height(root):
    if root is None:
        return 0
    else:
        # Compute the height of left and right subtree
        l_height = height(root.left)
        r_height = height(root.right)
        # Find the greater one, and return it
        if l_height > r_height:
            return l_height+1
        else:
            return r_height+1


def search(root, value):
    # node is empty
    if root is None:
        return False
    # if element is equal to the element to be searched
    elif root.data == value:
        print(True)
        return True
    # element to be searched is less than the current node
    elif root.data > value:
        return search(root.left, value)
    # element to be searched is greater than the current node
    else:
        return search(root.right, value)




def searchAtGivenLevel(root, level, search_elem):
    if root is None:
        return
    if level == 1:
        search(root, search_elem)
        # print(root.data, end=',')
    elif level > 1:
        searchAtGivenLevel(root.left, level-1, search_elem)
        searchAtGivenLevel(root.right, level-1, search_elem)


      


def search_level_order(root, search_elem):

    h = height(root)
    for i in range(1, h+1):
        searchAtGivenLevel(root, i, search_elem)


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        mid = nums[len(nums)//2]
        root = TreeNode(mid)
        root.left = self.sortedArrayToBST(nums[:len(nums)//2])
        root.right = self.sortedArrayToBST(nums[len(nums)//2 + 1:])
        return root


nums = A
ob1 = Solution()
bst = ob1.sortedArrayToBST(nums)
print("Найти число: ", end=' ')
search_elem = int(input())
search_level_order(bst, search_elem)
