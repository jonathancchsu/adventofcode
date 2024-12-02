with open('input.txt', 'r') as file:
    data = file.read()
# print(data)

first_numbers = []
second_numbers = []

for line in data.strip().split('\n'):  # Strip whitespace and split by newline
    num1, num2 = line.split()  # Split by space (default)
    first_numbers.append(int(num1))  # Convert to int and add to the first list
    second_numbers.append(int(num2))  # Convert to int and add to the second list

# print(first_numbers)
# print(second_numbers)

first_numbers.sort()
second_numbers.sort()
distances = [abs(a - b) for a, b in zip(first_numbers, second_numbers)]
# print(distances)
# print(sum(distances))

similarity = 0

for num in first_numbers:
    similarity += num * second_numbers.count(num)

print(similarity)