# Given an array of integers,
# return a new array
# such that each element at index i of the new array
# is the product of all the numbers in the original array except the one at i.
#
# For example, if our input was [1, 2, 3, 4, 5],
# the expected output would be [120, 60, 40, 30, 24].
#
# If our input was [3, 2, 1],
# the expected output would be [2, 3, 6].

array = [1, 2, 3, 4]


def convert_array(array_number):
    new_array = []

    for element_01 in array_number:
        new_element = 1
        for element_02 in array_number:
            if element_01 != element_02:
                new_element *= element_02
        new_array.append(new_element)

    return new_array


print("Origin array: ", array)
print("New array: ", convert_array(array))
