class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def create_link_list():       
    head = ListNode(-1)
    ln = head
    for i in [1,2,3]:
        ln.next = ListNode(i)
        ln = ln.next
    del ln
    return head.next