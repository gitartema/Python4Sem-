def func(start, stop=0, step=1):
    arr1 = [0] * (abs(stop - start))
    print(arr1)
    if stop == 0:
        arr = [0]
    else:
        arr = [start]
    for val in arr1:
        arr.append(arr[len(arr) - 1] + step)
    arr.pop()
    print(arr)
    return [1, 2, 3]



if __name__ == '__main__':
    for ind in func(2, 5, 3):
        print(ind)
