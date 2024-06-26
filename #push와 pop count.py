# 괄호를 저장할 리스트 초기화
a_count = list()

# 스택에 데이터를 추가하는 함수
def push(push_data):
    a_count.append(push_data)

# 스택에서 데이터를 삭제하고 반환하는 함수
def pop():
    if len(a_count) > 0:
        return a_count.pop()
    else:
        return None

# 괄호를 확인하고 스택 상태를 출력하는 함수
def check_brackets(sentence):
    print("스택에 추가되는 과정:", end=' ')
    
    for char in sentence:  # 입력된 문자열에서 한 글자씩 확인
        if char == '(':  # 왼쪽 괄호인 경우 스택에 추가
            push(char)
        elif char == ')':  # 오른쪽 괄호인 경우 스택에서 제거
            if pop() is None:  # 스택이 비어있는 경우 에러 출력 후 종료
                print("스택이 비어있음: error")
                return

        print(a_count, end=' ')  # 스택 상태 출력
        print()
    if len(a_count) == 0:  # 모든 문자열 확인 후 스택이 비어있는지 확인
        print("스택이 비어있음: OK")
    else:
        print("스택에 데이터가 있음: error")

# 사용자로부터 입력 받기
sentence = input("괄호가 포함된 문장을 입력하세요: ")

# 괄호 확인 함수 호출
check_brackets(sentence)
