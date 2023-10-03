# FAST EXPONENTATION
#Time Complexity O(N^2)
#Space Complexity O(N)

def pow(x, n):
    Start = 1.0
    if x > 0 :
        for i in range (n) :
            Start *= x
    if n < 0 :
        for i in range (-(n)) :
            Bagi = 1/x
            Start *= Bagi
    return Start

if __name__ == '__main__':
    print(pow(2, 3)) # 8
    print(pow(7, 2)) # 49
    print(pow(10, 5)) # 100000
    print(pow(17, 6)) # 24137569
    print(pow(5, 3)) # 125
    