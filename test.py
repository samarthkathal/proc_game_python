import numpy, pygame, sys, random

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
WINDOW_HEIGHT = 600
WINDOW_WIDTH = 800

BLOCKSIZE = 50


SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
CLOCK = pygame.time.Clock()

GAMEGRID = [ [] for i in range(0, WINDOW_HEIGHT, BLOCKSIZE)]


for vert in range(0, WINDOW_HEIGHT, BLOCKSIZE):
    for hor in range(0, WINDOW_WIDTH, BLOCKSIZE):
        i = int(hor/BLOCKSIZE)
        j = int(vert/BLOCKSIZE)
        GAMEGRID[j].insert(i, True)


PLAYERSTART_VERT_INDEX = random.randint(1, 2)
PLAYERSTART_HOR_INDEX = random.randint(1, 2)

PLAYEREND_VERT_INDEX = random.randint(9, 10)
PLAYEREND_HOR_INDEX = random.randint(13, 14)



GAMEGRID[PLAYERSTART_VERT_INDEX].insert(PLAYERSTART_HOR_INDEX, 0)
GAMEGRID[PLAYEREND_VERT_INDEX].insert(PLAYEREND_HOR_INDEX, -1)

print(PLAYERSTART_VERT_INDEX)
print(PLAYERSTART_HOR_INDEX)
print(PLAYEREND_VERT_INDEX)
print(PLAYEREND_HOR_INDEX)

for i in range(3):
    y = random.randint(PLAYERSTART_VERT_INDEX, PLAYEREND_VERT_INDEX)
    x = random.randint(PLAYERSTART_HOR_INDEX, PLAYEREND_HOR_INDEX)
    print(y, x)
    GAMEGRID[y].insert(x, 0)


s = [[str(e) for e in row] for row in GAMEGRID]
lens = [max(map(len, col)) for col in zip(*s)]
fmt = '  '.join('{{:{}}}'.format(x) for x in lens)
table = [fmt.format(*row) for row in s]
print('\n'.join(table))


def main():
    global SCREEN, CLOCK
    pygame.init()
    
    SCREEN.fill(BLACK)

    while True:
        drawGrid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


def drawGrid():
    global GAMEGRID, BLOCKSIZE
    for y in range(len(GAMEGRID)):
        for x in range(len(GAMEGRID[0])):
            wall = pygame.image.load('wall_1_1.png')
            if GAMEGRID[y][x] == True:
                SCREEN.blit(wall, (x*BLOCKSIZE,y*BLOCKSIZE))


class Map():
    def __init__(self, WINDOW_WIDTH, WINDOW_HEIGHT, BLOCKSIZE):
        self.WINDOW_WIDTH = WINDOW_WIDTH
        self.WINDOW_HEIGHT = WINDOW_HEIGHT
        self.BLOCKSIZE = BLOCKSIZE

        self.Grid = [ [] for i in range(0, self.WINDOW_HEIGHT, self.BLOCKSIZE)]
    
    def populateGrid(self):
        for x in range(0, self.WINDOW_WIDTH, self.BLOCKSIZE):
            for y in range(0, self.WINDOW_HEIGHT, self.BLOCKSIZE):
                wall = pygame.image.load('wall_1_1.png')
                SCREEN.blit(wall, (x,y))


if __name__ == "__main__":
    main()


