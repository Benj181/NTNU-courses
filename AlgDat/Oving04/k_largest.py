import random

generate_random_tests = False
random_tests = 10
numbers_lower = 10
numbers_upper = 10
seed = 0

def k_largest(A, n, k):
    import random as rd
    if not A:
        return []
    
    def partition(A, p, r):
        i = rd.randint(p, r)
        A[r], A[i] = A[i], A[r]
        x = A[r]
        i = p - 1
        for j in range(p, r):
            if A[j] <= x:
                i += 1 
                A[j], A[i] = A[i], A[j]
        A[i+1], A[r] = A[r], A[i+1]
        return i+1


    def select(A, p, r, i):
        if p == r:
            return A[p:]
        q = partition(A, p, r)
        k = q - p + 1
        if i == k:
            return A[q:]
        elif i < k:
            return select(A, p, q-1, i)
        else:
            return select(A, q+1, r, i-k)
        
    if n ==1:
        if k == 0: return []
        else: return A
    return select(A, 0, n-1, n-k+1)


# A = [5, 8, 11, 4, 5, 1, 17, 1, 12, 13]
# B = k_largest(A, 10, 4)
# print(f"A: {A}")
# print(f"B: {B}")
# Sett med hardkodete tester pÃ¥ format: (A, k)
tests = [
    ([], 0),
    ([1], 0),
    ([1], 1),
    ([1, 2], 1),
    ([-1, -2], 1),
    ([-1, -2, 3], 2),
    ([1, 2, 3], 2),
    ([3, 2, 1], 2),
    ([3, 3, 3, 3], 2),
    ([4, 1, 3, 2, 3], 2),
    ([4, 5, 1, 3, 2, 3], 4),
    ([9, 3, 6, 1, 7, 3, 4, 5], 4),
]

def gen_examples(k, lower, upper):
    for _ in range(k):
        A = [
                random.randint(-50, 50)
                for _ in range(random.randint(lower, upper))
            ]
        yield A, random.randint(0, len(A))


if generate_random_tests:
    if seed:
        random.seed(seed)
    tests += list(gen_examples(
        random_tests,
        numbers_lower,
        numbers_upper,
    ))

failed = False
for A, k in tests:
    answer = sorted(A, reverse=True)[:k][::-1]
    student = k_largest(A[:], len(A), k)

    if type(student) != list:
        if failed:
            print("-"*50)
        failed = True
        print(f"""
Koden feilet for fÃ¸lgende instans:
A: {A}
n: {len(A)}
k: {k}

Metoden mÃ¥ returnere en liste
Ditt svar: {student}
""")
    else:
        student.sort()
        if student != answer:
            if failed:
                print("-"*50)
            failed = True
            print(f"""
Koden feilet for fÃ¸lgende instans:
A: {A}
n: {len(A)}
k: {k}

Ditt svar: {student}
Riktig svar: {answer}
""")

if not failed:
    print("Koden ga riktig svar for alle eksempeltestene")

