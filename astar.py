from random import randint, getrandbits
from config import *

from gameGrid import screen, clock, SquareGrid

import heapq


g = SquareGrid(GRIDWIDTH, GRIDHEIGHT)



#UTILITY

def vec2int(v):
    return (int(v.x), int(v.y))

def heuristic(a, b):
    return (abs(a.x - b.x) + abs(a.y - b.y)) * 10

#def getRandVec(startVec, endVec):
#    return vec((random.randint(startVec.x, endVec.x)), (random.randint(startVec.y, endVec.y)))
#
#def genChambers(a = vec(0,0),b = vec(GRIDWIDTH-1, HEIGHT-1) ):
#    p1 = getRandVec(a, b)
#    p2 = getRandVec(a, b)


def getRooms():
    global GRIDWIDTH, GRIDHEIGHT, DIAGS, CROSS
    allowed = DIAGS + CROSS
    x, y = 1, 1
    centres = []
    full_grid = []
    while x < GRIDWIDTH:
        while y < GRIDHEIGHT:
            centres.append(vec(x,y))
            cods = []
            cods.append(vec(x,y))
            for i in allowed:
                cods.append( vec(x,y) + i )

            full_grid.append(cods)

            y = y + 3
        y = 1
        x = x + 3
    return full_grid


def buildRooms(full_grid):
    gridEmptySpace = []
    gridWalls = []
    for walls in full_grid:
        roomEmptySpace = []
        random.shuffle(walls)
        for x in range(randint(2, 7)):
            roomEmptySpace.append(walls.pop())

        gridEmptySpace.append(roomEmptySpace)
        gridWalls.append(walls)
    
    print(gridWalls[3], gridEmptySpace[3])
    
    return gridWalls, gridEmptySpace


class PriorityQueue:
    def __init__(self):
        self.nodes = []

    def put(self, node, cost):
        heapq.heappush(self.nodes, (cost, node))

    def get(self):
        return heapq.heappop(self.nodes)[1]

    def empty(self):
        return len(self.nodes) == 0




def draw_icons():
    start_center = (goal.x * TILESIZE + TILESIZE / 2, goal.y * TILESIZE + TILESIZE / 2)
    screen.blit(home_img, home_img.get_rect(center=start_center))
    goal_center = (start.x * TILESIZE + TILESIZE / 2, start.y * TILESIZE + TILESIZE / 2)
    screen.blit(cross_img, cross_img.get_rect(center=goal_center))


def movement(neighbors, move_vector, start):
    human_complexity = 0
    for allowed in neighbors:
        human_complexity += 1
        if start + move_vector == allowed:
            start += move_vector

    print(human_complexity) 
     





def a_star_search(graph, start, end): # start is destination, end is player.
    frontier = PriorityQueue()
    frontier.put(vec2int(start), 0)
    path = {}
    cost = {}
    path[vec2int(start)] = None
    cost[vec2int(start)] = 0
    

    x = graph.find_neighbors(end)

    while not frontier.empty():
        current = frontier.get()
        if current == end:
            break
        for next in graph.find_neighbors(vec(current)):
            next = vec2int(next)
            next_cost = cost[current] + graph.cost(current, next)
            if next not in cost or next_cost < cost[next]:
                cost[next] = next_cost
                priority = next_cost + heuristic(end, vec(next))
                frontier.put(next, priority)
                path[next] = vec(current) - vec(next)
    return path, cost, x


walls = []


def rebuildRoom():
    global walls
    gridWalls, gridEmptySpace = buildRooms(getRooms())

    walls = [j for sub in gridWalls for j in sub]
    #print(walls)

rebuildRoom()

#all = getRooms()
#sol = [j for sub in all for j in sub]
#walls = sol

def generateGenome(length):
    return random.choices([0, 1], k=length)

def generatePopulation(size, genomeLength):
    return [generateGenome(genomeLength) for _ in range(size)]

def fitnessFunction(genome, ):

    #fit == path is not none
    #human complexity ?
    pass


for wall in walls:
    g.walls.append(vec(wall))


goal = vec(14, 8)
start = vec(20, 0)
search_type = a_star_search

path, c, x = search_type(g, goal, start)



running = True
while running:
    q = False
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            pressed = pygame.key.get_pressed()
            move_vector = vec(0,0)
            
            for m in (move_map[key] for key in move_map if pressed[key]):
                move_vector += m
        
            if move_vector != vec(0,0):
                movement(neighbors, move_vector, start)


            if event.key == pygame.K_ESCAPE:
                running = False

                

#DEBUG CODE, DELETE LATER           
        if event.type == pygame.MOUSEBUTTONDOWN:
            mpos = vec(pygame.mouse.get_pos()) // TILESIZE
            if event.button == 1:
                if mpos in g.walls:
                    g.walls.remove(mpos)
                else:
                    g.walls.append(mpos)
            ####
            if event.button == 2:
                start = mpos
                q = True
            ####

            if event.button == 3:
                goal = mpos
                print(mpos)
        
#END

    path, c, neighbors = search_type(g, goal, start)
    
    

    pygame.display.set_caption("Spikes 'n' Stuff")
    screen.fill(DARKGRAY)


    g.draw()

    # draw path from start to goal
    current = start # + path[vec2int(start)]
    l = 0

    while current != goal:
        try:
            v = path[(current.x, current.y)]
        except KeyError:
            break
        if v.length_squared() == 1:
            l += 10
        else:
            l += 14
        img = arrows[vec2int(v)]
        x = current.x * TILESIZE + TILESIZE / 2
        y = current.y * TILESIZE + TILESIZE / 2
        r = img.get_rect(center=(x, y))
        screen.blit(img, r)
        # find next in path
        try:
            current = current + path[vec2int(current)]
        except KeyError:
            rebuildRoom()

    draw_icons()
    

    
    
    pygame.display.flip()