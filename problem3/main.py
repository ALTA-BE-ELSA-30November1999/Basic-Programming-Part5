def join_array_remove_duplicate(arrayA, arrayB):
    List = list(arrayA)
    if len(arrayA) < len(arrayB) :
        for i in arrayB :
            if i not in arrayA :
                List.append(i)
    elif len(arrayB) < len(arrayA) :
        for i in arrayB :
            if i not in arrayA :
                List.append(i)
                List = list(set(List))
    return List

if __name__ == '__main__':
    # Test cases
    print(join_array_remove_duplicate(["apel", "anggur"], ["lemon", "leci", "nanas"]))
    # ["apel", "anggur", "lemon", "leci", "nanas"]


    print(join_array_remove_duplicate(["samsung", "apple"], ["apple", "sony", "xiaomi"]))
    # ["samsung", "apple", "sony", "xiaomi"]


    print(join_array_remove_duplicate(["football", "basketball"], ["basketball", "football"]))
    # ["football", "basketball"]


