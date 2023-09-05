def anagram_example(s1, s2):
    if sorted(s1) == sorted(s2):
        print("Is a Anagram")
    else:
        print("Not a Anagram")


str1 = str(input("S1: "))
str2 = str(input("S2: "))
anagram_example(str1, str2)
