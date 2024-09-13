# a) Write a function that takes a list of numbers & returns the sum of even numbers
list1 = [1,2,3,4,5]
def sum_Even():
    sum = 0
    for i in range(5):
        if(list1[i]%2 == 0):
            sum =sum + list1[i]
    print("Sum of Even Numbers : ",sum)
sum_Even()
print("----------------------------------------    E N D    ----------------------------------------")

# b) Write function which print name starting with 'A' from given list
list2 = ['Ram', 'Shyam', 'Sai' , 'Abhi']
def Str_A():
    names_start_with_a = [name for name in list2 if name.lower().startswith('a')]
    print("Names starting with 'a':", names_start_with_a)
result = Str_A()
print(result)
print("----------------------------------------    E N D    ----------------------------------------")

# c) Write a function that takes a list of characters as input and removes all duplicate characters from the list.
def remove_duplicates(characters):
    # Create an empty list to store unique characters
    unique_characters = []

    # Iterate through the original list
    for char in characters:
        # Check if the character is not already in the unique list
        if char not in unique_characters:
            # Add the character to the unique list
            unique_characters.append(char)

    # Return the list with duplicates removed
    return unique_characters

input_characters = ['a', 'b', 'c', 'a', 'd', 'e', 'b', 'f', 'g', 'c']
result = remove_duplicates(input_characters)
print(f"Original list: {input_characters}")
print(f"List with duplicates removed: {result}")
print("----------------------------------------    E N D    ----------------------------------------")

# d) Write a program that takes a list of numbers as input and sorts the list in ascending order.
def sort_number_asc(numbers):
    # Use the sorted function to sort the list in ascending order
    sort_number = sorted(numbers)
    return sort_number

input_numbers = [5, 2, 8, 1, 9, 3, 6, 4, 7]
sorted_result = sort_number_asc(input_numbers)

print(f"Original list: {input_numbers}")
print(f"Sorted list in ascending order: {sorted_result}")
print("----------------------------------------    E N D    ----------------------------------------")

# e) Write a program that takes a list of words as input and reverses the order of the words in the list.
def reverse_order(words):
    # Use slicing to reverse the order of words in the list
    rev_word = words[::-1]

    return rev_word

input_word = ["apple", "banana", "orange", "grape", "kiwi"]
result = reverse_order(input_word)
print(f"Original list of words: {input_word}")
print(f"Reversed list of words: {result}")
print("----------------------------------------    E N D    ----------------------------------------")
