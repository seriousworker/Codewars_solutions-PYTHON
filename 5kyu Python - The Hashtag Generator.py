def generate_hashtag(s: str) -> str:
    if len(s) < 1:
        return False
    else:
        capitalized_words = []

        for i in s.split(' '):
            capitalized_words.append(i.capitalize())
        
        result = '#' + ''.join(capitalized_words)
        
        if len(result) > 140 or not result:
            return False
        else:
            return result
        
        


if __name__ == '__main__':
    assert generate_hashtag('') == False
    assert generate_hashtag('Do We have A Hashtag')[0] == '#'
    assert generate_hashtag('Codewars') == '#Codewars'
    assert generate_hashtag('Codewars      ') == '#Codewars'
    assert generate_hashtag('Codewars Is Nice') == '#CodewarsIsNice'
    assert generate_hashtag('codewars is nice') == '#CodewarsIsNice'
    assert generate_hashtag('CodeWars is nice') == '#CodewarsIsNice'
    assert generate_hashtag('c i n') == '#CIN'
    assert generate_hashtag('codewars  is  nice') == '#CodewarsIsNice'
    assert generate_hashtag('Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat') == False