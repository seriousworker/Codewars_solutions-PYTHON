def likes(names):
    match len(names):
        case 0:
            return f'no one likes this'
        case 1:
            return f'{names[0]} likes this'
        case 2:
            return f'{names[0]} and {names[1]} like this'
        case 3:
            return f'{names[0]}, {names[1]} and {names[2]} like this'
        case _:
            return f'{names[0]}, {names[1]} and {len(names) - 2} others like this'
            

"""
 or another solution 
def likes(names):
    answers = {
        0: 'no one likes this',
        1: '{} likes this',
        2: '{} and {} like this',
        3: '{}, {} and {} like this',
        4: '{}, {} and {others} others like this'
    }
    length = len(names)

    return answers[min(4, length)].format(*names, others=length - 2)
"""


if __name__ == '__main__':
    assert likes([]) == 'no one likes this'
    assert likes(['Peter']) == 'Peter likes this'
    assert likes(['Jacob', 'Alex']) == 'Jacob and Alex like this'
    assert likes(['Max', 'John', 'Mark']) == 'Max, John and Mark like this'
    assert likes(['Alex', 'Jacob', 'Mark', 'Max']) == 'Alex, Jacob and 2 others like this'
