import random
# Testsettet pÃ¥ serveren er stÃ¸rre og mer omfattende enn dette.
# Hvis programmet ditt fungerer lokalt, men ikke nÃ¥r du laster det opp,
# er det gode sjanser for at det er tilfeller du ikke har tatt hÃ¸yde for.

# De lokale testene bestÃ¥r av to deler. Et sett med hardkodete
# instanser som kan ses lengre nede, og muligheten for Ã¥ generere
# tilfeldig instanser. Genereringen av de tilfeldige instansene
# kontrolleres ved Ã¥ juste pÃ¥ verdiene under.

# Kontrollerer om det genereres tilfeldige instanser.
generate_random_tests = True
# Antall tilfeldige tester som genereres
random_tests = 10
# Lavest mulig antall verdier i generert instans.
n_lower = 3
# HÃ¸yest mulig antall verdier i generert instans.
n_upper = 10
# Om denne verdien er 0 vil det genereres nye instanser hver gang.
# Om den er satt til et annet tall vil de samme instansene genereres
# hver gang, om verdiene over ikke endres.
seed = 0

def find_maximum(x):
    if not x:
        raise ValueError("Empty array has no maximum")

    def bisect(A, p, r):
        if r - p > 1:
            q = (p + r) // 2
            ap, ar, aq = A[p], A[r], A[q]
            if max(ap,ar,aq) == aq:
                if A[q+1] > aq: 
                    return bisect(A, q, r)
                else: 
                    return bisect(A, p, q)
            else:
                if ar > ap: 
                    return bisect(A, q, r)
                else: 
                    return bisect(A, p, q)
                
        return A[p] if A[p] > A[r] else A[r]
    return bisect(x, 0, len(x) - 1)

# def find_maximum(x):
#     if not x:
#         raise ValueError("Empty array has no maximum")

#     def bisect(A, p, r):
#         while r - p > 1:
#             q = (p + r) // 2
#             ap, aq, ar = A[p], A[q], A[r]
#             if aq > ap and aq > ar:
#                 if A[q + 1] > aq:
#                     p = q
#                 else:
#                     r = q
#             else:
#                 if ap > ar:
#                     r = q
#                 else:
#                     p = q

#         return A[p] if A[p] > A[r] else A[r]
#     return bisect(x, 0, len(x) - 1)


# Hardkodete tester pÃ¥ format: (x, svar)
tests = [
    # ([1], 1),
    # ([1, 3], 3),
    # ([3, 1], 3),
    # ([1, 2, 1], 2),
    # ([1, 0, 2], 2),
    # ([2, 0, 1], 2),
    # ([0, 2, 1], 2),
    # ([0, 1, 2], 2),
    # ([2, 1, 0], 2),
    # ([2, 3, 1, 0], 3),
    # ([2, 3, 4, 1], 4),
    # ([2, 1, 3, 4], 4),
    # ([4, 2, 1, 3], 4),
    ([52, 59, 67, 70, 71, 80, 81, 82, 85, 88, 93, 99, 68, 12, 15, 18, 28, 35, 40, 50], 99),
]

# En liste som ikke kan skrives til
class List:
    def __init__(self, li):
        self.__internal_list = li

    def __getitem__(self, key):
        return self.__internal_list[key]

    def __len__(self):
        return len(self.__internal_list)

    def __setitem__(self):
        raise NotImplementedError(
            "Du skal ikke trenge Ã¥ skrive til listen"
        )
    def __str__(self):
        return str(self.__internal_list)

# Genererer tilfeldige instanser med svar
def generate_examples(k, nl, nu):
    for _ in range(k):
        n = random.randint(nl, nu)
        x = random.sample(range(5*n), k=n)
        answer = max(x)
        t = x.index(answer)
        x = sorted(x[:t]) + [answer] + sorted(x[t + 1:], reverse=True)
        t = random.randint(0, n)
        x = x[t:] + x[:t]
        yield x, answer


if generate_random_tests:
    if seed:
        random.seed(seed)

    tests.extend(generate_examples(random_tests, n_lower, n_upper))


failed = False
for x, answer in tests:
    x_ro = List(x[:])
    student = find_maximum(x_ro)
    if student != answer:
        if failed:
            print("-"*50)

        failed = True

        print(f"""
Koden ga feil svar for fÃ¸lgende instans:
x: {x}

Ditt svar: {student}
Riktig svar: {answer}
""")

if not failed:
    print("Koden ga riktig svar for alle eksempeltestene")