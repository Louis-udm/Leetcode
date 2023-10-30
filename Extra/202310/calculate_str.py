# 2 questions for Facebook (for Software Engineer, Machine Learning)

# 1. find local minimum in an integer array.
# [4,6,1] -> 4
# []-> None
# [1,2,3] -> 1
# [3,2,1] ->1
# [6,2,3,4,3,2,1] -> 2


# 2. calculate a string with only numbers and addition and multiplication
# "1+2*3" -> 7
def calcuate_str(str1: str) -> int:
    if not str1:
        return 0
    res=0
    for s in str1.split("+"):
        m_res=1
        for ss in s.split("*"):
            m_res*=int(ss)
        res+=m_res
    return res

print(calcuate_str("4+2*3")) #10
print(calcuate_str("")) #0
print(calcuate_str("2*3+4"))  #10