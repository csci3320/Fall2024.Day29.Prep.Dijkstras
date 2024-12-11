edges = set([
  ("ATL", "OMA", 200),
  ("ATL", "SFO", 100),
  ("ATL", "LAX", 60),
  ("ATL", "KC", 75),
  ("OMA", "KC", 100),
  ("LAX", "KC", 100),
  ("SFO", "LAX", 50)
])

start = "OMA"
destination = "SFO"

def get_connections(node):
  connections = set()
  for edge in edges:
    if edge[0] == node:
      connections.add((edge[1], edge[2]))
    if edge[1] == node:
      connections.add((edge[0], edge[2]))
  return connections

inf = 1_000_000

nodes = set()
for edge in edges:
  nodes.add(edge[0])
  nodes.add(edge[1])

visited = {node:False for node in nodes}
cheapest = {node:inf for node in nodes}
best_previous = {node:None for node in nodes}

current = start
cheapest[current] = 0

done = False
while not done:
  connections = get_connections(current)
  
  for connection in connections:
    new_cost = connection[1] + cheapest[current]
    best_cost = cheapest[connection[0]]
    if new_cost < best_cost:
      cheapest[connection[0]] = new_cost
      best_previous[connection[0]] = current
  
  visited[current] = True
  if current == destination:
    done = True

  next_best, next_best_cost = None, inf
  for node in nodes:
    if not visited[node]:
      if cheapest[node] < next_best_cost:
        next_best = node
        next_best_cost = cheapest[node]
  if next_best is None:
    done = True
  else:
    current = next_best

print(cheapest)

# Do a back track to the original airport
path = [destination]
current = best_previous[destination]
while current != start:
  path.append(current)
  current = best_previous[current]
path.append(start)
path.reverse()
print(path)
