class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


head = ListNode(0)
curr_node = head

new_node = ListNode(1)
curr_node.next = new_node
curr_node = curr_node.next

curr_node.next = ListNode(2)
curr_node = curr_node.next

curr_node.next = ListNode(3)
curr_node = curr_node.next

curr_node.next = ListNode(4)
curr_node = curr_node.next

# 노드 출력
node = head
while node:
    print(node.val)
    node = node.next

# 노드 탐색 후 삭제
node = head
while node.next:
    if node.next.val == 2:
        next_node = node.next.next
        node.next = next_node
        break
    node = node.next

node = head
while node:
    print(node.val)
    node = node.next
