import re

with open('input.txt', 'r') as file:
# with open('example.txt', 'r') as file:
  data = file.read()
input_string = data
# input_string = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

# Patterns for do(), don't(), and valid mul(x, y)
valid_mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
dont_pattern = r"don't\(\)"
do_pattern = r"do\(\)"

# Compile patterns
mul_re = re.compile(valid_mul_pattern)
dont_re = re.compile(dont_pattern)
do_re = re.compile(do_pattern)

# Parse sequentially
state = "count"  # Start in "count" mode
matches = []

# Tokenize and process valid patterns
tokens = re.split(r"(do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\))", input_string)
for token in tokens:
    token = token.strip()  # Remove whitespace
    if dont_re.match(token):
        state = "ignore"
    elif do_re.match(token):
        state = "count"
    elif state == "count" and mul_re.match(token):
        matches.append(mul_re.match(token).groups())  # Extract numbers from mul(x, y)

# Calculate the sum of products
products_sum = sum(int(x) * int(y) for x, y in matches)

print(f"Matches: {matches}")
print(f"Sum of products: {products_sum}")
