import sys
from collections import deque
ques= sys.stdin.readline().strip()
lens = len(ques)
stack = []
for i in ques:
    stack.append(i)

    if stack[-4:] == ['P','P','A','P']:
        stack.pop()
        stack.pop()
        stack.pop()
answer=(list(stack))
if answer == ['P']:
    print('PPAP')
else:
    print('NP')