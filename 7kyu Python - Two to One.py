def longest(a1: str, a2: str) -> str:
    temp = list(set(a1) | set(a2))
    sorted_temp = sorted(temp)
    return ''.join(sorted_temp)






if __name__ == '__main__':
    assert longest("xyaabbbccccdefww", "xxxxyyyyabklmopq") == "abcdefklmopqwxy"
    assert longest("abcdefghijklmnopqrstuvwxyz","abcdefghijklmnopqrstuvwxyz") == "abcdefghijklmnopqrstuvwxyz"
    assert longest("aretheyhere", "yestheyarehere") == "aehrsty"
    assert longest("loopingisfunbutdangerous", "lessdangerousthancoding") == "abcdefghilnoprstu"
    assert longest("inmanylanguages", "theresapairoffunctions") == "acefghilmnoprstuy"