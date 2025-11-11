#!/usr/bin/python3
# coding=utf-8
from math import ceil
import random
import itertools
from collections import defaultdict, deque

# Testsettet på serveren er større og mer omfattende enn dette.
# Hvis programmet ditt fungerer lokalt, men ikke når du laster det opp,
# er det gode sjanser for at det er tilfeller du ikke har tatt høyde for.

# De lokale testene består av to deler. Et sett med hardkodete
# instanser som kan ses lengre nedre, og muligheten for å generere
# tilfeldige instanser. Genereringen av de tilfeldige instansene
# kontrolleres ved å justere på verdiene under.

# Kontrollerer om det genereres tilfeldige instanser.
generate_random_tests = False
# Antall tilfeldige tester som genereres.
random_tests = 10
# Laveste mulige antall agenter i generert instans.
agents_lower = 3
# Høyest mulig antall agenter i generert instans.
# NB: Om denne verdien settes høyt (>25) kan det ta veldig lang tid å
# generere testene.
agents_upper = 8
# Laveste mulige antall gjenstander i generert instans.
items_lower = 3
# Høyest mulig antall gjenstander i generert instans.
# NB: Om denne verdien settes høyt (>25) kan det ta veldig lang tid å
# generere testene.
items_upper = 10
# Om denne verdien er 0 vil det genereres nye instanser hver gang.
# Om den er satt til et annet tall vil de samme instansene genereres
# hver gang, om verdiene over ikke endres.
seed = 0


def allocate(categories, valuations, n, m):
    """
    Find a proportional allocation of items to persons.
    
    Uses max-flow (Edmonds-Karp algorithm) to model the allocation problem:
    
    Network structure:
    - Source → Person nodes (capacity = fair share for each person)
    - Person nodes → Category-Person constraint nodes (capacity = category threshold)
    - Category-Person nodes → Item nodes (capacity = 1, only for valued items)
    - Item nodes → Sink (capacity = 1, ensures each item assigned at most once)
    
    The category-person constraint nodes ensure that each person gets at most
    'threshold' items from each category. The flow from source to sink must equal
    the sum of all fair shares for a valid proportional allocation to exist.
    """
    
    # Calculate fair share for each person
    fair_share = []
    for i in range(n):
        total_value = len(valuations[i])
        min_required = ceil(total_value / n)
        fair_share.append(min_required)
    
    # Check if we need to allocate anything
    if sum(fair_share) == 0:
        return [[] for _ in range(n)]
    
    # Build flow network
    # Nodes: source, person_0..person_(n-1), category_person pairs, items, sink
    source = "source"
    sink = "sink"
    
    def person_node(i):
        return f"person_{i}"
    
    def category_person_node(cat_idx, person_idx):
        return f"cat_{cat_idx}_person_{person_idx}"
    
    def item_node(j):
        return f"item_{j}"
    
    # Build graph with capacities
    graph = defaultdict(lambda: defaultdict(int))
    
    # Source to persons (capacity = fair share)
    for i in range(n):
        graph[source][person_node(i)] = fair_share[i]
    
    # Person to category-person nodes (through categories they value items from)
    # Category-person nodes to items (with category constraint)
    for cat_idx, (threshold, cat_items) in enumerate(categories):
        cat_items_set = set(cat_items)
        
        for i in range(n):
            # Find which items in this category person i values
            valued_items = [item for item in cat_items if item in valuations[i]]
            
            if valued_items:
                cat_person = category_person_node(cat_idx, i)
                # Person to category-person (no limit, category will enforce)
                graph[person_node(i)][cat_person] = float('inf')
                
                # Category-person controls the threshold
                # We need to split flow to items, but enforce max threshold
                for item in valued_items:
                    graph[cat_person][item_node(item)] = 1
                
                # To enforce category threshold, we limit total flow through cat_person
                # This is done by setting incoming capacity, but we already have inf
                # We need a different approach
    
    # Items to sink (capacity 1, each item used at most once)
    for j in range(m):
        graph[item_node(j)][sink] = 1
    
    # The above approach won't work directly because we can't enforce category constraints
    # Let me use a better modeling:
    
    # Better approach: Use category constraint nodes between persons and items
    graph = defaultdict(lambda: defaultdict(int))
    
    # Source to persons
    for i in range(n):
        graph[source][person_node(i)] = fair_share[i]
    
    # For each person and category, create a constraint node
    for i in range(n):
        for cat_idx, (threshold, cat_items) in enumerate(categories):
            cat_person = category_person_node(cat_idx, i)
            
            # Person to category-person with threshold capacity
            graph[person_node(i)][cat_person] = threshold
            
            # Category-person to each item in category that person values
            for item in cat_items:
                if item in valuations[i]:
                    graph[cat_person][item_node(item)] = 1
    
    # Items to sink
    for j in range(m):
        graph[item_node(j)][sink] = 1
    
    # Run max-flow (Ford-Fulkerson with BFS = Edmonds-Karp)
    def bfs(graph, source, sink, parent):
        visited = {source}
        queue = deque([source])
        
        while queue:
            u = queue.popleft()
            
            for v in graph[u]:
                if v not in visited and graph[u][v] > 0:
                    visited.add(v)
                    queue.append(v)
                    parent[v] = u
                    if v == sink:
                        return True
        return False
    
    def max_flow(graph, source, sink):
        # Create residual graph
        residual = defaultdict(lambda: defaultdict(int))
        for u in graph:
            for v in graph[u]:
                residual[u][v] = graph[u][v]
        
        parent = {}
        max_flow_value = 0
        
        while bfs(residual, source, sink, parent):
            # Find minimum capacity along path
            path_flow = float('inf')
            s = sink
            while s != source:
                path_flow = min(path_flow, residual[parent[s]][s])
                s = parent[s]
            
            # Update residual capacities
            v = sink
            while v != source:
                u = parent[v]
                residual[u][v] -= path_flow
                residual[v][u] += path_flow
                v = parent[v]
            
            max_flow_value += path_flow
            parent = {}
        
        return max_flow_value, residual
    
    flow_value, residual = max_flow(graph, source, sink)
    
    # Check if we achieved required flow (sum of fair shares)
    required_flow = sum(fair_share)
    if flow_value < required_flow:
        return None
    
    # Extract allocation from flow
    allocation = [[] for _ in range(n)]
    
    # For each person, trace which items they got
    for i in range(n):
        person = person_node(i)
        
        # Check all category-person nodes for this person
        for cat_idx in range(len(categories)):
            cat_person = category_person_node(cat_idx, i)
            
            # Check all items from this category
            for item in categories[cat_idx][1]:
                item_n = item_node(item)
                
                # If there's flow from cat_person to item in original direction
                # (meaning reduced capacity in residual)
                if graph[cat_person][item_n] > 0:
                    flow_to_item = graph[cat_person][item_n] - residual[cat_person][item_n]
                    if flow_to_item > 0:
                        allocation[i].append(item)
    
    return allocation


# Hardkodete tester på format:
# (kategorier, verdifunksjoner, n, m, eksisterer det en proporsjonal allokasjon)
tests = [
    (((1, (0, 1)), (2, (2, 3))),
     ([0, 2, 3], [0, 2]),
     2,
     4,
     True,
    ),
    (((1, (0, 1)),),
     ([0, 1], [0, 1]),
     2,
     2,
     True,
    ),
    (((2, (0, 1, 2)),),
     ([0, 1, 2], [0, 1, 2]),
     2,
     3,
     False,
    ),
    (((2, (0, 1, 2, 3)),),
     ([0, 1, 2, 3], [0, 1, 2, 3]),
     2,
     4,
     True,
    ),
    (((2, (0, 1, 2, 3)),),
     ([0, 1, 3], [0, 1, 3]),
     2,
     4,
     False,
    ),
    (((2, (0, 1, 2)), (1, (3,))),
     ([0, 1, 2, 3], [0, 1, 2, 3]),
     2,
     4,
     True,
    ),
    (((2, (0, 1, 2)), (1, (3,))),
     ([0, 1, 3], [0, 1, 3]),
     2,
     4,
     False,
    ),
    (((2, (0, 1, 2)), (1, (3, 5)), (1, (4,))),
     ([1, 2, 4, 5], [1, 2, 4, 5]),
     2,
     6,
     True,
    ),
]


def check_recursive(categories, likes, req, i, remaining):
    if i == len(likes):
        return True

    choices = remaining & likes[i]
    if len(choices) < req[i]:
        return False

    for comb in itertools.combinations(choices, req[i]):
        comb = set(comb)
        for threshold, items in categories:
            if len(comb & set(items)) > threshold:
                break
        else:
            if check_recursive(categories, likes, req, i + 1, remaining - comb):
                return True

    return False


# Treg bruteforce løsning
def bruteforce_solve(categories, valuations, n, m):
    req = [ceil(len(valuation)/n) for valuation in valuations]
    return check_recursive(categories, valuations, req, 0, set(range(m)))


def gen_examples(k, nl, nu, ml, mu):
    for _ in range(k):
        n = random.randint(nl, nu)
        m = random.randint(ml, mu)
        c = random.randint(1, m)

        boundaries = [0] + sorted([random.randint(0, m) for _ in range(c-1)]) + [m]
        categories = []
        items = list(range(m))
        random.shuffle(items)
        for a, b in zip(boundaries, boundaries[1:]):
            category_items = items[a:b]
            categories.append((random.randint(1, max(len(category_items), 1)),
                               tuple(category_items)))
        categories = tuple(categories)

        val_function = lambda L: lambda x: x in L

        valuations = [
                random.sample(items, random.randint(0, m))
                for _ in range(n)
        ]

        exists = bruteforce_solve(categories, valuations, n, m)

        yield categories, valuations, n, m, exists


if generate_random_tests:
    if seed:
        random.seed(seed)
    tests += list(gen_examples(
        random_tests,
        agents_lower,
        agents_upper,
        items_lower,
        items_upper,
    ))

def verify(m, categories, valuations, exists, student):
    if not exists:
        if student is not None:
            return "Du returnert ikke None selv om det ikke finnes en proporsjonal allokasjon."
        return None

    if type(student) != type([]):
        return "Du returnerte ikke en liste."

    if len(student) != len(valuations):
        return "Svaret inneholder ikke nøyaktig en samling med gjenstander for hver agent."

    # Test that each agent has a list as a bundle
    if any(type(bundle) != type([]) for bundle in student):
        return "En av samlingene med gjenstander er ikke en liste."

    # Test type of each item
    if any(type(item) != int for bundle in student for item in bundle):
        return "Du har returnert en gjenstand som ikke finnes."

    # Test that each item in each bundle is an item
    if not all(0 <= item < m for bundle in student for item in bundle):
        return "Du har returnert en gjenstand som ikke finnes."

    # Test that each item appears at most once in each bundle
    if any(len(set(bundle)) < len(bundle) for bundle in student):
        return "En samling inneholder samme gjenstand flere ganger."

    # Test that some item has not been allocated multiple times
    for i in range(len(valuations)):
        for j in range(i + 1, len(valuations)):
            if set(student[i]) & set(student[j]):
                return "Hver gjenstand kan kun gis til en av personene."

    # Test that each agent does not receive more than threshold items from
    # each category multiple items
    for bundle in student:
        for threshold, category in categories:
            if len(set(bundle) & set(category)) > threshold:
                print(threshold, category, bundle)
                return "En samling innholder flere gjenstander fra en kategori enn er lov."

    for valuation, bundle in zip(valuations, student):
        if len(set(valuation) & set(bundle)) < ceil(len(valuation) / len(valuations)):
            return "En person har ikke fått gjenstander med nok verdi."


def format_valuations(valuations, m):
    string = ""
    for i, valuation in enumerate(valuations):
        string += f"    Agent {i}: {valuation}\n"
    return string


failed = False
for categories, valuations, n, m, exists in tests:
    student = allocate(categories, [val[:] for val in valuations], n, m)
    feedback = verify(m, categories, valuations, exists, student)

    if feedback is not None:
        if failed:
            print("-"*50)
        failed = True
        print(f"""
Koden feilet for følgende instans:
n: {n}
m: {m}
categories: {categories}
valuations:
{format_valuations(valuations, m)}
Ditt svar: {student}
Feilmelding: {feedback}
""")

if not failed:
    print("Koden ga riktig svar for alle eksempeltestene")
