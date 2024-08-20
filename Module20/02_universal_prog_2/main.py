def is_prime(a):
    flag = True
    if a > 1:
        for i in range(2, a):
            if a % i == 0:
                flag = False
                break
    else:
        flag = False
    return flag

def crypto(line):
    return [char for i, char in enumerate(line) if is_prime(i)]



