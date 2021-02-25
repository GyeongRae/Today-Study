import sys
count = int(sys.stdin.readline())

stack = []

for i in range(count):
    order = sys.stdin.readline().split()
    if(order[0] == "push"):
        stack.append(order[1])
    
    elif(order[0] == "pop"):
        if(len(stack) == 0):
            print(-1)
        else:
            print(stack[len(stack) - 1])
            del stack[len(stack) - 1]
    
    elif(order[0] == "size"):
        if(len(order[0]) == 0):
            print(-1)
        else:
            print(len(stack))
            
    elif(order[0] == "empty"):
        if(len(stack) == 0):
            print(1)
        else:
            print(0)
    elif(order[0] == "top"):
        if(len(stack) == 0):
            print(-1)
        else:
            print(stack[len(stack) - 1])
