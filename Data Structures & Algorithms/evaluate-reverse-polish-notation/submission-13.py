class DoublyLinkedList:
    def __init__(self, val, next=None,prev=None):
        self.val = val
        self.next = next
        self.prev = prev
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        head = DoublyLinkedList(tokens[0])
        curr = head
        for token in tokens:
            curr.next = DoublyLinkedList(token,None,curr)
            curr = curr.next
        
        while head is not None:
            if head.val in "+-*/":
                l = int(head.prev.prev.val)
                r = int(head.prev.val)
                if head.val == '+':
                    res = l + r
                if head.val == '-':
                    res = l - r
                if head.val == '*':
                    res = l * r
                if head.val == '/':
                    res = int(l / r)
                head.val = res
                head.prev = head.prev.prev.prev
            res = int(head.val)
            head = head.next
        return res