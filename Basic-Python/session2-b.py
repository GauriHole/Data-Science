my_dict1 = {'c':3,'b':2,'a':1}
sorted_dict = {k : v for k , v in sorted(my_dict1.items())}
print(sorted_dict)

my_dict2 = {'a':2 , 'b':1 , 'c':3 }
print("Printing instruction : ",{k:v for k,v in sorted(my_dict2.items(), key = lambda item: item[1])})
sorted_dict_value_based = {k : v for k,v in sorted(my_dict2.items(), key= lambda item: item[1] , reverse = True)}
print(f"sorted dict value based is : {sorted_dict_value_based}")

my_dict = {'c':3, 'a':2, 'b':1 }