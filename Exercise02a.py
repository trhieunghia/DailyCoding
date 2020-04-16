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
    array_multiplication = 1

    for element in array_number:
        array_multiplication *= element

    for element in array_number:
        new_array.append(int(array_multiplication / element))

    return new_array


print("Origin array: ", array)
print("New array: ", convert_array(array))
