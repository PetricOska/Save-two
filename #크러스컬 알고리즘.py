def union_find(parent, x1, x2):
    a=parent[x1]
    b=parent[x2]
    if a<b:
        parent[x2]=a
        for i in range(6):
            if parent[i]==b:
                parent[i]=a
    else:
        parent[x1]=b
        for i in range(6):
            if parent[i]==a:
                parent[i]=b

gg=[[0, 1, 5],[0, 2, 2],[0, 6, 2],[1, 2, 1],[1, 4, 7],[2, 5, 4],[2, 3, 1],[3, 4, 3],[4, 5, 9],[6, 2, 10]]
print("인덱스로 변경시 A=0, B=1, C=2, D=3, E=4, F=5, G=6")
print("Original(노드, 노드, 가중치):",gg)

gg.sort(key=lambda x:x[2])
print("가중치 가장 작은 순서 정렬(노드, 노드, 가중치):\n",gg)
print()

min_tree=[]
sum=0

f_u=[0, 1, 2, 3, 4, 5, 6]

for i in gg:
    if len(min_tree)==6:
        break
    x=i[0]
    y=i[1]
    if f_u[x]==f_u[y]:
        continue
    else:
        min_tree.append(i)
        union_find(f_u,x,y)
        print("작은 가중치값 찾아가는 순서:", min_tree)
    print()

    for i in min_tree:
        sum=sum+i[2]

    print("최소신장트리 노드:", min_tree)
    print("가중치합:", sum)