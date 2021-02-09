class stack:
    def __init__ (self, n):
        self.list = [] #흑..
        self.pointer = 0

    def push(self, value): #  데이터 푸쉬 함수
        self.list.append(value)
        self.pointer += 1

    def pop(self): # 데이터 팝 함수
        if(len(self.list) == 0):
            print("stack is empty")
        else:
            self.pop()
            self.pointer -= 1

    def peek(self): # top 데이터 확인 함수
        if(self.pointer == 0):
            print("data is None")
        else:
            print(self.list[self.pointer-1])

    def find(self, value): # 데이터 검색 함수
        for i in range(self.pointer -1, 0, -1):
            if(self.list[i] == value):
                print('search success')
        

    def count(self): # 현재 데이터 개수 카운트 함수
        print(len(self.list))

    def clear(self): # 모든 데이터 삭제 함수
        self.list = []
        self.pointer = 0
    def dump(self): # 모든 데이터 출력 함수
        if(self.pointer == 0):
            print("data is None")
        else:
            print(self.list[:self.pointer])

n = int(input('주어질 명령의 수: '))

s = stack(n)

for i in range(n):
    print("push, pop, peek, find, count, clear, dump")
    print(f'stack: {s.list} pointer: {s.pointer}')
    order = input()

    if(order == "push"):
        x = int(input("push data"))
        s.push(x)
    if(order[0] == "pop"):
        s.pop()
    if(order[0] == "count"):
        s.count()
    if(order[0] == "peek"):
        s.peek()
    if(order[0] == "find"):
        s.find(order[1])
    if(order[0] == "clear"):
        s.clear()
