# Have the function StringChallenge(str) take the str parameter being passed and
# return the smallest number you can get through the following reduction method.
# The method is: Only the letters a, b, and c will be given in str and you must
# take two different adjacent characters and replace it with the third. For example
# "ac" can be replaced with "b" but "aa" cannot be replaced with anything. This
# method is done repeatedly until the string cannot be further reduced, and the
# length of the resulting string is to be outputted. For example: if str is "cab",
# "ca" can be reduced to "b" and you get "bb" (you can also reduce it to "cc").
# The reduction is done so the output should be 2. If str is "bcab", "bc" reduces
# to "a", so you have "aab", then "ab" reduces to "c", and the final string "ac"
# is reduced to "b" so the output should be 1.
#
# Examples
# Input: "abcabc"
# Output: 2
# Input: "cccc"
# Output: 4
# Input: "cccb"
# Output: 1
# Input: "cab"
# Output: 2
# Input: "bcab"
# Output: 1
# Input: "aabbbc"
# Output: 1

def reduce_abc(strParam):
  # code goes here
  def one_loop(st, init_i):
    i=init_i
    while True:
      if i+1>len(st)-1:
        break
      if st[i]!=st[i+1]:
        new_char={"a","b","c"}-{st[i],st[i+1]}
        st=f"{st[:i]}{new_char.pop()}{st[i+2:]}"
      else:
        i=i+1
    return st

  def reduce_str(st):
    unique_set={c for c in st}
    if len(unique_set)==1:
      return len(st)
    st1=one_loop(st,0)
    st2=one_loop(st,1)
    st=st1 if len(st1)<len(st2) else st2
    return reduce_str(st)
  
  return reduce_str(strParam)

# chatgpt version is wrong
def reduce_abc2(str):
    # Define a function to check if reduction is possible
    def can_reduce(s):
        return 'ab' in s or 'bc' in s or 'ca' in s

    # Continue reducing the string until no more reductions are possible
    while can_reduce(str):
        str = str.replace('ab', 'c').replace('bc', 'a').replace('ca', 'b')

    # Return the length of the final reduced string
    return len(str)

print(reduce_abc("abcabc"))
print(reduce_abc("cccc"))
print(reduce_abc("cccb"))
print(reduce_abc("bcab"))