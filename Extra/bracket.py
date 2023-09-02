
# Question: match the parentheses.
# e.g. do not need to consider #1*(2+3) != (1*2)+3
# Examples:
# "a(b)c)" -> "a(b)c" or "a(bc)"
# balance("()") -> "()" 
# balance(")(") -> ""
# balance("(((((") -> ""
# balance("(()()(") -> "()()"

def balance(s:str):
    # 注意这个题目不是为了做演算并得出结果，而是为了检查并去除多余的括号
    # 所以使用一个同样长度的array记录"去除/留下"每个括号
    res=[0]*len(s)
    # stack辅助，用于暂存(
    stack=[]
    for i,c in enumerate(s):
        if c not in (')','('):
            res[i]=1
        if c==')' and len(stack)>0:
            res[stack.pop()]=1
            res[i]=1
        if c=='(':
            stack.append(i)
    return "".join([c for r,c in zip(res,s) if r])

def balance2(s:str):
    # 这个算法使用recurive, 对于这个题目没必要
    stack=[]
    res=[0]*len(s)

    def recu(pos):
        nonlocal s
        nonlocal stack
        nonlocal res
        i=pos
        while i<len(s):
            if s[i]=='(':
                stack.append(i)
                i=recu(i+1)
            elif s[i]==')':
                if len(stack)>0:
                    res[stack.pop()]=1
                    res[i]=1
                    return i
            i+=1
        return i

    recu(0)
    return "".join([c for r,c in zip(res,s) if r])
                

print(balance("()(()()")) # -> () () ()
print(balance("(a)b(1(c)(d)")) # -> () () ()
print(balance(")((()(()))")) # -> (( () () )) or ( () (()) )
print(balance(")((()(()))))))")) # -> (( () ( () ) ))