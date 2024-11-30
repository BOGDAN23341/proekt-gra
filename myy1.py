# імпорт бібліотеки pygame
import pygame
pygame.init()

class Player():  # клас для створення шаблону персонажа
    def __init__(self, x, y, width, height, image):
        self.original_image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.original_image, (width, height))  # Зміна розміру зображення
        self.rect = self.image.get_rect()  # "межі" персонажа
        self.rect.x = x  # координати по ширині
        self.rect.y = y  # координати по висоті
        self.width = width  # ширина
        self.height = height  # висота

    def move(self):
        keys = pygame.key.get_pressed()  # зберігаємо всі можливі натиснуті клавіші в список keys
        if keys[pygame.K_a]:  # якщо натиснута клавіша "стрілка ліворуч"
            self.rect.x -= 2  # змінюємо координати гравця по x на -2
        if keys[pygame.K_d]:  # якщо натиснута клавіша "стрілка праворуч"
            self.rect.x += 2  # змінюємо координати гравця по x на +2
        if keys[pygame.K_w]:  # якщо натиснута клавіша "стрілка вверх"
            self.rect.y -= 2  # змінюємо координати гравця по y на -2
        if keys[pygame.K_s]:  # якщо натиснута клавіша "стрілка вниз"
            self.rect.y += 2  # змінюємо координати гравця по y на +2

# створення головного вікна
window = pygame.display.set_mode((500, 500))

# Завантаження зображення фону 
background_image = pygame.image.load('background.png') 
background_image = pygame.transform.scale(background_image, (500, 500))

# створення персонажа
player = Player(100, 100, 50, 50, 'bird.png')

# Створення ялинок
trees = [
    Player(30, 50, 100, 100, 'tree.png'),    # Ліва сторона
    Player(120, 100, 100, 100, 'tree.png'),
    Player(200, 150, 100, 100, 'tree.png'),
    Player(250, 200, 100, 100, 'tree.png'),
    Player(80, 250, 100, 100, 'tree.png'),
    Player(180, 300, 100, 100, 'tree.png'),
    Player(300, 70, 100, 100, 'tree.png'),
    Player(350, 150, 100, 100, 'tree.png'),
    Player(50, 300, 100, 100, 'tree.png'),
    Player(200, 400, 100, 100, 'tree.png'),
    Player(300, 400, 100, 100, 'tree.png'),
    Player(400, 100, 100, 100, 'tree.png'),  # Права сторона
    Player(400, 250, 100, 100, 'tree.png'),
    Player(350, 350, 100, 100, 'tree.png'),
    Player(250, 400, 100, 100, 'tree.png'),
    Player(450, 150, 100, 100, 'tree.png'),
    Player(400, 200, 100, 100, 'tree.png'),
    Player(450, 50, 100, 100, 'tree.png'),
    Player(500, 300, 100, 100, 'tree.png'),
    Player(550, 250, 100, 100, 'tree.png')
]



# кольори
white = (255, 255, 255)
black = (0, 0, 0)

# створення об'єкту "годинник" для встановлення частоти кадрів
clock = pygame.time.Clock()

# головний цикл гри
game = True
while game:
    window.fill(white)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    
    # відображення фону
    window.blit(background_image, (0, 0))

    # відображення ялинок
    for tree in trees:
        window.blit(tree.image, (tree.rect.x, tree.rect.y))  
    
    # відображення персонажа
    window.blit(player.image, (player.rect.x, player.rect.y))  
    
    player.move()

    # задання частоти кадрів та оновлення екрану
    clock.tick(30)
    pygame.display.update()

pygame.quit()

