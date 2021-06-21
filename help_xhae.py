tc = int(input())

number_dict = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'ten': 10
}

def calculate(n1, n2, op):
    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2
    elif op == '/':
        return 11
    elif op == '*':
        return n1 * n2
tc_q = []
for _ in range(tc):
    tc_q.append(input().split(' '))

for q in tc_q:
    left, op, right, _, answer = q

    n_left = number_dict[left]
    n_right = number_dict[right]

    real_answer = calculate(n_left, n_right, op)

    if 0 <= real_answer <= 10:
        real_answer = list(number_dict.keys())[real_answer]
        answer = sorted(answer)
        real_answer = sorted(real_answer)
        print(answer, real_answer)
        if answer == real_answer:
            print('Yes')
        else:
            print('No')
    else:
        print('No')


# 16
# two + one = there
# three + four = svene
# one * three = four
# four * two = eigth
# five * five = two
# five * five = hello
# three + four = svnnn
# three + four = svnne
# three * four = two
# eight + one = nine
# eight + one = nien
# four + three = three
# four - one = teerh
# seven * one = svene
# ten - three = seven
# ten - three = seven

# Y, Y, N, Y, N, N, N, N, N, Y, Y, N, Y, Y, Y, Y
