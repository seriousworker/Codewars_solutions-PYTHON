def scramble(s1: str, s2: str) -> bool:
    for c in set(s2):
        if s1.count(c) < s2.count(c):
            return False
    return True


# from collections import Counter
#
# def scramble(s1,s2):
#     # Counter basically creates a dictionary of counts and letters
#     # Using set subtraction, we know that if anything is left over,
#     # something exists in s2 that doesn't exist in s1
#     return len(Counter(s2)- Counter(s1)) == 0


if __name__ == '__main__':
    assert scramble('rkqodlw', 'world') == True
    assert scramble('cedewaraaossoqqyt', 'codewars') == True
    assert scramble('katas', 'steak') == False
    assert scramble('scriptjava', 'javascript') == True
    assert scramble('scriptingjava', 'javascript') == True
    assert scramble("najdqgmfpss", "ffpqdjn") == False
    assert scramble("rihtrclhtseoiepcq", "tcqphcseiic") == False
    assert scramble("emnoatoabunlfb", "meolueabo") == False
    assert scramble("htirbsrdyxufvknwwb", "nwssrwhxbt") == False
    assert scramble("lzkujszwbthtdkt", "ztuzjtsuwkbk") == False
    assert scramble("ffqvmvvykmmlev", "evfqylmlm") == False
    assert scramble("ydrcnkevxxtkrwwhznq", "wrvwnzkcxrnrx") == False
    assert scramble("ehwpzwryesj", "swzywry") == False

