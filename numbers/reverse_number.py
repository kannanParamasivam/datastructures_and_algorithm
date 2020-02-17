

def reverse_number(num):

    if num <= 10:
        return num

    rem = 0
    res = 0

    while num > 0:
        rem = num % 10
        res = (res*10) + rem
        num = int(num/10)
        print(res)

    return res


print(reverse_number(1234))