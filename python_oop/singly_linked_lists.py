class Node(object):
    def __init__(self,value):
        self.value = value
        self.next = None

class SinglyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

list = SinglyLinkedList()
list.head = Node('Alice')
list.head.next = Node('Chad')
list.head.next.next = Node('Debra')

# something close to this should be utilized for all of the above problems
runner = list.head
print runner.value
print runner.next
print runner.next.value
print runner.next.next
print runner.next.next.value
print runner.next.next.next
while runner.next != None:
    print runner.value
    runner = runner.next
print runner.value

def printAllVals():
