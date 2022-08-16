# "11", "10"), True
# "11", "11"), True
# "10.4.6", "10.4"), True
# "10.4", "10.4.8"), False
# "10.4", "11"), False
# "10.4", "10.10"), False
# "10.4.9", "10.5"),False

def compare_versions(version1: str, version2: str) -> bool:
    get_list_1 = [int(i) for i in version1.split('.')]
    get_list_2 = [int(i) for i in version2.split('.')]

    if (get_list_1 >= get_list_2): return True
    else: return False
        

print(compare_versions("11", "10"))
print(compare_versions("11", "11"))
print(compare_versions("10.4.6", "10.4"))
print(compare_versions("10.4", "10.4.8"))
print(compare_versions("10.4", "11"))
print(compare_versions("10.4", "10.10"))
print(compare_versions("10.4.9", "10.5"))