from timer import time_function
import itertools
from math import sqrt

# maybe match against list of squares of appropriate length

DIGITS = [i for i in range(0,10)]

class LeadingZeroException(Exception):
    pass

def anagrams(words):
    anagrams = {}
    for word in words:
        s = ''.join(sorted(word))
        l = len(s)
        if l not in anagrams:
            anagrams[l] = {s:[word]}
        elif s not in anagrams[l]:
            anagrams[l][s] = [word] 
        else:
            anagrams[l][s].append(word)
    for_deletion = []
    for l in anagrams:
        for s in anagrams[l]:
            if len(anagrams[l][s]) < 2:
                for_deletion.append((l,s))
    for l,s in for_deletion:
        del(anagrams[l][s])
    for_deletion = []
    for l in anagrams:
        if len(anagrams[l]) == 0:
            for_deletion.append(l)
    for l in for_deletion:
        del(anagrams[l])
    return anagrams

def sort_words():
    with open('p098_words.txt','r') as f:
        words = [i.strip('"') for i in f.read().split(',')]
    wordagrams = anagrams(words)
    mx = max(wordagrams)
    mn = min(wordagrams)
    sqs = [str(i*i) for i in range(int(sqrt(10**mn))+1,int(sqrt(10**mx))+1)]
    squaragrams = anagrams(sqs)
    return wordagrams,squaragrams

# Take squares and form keys, if encounter double valued digit, bail.
# Apply key to paired word and see if that square is also in the set

def assign_digits(letters):
    s = ''.join(set(letters))
    L = len(s)
    for _c in itertools.combinations(DIGITS,L):
        for c in itertools.permutations(_c):
            yield {i:j for i,j in zip(s,c)} 

def assign_digits(key,letters):
    for c in itertools.permutations(key):
        yield {i:j for i,j in zip(letters,c)} 

def word_to_num(word,key):
    s = ''
    for e in word:
        s += str(key[e])
    return s

def solve():
    w,s = sort_words()
    m = max(w)
    for l in range(m,0,-1):
        f = []
        try:
            for letters,words in w[l].items():
                for sqs in s[l].values():
                    for sq in sqs:
                        key = {}
                        digits = []
                        good_key = True
                        for letter,digit in zip(words[0],sq):
                            if digit not in digits and letter not in key:
                                key[letter] = digit
                                digits.append(digit)
                            elif letter not in key or key[letter] != digit:
                                good_key = False
                                break
                        if good_key:
                            sq2 = word_to_num(words[1],key)
                            if sq2 in sqs:
                                f += [int(sq),int(sq2)]
            if len(f) > 0:
                return max(f)
        except KeyError:
            pass

print(time_function(solve,problem_number=98))

"""
def word_to_num(word,key):
    s = ''
    for e in word:
        s += str(key[e])
    if s[0] == '0':
        raise LeadingZeroException()
    return int(s)

def solve():
    anagrams = sort_words()
    M = max(anagrams)
    for l in range(M,0,-1): 
        f = []
        for letters,words in anagrams[l].items():
            for key in assign_digits(letters):
                try:
                    n = [word_to_num(word,key) for word in words]
                    if all(x//1 == x for x in map(sqrt,n)):
                        f += n
                except LeadingZeroException:
                    pass
        if len(f) > 0:
            return max(f)
print(time_function(solve))
"""
