# a) Write a funcƟon that takes two sets as input and returns the intersecƟon of the two sets
def find_intersec(seta, setb):
    intersection_result = seta.intersection(setb)
    return intersection_result
set1 = {5, 2, 6, 2, 3}
set2 = {5, 3, 1, 4, 2}

final_res = find_intersec(set1, set2)
print("Intersection of the sets:", final_res)
print("----------------------------------------    E N D    ----------------------------------------")

# b) Write a function that takes a set of numbers and returns the sum of the numbers in the set.
def cal_sum(input):
    final_sum = sum(input)
    return final_sum
number = {4, 1, 3, 2, 5}
res = cal_sum(number)
print("Sum of the set:", res)
print("----------------------------------------    E N D    ----------------------------------------")

# c) Write a program that takes a set of words and removes all duplicate words from the set
def remove_duplicates(word_set):
    uniword = set()
    for word in words:
        uniword.add(word)
    return uniword
words = {"gauri", "vidya", "aditi", "nikita", "ishwari","vidya"}

result = remove_duplicates(words)
print("Set after removing duplicates:", result)
print("----------------------------------------    E N D    ----------------------------------------")

# d) Write a program that takes a set of numbers and finds the maximum and minimum values in the set
def findMaxMin(numbers_set):
    maxVal = max(numbers_set)
    minVal = min(numbers_set)
    return maxVal, minVal

numbers = {15, 25, 23, 5, 31, 10}
max, min = findMaxMin(numbers)
print("Maximum value in the set:", max)
print("Minimum value in the set:", min)
print("----------------------------------------    E N D    ----------------------------------------")

# e) Write a program that takes two sets as input and checks if the two sets are equal.
def checkEqual(setA, setB):
    return set1 == set2
setA = {5, 1, 6, 2, 3}
setB = {4, 1, 5, 2, 3}

result = checkEqual(set1, set2)
if result:
    print("Sets are equal.")
else:
    print("Sets are not equal.")

