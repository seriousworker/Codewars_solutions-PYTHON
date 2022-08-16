def what_century(year: str) -> str:
    ends_dict = {'1': 'st', '2': 'nd', '3': 'rd'}
    if (year[2 : ] == '00'):
        end = 'th' if year[0 : 2] in ['11', '12', '13'] else ends_dict.get(year[1], 'th')
        return f'{year[0 : 2]}{end}'
    else:
        century = str(int(year[0 : 2]) + 1)
        end = 'th' if century in ['11', '12', '13'] else ends_dict.get(century[1], 'th')
        return f"{century}{end}"
    


if __name__ == '__main__':
    assert what_century('1999') == '20th'
    assert what_century('2011') == '21st'
    assert what_century('2154') == '22nd'
    assert what_century('2259') == '23rd'
    assert what_century('1124') == '12th'
    assert what_century('2000') == '20th'
    assert what_century('1100') == '11th'
    assert what_century('1200') == '12th'