def print_positive_numbers(input_list):
    positive_numbers = [num for num in input_list if num > 0]
    return positive_numbers

list1 = [12, -7, 5, 64, -14]
list2 = [12, 14, -95, 3]

out1 = print_positive_numbers(list1)
out2 = print_positive_numbers(list2)


print("Input:", "list1 =", list1, "Output:", out1)
print("Input:", "list2 =", list2, "Output:", out2)
