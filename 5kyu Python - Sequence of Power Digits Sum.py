from math import pow, trunc

# get number of splitted and rised to the given power digits
def get_sum_of_powered_digits(numb: int, power: int) -> int:
    to_list = [trunc(pow(int(i), power)) for i in str(numb)]
    sum_items = sum(to_list)
    return sum_items


def sum_pow_dig_seq(start: int, n: int, k: int) -> list:
    results = [start]
    sums_of_digits = get_sum_of_powered_digits(start, n)

    while k > 0:
        results.append(sums_of_digits)
        sums_of_digits = get_sum_of_powered_digits(sums_of_digits, n)
        k -= 1

    repeated_sequence = [i for i in results if results.count(i) > 1]
    first_number = repeated_sequence[0]
    with_out_first_item = repeated_sequence[1:]
    index_of_the_next_patt = with_out_first_item.index(first_number)
    cyc_patt_arr = repeated_sequence[0 : (index_of_the_next_patt + 1)]
    patt_len = len(cyc_patt_arr)
    h = results.index(first_number)
    last_term = results[-1]
    
    return [h, cyc_patt_arr, patt_len, last_term]


# print(sum_pow_dig_seq(420, 4, 30))

if __name__ == '__main__':
    assert sum_pow_dig_seq(420, 4, 30) == [12, [13139, 6725, 4338, 4514, 1138, 4179, 9219], 7, 1138]
    assert sum_pow_dig_seq(420, 3, 5) == [3, [153], 1, 153]
    assert sum_pow_dig_seq(420, 4, 30) == [12, [13139, 6725, 4338, 4514, 1138, 4179, 9219], 7, 1138]
    assert sum_pow_dig_seq(420, 5, 100) == [23, [9045, 63198, 99837, 167916, 91410, 60075, 27708, 66414, 
                                                17601, 24585, 40074, 18855, 71787, 83190, 92061, 66858, 84213, 
                                                34068, 41811, 33795, 79467, 101463], 22, 18855]

