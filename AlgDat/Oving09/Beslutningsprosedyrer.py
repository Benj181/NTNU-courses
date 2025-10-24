# !/usr/bin/python3
# coding=utf-8

# Testsettet på serveren er større og mer omfattende enn dette.
# Hvis programmet ditt fungerer lokalt, men ikke når du laster det opp,
# er det gode sjanser for at det er tilfeller du ikke har tatt høyde for.

# De lokale testene består av to deler. Et lite sett med hardkodete
# instanser som kan ses lengre nede, og muligheten for å teste på
# et større sett med 1000 genererte instanser. For å teste på det
# større settet med genererte instanser, må du (1) laste ned filen med
# testene fra øvingssystemet, (2) legge den samme plass som denne
# python-filen og (3) sette variabelen under til True.
use_extra_tests = False


def check(variables, constraints):
    # Use DSU to group variables that must be equal
    parent = {}
    
    def find(x):
        if x not in parent:
            parent[x] = x
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        px, py = find(x), find(y)
        if px != py:
            parent[px] = py
    
    # Initialize all variables
    for var in variables:
        find(var)
    
    # Process equality constraints first
    eq_constraints = []
    ineq_constraints = []
    
    for a, comp, b in constraints:
        if comp == "=":
            eq_constraints.append((a, b))
        else:
            ineq_constraints.append((a, comp, b))
    
    # Union all variables that must be equal
    for a, b in eq_constraints:
        union(a, b)
    
    # Build adjacency list for inequality constraints between equivalence classes
    from collections import defaultdict, deque
    
    # Check for contradictions in inequality constraints
    for a, comp, b in ineq_constraints:
        ra, rb = find(a), find(b)
        
        # If two variables must be equal but have strict inequality, contradiction
        if ra == rb and comp in ("<", ">"):
            return False
    
    # Build directed graph of strict inequalities between equivalence classes
    # Edge from u to v means u < v
    graph = defaultdict(set)
    
    for a, comp, b in ineq_constraints:
        ra, rb = find(a), find(b)
        
        if ra == rb:
            continue  # Already handled above
        
        if comp == "<":
            graph[ra].add(rb)
        elif comp == ">":
            graph[rb].add(ra)
    
    # Check for cycles using topological sort (Kahn's algorithm)
    # If there's a cycle, the constraints are unsatisfiable
    in_degree = defaultdict(int)
    all_nodes = set()
    
    for u in graph:
        all_nodes.add(u)
        for v in graph[u]:
            all_nodes.add(v)
            in_degree[v] += 1
    
    # Start with nodes having in-degree 0
    queue = deque([node for node in all_nodes if in_degree[node] == 0])
    processed = 0
    
    while queue:
        node = queue.popleft()
        processed += 1
        
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # If we processed all nodes, no cycle; otherwise there's a cycle
    return processed == len(all_nodes)


# Hardkodete tester på format: (variables, constraints), riktig svar
tests = [
    ((["x1"], []), True),
    ((["x1", "x2"], [("x1", "=", "x2")]), True),
    ((["x1"], [("x1", ">", "x1")]), False),
    ((["x1"], [("x1", "=", "x1")]), True),
    ((["x1", "x2"], [("x1", "<", "x2")]), True),
    ((["x1", "x2"], [("x2", "<", "x1"), ("x1", "=", "x2")]), False),
    ((["x1", "x2"], [("x2", ">", "x1"), ("x1", "<", "x2")]), True),
    ((["x1", "x2"], [("x1", ">", "x2"), ("x2", ">", "x1")]), False),
    (
        (
            ["x1", "x2", "x3"],
            [("x1", "<", "x2"), ("x2", "<", "x3"), ("x1", ">", "x3")],
        ),
        False,
    ),
    (
        (
            ["x1", "x2", "x3"],
            [("x1", "<", "x2"), ("x3", "=", "x1"), ("x2", "<", "x3")],
        ),
        False,
    ),
    ((["x4", "x0", "x1"], [("x1", "<", "x0")]), True),
    ((["x5", "x8"], [("x8", "<", "x5"), ("x8", "<", "x5")]), True),
    ((["x1", "x0", "x2"], []), True),
    (
        (
            ["x4", "x8", "x5"],
            [("x4", "<", "x5"), ("x8", ">", "x5"), ("x5", "<", "x8")],
        ),
        True,
    ),
    (
        (
            ["x5", "x9", "x0"],
            [
                ("x9", ">", "x5"),
                ("x9", "=", "x0"),
                ("x0", "=", "x9"),
                ("x0", "=", "x9"),
            ],
        ),
        True,
    ),
    (
        (
            ["x0", "x6", "x7"],
            [("x7", "=", "x0"), ("x7", ">", "x0"), ("x6", ">", "x0")],
        ),
        False,
    ),
    ((["x8", "x6", "x0"], []), True),
    (
        (
            ["x8", "x7", "x0"],
            [("x8", "=", "x0"), ("x0", "=", "x8"), ("x0", "=", "x8")],
        ),
        True,
    ),
    (
        (
            ["x8", "x4"],
            [
                ("x4", ">", "x8"),
                ("x4", ">", "x8"),
                ("x8", "<", "x4"),
                ("x4", ">", "x8"),
                ("x8", "=", "x4"),
            ],
        ),
        False,
    ),
    ((["x3", "x8", "x5"], [("x3", ">", "x8")]), True),
]


failed = False
for test_case, answer in tests:
    variables, constraints = test_case
    student = check(variables, constraints)
    if student != answer:
        if failed:
            print("-"*50)
        failed = True
        print(f"""
Koden feilet for følgende instans:
variables: {', '.join(variables)}
constraints:
    {(chr(10) + '    ').join(' '.join(x) for x in constraints)}

Ditt svar: {student}
Riktig svar: {answer}
""")

if use_extra_tests:
    with open("tests_theory_solver.txt") as extra_tests_data:
        extra_tests = []
        for line in extra_tests_data:
            variables, constraints, answer = line.strip().split(" | ")
            variables = variables.split(",")
            constraints = [x.split(" ") for x in constraints.split(",")]
            extra_tests.append(((variables, constraints), bool(int(answer))))

    n_failed = 0
    for test_case, answer in extra_tests:
        variables, constraints = test_case
        student = check(variables, constraints)
        if student != answer:
            n_failed += 1
            if failed and n_failed <= 5:
                print("-"*50)

            failed = True
            if n_failed <= 5:
                print(f"""
Koden feilet for følgende instans:
variables: {', '.join(variables)}
constraints:
    {(chr(10) + '    ').join(' '.join(x) for x in constraints)}

Ditt svar: {student}
Riktig svar: {answer}
""")
            elif n_failed == 6:
                print("Koden har feilet for mer enn 5 av de ekstra testene.")
                print("De resterende feilene vil ikke skrives ut.")

    if n_failed > 0:
        print(f"Koden feilet for {n_failed} av de ekstra testene.")

if not failed:
    print("Koden ga riktig svar for alle eksempeltestene")