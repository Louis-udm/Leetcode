"""
将一个integer array拆分为两个array，返回第一个array。
要求第一个array的sum大于第二个的同时个数最少。
arr1和arr2不能有交集，并且完全划分原array
"""
def minimize_heaviest_first_box(arr):
    # 要慎用python的一些函数，比如这里每次都用sum的话，
    # 14个测试用例中只能通过7个，数量大的array就会超时。
    # arr=sorted(arr)
    # for i in range(-1,-len(arr)-1,-1):
    #     if sum(arr[i:])>sum(arr[:i]):
    #         return arr[i:]
    
    arr=sorted(arr)
    sum1, sum2=sum(arr[:-1]), arr[-1]
    if sum1<sum2:
        return [arr[-1]]
    for i in range(-2,-len(arr)-1,-1):
        sum1-=arr[i]
        sum2+=arr[i]
        if sum1<sum2:
            return arr[i:]