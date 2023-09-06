while True:
    n = int(input())
    if n == -1:  # -1인 경우 종료
        break
    divisor = []
    divisor_str = ""

    for i in range(1, n):
        if n % i == 0:
            divisor.append(i)  # 자기자신은 포함 안됨

    if sum(divisor) == n:
        result = f"{n} = "
        divisor_str = " + ".join(map(str, divisor))
        result += divisor_str
        print(result)
    else:
        print(f"{n} is NOT perfect.")
