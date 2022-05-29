import operator
string = input("Enter the String:- ")
def most_frequent(string_name):
    my_dict = {}
    for letter in string_name:
        if letter not in my_dict:
            my_dict[letter] = 1
        else:
            my_dict[letter] += 1
        my_dict1 = dict(sorted(my_dict.items(), key = operator.itemgetter(1), reverse = True))
    return my_dict1
print(most_frequent(string))
