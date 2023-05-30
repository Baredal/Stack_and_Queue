'''
Queue to stack converter.
'''
from arrayqueue import ArrayQueue    # or from linkedqueue import LinkedQueue
from arraystack import ArrayStack    # or from linkedstack import LinkedStack
def queue_to_stack(queue):
    '''
    Accepts a queue and returns the stack in a different order
    without changing the original queue
    '''
    stack = ArrayStack(queue)
    new_stack = ArrayStack()
    while not stack.isEmpty():
        new_stack.push(stack.pop())
    return new_stack
