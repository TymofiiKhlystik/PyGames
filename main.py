import pygame

pygame.init()

WIDTH, HEIGHT = 860, 540
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("half pong")
clock = pygame.time.Clock()

PLATFORM_WIDTH = 120
PLATFORM_HEIGHT = 15
SPEED_PLATFORM = 10
platform_rect = pygame.rect.Rect(WIDTH // 2 - PLATFORM_WIDTH / 2,
                                 HEIGHT - PLATFORM_HEIGHT * 2,
                                 PLATFORM_WIDTH,
                                 PLATFORM_HEIGHT)

game = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    if not game:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            platform_rect.x -= SPEED_PLATFORM
            if platform_rect.x < 0:
                platform_rect.x = 0
        if keys[pygame.K_RIGHT]:
            platform_rect.x += SPEED_PLATFORM
            if platform_rect.x > WIDTH-platform_rect.width:
                platform_rect.x = WIDTH-platform_rect.width

    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, platform_rect)
    pygame.display.update()
    clock.tick(FPS)


