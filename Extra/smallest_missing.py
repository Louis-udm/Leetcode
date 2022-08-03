# Question:
# Given a list of positive integers (greater than 0), find the smallest missing one from the list range.
# Example: list = [2,4,6], your function will return 3, which will be the smallest one in this case.

def smallest_list(l):
    list_b=list(range(min(l),max(l)+1)) #[2,3,4,5,6]
    a=set(list_b)-set(l) # (3,5) #unique element, unorder 
    # (2,3,4,5,6) - (6,4,2) = (3,5) #(5,3)
    if min(a)<0: 
        print("input should be all positive integers")
        return None
    return min(a) # 3


# print(smallest_list([-2,4,6]))
print(smallest_list([2,4,6]))
print(smallest_list([6,4,2]))