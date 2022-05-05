class Stack (object):
    def __init__ (self):
        self.stack = []

  # add an item to the top of the stack
    def push (self, item):
        self.stack.append (item)

  # remove an item from the top of the stack
    def pop (self):
        return self.stack.pop()

  # check the item on the top of the stack
    def peek (self):
        return self.stack[-1]
    
  # check if the stack if empty
    def is_empty (self):
        return (len (self.stack) == 0)

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False for i in rooms]
        
        # return an unvisited vertex adjacent to vertex v (index)
        def get_adj_unvisited_vertex (v):
            nVert = len (rooms)
            for i in range (nVert):
                if (i in rooms[v]) and (not visited[i] == True):
                    return i
            return -1

        # create the Stack
        theStack = Stack ()

        # mark the vertex v as visited and push it on the Stack
        visited[0] = True
        #print (self.Vertices[v])
        theStack.push (0)

        # visit all the other vertices according to depth
        while (not theStack.is_empty()):
          # get an adjacent unvisited vertex
            u = get_adj_unvisited_vertex (theStack.peek())
            if (u == -1):
                u = theStack.pop()
            else:
                visited[u] = True
                #print (self.Vertices[u])
                theStack.push (u)

        if False in visited:
            return False
        return True
        