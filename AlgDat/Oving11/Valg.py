# !/usr/bin/python3
# coding=utf-8

# Testsettet på serveren er større og mer omfattende enn dette.
# Hvis programmet ditt fungerer lokalt, men ikke når du laster det opp,
# er det gode sjanser for at det er tilfeller du ikke har tatt høyde for.

# De lokale testene består av to deler. Et lite sett med hardkodete
# instanser som kan ses lengre nede, og muligheten for å teste på
# et større sett med 500 genererte instanser. For å teste på det
# større settet med genererte instanser, må du (1) laste ned filen med
# testene fra øvingssystemet, (2) legge den samme plass som denne
# python-filen og (3) sette variabelen under til True. Merk at det kan
# ta litt tid å kjøre alle de 500 ekstra testene.
use_extra_tests = False


def schulze_method(W, n):
    # Step 1: Compute strongest paths using modified Floyd-Warshall
    # p[i][j] = strength of strongest path from i to j
    p = [[0] * n for _ in range(n)]
    
    # Initialize: direct paths have strength w(i,j) if w(i,j) > w(j,i)
    for i in range(n):
        W_i = W[i]  # Cache row
        p_i = p[i]  # Cache row
        for j in range(n):
            if i != j and W_i[j] > W[j][i]:
                p_i[j] = W_i[j]
    
    # Modified Floyd-Warshall with optimizations
    for k in range(n):
        p_k = p[k]  # Cache k-th row
        for i in range(n):
            p_i = p[i]  # Cache i-th row
            p_ik = p_i[k]  # Cache p[i][k]
            if p_ik > 0:  # Skip if no path from i to k
                for j in range(n):
                    p_kj = p_k[j]
                    if p_kj > 0:  # Skip if no path from k to j
                        # p[i][j] = max(p[i][j], min(p[i][k], p[k][j]))
                        new_strength = min(p_ik, p_kj)
                        if new_strength > p_i[j]:
                            p_i[j] = new_strength
    
    # Step 2: Pre-compute comparison results to avoid repeated lookups
    # beats[i] = set of candidates that i beats (p[i][j] > p[j][i])
    # unbeaten_by[i] = set of candidates that don't beat i (p[i][j] >= p[j][i])
    beats = [set() for _ in range(n)]
    unbeaten_by = [set() for _ in range(n)]
    
    for i in range(n):
        p_i = p[i]
        for j in range(n):
            if i != j:
                if p_i[j] > p[j][i]:
                    beats[i].add(j)
                if p_i[j] >= p[j][i]:
                    unbeaten_by[i].add(j)
    
    # Step 3: Select winners efficiently
    result = []
    remaining = set(range(n))
    
    while remaining:
        # Rule 1: Find candidate u where p(u,v) > p(v,u) for all other v
        winner = None
        
        for u in remaining:
            remaining_minus_u = remaining - {u}
            if beats[u] >= remaining_minus_u:  # Set comparison is fast
                winner = u
                break
        
        if winner is not None:
            result.append(winner)
            remaining.remove(winner)
            continue
        
        # Rule 2: Among candidates where p(u,v) >= p(v,u) for all v,
        # pick the one with most strict wins
        best_candidate = None
        best_strict_wins = -1
        
        for u in sorted(remaining):
            remaining_minus_u = remaining - {u}
            if unbeaten_by[u] >= remaining_minus_u:
                strict_wins = len(beats[u] & remaining_minus_u)
                
                if strict_wins > best_strict_wins:
                    best_strict_wins = strict_wins
                    best_candidate = u
        
        if best_candidate is not None:
            result.append(best_candidate)
            remaining.remove(best_candidate)

    return result


# Hardkodete tester på format: (W, svar)
tests = [
    ([[0]], [0]),
    ([[0, 1], [3, 0]], [1, 0]),
    ([[0, 2], [2, 0]], [0, 1]),
    ([[0, 4, 3], [2, 0, 2], [3, 4, 0]], [0, 2, 1]),
    ([[0, 2, 1], [4, 0, 4], [5, 2, 0]], [1, 2, 0]),
    (
        [
            [0, 1, 3, 3, 3],
            [9, 0, 5, 5, 7],
            [7, 5, 0, 5, 4],
            [7, 5, 5, 0, 6],
            [7, 3, 6, 4, 0],
        ],
        [1, 3, 4, 2, 0],
    ),
    (
        [
            [0, 6, 7, 8, 7, 8],
            [6, 0, 6, 8, 7, 8],
            [5, 6, 0, 6, 5, 7],
            [4, 4, 6, 0, 5, 6],
            [5, 5, 7, 7, 0, 6],
            [4, 4, 5, 6, 6, 0],
        ],
        [0, 1, 4, 2, 3, 5],
    ),
]


def validate(student, answer):
    try:
        len(student)
    except:
        return "Koden returnerte ikke en liste"

    if len(student) != len(answer):
        return "Listen inneholder ikke riktig antall kandidater"

    if set(student) != set(answer):
        return "Listen inneholder ikke alle kandidatene"

    if any(a != b for a, b in zip(student, answer)):
        return "En eller flere av kandidatene opptrer i feil rekkefølge"


def generate_feedback(test, expected, student):
    feedback = ""
    feedback += "Koden din feilet for input\n"
    feedback += str(test) + "\n"
    feedback += "Ditt svar er\n"
    feedback += str(student) + ",\n"
    feedback += "men riktig svar er\n"
    feedback += str(expected) + "."
    return feedback


table_format = lambda T: "\n    " + "\n    ".join(map(str, T))
failed = False
for W, answer in tests:
    student = schulze_method([row[:] for row in W], len(W))
    feedback = validate(student, answer)
    if feedback is not None:
        if failed:
            print("-"*50)
        failed = True
        print(f"""
Koden feilet for følgende instans.
W: {table_format(W)}
n: {len(W)}

Ditt svar: {student}
Riktig svar: {answer}
Feedback: {feedback}
""")

if use_extra_tests:
    with open("tests_schulze_method.txt") as extra_tests_data:
        extra_tests = []
        for line in extra_tests_data:
            W, answer = map(eval, line.strip().split(" | "))
            extra_tests.append((W, answer))

    n_failed = 0
    for W, answer in extra_tests:
        student = schulze_method([row[:] for row in W], len(W))
        feedback = validate(student, answer)
        if feedback is not None:
            n_failed += 1
            if failed and n_failed <= 5:
                print("-"*50)

            failed = True
            if n_failed <= 5:
                print(f"""
Koden feilet for følgende instans.
W: {table_format(W)}
n: {len(W)}

Ditt svar: {student}
Riktig svar: {answer}
Feedback: {feedback}
""")
            elif n_failed == 6:
                print("Koden har feilet for mer enn 5 av de ekstra testene.")
                print("De resterende feilene vil ikke skrives ut.")

    if n_failed > 0:
        print(f"Koden feilet for {n_failed} av de ekstra testene.")

if not failed:
    print("Koden din passerte alle eksempeltestene.")