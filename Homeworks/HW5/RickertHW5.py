class Node:

    def __init__(self, _value=None, _next=None):
        self.value = _value
        self.next = _next

    def __str__(self):
        return str(self.value)

class LinkedList():

    def __init__(self, value):
        self.head = Node(value)
        self.latest = self.head
        self.size = 1
        self.rev = None

    def length(self):
        return self.size
# This is as efficient as possible at O(1) because it only returns without
# needing to perform calculations dependent on the length of the list

    def addNode(self, new_value):
        if type(new_value) is not int:
            print "Please enter an integer"
        if Node(new_value).value is not None:
            new_node = Node(new_value)
            newone = self.head
            while newone.next != None:
                newone = newone.next
            newone.next
            self.size += 1
            return "Node added to list"

# This is also complex at O(1) because adding a new Node doesn't increase in
# complexity with the number of Nodes already added
    def addNodeAfter(self, new_node, after_node):
        if type(new_node) is not int:
            print "Need integer"
        else:
            Node(new_node).next = Node(after_node).next
            Node(after_node).next = Node(new_node)
            self.size += 1
            return "Node Added"

# This is complex at O(n) because it has to iterate through the Nodes in order
# to find the Node to add after, which takes up to n iterations


    def addNodeBefore(self, new_value, before_Node):
        if type(before_Node) is not int:
            print "Please enter an integer as your before Node"
        if Node(new_value).value is not None:
            if before_Node == 1:
                move_after = self.head
                self.head = Node(new_value)
                self.head.next = move_after
                self.size += 1
            else:
                self.addNodeAfter(new_value, before_Node - 1)
                self.size += 1
            return "Added new Node before Node %s." %before_Node
# This has the same complexity as the previous function O(n), because it just
# uses that same function


    def removeNode(self, Node_to_remove):
        if type(Node_to_remove) is not int:
            print "Please enter an integer as the Node number"
        if Node_to_remove == 1:
            self.head = self.head.next
            self.size -= 1
        else:
            count = 1
            check = self.head
            while count != Node_to_remove:
                count += 1
                check = check.next
            while check != None:
                check = check.next
            check = None
            self.size -= 1
            return "Node Removed"

# This is also complex at O(n) because it uses iterative processes. Removing those
# would be the way to create more efficiency.


    def removeNodesByValue(self, value):
        if type(value) is not int:
            print "Please enter an integer."
        count = 1
        node = self.head
        while node.value != value and node.next != None:
            count += 1
            node = node.next
        if count == self.length() and Node.value != Value:
            return "Removed all Nodes with the value %s" % value
        else:
            self.removeNode(count)
            self.size -= 1
            return "Node removed!"
# This is complex at O(n^2) because you have to iterate over n Nodes n times

    def findNodeBefore(self, before_node):
        check = self.head
        while check.next != before_node:
            check = check.next
        return check

    def reverse(self):
        check = self.head
        while check.next != None:
            check = check.next
        new_head = check
        while check != self.head:
            check.next = self.findNodeBefore(check)
            check = check.next
        self.head.next = None
        self.head = new_head
        print self
# This is complex at O(n!) because you have to iterate over the entire list and
# create a new link in each iteration, thus requiring n! calculations
    def __str__(self):
        lists = "%s" %self.head
        h = self.head
        while 'next' in dir(h.next):
            lists += ",%s" %(h.next)
            h=h.next
        return lists
