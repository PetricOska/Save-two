import random

def bubble(arr):
    for i  in range(len(arr)-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print(f'리스트에서 서로 이웃한 현재 값 중 작은값인 "{arr[j]}"의 인덱스[{j+1}] 위치를 변경하면')
                print(f'[단계별 교환 후 정렬 과정 :{arr}]')
            else:
                print(f'[단계별 교환 후 정렬 과정 :[{arr[j]}]와 {[arr[j+1]]}의 값 크기가 변동없음')
            print()
        
    print('+'*50)
    print(f'정렬 후: {arr}')

array1=random.sample(range(1, 101), 6)
print(f'정렬 전: {array1}')
print('='*50)
bubble(array1)