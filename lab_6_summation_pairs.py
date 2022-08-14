numbers = input().split(' ')
target_number = int(input())
total_iterations = 0
pairs = {}

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        total_iterations += 1
        n1 = int(numbers[i])
        n2 = int(numbers[j])
        current_sum = n1 + n2
        if current_sum == target_number:
            print(f"{n1} + {n2} = {target_number}")
            pairs[n1] = n2
print(f'Iterations done: {total_iterations}')
for num1, num2 in pairs.items():
    print(f'({num1}, {num2})')


