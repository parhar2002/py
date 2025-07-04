from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        """Add an item to the rear of the queue."""
        self.queue.append(item)
        print(f"Enqueued: {item}")

    def dequeue(self):
        """Remove and return the front item of the queue. If the queue is empty, return None."""
        if self.is_empty():
            print("Queue is empty, cannot dequeue.")
            return None
        return self.queue.popleft()

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.queue) == 0

    def peek(self):
        """Return the front item of the queue without removing it."""
        if self.is_empty():
            print("Queue is empty.")
            return None
        return self.queue[0]

    def size(self):
        """Return the number of items in the queue."""
        return len(self.queue)

    def display(self):
        """Display the entire queue."""
        if self.is_empty():
            print("Queue is empty.")
        else:
            print("Queue contents:", list(self.queue))

# Example usage
q = Queue()
q.enqueue('Apple')
q.enqueue('Banana')
q.enqueue('Cherry')

print(f"Front of the queue: {q
