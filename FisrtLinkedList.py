import sqlalchemy

class Node:
    def __init__(self,d,n=None):
        self.data = d
        self.next = n

class LinkedList:
    def __init__(self, r= None):
        self.root =r
        self.size = 0

    def add(self,d):
        if self.root:
            new_node = Node(d,self.root)
            self.root = new_node
        else:
            new_node = Node(d)
            self.root = new_node

    def find(self,d):
        next_node = self.root
        while next_node:
            if next_node.data == d:
                return print('Find :{}'.format(d))
            else:
                next_node = next_node.next
        return print('Value Not find')

    def remove(self,d):
        prev_node = None
        curr_node = self.root
        while curr_node:
            if curr_node.data == d:
                if prev_node:
                    prev_node.next = curr_node.next
                    return print('Value deleted {}'.format(d))
                else:
                    self.root = curr_node.next
                    return print('Value deleted {}'.format(d))
            else:
                prev_node = curr_node
                curr_node = curr_node.next
        return print('Value:{} not find in list'.format(d))

    def display(self):
        new_node = self.root
        while new_node:
            print(new_node.data)
            new_node = new_node.next
    #         this is commented out

    def Merge(self,l2):
        pass

l1=LinkedList()
l1.add(20)
l1.add(10)
#l1.display()
#print(l1.root.data)

l2=LinkedList()
l2.add(40)
l2.add(30)
#l2.display()
#print(l2.root.data)

#passing two list to merge:

def MergeLL(l1,l2):
    # l3 = LinkedList()
    # l1_node = l1.root
    # l2_node = l2.root
    # if l1_node is None:
    #     return l2
    # if l1_node is None:
    #     return l2
    # while l1_node and l2_node:
    #     if l1_node.data<l2_node.data:
    #         l3_node = l1_node
    #         l3_node = l3_node.next
    #         l1_node = l1_node.next
    #     else:
    #         l3_node = l2_node
    #         l3_node = l3_node.next
    #         l2_node = l2_node.next
    #
    # while l1_node:
    #     l3_node = l1_node
    #     l3_node=l3_node.next
    #     l1_node= l1_node.next
    # while l2_node:
    #     l3_node = l2_node
    #     l3_node=l3_node.next
    #     l2_node= l2_node.next
    # return l3
        l3 = LinkedList()
        l1_node = l1.root
        l2_node = l2.root
        if l1_node is None:
            return l2
        if l1_node is None:
            return l2
        while l1_node and l2_node:
            if l1_node.data < l2_node.data:
                l3.add(l1_node.data)
                l1_node = l1_node.next
            else:
                l3.add(l2_node.data)
                l2_node=l2_node.next

        while l1_node:
            l3.add(l1_node.data)
            l1_node = l1_node.next

        while l2_node:
            l3.add(l2_node.data)
            l2_node= l2_node.next
        return l3

l3 = MergeLL(l1,l2)
l1.display()
