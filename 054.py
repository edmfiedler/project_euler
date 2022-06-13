"""
2 Poker hands are presented.

Determine how many of player 1's hands win.
"""

# Pre-process given data
with open('txt_files/p054_poker.txt') as f:
    lines = f.readlines()

for c, l in enumerate(lines):
    lines[c] = l[0:-1]

def royalflush(h):
    # Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
    if 'T' in h and 'J' in h and 'Q' in h and 'K' in h and 'A' in h:
        if len(list(set(h[1::3]))) == 1:
            return 10
    return 0

def straightflush(h):
    # Straight Flush: All cards are consecutive values of same suit.
    ref = list("23456789TJQKA")
    hval = list(h[0::3])
    sort_hval = sorted(set(ref).intersection(hval), key = ref.index)
    max_val = ref.index(sort_hval[-1])
    if len(sort_hval) == 5:
        cons = "23456789TJQKA23456789TJQKA"
        sort_hval = sort_hval + sort_hval
        j = 0
        for k in range(5,11):
            check = sort_hval[j:k]
            if "".join(check) in cons and len(list(set(h[1::3]))) == 1:
                return [9,max_val]
            j += 1
    return 0

def fourkind(h):
    # Four of a Kind: Four cards of the same value.
    ref = list("23456789TJQKA")

    hval = list(h[0::3])
    hval_set = list(set(list(h[0::3])))
    for v in hval_set:
        if hval.count(v) == 4:
            return [8,ref.index(v)]
    return 0

def fullhouse(h):
    # Full House: Three of a kind and a pair.
    ref = list("23456789TJQKA")

    hval = list(h[0::3])
    hval_set = list(set(list(h[0::3])))

    check = 0
    for v in hval_set:
        if hval.count(v) == 3:
            max_three = ref.index(v)
            check += 2
        if hval.count(v) == 2:
            max_pair = ref.index(v)
            check += 1

    if check == 3:
        return [7,max_three,max_pair]
    return 0

def flush(h):
    # Flush: All cards of the same suit.
    ref = list("23456789TJQKA")
    hval = list(h[0::3])
    sort_hval = sorted(set(ref).intersection(hval), key = ref.index)
    max_val = ref.index(sort_hval[-1])

    suits = list(h[1::3])
    if len(set(suits)) == 1:
        return [6,max_val]
    return 0

def straight(h):
    # Straight: All cards are consecutive values.
    ref = list("23456789TJQKA")
    hval = list(h[0::3])
    sort_hval = sorted(set(ref).intersection(hval), key = ref.index)
    max_val = ref.index(sort_hval[-1])

    if len(sort_hval) == 5:
        cons = "23456789TJQKA23456789TJQKA"
        sort_hval = sort_hval + sort_hval
        j = 0
        for k in range(5,11):
            check = sort_hval[j:k]
            if "".join(check) in cons:
                return [5,max_val]
            j += 1
    return 0

def threekind(h):
    # Three of a Kind: Three cards of the same value.
    ref = list("23456789TJQKA")

    hval = list(h[0::3])
    hval_set = list(set(list(h[0::3])))
    for v in hval_set:
        if hval.count(v) == 3:
            return [4,ref.index(v)]
    return 0

def twopair(h):
    # Two Pairs: Two different pairs.
    ref = list("23456789TJQKA")

    hval = list(h[0::3])
    hval_set = list(set(list(h[0::3])))
    check = 0

    vals = []
    for v in hval_set:
        if hval.count(v) == 2:
            vals.append(ref.index(v))
            check += 1

    if check == 2:
        return [3] + vals
    return 0

def pair(h):
    # One Pair: Two cards of the same value.
    ref = list("23456789TJQKA")

    hval = list(h[0::3])
    hval_set = list(set(list(h[0::3])))
    for v in hval_set:
        if hval.count(v) == 2:
            return [2, ref.index(v)]
    return 0

def high(h):
    # High Card: Highest value card.
    ref = list("23456789TJQKA")
    hval = list(h[0::3])
    sort_hval = sorted(set(ref).intersection(hval), key = ref.index)[::-1]
    vals = []
    for v in sort_hval:
        vals.append(ref.index(v))
    return [1] + vals


w = 0
for hands in lines:
    s1 = []
    p1 = hands[0:14]
    s1.append(royalflush(p1))
    s1.append(straightflush(p1))
    s1.append(fourkind(p1))
    s1.append(fullhouse(p1))
    s1.append(flush(p1))
    s1.append(straight(p1))
    s1.append(threekind(p1))
    s1.append(twopair(p1))
    s1.append(pair(p1))
    s1.append(high(p1))

    s2 = []
    p2 = hands[15:]
    s2.append(royalflush(p2))
    s2.append(straightflush(p2))
    s2.append(fourkind(p2))
    s2.append(fullhouse(p2))
    s2.append(flush(p2))
    s2.append(straight(p2))
    s2.append(threekind(p2))
    s2.append(twopair(p2))
    s2.append(pair(p2))
    s2.append(high(p2))

    # Obtain the highest value category
    cat1 = []
    for x in s1:
        if type(x) is list:
            cat1.append(x[0])
        else:
            cat1.append(x)
    cat2 = []
    for x in s2:
        if type(x) is list:
            cat2.append(x[0])
        else:
            cat2.append(x)

    # Not a perfect decision algorithm, however, it works for the dataset
    if max(cat1) > max(cat2):
        w += 1
    if max(cat1) == max(cat2):
        idx = cat1.index(max(cat1))
        if max(s1[idx][1:]) > max(s2[idx][1:]):
            w += 1
        if max(s1[idx][1:]) == max(s2[idx][1:]):
            if max(s1[-1][1:]) > max(s2[-1][1:]):
                w += 1

print(w)