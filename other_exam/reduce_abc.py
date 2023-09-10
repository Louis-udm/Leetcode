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


print(reduce_abc("abcabc"))