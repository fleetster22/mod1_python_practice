# Reverse a list

list4 = [100, 200, 300, 400, 500]
list4.reverse()
print(list4)

# Concatenate two lists by index
list1 = ["M", "na", " ", " "]
list2 = ["y", "me", "is", "Anaka"]
list3 = []

for i in range(len(list1)):
    list3.append(list1[i] + list2[i])
result = str(list3)

print(result)

# Turn every item of a list into its square
numbers = [1, 2, 3, 4, 5, 6, 7]

for num in numbers:
    num = num**2
    print(num)


# Given two lists, iterate both lists simultaneously and display items from
# list1 in the original order and items from list2 in reverse order.
list5 = [10, 20, 30, 40]
list6 = [100, 200, 300, 400]
list6.reverse()

list7 = [list(i) for i in zip(list5, list6)]
print(list7)

# Remove empty strings from the list
list8 = ["Mike", "", "Emma", "Aisha", "", "Anaka"]
filtered_list = [i for i in list8 if i != ""]
print(filtered_list)


# OR
def check_list(name):
    if name != "":
        return True


filtered_list = filter(check_list, list8)
result = list(filtered_list)
print(result)

# Add new item to a list after a specified item
# Task: Add item 7000 after 6000 in the following list
list9 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list9[2][2].append(7000)
print(list9)

# Extend nested list by adding the sub-list
# Expected output ['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'],
#  'k'], 'l'], 'm', 'n']
list10 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list = ["h", "i", "j"]
# print(list10[2]) print to find the index if can't figure out
list10[2][1][2].extend(sub_list)
print(list10)

# Keys, values, dictionaries
numbers_to_words = {
    1: "one",
    2: "two",
    3: "three",
}

for key in numbers_to_words:
    print("The key is key:", key)

    # Use the key to get the value from
    # the dictionary
    value = numbers_to_words[key]
    print("The associated value is:", value)


countries = {
    "Asia": ["China", "Mongolia", "India"],
    "South America": ["Brazil", "Argentina", "Chile"],
    "North America": ["United States", "Canada", "Mexico"],
    "Antarctica": [],
    "Africa": ["South Africa", "Algeria", "Kenya", "Ethiopia", "Egypt"],
    "Europe": ["France", "Germany", "England", "Spain", "Greece", "Italy"],
    "Australia": ["New Zealand", "Fiji", "Australia"],
}

# Use the dictionary to print the value of "Asia"

value = countries["Asia"]
print(value)


# use the dictionary to print the third item in the value of "Australia"
values = countries["Australia"]
print(values[2])

# print a list of all the keys, in alphabetical order
print(sorted(countries))


# Use the dictionary keys and string interpolation to print out this string:
# "The candidate's name is W.L. McCrea. She has
# 4 years of experience as a graphic designer
# at Voltage Ad in Louisville, Kentucky"

employees = {
    "first_name": "W.L.",
    "last_name": "McCrea",
    "company": "Voltage Ad",
    "company_location": "Louisville, Kentucky",
    "years_experience": 4,
    "role": "graphic designer",
}


print(
    f"The candidate's name is {employees['first_name']} {employees['last_name']}. She has {employees['years_experience']} years of experience as a {employees['role']} at {employees['company']} in {employees['company_location']}"
)

# Print a dictionary that indicates the number of times each letter occurs in the list.

# sort the list alphabetically then count the number of times each letter occurs and add it to a dictionary

letter_list = [
    "s",
    "a",
    "j",
    "q",
    "l",
    "m",
    "v",
    "l",
    "t",
    "h",
    "b",
    "w",
    "r",
    "g",
    "n",
    "c",
    "y",
    "i",
    "z",
    "a",
    "l",
    "t",
    "x",
    "e",
    "k",
    "o",
    "r",
    "u",
    "p",
    "l",
    "n",
    "c",
    "d",
    "q",
    "l",
    "w",
]
my_dict = {}

# check to see if already in dictionary then count the number of times each letter occurs during each iteration
for letter in letter_list:
    if letter not in my_dict:
        my_dict[letter] = 1
    else:
        my_dict[letter] += 1

print(my_dict)


# Loop through the dictionary and create a new one where the values are the squares of the current values.

dict2 = {"a": 1, "b": 2, "c": 3}
new_dict = {}
for key, value in dict2.items():
    new_dict[key] = value**2

# below is if you don't have to create a new dictionary
# dict2.update((key, value**2) for key, value in dict2.items())

print(new_dict)


products = [
    {"item": "Bubble tea", "quantity": 6, "price_per_unit": 5.00},
    {"item": "Unicorn onesie", "price_per_unit": 49.99},
    {"item": "Legal briefcase", "quantity": 1, "price_per_unit": 149.99},
    {
        "item": "Fake mustaches",
        "quantity": 10,
        "price_per_unit": 1.00,
    },
]

# Write some code that will print a list of each of the products
list_of_prods = []
for product in products:
    list_of_prods.append(product["item"])
print(list_of_prods)

sub_total = 0
for product in products:
    if "quantity" in product:
        line_item = product["quantity"] * product["price_per_unit"]
    else:
        line_item = 0.0

    sub_total += line_item

    print(product["item"], line_item)

# write some code that calculates the total invoice + tax of 8%
total = sub_total * 1.08
print(total)


# dict2.update((key, value**2) for key, value in dict2.items())


# If the shipment list is empty, then the function should return 0.
# sum all the weights in the shipment dict
def find_shipment_weight(shipment):
    weight = 0
    for item in shipment:
        weight += item["product_weight_pounds"] * item["quantity"]
    return weight

    # retuen longest string


def find_longest(strings):
    longest = ""

    if len(strings) == 0:
        return None
    else:
        for string in strings:
            if len(string) > len(longest):
                longest = string
        return longest


# return true if base and number are ints and also
# if number is a multiple of base (6, 2)
def is_multiple_of(number, base):
    if int(number) != number or int(base) != base:
        return False
    return number % base == 0


def shift_cipher(message, shift):
    res = ""
    for char in message:
        char_num = ord(char)
        res += chr(char_num + shift)
    return res


print(shift_cipher("Raining-Frogs", -10))  # expected "HW_d_d]#<he]i"

# return a list of values in the string with delimiter/separator
# removed


def read_delimited(line, separator):
    list = line.split(separator)
    return list


# input = [1,2,3,4,5,6,7]  outcome = [[1,2], [3,4], [5,6]]
def pair_up(items):
    pairs = []
    for i in range(0, len(items), 2):
        if i + 1 < len(items):
            pair = [items[i], items[i + 1]]
            list.append(pair)
    return pairs


# strings, separated by the separator. (["aaa", "bbb", "ccc"], "--") returns
# "aaa--bbb--ccc"
def join_strings(strings, separator):
    str_len = len(strings)
    if str_len == 0:
        return ""

    return separator.join(strings)


list22 = ["aaa", "bbb", "ccc"]
sep = "--"
print(join_strings(list22, sep))


def mean(numbers22):
    if (len(numbers22)) == 0:
        return float("nan")
    totals = sum(numbers)

    return totals / len(numbers)


def get_list_of_managers(company):
    manager_list = []
    for person in company:
        if person.get("position") == "manager":
            manager_list.append(person.get("name"))
    return manager_list


def get_list_of_workers(company):
    worker_list = []
    for person in company:
        if person.get("position") == "worker":
            worker_list.append(person["name"])
    return worker_list


def longest_name(company):
    long_name = ""
    for employee in company:
        if len(employee.get("name")) > len(long_name):
            long_name = employee["name"]
    return long_name


def get_manager_pay(company):
    total = 0
    for person in company:
        if person.get("position") == "manager":
            total += person.get("rate") * person.get("hours")
    return total


def who_made_the_most(company):
    made_most = ""
    most_money = 0
    for employee in company:
        money = employee.get("rate") * employee.get("hours")
        if money > most_money:
            made_most = employee.get("name")
            most_money = money
    return made_most


company1 = [
    {"name": "leah", "position": "manager", "rate": 55, "hours": 15},
    {"name": "freddy", "position": "manager", "rate": 25, "hours": 30},
    {"name": "isaac", "rate": 20, "hours": 20},
    {"name": "murphey", "position": "worker", "rate": 41, "hours": 25},
    {"name": "phil", "position": "worker", "rate": 9, "hours": 45},
]

print(who_made_the_most(company1))


def letter_occurences(str):
    result = ""
    cache = {}
    for letter in str:
        if letter != " ":
            if letter not in cache:
                cache[letter] = 0
            cache[letter] += 1
    for key in cache:
        result += f"There are {cache[key]} {key}'s. "
    return result


nums = [2, 4, 6, 8, 10, 12, 3, 5, 6, 6, 7, 8, 9, 7, 5, 5, 89, 8, 6, 78, 9, 87, 5]


def remove_duplicates(lst):
    cache = {}
    result = []
    for item in lst:
        if item not in cache:
            cache[item] = True
            result.append(item)
    return result


print(remove_duplicates(nums))


# Pretty Printing
# to make your dictionaries and nested lists easy to read, you can add this to the top of your code.


def using_if_variable_in_dictionary(my_dict4):
    result4 = []
    for key in my_dict4.keys():
        if key in my_dict4:
            result4.append(key)
    return result4


my_dict4 = {"a": 1, "b": 2, "c": 3}
print(using_if_variable_in_dictionary(my_dict4))

example = {
    "a": 0,
    "b": 4,
    "c": "x",
    "d": "",
    "e": True,
    "f": False,
    "g": [1, 2, 3],
    "h": [],
    "i": {"a_key": "a value"},
    "j": {},
    "k": None,
}
print(using_if_variable_in_dictionary(example))

# OUTPUT ==> ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']


students = [
    "Stan",
    "Kyle",
    "Cartman",
    "Kenny",
    "Butters",
    "Craig",
    "Clyde",
    "Tweek",
    "Tolken",
    "Wendy",
    "Bebe",
    "Jimmy",
    "Timmy",
]

sent_attendance_token = [
    "Stan",
    "Kyle",
    "Butters",
    "Craig",
    "Tweek",
    "Tolken",
    "Wendy",
    "Bebe",
    "Jimmy",
    "Timmy",
]

did_exploration = [
    "Butters",
    "Craig",
    "Kyle",
    "Tweek",
    "Tolken",
    "Wendy",
    "Bebe",
    "Jimmy",
    "Timmy",
]

finished_project = [
    "Stan",
    "Cartman",
    "Butters",
    "Craig",
    "Tweek",
    "Tolken",
    "Wendy",
    "Jimmy",
]

failed_assessment = ["Cartman", "Kenny", "Clyde", "Butters"]


def who_is_absent(students, sent_tokens):
    cache = {}
    absent = []
    for student in students:
        cache[student] = True
    for token in sent_tokens:
        cache[token] = False
    for kid in cache:
        if cache.get(kid):
            absent.append(kid)
    return absent


print(who_is_absent(students, sent_attendance_token))

# OUTPUT ==>  ['Cartman', 'Kenny', 'Clyde']


def who_skipped_the_exploration(students, exploration):
    cache = {}
    did_not_do_exploration = []
    for name in exploration:
        cache[name] = True
    for student in students:
        if not cache.get(student):
            did_not_do_exploration.append(student)
    return did_not_do_exploration


print(who_skipped_the_exploration(students, did_exploration))

# OUTPUT ==>  ['Stan', 'Cartman', 'Kenny', 'Clyde']


def who_finished_project_and_passed_assessment(projects, assessments):
    cache = {}
    passed_both = []
    for project in projects:
        cache[project] = True
    for assessment in assessments:
        cache[assessment] = False
    for student in cache:
        if cache.get(student):
            passed_both.append(student)
    return passed_both


print(who_finished_project_and_passed_assessment(finished_project, failed_assessment))

# OUTPUT ==>  ['Stan', 'Craig', 'Tweek', 'Tolken', 'Wendy', 'Jimmy']


# Create a fxn named “double_index” with two parameters: a list and an index number. The fxn should double the value of the list element at the specified index and return the list with the doubled value.
# If the index is not a valid index, the fxn should return the original list.

# Input: ([3,8,-10,12], 2) => Output: [3,8,-20,12]
# Input: ([3,8,-10,12], 6) => Output: [3,8,-10,12]


def double_index(list, index):
    if index < 0 or index > len(list):
        return list

    list[index] = list[index] * 2
    return list


list_nums = [3, 8, -10, 12]
index_num = 2
print(double_index(list_nums, index_num))


# Create a fxn named “remove_middle” which has three parameters: a list, a start number, an end number. The fxn should return a sub-list of the list containing all of the elements between the start and end indexes.
def remove_middle(list, start, end):
    end = end + 1
    return list[start:end]


print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))


# Create a fxn named “more_than_n” that has three parameters: a list, an item, and a number. The fxn should return “True” if the item appears more then the number of times specified. Otherwise, the fxn should return “False”.
def more_than_n(list, item, num):
    count = list.count(item)
    if count > num:
        return True
    else:
        return False


print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))


# Create a fxn named “most_frequent_item” that has three parameters: a list, a first item, a second item. Return either the first item or the second item depending on which occurs more often in the list. If the two items appear the same number of times, return the first item.
def most_frequent_item(list, first, second):
    count1 = list.count(first)
    count2 = list.count(second)

    if count2 > count1:
        return second
    else:
        return first


print(most_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))


# Create a fxn named “middle_element” that has one parameter: a list. If there are an odd number of elements in the list, return the middle element. If there are an even number, return the average of the middle elements.


def middle_element(list):
    middle = int(len(list) / 2)
    if len(list) % 2 != 0:
        return list[middle]
    else:
        avg = (list[middle] + list[middle - 1]) / 2
        return avg


print(middle_element([5, 2, -10, -4, 4, 5]))
print(
    middle_element(
        [
            5,
            2,
            -10,
            -4,
            4,
        ]
    )
)


# Create a fxn named “append_sum” that has one parameter: a list. The fxn should add the last two elements of the list together and add the result to the end of the list. It should perform this process three times and then return the list.


def append_sum(list):
    for i in range(3):
        sum = list[-1] + list[-2]
        list.append(sum)
    return list


print(append_sum([1, 1, 2]))


# Create a fxn named “combine_sort” that has two parameters: two lists. The fxn should combine the two lists into a new list, sort the result, and then return the new list.


def combine_sort(list11, list19):
    list11 += list19
    return list11


print(combine_sort)
