item_count = 4
BW = 10
w = [3, 4, 6, 5]
v = [12, 48, 30, 40]
ratio = [[0, 0], [0, 0], [0, 0], [0, 0]]
print("아이템 개수: ", item_count)
print("배낭 무게: ", BW, "kg")
print("각 짐의 무게: ", w)
print("각 짐의 가치: ", v)
print()

for i in range(item_count):
    vm = v[i]/w[i]
    ratio[i][0] = vm
    ratio[i][1] = i
    print("무게당 가치(v/w):", ratio[i][0], ",", "아이템:",(ratio[i][1]+1))
print()

f_value = 0

for i in sorted(ratio, key = lambda x:-x[0]):
    print("무게당 가치가 가장 높은 것 : ", i[0])
    if w[i[1]] <= BW:
        BW = BW-w[i[1]]
        f_value=f_value+v[i[1]]
    else:
        f_value = f_value+(BW * i[0])
        break

print()
print(f'따라서, 이때 얻을 수 있는 가치: {f_value}')