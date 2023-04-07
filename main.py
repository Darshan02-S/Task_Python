def anagram(str1, str2):
    if len(str1) != len(str2):
        return False
    str1 = str1.casefold()
    str2 = str2.casefold()
    dict_s1 = {}
    dict_s2 = {}
    for char in str1:
        dict_s1[char] = +1
    for char in str2:
        dict_s2[char] = +1
    return dict_s2 == dict_s2
str1 = "hello"
str2 = "lelho"
print(anagram(str1, str2))


