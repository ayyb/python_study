# 메모 변수를 만듭니다.
dictionary = {
    1: 1,
    2: 2
}

# 함수를 선언합니다.


def fibonacci(n):
    if n in dictionary:
        # 메모가 되어 있으면 메모된 값을 리턴
        return dictionary[n]

    else:
        # 메모가 되어 있지 않으면 값을 구함
        output = fibonacci(n - 1) + fibonacci(n - 2)
        dictionary[n] = output
        return output


# 함수를 호출합니다.
print("fibonacci(10):", fibonacci(10))
print("fibonacci(10):", fibonacci(10))
print("fibonacci(10):", fibonacci(10))
print("fibonacci(10):", fibonacci(10))
print("fibonacci(10):", fibonacci(10))
