#선형 검색 알고리즘 구현
import copy
def search(n, k):
    copyset = copy.deepcopy(numset)
    copyset.append(k)
    for i in range(num):
        if n[i] == k:
            print('탐색 성공')
            return i
    return -1

    
num = int(input("원소 수 입력: "))
numset = [None] * num

for i in range(num):
    numset[i] = int(input(f' x[{i}]: '))

key = int(input('탐색 할 값 입력: '))

want = search(numset, key)

if(want == -1):
    print("탐색값 x")
else:
    print(f'탐색 값은 x[{want}]에 있다. ')
