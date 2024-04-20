from typing import List
from copy import deepcopy

stack: List[str] = []

stack.append('A')
stack.append('B')
stack.append('C')

for item in stack[::-1]:
    print(item)

while stack:
    item = stack.pop()
    print(item)

top_item = stack.pop()