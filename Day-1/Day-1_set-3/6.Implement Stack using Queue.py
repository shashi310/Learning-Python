# 1. **Implement Stack using Queue**: Use Python's queue data structure to implement a stack.
#     - *Input*: push(1), push(2), pop(), push(3), pop(), pop()
#     - *Output*: "1, None, 3, None, None"


from queue import Queue

class StackUsingQueue:
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()

    def push(self, element):
        # Push the element into queue1
        self.queue1.put(element)

    def pop(self):
        # Move all elements except the last one from queue1 to queue2
        while self.queue1.qsize() > 1:
            self.queue2.put(self.queue1.get())

        # Pop the last element from queue1 (which is the top of the stack)
        if not self.queue1.empty():
            popped_element = self.queue1.get()

        # Swap the names of queue1 and queue2
        self.queue1, self.queue2 = self.queue2, self.queue1

        return popped_element if hasattr(self, 'popped_element') else None

# Example usage
stack = StackUsingQueue()
output = []

output.append(stack.pop())  # Output: None

stack.push(1)
stack.push(2)
output.append(stack.pop())  # Output: 2

stack.push(3)
output.append(stack.pop())  # Output: 1
output.append(stack.pop())  # Output: None

print(", ".join(map(str, output)))
