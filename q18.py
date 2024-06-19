def anagrams(str1, str2):
    
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    
    return sorted(str1) == sorted(str2)


string1 = "listen"  
string2 = "silent"  
if anagrams(string1, string2):
    print(f"'{string1}' and '{string2}' are anagrams.")
else:
    print(f"'{string1}' and '{string2}' are not anagrams.")
