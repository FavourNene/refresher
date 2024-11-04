fibonacci_sequence = [0, 1]
while len(fibonacci_sequence) < 51:
    next_num = fibonacci_sequence[-1] + fibonacci_sequence[-2]
    fibonacci_sequence.append(next_num)
print("THIS IS A LIST OF THE FIRST 50 NUMBERS IN THE FIBONACCI SEQUENCE:")
for i in fibonacci_sequence:
    print(str(i) + '\n')
