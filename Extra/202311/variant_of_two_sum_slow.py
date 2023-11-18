# Given a list of words L and a number N, 
# write a function that returns all words from "L" that 
# are of lenght "N" and are formed from two smaller words in "L".
# Example:
# N=6, L=["hot", "bird", "dog", "tailor", "hotdog", "or", "if", "tail"]
# Output: ["hotdog", "tailor"]
#
from collections import defaultdict

def combined_words_slow(N: int, L: list[str]) -> list[str]:
    if N<2:
        return []
    if not L:
        return []
    len_words=defaultdict(set)
    for w in L:
        w=w.strip()
        if w and len(w)<=N:
            len_words[len(w)].add(w)
    target_words=len_words.pop(N, None)
    if not target_words:
        return []
    # for k in list(len_words.keys()):
    #     if k>=N:
    #         len_words.pop(k)
    print(len_words)
    # len_words=sorted(len_words.items())
    results=set()
    for i in list(len_words.keys()):
        if N-i==i:
            words=list(len_words.pop(i))
            for target in target_words:
                for j,w1 in enumerate(words[:-1]):
                    for w2 in words[j+1:]:
                        if f"{w1}{w2}"==target or f"{w2}{w1}"==target:
                            results.add(target)
        elif N-i in len_words:
            words1=list(len_words.pop(i))
            words2=list(len_words.pop(N-i))
            for target in target_words:
                for w1 in words1:
                    for w2 in words2:
                        if f"{w1}{w2}"==target or f"{w2}{w1}"==target:
                            results.add(target)
    return list(results)

# def combined_words3(N: int, L: list[str]) -> list[str]:
#     mapping = {}
#     for index, val in enumerate(nums):
#         diff = target - val
#         if diff in mapping:
#             return [index, mapping[diff]]
#         else:
#             mapping[val] = index


    # for w in words:

    
    # print(len_words)

# print(combined_words(6, [" ", "permutations ","hot ", "bird", "dog", "tailor", "hotdog", "or", "if", "tail"]))
# print(combined_words(6, ["","hot", "bird", "dog", "", "", "or", "if", "tail"]))
# print(combined_words(6, ["","hot", "hotdog", "dog", "ho", "tdog"]))
# print(combined_words(6, ["","hot", "hotdog", "dog", "ho", "tdog"]))
# print(combined_words())
