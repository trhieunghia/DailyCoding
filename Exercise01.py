# Given a list of numbers and a number k.
# Return whether any two numbers from the list add up to k.
#
# For example:
# Give [1,2,3,4] and k of 7
# Return true since 3 + 4 is 7


def input_array():
    print("Len of array = ", end='')
    array_len = int(input())
    print()

    array = []
    for i in range(array_len):
        print("Value of array[{}] = ".format(i), end='')
        element = int(input())
        array.append(element)
    print("Array is: ", array)
    return array


def input_k():
    print("\nk = ", end='')
    k = int(input())
    return k


def have_two_element_up_to_k(numbers, k):
    for i in range(0, len(numbers) - 1):
        for j in range(1, len(numbers)):
            if numbers[i] + numbers[j] == k:
                return True
    return False


def main_program():
    numbers = input_array()
    k = input_k()
    print("\nResult: ", have_two_element_up_to_k(numbers, k))


main_program()
