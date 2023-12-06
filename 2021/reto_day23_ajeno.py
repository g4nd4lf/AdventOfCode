import dataclasses, functools, re
from typing import Optional
#f = open("input_day23.txt", "r")
with open("input_day23.txt", "r") as fp:
  data = ''.join(re.findall('[ABCD]', fp.read()))

@dataclasses.dataclass
class Node:
  can_stop: bool = True
  room: Optional[str] = None
  
  @property
  def hallway(self) -> bool:
    return self.room is None

room_map = {id: 'ABCD'[i%4] for i, id in enumerate('lnprmoqsLNPRMOQS')}
make_space = lambda id: Node(can_stop=id not in 'cegi', room=room_map.get(id))

# abcdefghijk
#   l n p r
#   m o q s

costs = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
edges = {
    'a': 'b', 'b': 'ac', 'c': 'bdl', 'd': 'ce', 'e': 'dfn', 'f': 'eg', 
    'g': 'fhp', 'h': 'gi', 'i': 'hjr', 'j': 'ik', 'k': 'j', 'l': 'cm',
    'n': 'eo', 'p': 'gq', 'r': 'is', 'm': 'l', 'o': 'n', 'q': 'p', 's': 'r',
}
rooms = {'A': 'lm', 'B': 'no', 'C': 'pq', 'D': 'rs'}
spaces = {id: make_space(id) for id in 'abcdefghijklmnopqrs'}

def room_ready(state, kind):
  return all(state.get(id) in (None, kind) for id in rooms[kind])

def available_moves(state, pos, kind, step=1, seen=()):
  if not kind: return
  first_pos = pos if not seen else seen[0]
  for adj in edges[pos]:
    if adj in seen or state.get(adj): continue
    if (spaces[pos].hallway and spaces[adj].room and
        (spaces[adj].room != kind or not room_ready(state, kind))):
      continue
    if spaces[pos].room == kind and spaces[adj].hallway:
      if room_ready(state, kind):
        continue
    if spaces[pos].hallway and adj in rooms[kind] and room_ready(state, kind):
      yield max((step+i, room) for i, room in enumerate(rooms[kind])
                if not state.get(room))
      continue
    if spaces[adj].can_stop and spaces[first_pos].room != spaces[adj].room:
      yield step, adj
    yield from available_moves(state, adj, kind, step+1, seen+(pos,))  

@functools.lru_cache(maxsize=None)
def recursive(state):
  if all(spaces[id].room == kind for id, kind in state): return 0
  state_map = dict(state)
  return min((
      cost * costs[kind] + recursive(state[:i]+((target, kind),)+state[i+1:])
      for i, (current, kind) in enumerate(state)
      for cost, target in available_moves(state_map, current, kind)
  ), default=float('inf'))

initial_state = tuple(zip('lnprmoqs', data))
print('Part 1:', recursive(initial_state))


# abcdefghijk
#   l n p r
#   m o q s
#   L N P R
#   M O Q S

edges.update({
  'm': 'lL', 'o': 'nN', 'q': 'pP', 's': 'rR',
  'L': 'mM', 'N': 'oO', 'P': 'qQ', 'R': 'sS',
  'M': 'L', 'O': 'N', 'Q': 'P', 'S': 'R',
})
rooms.update({'A': 'lmLM', 'B': 'noNO', 'C': 'pqPQ', 'D': 'rsRS'})
spaces.update({id: make_space(id) for id in 'abcdefghijklmnopqrsLMNOPQRS'})

new_data = data[:4] + 'DCBADBAC' + data[4:]
initial_state = tuple(zip('lnprmoqsLNPRMOQS', new_data))
print('Part 2:', recursive(initial_state))