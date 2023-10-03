#Pair with Target Sum
#Time Complexity O(N^2)
#Space Complexity O(N)

def pair_sum(arr, target):
    pair_sum = []

    for i in range (len(arr)) :
        for j in range (i+1, len(arr)) :
            if arr[i] + arr [j] == target :
                pair_sum.append(i)
                pair_sum.append(j)
                return pair_sum
            elif arr[i] + arr [j] == 0 :
                return None
     
    

if __name__ == '__main__':
    print(pair_sum([1, 2, 3, 4, 6], 6)) # [1, 3]
    print(pair_sum([2, 5, 9, 11], 11)) # [0, 2]
    print(pair_sum([1, 3, 5, 7], 12)) # [2, 3]
    print(pair_sum([1, 4, 6, 8], 10)) # [1, 2]
    print(pair_sum([1, 5, 6, 7], 6)) # [0, 1]