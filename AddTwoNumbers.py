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
# List 1: 2 -> 4 -> 3
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

print(l1.val)
print(l1.next.val)
print(l1.next.next.val)

# List 2: 5 -> 6 -> 4
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

# merge two list
merged_list = merge_two_list(l1, l2)

# print merged list
while merged_list:
  print(merged_list.val, end=" ")
  merged_list = merged_list.next
  
## 3. Add Two numbers

# If there's two node, first add two number and if over ten, give to another node the ten and remain is in the result node. 
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.


def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    
    result = ListNode(0)
    result_tail = result
    carry = 0
            
    while l1 or l2 or carry:            
        val1  = (l1.val if l1 else 0)
        val2  = (l2.val if l2 else 0)
        carry, out = divmod(val1+val2 + carry, 10)    
                  
        result_tail.next = ListNode(out)
        result_tail = result_tail.next                      
        
        l1 = (l1.next if l1 else None)
        l2 = (l2.next if l2 else None)
           
    return result.next


solution = addTwoNumbers(l1, l2)

solution.val 
solution.next.val 
solution.next.next.val

