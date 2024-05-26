def max_heap(b, c):
    for i in range(1, c+1):
        c=i
        while c!=0:
            r=(c-1)//2
            print("부모노드 인덱스위치=", r, ", 해당값=", b[r], end=" ")
            print("자식노드 인덱스위치=", c, ", 해당값=", b[r], end=" ")
            if b[c]>b[r]:
                b[c],b[r]=b[r],b[c]
                print("서로 교환")
            else:
                print(f"index{r}의{b[r]}와/과 index{c}의 {b[c]}는 교환필요없음")
            c=r
            print()

def heap_sort(a):
    for i in range(len(a)-1, 0, 1):
        print()
        max_heap(a, i)
        print(f"a[{0}]값={a[0]}, a[{i}]값={a[i]}서로 교환")
        a[0], a[i]=a[i], a[0]
        print("변경된 리스트값", a)
        print("+"*25)
        print()

array=[4, 10, 3, 5, 1]

print(f'정렬전:{array}')
print()
print("====알고리즘 동작과정 ====")
heap_sort(array)
print("="*25)
print(f'힙정렬 후:{array}')