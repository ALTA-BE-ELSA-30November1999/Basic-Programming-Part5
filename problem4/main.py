# Angka Muncul Sekali
#Time Complexity O(N)
#Space Complexity O(N)

def muncul_sekali(angka):
    List = []
    a = 0
    for i in angka :
        H = angka.count(i)
        a += 1
        if H == 2 :
            print(end="")
        else :
            List.append(int(i))
    return List

if __name__ == '__main__':
    print(muncul_sekali("1234123")) # [4]
    print(muncul_sekali("76523752")) # [6, 3]
    print(muncul_sekali("12345")) # [1, 2, 3, 4, 5]
    print(muncul_sekali("1122334455")) # []
    print(muncul_sekali("0872504")) # [8, 7, 2, 5, 4]