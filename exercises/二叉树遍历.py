"""

"""

# 创建树的节点

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Solution:
    def print_tree(self,root):
        """
        广度遍历  二叉树
        :param root:
        :return:
        """
        if not root:
            return
        cur_list = [root]
        next_list = []
        while cur_list:
            cur_node = cur_list.pop(0)
            print(cur_node.value,end= " ")
            if cur_node.left:
                next_list.append(cur_node.left)
            if cur_node.right:
                next_list.append(cur_node.right)

            if not cur_list:
                cur_list,next_list = next_list,cur_list
    def pre_tree(self,root):
        """
        前序遍历 二叉树
        :param root:
        :return:
        """
        if root is None:
            return
        print(root.value,end=" ")
        self.pre_tree(root.left)
        self.pre_tree(root.right)

    def mid_tree(self,root):
        """
        中序遍历 二叉树
        :param root:
        :return:
        """
        if root is None:
            return
        self.mid_tree(root.left)
        print(root.value,end=" ")
        self.mid_tree(root.right)

    def last_tree(self,root):
        if root is None:
            return
        self.last_tree(root.left)
        self.last_tree(root.right)
        print(root.value,end=" ")



if __name__ == '__main__':
    s = Solution()
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t4 = TreeNode(4)
    t5 = TreeNode(5)
    t6 = TreeNode(6)
    t7 = TreeNode(7)
    t8 = TreeNode(8)
    t9 = TreeNode(9)
    t10 = TreeNode(10)
    # 开始创建树
    t1.left = t2
    t1.right = t3
    t2.left = t4
    t2.right = t5
    t4.left = t8
    t4.right = t9
    t5.left = t10
    t3.left = t6
    t3.right = t7
    t8.next = t9.next = t4
    t10.next = t5
    t4.next = t5.next = t2
    t6.next = t7.next = t3
    t2.next = t3.next = t1
    s.print_tree(t1)
    print()
    s.pre_tree(t1)
    print()
    s.mid_tree(t1)
    print()
    s.last_tree(t1)




