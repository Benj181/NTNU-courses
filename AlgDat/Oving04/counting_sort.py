import random

generate_random_tests = False
random_tests = 10
numbers_lower = 3
numbers_upper = 8
seed = 0


def counting_sort(A, n):
    if A:
        k = max(A) + 1
        B = [0]*n
        C = [0]*k     
        for j in range(0, n):
            C[A[j]] += 1
        for i in range(1, k):
            C[i] += C[i-1]
        for j in range(0, n):
            B[C[A[n-j-1]]-1] = A[n-j-1]
            C[A[n-j-1]] -= 1
        return B
    else:
        return []

# print(counting_sort([0,0,995, 334, 709, 999, 502, 303, 274, 488, 997, 568, 546, 756], 14))
# Hardkodete tester
tests = [
    [],
    [1],
    [1, 2, 3, 4],
    [4, 3, 2, 1],
    [1, 1, 2, 1],
    [1281, 1, 2],
    [0, 2047, 0, 2047],
    [995, 334, 709, 999, 502, 303, 274, 488, 997, 568, 546, 756],
    [648, 298, 568, 681, 795, 356, 603, 772, 373, 50, 253, 116],
]

def gen_examples(k, lower, upper):
    for _ in range(k):
        yield [
                random.randint(0, 2047)
                for _ in range(random.randint(lower, upper))
            ]


if generate_random_tests:
    if seed:
        random.seed(seed)
    tests += list(gen_examples(
        random_tests,
        numbers_lower,
        numbers_upper,
    ))

failed = False
for A in tests:
    answer = sorted(A)
    student = counting_sort(A[:], len(A))
    if student != answer:
        if failed:
            print("-"*50)
        failed = True
        print(f"""
Koden feilet for fÃ¸lgende instans:
A: {A}
n: {len(A)}

Ditt svar: {student}
Riktig svar: {answer}
""")

if not failed:
    print("Koden ga riktig svar for alle eksempeltestene")