integer_list = []
floats_list = []

for question in range(2):
    integer_list.append(int(input('Type a integer number: ')))
    if question == 1:
        floats_list.append(float(input('Type a float number: ')))

operation_1 = (integer_list[0] * 2) * (integer_list[1] / 2)
operation_2 = (integer_list[0] * 3) + floats_list[0]
operation_3 = floats_list[0] ** 3

print(round(operation_1, 2))
print(round(operation_2, 2))
print(round(operation_3, 2))
