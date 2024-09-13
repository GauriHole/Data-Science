# a)  Write a funcƟon that takes a tuple of numbers as input and returns the average of the numbers in the tuple
import numbers
def avg_of_num(numb_tuple):
    # Check tuple is not empty
    if not numb_tuple:
        return None  # Return None for an empty tuple
    # Calculate average
    average = sum(numb_tuple) / len(numb_tuple)
    return average
input_tuple = (5, 10, 15, 20, 25)
result = avg_of_num(input_tuple)

print(f"Tuple : {input_tuple}")
if result is not None:
    print(f"Average of numbers: {result}")
else:
    print("Tuple is empty.")
print("----------------------------------------    E N D    ----------------------------------------")

# b) Write a funcƟon that takes a tuple of characters as input and returns the number of vowels in the tuple
def countVowel(char_tuple):
    # Define a set of vowels
    vowels = set("aeiouAEIOU")
    # Count the number of vowels in the tuple
    count = sum(1 for char in char_tuple if char in vowels)
    return count

input = ('a', 'x', 'd', 'c', 'e', 'f', 'i', 'o')
result_tup = countVowel(input)

print("Tuple of characters: ",input)
print("Number of vowels in the tuple: ",result_tup)
print("----------------------------------------    E N D    ----------------------------------------")

# c) Write a program that takes a tuple of numbers as input and finds the maximum and minimum values in the tuple.
def find_max_min_values(num_tuple):
    # Check tuple is not empty
    if not num_tuple:
        return None, None
    # Find the max and min value
    max_Val = max(num_tuple)
    min_Val = min(num_tuple)
    return max_Val, min_Val

input = (5, 10, 15, 20, 25)
max_Val, min_Val = find_max_min_values(input)
print(f"Tuple of numbers: {input_tuple}")
if max_Val is not None and min_Val is not None:
    print(f"Maximum value in the tuple: {max_Val}")
    print(f"Minimum value in the tuple: {min_Val}")
else:
    print("The tuple is empty.")
print("----------------------------------------    E N D    ----------------------------------------")

# d)  Write a program that takes a tuple of words as input and prints each word in the tuple in reverse order.
def rev_word(words):
    for word in words:
        rev_word = word[::-1]
        print(rev_word)

tuple1 = ("Gauri", "Vidya", "Aditi", "Nikita", "Ishwari")
print(f"Original words: {tuple1}")
print("Words in reverse order:")
rev_word(tuple1)
print("----------------------------------------    E N D    ----------------------------------------")

# e) Write a program that takes a tuple of characters as input and checks if the tuple is a palindrome
def palindrome(charTuple):
    str = ''.join(charTuple)
    return str == str[::-1]

samp_tuple = ('a', 'e', 'i', 'z', 'i', 'e', 'a')
print(f"Original tuple of characters: {samp_tuple}")
if palindrome(samp_tuple):
    print("This a palindrome.")
else:
    print("This not a palindrome.")
samp_tuple = ('a', 'e', 'i', 'o', 'x', 'e', 'a')
print(f"Original tuple of characters: {samp_tuple}")
if palindrome(samp_tuple):
    print("This a palindrome.")
else:
    print("This not a palindrome.")
print("----------------------------------------    E N D    ----------------------------------------")
