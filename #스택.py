# 사용자로부터 정수 N을 입력받습니다.
N = int(input())

# 크기가 N인 리스트 A를 생성합니다. 초기값은 모두 0으로 설정합니다.
A = [0]*N

# 리스트 A의 각 인덱스에 사용자로부터 정수를 입력받습니다.
for i in range(N):
    A[i] = int(input())

# 스택을 초기화합니다.
stack = []

# 수열을 만들기 위한 변수를 초기화합니다.
num = 1

# 결과값을 저장할 변수를 초기화합니다.
result = True

# 수열 생성 과정을 문자열 형태로 저장할 변수를 초기화합니다.
answer = ""

# 리스트 A의 각 요소에 대해 반복합니다.
for i in range(N):
    # 현재 수열의 값을 변수 su에 저장합니다.
    su = A[i]
    
    # 현재 수열의 값이 num보다 크거나 같은지 확인합니다.
    if su >= num:
        # 수열을 만들기 위해 num부터 su까지의 값을 스택에 추가합니다.
        while su >= num:
            stack.append(num)
            num += 1
            # 수열 생성 과정을 문자열에 추가합니다.
            answer += "+\n"
        
        # 수열 생성이 완료된 경우, 스택에서 요소를 하나 제거합니다.
        stack.pop()
        # 수열 생성 과정을 문자열에 추가합니다.
        answer += "\n"
    else:
        # 스택에서 요소를 하나 제거합니다.
        n = stack.pop()
        
        # 스택에서 제거한 요소가 현재 수열의 값보다 큰 경우, "NO"를 출력하고 결과값을 False로 설정합니다.
        if n > su:
            print("NO")
            result = False
            break
        # 스택에서 제거한 요소가 현재 수열의 값보다 작거나 같은 경우, 수열 생성 과정을 문자열에 추가합니다.
        else:
            answer += "-\n"

# 결과값이 True인 경우, 수열 생성 과정을 출력합니다.
if result:
    print(answer)
