def count_character_frequencies(input_string):
    dict = {}
    for char in input_string:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    return dict


input_string = "hello world"  
frequencies = count_character_frequencies(input_string)

print("Character frequencies:")
for char, freq in frequencies.items():
    print(f"'{char}': {freq}")