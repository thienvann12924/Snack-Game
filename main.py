import pygame
import sys
import random
import math
from pygame.math import Vector2
from design_elements import *


# We are using vector instead of list as they are more useful in 2D  calculations
# Vector2 is is 2d matris 2X1 matrix

# snake class for sanke movements
class Snake:
    def __init__(self):
        # this is initial position of snake
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        # this is direction vector
        self.direction = Vector2(0, 0)

        self.head_up = pygame.image.load('Graphics/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('Graphics/head_down.png').convert_alpha()
        self.head_right = pygame.image.load('Graphics/head_right.png').convert_alpha()
        self.head_left = pygame.image.load('Graphics/head_left.png').convert_alpha()

        self.tail_up = pygame.image.load('Graphics/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('Graphics/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('Graphics/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('Graphics/tail_left.png').convert_alpha()

        self.body_vertical = pygame.image.load('Graphics/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('Graphics/body_horizontal.png').convert_alpha()

        self.body_tr = pygame.image.load('Graphics/body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load('Graphics/body_tl.png').convert_alpha()
        self.body_br = pygame.image.load('Graphics/body_br.png').convert_alpha()
        self.body_bl = pygame.image.load('Graphics/body_bl.png').convert_alpha()
        self.fruit_eat_sound = pygame.mixer.Sound('sounds/game_sound.mp3')
        self.collision_sound = pygame.mixer.Sound('sounds/collision_sound.mp3')
        self.head = self.head_right
        self.alive = True
        # importing snake graphics

    def change_direction(self, direction_vector):
        self.direction = direction_vector

    def draw_snake(self):
        self.update_midlle_body()
        self.update_head_graphics()
        self.update_tail_graphics()
        for index, block in enumerate(self.body):
            # cycling through all blocks and drawing the rectangles
            x_pos = block.x * CELL_SIZE
            y_pos = block.y * CELL_SIZE
            height = CELL_SIZE
            block_rect = pygame.Rect(x_pos, y_pos, height, height)
            if index == 0:
                screen.blit(self.head, block_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail, block_rect)
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical, block_rect)
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal, block_rect)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_tl, block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_bl, block_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        screen.blit(self.body_tr, block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        screen.blit(self.body_br, block_rect)

                # pygame.draw.rect(screen,(180,110,122),block_rect)

    # snake motion
    def mov_snake(self):
        # this would give all blocks except last
        body_copy = self.body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]

    # updating head position
    def update_head_graphics(self):
        head_position = self.body[1] - self.body[0]
        # head will be in opposite postion of our head_position
        if head_position == Vector2(1, 0):
            self.head = self.head_left
        elif head_position == Vector2(-1, 0):
            self.head = self.head_right
        elif head_position == Vector2(0, 1):
            self.head = self.head_up
        elif head_position == Vector2(0, -1):
            self.head = self.head_down

    def update_tail_graphics(self):
        tail_direction = self.body[len(self.body) - 2] - self.body[-1]
        if tail_direction == Vector2(1, 0):
            self.tail = self.tail_left
        elif tail_direction == Vector2(-1, 0):
            self.tail = self.tail_right
        elif tail_direction == Vector2(0, 1):
            self.tail = self.tail_up
        elif tail_direction == Vector2(0, -1):
            self.tail = self.tail_down

    def update_midlle_body(self):
        last_index = len(self.body) - 1
        for i in range(1, last_index):
            body_alignment = self.body[i] - self.body[i - 1]
            if body_alignment.x == 0:
                self.body_block = self.body_vertical
            else:
                self.body_block = self.body_horizontal

    def play_sound(self):
        self.fruit_eat_sound.play()

    def reset_snake(self):
        self.body = self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0, 0)
        self.alive = True


# creating class Fruit---------------------------
class Fruit:
    def __init__(self):
        # as it may go out side subtracting 1
        self.x = random.randint(0, CELL_NUMBER - 1)
        self.y = random.randint(0, CELL_NUMBER - 1)
        self.pos = Vector2(self.x, self.y)
        # create x and y pos
        # draw square

    # method to draw fruit on board
    def draw_fruit(self):
        # create a rectangle
        # cell size contains size of each object
        fruit_rect = pygame.Rect(self.pos.x * CELL_SIZE, self.pos.y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        screen.blit(fruit_img, fruit_rect)
        # drawing pruit on screen
        # pygame.draw.rect(screen,(126,116,114),fruit_rect)

    # after eating this would update the position of freuit
    def update_fruit(self):
        self.x = random.randint(0, CELL_NUMBER - 1)
        self.y = random.randint(0, CELL_NUMBER - 1)
        self.pos = Vector2(self.x, self.y)


# Main class
class Main:
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()

    # update function for snake
    def update(self):
        self.snake.mov_snake()
        # we would check if snake has collided with fruit
        self.check_colliosion()  # check collision is for snake eating the fruit
        self.check_snake_dead()

    def draw_elements(self):
        self.snake.draw_snake()
        self.fruit.draw_fruit()
        self.draw_score()

    # this will check if snake is eating the fruit
    def check_colliosion(self):
        if self.fruit.pos == self.snake.body[0]:
            # playing sound only if game audio is not muted
            if not Menu.get_buttom_state(2):
                self.snake.play_sound()
            # extending snake by one block
            # this gives last block of snake
            snake_tail = self.snake.body[-1]
            if self.snake.direction.y != 0:
                x = snake_tail.x
                y = snake_tail.y + 1
            else:
                x = snake_tail.x + 1
                y = snake_tail.y
            # adding new block to end to snake
            self.snake.body.append(Vector2(x, y))

            self.fruit.update_fruit()
            for block in self.snake.body[1:]:
                if block == self.fruit.pos:
                    self.fruit.update_fruit()

    # this function will cheack if sanke itself up or collided with window boundry
    def check_snake_dead(self):
        # if snake is outside of screen
        if not (0 <= self.snake.body[0].x < CELL_NUMBER) or not (0 <= self.snake.body[0].y < CELL_NUMBER):
            self.snake.alive = False

        # if snake head itself
        head = self.snake.body[0]
        for block in self.snake.body[1:]:
            if block == head:
                self.snake.alive = False
        if self.snake.alive == False:
            self.GAME_OVER()

    # this will end the game
    def GAME_OVER(self):
        self.snake.reset_snake()

    # drawing grass over the complete map
    def draw_grass(self, cell_size, cell_number):
        for row in range(0, cell_number, 2):
            for cell in range(0, cell_number, 2):
                cell_rect = pygame.Rect(row * cell_size, cell * cell_size, cell_size, cell_size)
                pygame.draw.rect(screen, (100, 241, 48), cell_rect)

    # this will drow score on our screen
    def draw_score(self):
        # sice lenght is equivalent to score
        score_text = len(self.snake.body) - 3
        score_surface = game_font.render("Score: " + str(score_text), True, (56, 70, 12))
        x = CELL_NUMBER * CELL_SIZE - 100
        y = CELL_NUMBER * CELL_SIZE - 40
        score_rect = score_surface.get_rect(center=(x, y))
        score_icon_rect = fruit_img.get_rect(midright=(score_rect.left - 4, score_rect.centery - 5))
        border = pygame.Rect(score_icon_rect.left - 5, score_icon_rect.top - 4,
                             score_icon_rect.width + score_rect.width + 15,
                             score_icon_rect.height + score_rect.height - 5)

        screen.blit(score_surface, score_rect)
        screen.blit(fruit_img, score_icon_rect)
        pygame.draw.rect(screen, (77, 249, 205), border,
                         3)  # last argument 2 is line width it  will draw a frame insteda of rectangle


# this function is to move snake with joy stick input:

def mov_snake_with_joystick(direction):
    if direction != None:
        if direction.y == 0:
            if main_game.snake.direction.x != -direction.x:
                main_game.snake.change_direction(direction)
        else:
            if main_game.snake.direction.y != -direction.y:
                main_game.snake.change_direction(direction)


# making pygame sounds play immediately
pygame.mixer.pre_init(44100, -16, 2, 512)
# initializing pygame
pygame.init()
# variable to store cell size and numbers-----------------
CELL_SIZE = 40
CELL_NUMBER = 16
SPEED = 300

# screen variable BASED ON CELL
screen = pygame.display.set_mode((CELL_NUMBER * CELL_SIZE, CELL_NUMBER * CELL_SIZE))
pygame.display.set_caption("Snake")
icon = pygame.image.load('images/snake_icon.png').convert_alpha()
pygame.display.set_icon(icon)

# loading image of fruit
fruit_img = pygame.image.load('images/fruit.png').convert_alpha()

# dispaly surface is main surface
# we can create another surfaces with pygame.Surface(size) method

# creating object of main game class
main_game = Main()

# declaring an event
SCREEN_UPDATE = pygame.USEREVENT
# this event will be captured every 300 ms so sanke would move every 150 ms
pygame.time.set_timer(SCREEN_UPDATE, SPEED)

# LOADING GAME FONT
game_font = pygame.font.Font('Fonts/Pixeltype.ttf', 25)

# creating clock object for manipulating fps of game
clock = pygame.time.Clock()

Menu_button = Button(CELL_SIZE * CELL_NUMBER - 65, 5, game_font, True, 'Menu')

Menu = Tab(CELL_SIZE * CELL_NUMBER - 300, 20, 10, 10, 5, 20, game_font, (255, 0, 0), 'Menu')
Menu.add_item('Trun on screen arrow keys', 'Arrow On')
Menu.add_item('Change Speed', 'Speed')
Menu.add_item('Mute audio', 'Mute')
Menu.set_toggle_button(0, 'Arrow off')
Menu.set_toggle_button(1, "Slow")
Menu.set_toggle_button(2, 'Unmute')
Menu.set_visibility(False)

side_len = CELL_SIZE * CELL_NUMBER
size = CELL_SIZE * 3
joy_stick = ArrowButtons(20, side_len - size - 10, game_font, size)

Prev_state = Menu.get_buttom_state(1)

while True:
    # adding color to our screen
    screen.fill((106, 234, 43))
    main_game.draw_grass(CELL_SIZE - 10, CELL_NUMBER + 10)
    # this will generate button with hover effects (inbuilt module)
    mouse = pygame.mouse.get_pos()
    Menu_button.draw(screen, mouse, (255, 25, 25))
    Menu.draw(screen, mouse)  # drawing items

    if Prev_state != Menu.get_buttom_state(1):
        if Prev_state == False:
            SPEED = 130
        else:
            SPEED = 300
        pygame.time.set_timer(SCREEN_UPDATE, SPEED)
        Prev_state = Menu.get_buttom_state(1)

    # his for loop will check for any events accurring on computer like click, mouse movement etc
    for event in pygame.event.get():
        # this will stop game when cross button is clicked
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == SCREEN_UPDATE:
            main_game.update()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()

            # This will make menu tab visible
            if Menu_button.draw(screen, mouse_pos, (100, 255, 25)):
                Menu.set_visibility(True)
                Menu.draw(screen, mouse_pos)
                print('Menu button clicked')

            # this will close the menu tab
            Menu.close_button_clicked(mouse)

            # this will check if any button is clicked in tab and then it will toggle it
            Menu.check_button_clicked(mouse_pos)

            # this would check which buton is clicked on joystick
            mov_snake_with_joystick(joy_stick.check_button_clicked(mouse_pos))

        # this will allow user to move the snake
        if event.type == pygame.KEYDOWN:
            # moving snake up
            if event.key == pygame.K_UP:
                # if snake is moving down we can't move it up this not possible as snake would collide with itself similarly below.....
                if main_game.snake.direction.y != 1:
                    main_game.snake.change_direction(Vector2(0, -1))
            # moving snake down
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.change_direction(Vector2(0, 1))
            # moving snake left
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.change_direction(Vector2(-1, 0))
            # moving snake rigth
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.change_direction(Vector2(1, 0))

    joy_stick.draw_keys(screen, Menu.get_buttom_state(0))
    main_game.draw_elements()
    pygame.display.update()
    # setting frame rate to 60 hz
    clock.tick(60)
