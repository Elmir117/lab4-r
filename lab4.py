numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


with open('all_numbers.txt', 'w') as file:
    for number in numbers:
        file.write(f"{number}\n")


even_numbers_doubled = []
with open('all_numbers.txt', 'r') as file:
    for line in file:
        number = int(line.strip())
        if number % 2 == 0:
            even_numbers_doubled.append(number * 2)

with open('doubled_even_numbers.txt', 'w') as file:
    total = sum(even_numbers_doubled)
    count = len(even_numbers_doubled)
    if count > 0:
        average = total / count
    else:
        average = 0

    for number in even_numbers_doubled:
        file.write(f"{number}\n")
    file.write(f"Average: {average}\n")

print(f"Cüt nömrəsi olan ədədlərin 2 dəfə artırılmış qiymətlərinin ədədi ortası: {average}")