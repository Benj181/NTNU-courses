#!/usr/bin/python3
# coding=utf-8

from collections import deque

def max_flow_highscore(source, sink, nodes, capacities):
    """
    Optimized Edmonds-Karp implementation for maximum flow.
    
    Key optimizations:
    1. Direct residual graph manipulation (no separate flow tracking)
    2. Inline BFS without separate path construction
    3. Early termination when sink is reached in BFS
    4. Minimal memory allocations per iteration
    
    Time complexity: O(V * E^2) where V is nodes and E is edges
    Space complexity: O(V^2) for residual graph
    """
    # Build residual graph directly from capacities
    residual = [row[:] for row in capacities]
    
    max_flow_value = 0
    
    while True:
        # BFS to find augmenting path
        parent = [-1] * nodes
        visited = [False] * nodes
        visited[source] = True
        queue = deque([source])
        
        # Find path to sink
        found_path = False
        while queue:
            u = queue.popleft()
            
            if u == sink:
                found_path = True
                break
            
            # Check all neighbors with residual capacity
            for v in range(nodes):
                if not visited[v] and residual[u][v] > 0:
                    visited[v] = True
                    parent[v] = u
                    queue.append(v)
                    
                    if v == sink:
                        found_path = True
                        break
            
            if found_path:
                break
        
        # No more augmenting paths
        if not found_path:
            break
        
        # Find minimum capacity along the path
        path_flow = float('inf')
        v = sink
        while v != source:
            u = parent[v]
            path_flow = min(path_flow, residual[u][v])
            v = u
        
        # Update residual capacities along the path
        v = sink
        while v != source:
            u = parent[v]
            residual[u][v] -= path_flow
            residual[v][u] += path_flow
            v = u
        
        max_flow_value += path_flow
    
    return max_flow_value


# Hjelpefunksjoner du kan bruke
def find_augmenting_path(source, sink, nodes, flows, capacities):
    def create_path(source, sink, parent):
        """Lager stien ved hjelp av foreldrelisten"""
        node = sink
        path = [sink]
        while node != source:
            node = parent[node]
            path.append(node)
        path.reverse()
        return path

    discovered = [False] * nodes
    parent = [0] * nodes
    queue = deque()
    queue.append(source)

    while queue:
        node = queue.popleft()
        if node == sink:
            return create_path(source, sink, parent)

        for neighbour in range(nodes):
            if (
                not discovered[neighbour]
                and flows[node][neighbour] < capacities[node][neighbour]
            ):
                queue.append(neighbour)
                discovered[neighbour] = True
                parent[neighbour] = node
    return None


def max_path_flow(path, flows, capacities):
    """
    Finn maksimal flyt som kan sendes gjennom den oppgitte stien
    """
    flow = float("inf")
    for i in range(1, len(path)):
        u, v = path[i - 1], path[i]
        flow = min(flow, capacities[u][v] - flows[u][v])
    return flow


def send_flow(path, flow, flows):
    """
    Oppdaterer "flows" ved å sende "flow" flyt gjennom stien "path"
    """
    for i in range(1, len(path)):
        u, v = path[i - 1], path[i]
        flows[u][v] += flow
        flows[v][u] -= flow

tests = [
    (
        0,
        5,
        6,
        [
            [0, 16, 13, 0, 0, 0],
            [0, 0, 0, 12, 0, 0],
            [0, 4, 0, 0, 14, 0],
            [0, 0, 9, 0, 0, 20],
            [0, 0, 0, 7, 0, 4],
            [0, 0, 0, 0, 0, 0],
        ],
        23,
    ),
    (
        0,
        5,
        6,
        [
            [0, 16, 13, 0, 0, 0],
            [16, 0, 4, 12, 0, 0],
            [13, 4, 0, 9, 14, 0],
            [0, 12, 9, 0, 7, 20],
            [0, 0, 14, 7, 0, 4],
            [0, 0, 0, 20, 4, 0],
        ],
        24,
    ),
    (
        0,
        5,
        6,
        [
            [0, 16, 13, 0, 0, 0],
            [16, 0, 4, 12, 0, 0],
            [13, 4, 0, 7, 14, 0],
            [0, 12, 7, 0, 1, 20],
            [0, 0, 14, 1, 0, 4],
            [0, 0, 0, 20, 4, 0],
        ],
        24,
    ),
    (
        0,
        4,
        5,
        [
            [0, 1, 1, 1, 1, 1],
            [1, 0, 1, 1, 1, 1],
            [1, 1, 0, 1, 1, 1],
            [1, 1, 1, 0, 1, 1],
            [1, 1, 1, 1, 0, 1],
            [1, 1, 1, 1, 1, 0],
        ],
        4,
    ),
]

failed = False

for test_case in tests:
    (
        source,
        sink,
        nodes,
        capacities,
        answer_flow,
    ) = test_case
    student_flow = max_flow_highscore(
        source, sink, nodes, capacities
    )
    if student_flow != answer_flow:
        failed = True
        response = "Koden feilet for følgende input: (tasks={:}). ".format(
            test_case[:4]
        ) + "Din flyt: {:}. Riktig maksflyt: {:}".format(
            student_flow, answer_flow
        )
        print(response)
        break

if not failed:
    print("Koden fungerte for alle eksempeltestene.")