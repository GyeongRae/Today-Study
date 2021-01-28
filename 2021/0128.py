class stack:
    def __init__(self, capacity):
        self.stk = [None] * capacity #스택의 배열 
        self.capacity = capacity #스택의 총 크기
        self.ptr = 0 # 스택 포인터
        
    def push(self, value): #push 기능
        self.stk[self.ptr] = value 
        self.ptr += 1
        
    def pop(self):
        if(self.stk[self.ptr] == [None]):
            print(-1)
        else:
            print(self.stk[self.ptr])
            self.stk[self.ptr] = [None]
            self.ptr -= 1
    def size(self):
        print(self.ptr - 1)
    def empty(self):
        if (self.ptr == 0):
            print(1)
        else:
            print(0)
    def top(self):
        if(self.ptr == 0):
            print(-1)
        else:
            print(self.stk[self.ptr])
            
count = int(input()) # 주어지는 명령의 수

for i in range(count):
    order = map(str, input("주어질 명령").split())
    order = list(order)
    if(order[0] == "push"):
        push(order[1])
    
    elif(order[0] == "pop"):
        pop()
    
    elif(order[0] == "size"):
        size()
        
    elif(order[0] == "empty"):
        empty()
    
    elif(order[0] == "top"):
        top()
        
    order.clear()
