#list of motion vectors for each discrete "step"
'''
carbon1 = [(0,-1),(0,-1),(0,-1),(0,-1),(0,-1),(0,-1)]
oxygen1 = [(1,0),(0,-1),(0,-1),(0,-1),(0,-1),(0,-1),(0,-1)]
hydrogen1 = [(1,0),(0,-1),(0,-1),(0,-1),(0,-1),(0,-1),(0,-1),(0,-1)]
hydrogen2 = [(1,0),(0,-1),(0,-1),(0,-1),(0,-1),(0,-1),(0,-1)]
carbon2 = [(1,0),(1,0),(1,0),(0,-1),(0,-1),(0,-1),(0,-1),(0,-1),(0,-1)]
hydrogen3 = [(1,0),(1,0),(1,0),(0,-1),(0,-1),(0,-1),(0,-1),(0,-1),(0,-1)]
hydrogen4 = [(0,-1),(0,-1),(0,-1),(0,-1),(0,-1),(0,-1),(0,-1)]
hydrogen5 = [(0,-1),(0,-1),(0,-1),(0,-1),(0,-1),(0,-1),(0,-1),(0,-1)]
carbon3 = [(-1,0),(-1,0),(0,-1),(0,-1),(0,-1),(0,-1),(0,-1),(0,-1),(0,-1)]
hydrogen6 = [(-1,0),(-1,0),(0,-1),(0,-1),(0,-1),(0,-1),(0,-1),(0,-1),(0,-1)]
'''

class Atom:
  def __init__(name, vectors, startPos):
    name.vectors = vectors
    name.startPos = startPos

#initialize atom objects
#numbering is currently arbitrary
#start positions assume a 13x13 grid where (1,1) is the node in the bottom-left corner
carbon1 = Atom([(0,-1),(0,-1),(0,-1),(0,-1),(0,-1),(0,-1)],(7,13))
oxygen1 = Atom([(1,0),(0,-1),(0,-1),(0,-1),(0,-1),(0,-1),(0,-1)],(6,13))
hydrogen1 = Atom([(1,0),(0,-1),(0,-1),(0,-1),(0,-1),(0,-1),(0,-1),(0,-1)],(5,13))
hydrogen2 = Atom([(1,0),(0,-1),(0,-1),(0,-1),(0,-1),(0,-1),(0,-1)],(4,13))
carbon2 = Atom([(1,0),(1,0),(1,0),(0,-1),(0,-1),(0,-1),(0,-1),(0,-1),(0,-1)],(3,13))
hydrogen3 = Atom([(1,0),(1,0),(1,0),(0,-1),(0,-1),(0,-1),(0,-1),(0,-1),(0,-1)],(2,13))
hydrogen4 = Atom([(0,-1),(0,-1),(0,-1),(0,-1),(0,-1),(0,-1),(0,-1)],(8,13))
hydrogen5 = Atom([(0,-1),(0,-1),(0,-1),(0,-1),(0,-1),(0,-1),(0,-1),(0,-1)],(9,13))
carbon3 = Atom([(-1,0),(-1,0),(0,-1),(0,-1),(0,-1),(0,-1),(0,-1),(0,-1),(0,-1)],(10,13))
hydrogen6 = Atom([(-1,0),(-1,0),(0,-1),(0,-1),(0,-1),(0,-1),(0,-1),(0,-1),(0,-1)],(11,13))