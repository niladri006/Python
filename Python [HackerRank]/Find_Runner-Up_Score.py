if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    mx = max(arr)
    sc = None

    for num in arr:
        if num == mx:
            pass
        elif sc == None:
            sc = num
        elif num > sc:
            sc = num

    print(sc)