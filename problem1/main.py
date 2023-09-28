def prime_number(number):
    prima = True
    a = 1
    if number <= 1 :
        prima = False
    else :
        for x in range (2, number) :
                if number % x == 0 :
                    prima = False
                    break
                if 10000000 <= x :
                    break
    return prima

if __name__ == '__main__':
    print(prime_number(1000000007)) # True
    print(prime_number(1500450271)) # True
    print(prime_number(1000000000)) # False
    print(prime_number(10000000019)) # True
    print(prime_number(10000000033)) # True

    # print(prime_number(10000000025)) # True
    # print(prime_number(1000000000)) # True
    # print(prime_number(10000000010)) # True
    # print(prime_number(6)) # True
    # print(prime_number(8)) # True
    # print(prime_number(10)) # True
    # print(prime_number(4)) # True