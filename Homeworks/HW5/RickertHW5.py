class Node:

    def __init__(self, _value=None, _next=None):
        self.value = _value
        self.next = _next

    def __str__(self):
        return str(self.value)

class LinkedList():

    def __init__(self, value):
        self.head = self.Node(value)
        self.latest = self.head
        self.size = 1
        self.rev = None

    def length(self):
        return self.size
# This is as efficient as possible at O(1) because it only returns without
# needing to perform calculations dependent on the length of the list

    def addNode(self, new_value):
        if type(new_value) is not int:
            print "PLease enter an integer"
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

	def addNodeAfter(self, new_value, after_node):
		if type(after_node) is not int:
			print "Node number must be an integer value. I'll try and convert it for you by rounding down!"
			try:
				after_node = int(after_node)
			except:
				return "I can only convert floats and numeric strings to integers. Please try again with a valid input type."
		if self.Node(new_value).value is not None:
            while node.next != None:
                tally = 1
                node = self.head
                while tally != after_node:
                    tally += 1
                    node = node.next
                move_after = node.next
                node.next = self.Node(new_value)
                node.next.next = move_after
                self.size += 1
                return 'Added new node after node %d.' % after_node


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
                Node = self.head
                while count != Node_to_remove:
                    count +=1
                    Node = Node.next
                    move_after = Node.next
                    count = 1
                    Node = self.head
                    while count != Node_to_remove - 1:
                        count += 1
                        Node = Node.next
                        Node.next = move_after
        self.size -= 1
        return "Removed Node %s" % Node_to_remove
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
            return "Node removed!"
# This is complex at O(n^2) because you have to iterate over n Nodes n times


    def reverse(self):
        Node = self.head
        new = self.rev
        if Node is None:
            self.head = self.rev
            self.rev = None
            return "Nodes reversed"
        forward_count = 1
        while Node.next is not None:
            forward_count += 1
            Node = Node.next
        if new is None:
            self.rev = Node(Node.value)
        else:
            reverse_count = 1
            while new.next is not None:
                reverse_count += 1
                new = new.next
            new.next = Node(Node.value)
        self.removeNode(forward_count)
        return self.reverse()
# This is complex at O(n!) because you have to iterate over the entire list and
# create a new link in each iteration, thus requiring n! calculations

    def __str__(self):
