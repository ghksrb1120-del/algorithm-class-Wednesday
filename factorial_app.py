#############################################################################
#  시스템 스택 호출과 재귀함수를 이용한 팩토리얼 계산 콘솔 인터렉티브 프로그램 
#  작성자: 이한규
#  작성일: 2024-09-21
# 순환(recursion)과 반복(iteration)의 차이점 이해
#  - 반복문 기반과 재귀 기반의 팩토리얼 계산 함수 구현
#  - 유효성 검사 포함 (0 이상 정수 확인)
#  - 문자열 입력 → 정수 변환 → 유효성 검사 → 팩토리얼 계산까지 포함된 콘솔 프로그램 형태
#  - q 또는 quit 입력 시 종료
#############################################################################

import time #시간 측정용

Test_data = [0, 1, 2, 3, 5, 10, 15, 20, 30, 50, 100] #테스트용 데이터

def factorial_iter(n):
    #반복문 기반 n!
    result = 1
    if n < 0:
        raise ValueError("정수(0 이상의 숫자)만 입력하세요.") #유효성 검사 
    for k in range(2, n+1):
        result *= k
    return result

def factorial_rec(n):
    #재귀적으로 문제 해결 n! -> 재귀함수 정의

    #1. base case (재귀호출 종료 조건)
    if n == 1 or n == 0:
        return 1
    #2. 유효성 검사
    if n < 0:
        raise ValueError("정수(0 이상의 숫자)만 입력하세요.") #유효성 검사 
    #2. 재귀 분할
    return n * factorial_rec(n-1)

def run_with_time(n):
    print(f"[반복] {n}! = {factorial_iter(n)}")
    print(f"[재귀] {n}! = {factorial_rec(n)}")

    #일치여부 확인
    if factorial_iter(n) == factorial_rec(n):
        print("결과 일치 여부: 일치")
    else:
        raise ValueError("결과 일치 여부: 불일치")
    
    #시간 측정
    start = time.time()
    iter_result = factorial_iter(n)
    end = time.time()
    iter_time = end - start #반복문 수행 시간

    start = time.time()
    rec_result = factorial_rec(n)
    end = time.time()
    rec_time = end - start #재귀 수행 시간

    print(f"[반복] 시간: {iter_time:.6f} s  |  [재귀] 시간: {rec_time:.6f} s") #시간 출력

def show_menu():
    print("================ Factorial test ================")
    print("1) 반복법으로 n! 계산")
    print("2) 재귀법으로 n! 계산")
    print("3) 두 방법 모두로 n! 계산 및 시간 측정")
    print("4) 준비된 테스트 데이터 일괄 실행")
    print("q) 종료")

if __name__ == "__main__":
    while True:
        show_menu()
        choice = input("선택: ").strip()

        if choice == '1':
            n = int(input("n 값(정수, 0이상)을 입력하세요: ").strip())
            print(f"[반복] {n}! = {factorial_iter(n)}")
            
        elif choice == '2':
            n = int(input("n 값(정수, 0이상)을 입력하세요: ").strip())
            print(f"[재귀] {n}! = {factorial_rec(n)}")

        elif choice == '3':
            n = int(input("n 값(정수, 0이상)을 입력하세요: ").strip())
            run_with_time(n)
            
        elif choice == '4':
            for n in Test_data:
                print(f"\n=== 테스트 데이터: {n} ===")
                run_with_time(n)
            
        elif choice == 'q':
            print("종료합니다.")
            break   

        else:
            print("잘못된 선택입니다. 다시 시도하세요.")
        



    
