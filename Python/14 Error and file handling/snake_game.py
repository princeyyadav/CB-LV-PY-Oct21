import pygame, random
pygame.init() # initialize the module

w, h = 500, 500
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("SNAKE GAME")

snake = [[300,300], [320, 300], [340, 300], [360,300]]
def draw_snake(screen, snake):
    for pos in snake:
        pygame.draw.circle(screen, (249, 222, 68), pos, 10)

step = 20

left = (-step, 0)
right = (step,0)
up = (0,-step)
down = (0, step)

direction = left

r = 10
margin = 10

FPS = 60
clock = pygame.time.Clock()

## apple
apple = [200,200]

score = 0

timer = 0

font = pygame.font.SysFont("Arial", 32, True)

def display_score(screen, score):
    text_surface = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(text_surface, (15,15))

run = True
while run:

    screen.fill((153, 207, 52))
    clock.tick(FPS)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            print("QUIT")
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != down:
                direction =  up
            elif event.key == pygame.K_DOWN and direction != up:
                direction =  down
            elif event.key == pygame.K_LEFT and direction != right:
                direction = left
            elif event.key == pygame.K_RIGHT and direction != left:
                direction = right

    # snake movement
    timer += 1
    if timer==5:
        snake =  [[snake[0][0]+direction[0], snake[0][1]+direction[1]]] + snake[:-1]
        timer = 0

    if snake[0][1] < 0:
        snake[0][1] = h

    # snake eats apple
    if snake[0] == apple:
        score += 1
        apple[0] = (random.randint(r+margin, w-r-margin)//step)*step
        apple[1] = (random.randint(r+margin, w-r-margin)//step)*step
        snake.append(snake[-1])

    # game over
    for pos in snake[1:]:
        if snake[0] == pos:
            print("gameover")
            run = False

        

    draw_snake(screen, snake)

    pygame.draw.circle(screen, (217, 12, 44), apple, 10)

    display_score(screen, score)

    pygame.display.update()


