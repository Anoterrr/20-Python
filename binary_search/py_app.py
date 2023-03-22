def binarySearch(vector, target):
    vector.sort()
    left = 0
    right = len(vector)
    while(left <= right):
        midle = (left + right) //2
        if midle == target:
            return midle
        elif midle > target:
            left = midle-1
        elif midle < target:
            right = midle+1
    return -1

print(binarySearch([1,5,3,4,2], 2))