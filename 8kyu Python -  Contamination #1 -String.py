# def contamination(text: str, char: str) -> str:
#     if len(text) == 0 or len(char) == 0:
#         return ""
#     else:
#         return char * len(text)


def contamination(text: str, char: str) -> str:
    match char, text:
        case "":
            return ""
    return char * len(text)

if __name__ == '__main__':
    assert contamination('abc', 'z') == 'zzz'
    assert contamination("" ,"z") == ""
    assert contamination("abc", "") == ""
    assert contamination("_3ebzgh4", "&") == "&&&&&&&&"
    assert contamination("//case", " ") == "      "