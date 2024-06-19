def occurrences(lst, element):
    return lst.count(element)


numbers = [1, 2, 3, 4, 5, 2, 2, 3, 4, 2]  
element_to_count = 2  
occurrences = occurrences(numbers, element_to_count)

print("List of numbers:", numbers)
print(f"Number of occurrences of {element_to_count}: {occurrences}")
