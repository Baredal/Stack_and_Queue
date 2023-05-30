"""
Stack to queue converter.
"""
from arraystack import ArrayStack   # or from linkedstack import LinkedStack
from arrayqueue import ArrayQueue   # or from linkedqueue import LinkedQueue
def stack_to_queue(stack):
    '''
    Accepts a stack and returns the queue in a different order
    without changing the original stack
    '''
    queue = ArrayQueue()
    new_stack = ArrayStack(stack)
    while not new_stack.isEmpty():
        queue.add(new_stack.pop())
    return queue
