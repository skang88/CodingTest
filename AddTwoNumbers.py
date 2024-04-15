# Add Two numbers

## 1. Linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

## 2. Basic calculation
class LinkedList:
  def __init__(self):
    self.head = None

  def append(self, val):
    if not self.head:
      self.head = ListNode(val)
      return
    curr = self.head
    while curr.next:
      curr = curr.next
    curr.next = ListNode(val)
    
  def print_list(self):
    curr = self.head
    while curr: 
      print(curr.val, end=" ")
      curr = curr.next
    print()


def merge_two_list(l1, l2):
  dummy = ListNode()
  curr = dummy
  
  while l1 and l2:
    if l1.val < l2.val:
      curr.next = l1
      l1 = l1.next
    else:
      curr.next = l2
      l2 = l2.next
    curr = curr.next
    
  curr.next = l1 or l2
  
  return dummy.next

  
print("hi")
      
# Sample Data
# List 1: 1 -> 2 -> 4
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

print(l1.val)
print(l1.next.val)
print(l1.next.next.val)

# List 2: 1 -> 3 -> 4
l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)
l2.next.next.next = ListNode(9)
l2.next.next.next.next = ListNode(8)

# merge two list
merged_list = merge_two_list(l1, l2)

# print merged list
while merged_list:
  print(merged_list.val, end=" ")
  merged_list = merged_list.next
  

      
      
      
    



