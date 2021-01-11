import pygame
import random

width = 600
height = 600
fps = 30

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Змейка")
clock = pygame.time.Clock()

app_alive = True


class Zmeika:
    def __init__(self):
        self.blocks = [[i*10+250, 0] for i in range(5)]
        self.apple = [50, 50]
        self.wasd = 'd'

    def frame(self):
        if self.blocks[-1] in self.blocks[0:-1]:
            return 'Смерть'
        if self.wasd == 'w':
            if self.blocks[-1][1] == 0: self.blocks.append([self.blocks[-1][0], height - 10])
            else: self.blocks.append([self.blocks[-1][0], self.blocks[-1][1] - 10])
        elif self.wasd == 'a':
            if self.blocks[-1][0] == 0: self.blocks.append([width - 10, self.blocks[-1][1]])
            else: self.blocks.append([self.blocks[-1][0] - 10, self.blocks[-1][1]])
        elif self.wasd == 's':
            if self.blocks[-1][1] == height - 10: self.blocks.append([self.blocks[-1][0], 0])
            else: self.blocks.append([self.blocks[-1][0], self.blocks[-1][1] + 10])
        elif self.wasd == 'd':
            if self.blocks[-1][0] == width - 10: self.blocks.append([0, self.blocks[-1][1]])
            else: self.blocks.append([self.blocks[-1][0] + 10, self.blocks[-1][1]])
        if self.blocks[-1] != self.apple:
            self.blocks.pop(0)
        else:
            self.apple = [random.randint(0, 59)*10, random.randint(0, 59)*10]


while app_alive:
    zmeika = Zmeika()
    while True:
        screen.fill('black')
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                pygame.quit()
            elif i.type == pygame.KEYDOWN:
                if i.key == pygame.K_w and zmeika.wasd != 's': zmeika.wasd = 'w'
                elif i.key == pygame.K_a and zmeika.wasd != 'd': zmeika.wasd = 'a'
                elif i.key == pygame.K_s and zmeika.wasd != 'w': zmeika.wasd = 's'
                elif i.key == pygame.K_d and zmeika.wasd != 'a': zmeika.wasd = 'd'
        if zmeika.frame() == 'Смерть': break
        for i in zmeika.blocks:
            pygame.draw.rect(screen, 'red', pygame.Rect(i[0], i[1], 10, 10))
        pygame.draw.rect(screen, 'green', pygame.Rect(zmeika.apple[0], zmeika.apple[1], 10, 10))
        pygame.display.flip()
        clock.tick(fps)
