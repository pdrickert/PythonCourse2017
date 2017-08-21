"""Data Structures
Working with Graphs/Networks"""

def makeLink(G, node1, node2):
  if node1 not in G:
    G[node1] = {}
  (G[node1])[node2] = 1
  if node2 not in G:
    G[node2] = {}
  (G[node2])[node1] = 1
  return G

# Ring Network
ring = {} # empty graph

n = 5 # number of nodes

# Add in edges
for i in range(n):
  ring = makeLink(ring, i, (i+1)%n)

# How many nodes?
print len(ring)

# How many edges?
print sum([len(ring[node]) for node in ring.keys()])/2


# Grid Network
# TODO: create a square graph with 256 nodes and count the edges
Jeff = {}
for i in range(256):
  Jeff1 = makeLink(Jeff, i, (i+1)%16)
for i in range(240):
  Jeff2 = makeLink(Jeff1, i, i+16)
for i in range(240):
    if i%15 == 0:
        pass
    else:
        Jeff3 = makeLink(Jeff2, i, i + 17)
for i in range(240):
    if i%16 == 0:
        pass
    else:
        Jeff4 = makeLink(Jeff3, i, i+15)


# TODO: define a function countEdges
def countEdges(network):
    NumEdges = sum([len(network[node]) for node in network.keys()])/2
    print "There are %s edges in this network" %NumEdges


# Social Network
class Actor(object):
  def __init__(self, name):
    self.name = name

  def __repr__(self):
    return self.name

ss = Actor("Susan Sarandon")
jr = Actor("Julia Roberts")
kb = Actor("Kevin Bacon")
ah = Actor("Anne Hathaway")
rd = Actor("Robert DeNiro")
ms = Actor("Meryl Streep")
dh = Actor("Dustin Hoffman")

movies = {}

makeLink(movies, dh, rd) # Wag the Dog
makeLink(movies, rd, ms) # Marvin's Room
makeLink(movies, dh, ss) # Midnight Mile
makeLink(movies, dh, jr) # Hook
makeLink(movies, dh, kb) # Sleepers
makeLink(movies, ss, jr) # Stepmom
makeLink(movies, kb, jr) # Flatliners
makeLink(movies, kb, ms) # The River Wild
makeLink(movies, ah, ms) # Devil Wears Prada
makeLink(movies, ah, jr) # Valentine's Day



# How many nodes in movies?
len(movies)
# How many edges in movies?
countEdges(movies)




def tour(graph, nodes):
  for i in range(len(nodes)):
    node = nodes[i]
    if node in graph.keys():
      print node
    else:
      print "Node not found!"
      break
    if i+1 < len(nodes):
      next_node = nodes[i+1]
      if next_node in graph.keys():
        if next_node in graph[node].keys():
          pass
        else:
          print "Can't get there from here!"
          break

# TODO: find an Eulerian tour of the movie network and check it
tour(movies, [ah,ms])
tour(movies, [rd,ms,kb,jr,ah,ms])
movie_tour = []
tour(movies, movie_tour)
def findEulerian(graph, path = []):






def findPath(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if not graph.has_key(start):
            return None
        for node in graph[start]:
            if node not in path:
                newpath = findPath(graph, node, end, path)
                if newpath: return newpath
        return None

print findPath(movies, jr, ms)


# TODO: implement findShortestPath()
def findShortestPath(graph, start, end, path = []):
    PathLength = []
    AllPaths = findAllPaths(graph, start, end)
    for i in range(0,len(AllPaths)):
        PathLength.append(len(AllPaths[i]))
    m = min(PathLength)
    PathIndex = [i for i, j in enumerate(PathLength) if j == m][0]
    return AllPaths[PathIndex]

# print findShortestPath(movies, ms, ss)

# TODO: implement findAllPaths() to find all paths between two nodes
def findAllPaths(graph, start, end, path = []):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return None
    paths = []
    for node in graph[start]:
        if node not in path:
            newpath = findAllPaths(graph, node, end, path)
            for p in newpath:
                paths.append(p)
    return paths


# for path in allPaths:
#   print path

# Copyright (c) 2014 Matt Dickenson
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
