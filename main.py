import math

number_list = []
m = 2147483647
x0 = 123457
a = 16807
c = 0
# Linear Congruential Method for Generating Random Numbers
for i in range(100):
    x1 = ((a * x0) + c) % m
    # print("x -", i + 1, ":", x1)
    R = round(x1 / m, 3)
    number_list.append(R)
    # print("R -", i + 1, ":", number_list[i])

    i += 1
    x0 = x1
print(number_list)
print("Number List:")
number_list_printer = 0

for i in range(0, 10):
    print(number_list[number_list_printer:number_list_printer+10])  # to see numbers in the list
    number_list_printer += 10

N = len(number_list)
counter = 0
number = 0
list_indice = 1
status = 0
previous_status = 0
run = 0
critical_value = 1.96
# Runs up and down method
for counter in number_list:
    if number == 0:
        current = number_list[list_indice]
        before = number_list[list_indice - 1]
        if number_list[list_indice] < number_list[list_indice - 1]:
            status = 1
            previous_status = status
        elif number_list[list_indice] > number_list[list_indice - 1]:
            status = 2
            previous_status = status
        run += 1
        number += 1
        list_indice += 1
    else:
        while number_list[list_indice - 1] != 0.373:
            before = number_list[list_indice - 1]
            current = number_list[list_indice]

            if number_list[list_indice] < number_list[list_indice - 1]:
                status = 1
                if previous_status != status:
                    run += 1
                else:
                    pass
            elif number_list[list_indice] > number_list[list_indice - 1]:
                status = 2
                if previous_status != status:
                    run += 1
                else:
                    pass

            number += 1
            list_indice += 1
            counter += 1
            previous_status = status

mean_value = ((2 * N) - 1) / 3
variance_square = ((16 * N) - 29) / 90
variance = math.sqrt(variance_square)
Z = (run - mean_value) / variance
print("\nResults")
print("Run Value:", run)
print("Mean Value:", round(mean_value, 2))
print("Variance Sqaure:", round(variance_square, 2))
print("Variance:", round(variance, 3))
print("Z:", round(Z, 3))

if -critical_value <= Z <= critical_value:
    print("Failure to reject the hypothesis of indepence occurs ")
else:
    print("Hypothesis is rejected")
