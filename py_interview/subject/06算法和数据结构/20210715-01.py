"""
链表反转
描述
    输入一个链表，反转链表后，输出新链表的表头。
    示例1
    输入：
    {1,2,3}
    返回值：
    {3,2,1}
"""


def ReverseList(pHead):
    # write code here
    if not pHead:
        return None
    root = None
    while pHead:
        pHead.next, root, pHead = root, pHead, pHead.next
    return root

pHeads = {1,2,3}
print(ReverseList(pHeads))
