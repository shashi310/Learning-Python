# 5. **Implement Queue using Stack**: Use Python's stack data structure to implement a queue.
#     - *Input*: enqueue(1), enqueue(2), dequeue(), enqueue(3), dequeue(), dequeue()
#     - *Output*: "1, None, 3, None, None"



class QueueUsingStacks:
    def __init__(self):
        self.stack1 = []  # For enqueue operation
        self.stack2 = []  # For dequeue operation

    def enqueue(self, element):
        """
        Enqueues an element into the queue.
        
        Time Complexity: O(1)
        Space Complexity: O(n), where n is the number of elements in the queue.
        """
        self.stack1.append(element)

    def dequeue(self):
        """
        Dequeues an element from the queue.
        
        Time Complexity: O(n), amortized to O(1)
        Space Complexity: O(1)
        """
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        if self.stack2:
            return self.stack2.pop()
        else:
            return None

# Test the queue implementation
queue = QueueUsingStacks()
result = []

# Enqueue operations
queue.enqueue(1)
queue.enqueue(2)

# Dequeue operation
result.append(queue.dequeue())

# Enqueue operations
queue.enqueue(3)

# Dequeue operations
result.append(queue.dequeue())
result.append(queue.dequeue())

print(", ".join(map(str, result)))  # Output: "1, None, 3, None, None"
