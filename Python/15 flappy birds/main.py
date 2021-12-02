import pygame, random
from pygame.constants import K_SPACE
pygame.init()

SKY_BLUE = (100, 191, 244)
w, h = 300, 500
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("FLAPPY BIRD")
icon = pygame.image.load("images/bird.png")
pygame.display.set_icon(icon)

bg = pygame.image.load("images/intro.png")
base = pygame.image.load("images/base.png").convert()
gameover_png = pygame.image.load("images/gameover.png")

die_sound = pygame.mixer.Sound("sounds/die.wav")
point_sound = pygame.mixer.Sound("sounds/point.wav")
wing_sound = pygame.mixer.Sound("sounds/wing.wav")

class Bird:

    def __init__(self, pos):
        self.image = pygame.image.load("images/bird.png").convert()
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos
        self.vel = 3
        self.fly = False
        self.score = 0

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def move(self):
        if self.fly:
            self.rect.y -= self.vel
        else:
            self.rect.y += self.vel
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > 400:
            self.rect.bottom = 400

    def is_collision(self, p):
        return self.rect.colliderect(p.trect) or self.rect.colliderect(p.brect)

class Pipes:

    def __init__(self, pos):
        self.top = pygame.image.load("images/pipe-up.png").convert()
        self.bottom = pygame.image.load("images/pipe-down.png").convert()
        self.trect = self.top.get_rect()
        self.brect = self.bottom.get_rect()
        self.trect.x, self.trect.y = pos
        self.brect.x, self.brect.y = self.trect.x, self.trect.bottom + 100 
        self.xvel = 7

    def draw(self, screen):
        screen.blit(self.top, self.trect)
        screen.blit(self.bottom, self.brect)

    def move(self, b):
        self.trect.x -= self.xvel
        self.brect.x -= self.xvel

        if self.trect.right < 0:
            self.respawn()
            point_sound.play()
            b.score += 1

    def respawn(self):
        self.trect.x = 300
        self.brect.x = 300
        self.trect.y = random.randint(-150, -50)
        self.brect.y = self.trect.bottom + random.choice([100, 80])



def gameover(screen, font, b, pipes, base):

    run = True
    while run:
        screen.fill(SKY_BLUE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        b.draw(screen)
        for p in pipes:
            p.draw(screen)
        screen.blit(gameover_png, (60,100))
        display_score(screen, font, b, (110, 150))
        screen.blit(base, (0,400))
        pygame.display.update()

font = pygame.font.SysFont("Arial", 32, True)
def display_score(screen, font, b, pos):
    text_surface = font.render(f"Score: {b.score}", True, (255, 255, 255))
    screen.blit(text_surface, pos)

pipe_pos = [[200,-100], [400,-150]]        
        
FPS = 60 # frame per second
clock = pygame.time.Clock()
def gamestart(screen):

    b = Bird((40,270))

    pipes = []
    for pos in pipe_pos:
        p = Pipes(pos)
        pipes.append(p)

    run = True
    while run:

        screen.fill(SKY_BLUE)
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN and event.key == K_SPACE:
                b.fly = True
                wing_sound.play()
            if event.type == pygame.KEYUP and event.key == K_SPACE:
                b.fly = False

        # movement
        b.move()
        for p in pipes:
            p.move(b)

        # gameover 
        for p in pipes:
            if b.is_collision(p):
                die_sound.play()
                gameover(screen, font, b, pipes, base)
                run = False

        b.draw(screen)
        for p in pipes:
            p.draw(screen)
        display_score(screen, font, b, (15, 15))
        screen.blit(base, (0,400))
        pygame.display.update()

run = True
while run:

    screen.fill(SKY_BLUE)
    screen.blit(bg, (60,100))

    for event  in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            print("START THE GAME")
            gamestart(screen)

    pygame.display.update()