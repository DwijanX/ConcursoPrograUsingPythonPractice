"""
deque is used instead of a list when we need O(1) to append or pop 
"""
"""
Stacks are used when we have Last in first out problems
"""

#List or deque are used for both, queue and stacks

from collections import deque



queue= deque(["test1","test2","test3"])
queue.pop()
