with open('input.txt', 'r') as file:
# with open('example.txt', 'r') as file:
  data = file.read()

lines = data.splitlines()

def valid_sequence(numbers, ascending):
  if ascending:
    return all(numbers[i] < numbers[i + 1] and abs(numbers[i] - numbers[i + 1]) <= 3 for i in range(len(numbers) - 1))
  else:
    return all(numbers[i] > numbers[i + 1] and abs(numbers[i] - numbers[i + 1]) <= 3 for i in range(len(numbers) - 1))

count = 0

for line in lines:
  numbers = list(map(int, line.split()))
    
  if valid_sequence(numbers, True) or valid_sequence(numbers, False):
    count += 1
  else:
    for i in range(len(numbers)):
      new_numbers = numbers[:i] + numbers[i + 1:]
      if valid_sequence(new_numbers, True) or valid_sequence(new_numbers, False):
        count += 1
        break  

print(count)
