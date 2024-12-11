airports = set(["ATL", "OMA", "SFO", "LAX", "KC"])

flights = set([
  ("ATL", "OMA", 100),
  ("ATL", "SFO", 100),
  ("ATL", "LAX", 100),
  ("ATL", "KC", 100),
  ("OMA", "KC", 100),
  ("LAX", "KC", 100),
  ("SFO", "LAX", 50)
])

def find_connecting_flights(parent):
  connections = set()
  for flight in flights:
    if flight[0] == parent:
      connections.add((flight[1], flight[2]))
    if flight[1] == parent:
      connections.add((flight[0], flight[2]))
  return connections

visited = set()

inf = 10000

cheapest = {"ATL":inf, "OMA": inf, "SFO": inf, "LAX": inf, "KC": inf}
best_previous = {"ATL":None, "OMA": None, "SFO": None, "LAX": None, "KC": None}


current = "OMA"
destination = "SFO"

cheapest[current] = 0

print(cheapest)

done = False
while not done:
  connections = find_connecting_flights(current)
  print(connections)
  for connection in connections:
    new_cost = connection[1] + cheapest[current]
    best_cost = cheapest[connection[0]]
    # cheapest[connection[0]] = min(cheapest[connection[0]], new_cost)
    if new_cost < best_cost:
      cheapest[connection[0]] = new_cost
      best_previous[connection[0]] = current
  visited.add(current)
  if current == destination:
    done = True

  next_best, next_best_cost = None, inf
  for airport in airports:
    if airport not in visited:
      if cheapest[airport] < next_best_cost:
        next_best = airport
        next_best_cost = cheapest[airport]
  if next_best is None:
    print("I couldn't find a better airport")
    done = True
  else:
    current = next_best

print(cheapest)
print(best_previous)

# Do a back trace to the original airport
path = []
previous = best_previous[destination]
# while previous != start
