# Day 6
# Enter your code here. Read input from STDIN. Print output to STDOUT
runs = int(input())

for run in range(0, runs):
    even_string = []
    odd_string = []
    input_str = input()

    for r in range(len(input_str)):
        if r % 2 == 0:
            even_string.append(input_str[r])
        else:
            odd_string.append(input_str[r])

    print(''.join([str(elem) for elem in even_string]) +
          " " + ''.join([str(elem) for elem in odd_string]))
