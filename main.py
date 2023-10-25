import pygame
import random


pygame.init()


# Setting the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("Snake Game")

#Snake Colour
white = (255,255,255)

#Background colour
black = (0,0,0)

#Food Colour
red = (255,0,0)

clock = pygame.time.Clock()


game_over = False

#Variable starting point of snake based on the window..
x1 = window_width/2
y1 = window_height/2


x1_change = 0
y1_change = 0

#Representing food at random co-ordinate
foodx = round(random.randrange(0,window_width-10)/10)*10.0
foody = round(random.randrange(0,window_height-10)/10)*10.0

#Length of snake and the score of it
length_of_snake = 1
score = 0

#Starting speed of snake
init_speed = 15


#Points at which the snake's body is dispersed all over.. 
snake_body = []
# This keeps the game window keep on running until the user quits the game..
# So basically this listens to the user's action
while not game_over:
    for event in pygame.event.get():
        #QUIT is prompted as an event whenever user clicks exit button on top.. and game is closed.. 
        if event.type == pygame.QUIT:
            game_over = True
        
        #CHECK FOR ARROWS PRESSED
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP:
                x1_change = 0
                y1_change = -10
            elif event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = 10


    x1 = x1 + x1_change
    y1  = y1 + y1_change

    #Snake crashing at the boundaries
    if x1>=window_width or x1<0 or y1>=window_height or y1<0:
        game_over = True

    window.fill(black)

    snake_head = []
    snake_head.append(x1)
    snake_head.append(y1)

    snake_body.append(snake_head)

    #Clearing the tails from leaving traces..
    if len(snake_body)>length_of_snake:
        del snake_body[0]

    # When Snake hits itself..
    for segment in snake_body[:-1]:
        if segment == snake_head:
            game_over = True
    
    #Displaying the score..
    font_style = pygame.font.SysFont(None,50)
    score_text = font_style.render("Score: "+ str(score),True, white)
    window.blit(score_text,(10,10))

    increasing_speed = init_speed


    #If snake eats food.. 
    if x1 == foodx and y1==foody:
        foodx = round(random.randrange(0,window_width-10)/10)*10.0
        foody = round(random.randrange(0,window_height-10)/10)*10.0
        length_of_snake += 1
        if length_of_snake%5 == 0:
            increasing_speed += 5
        score += 1

    #Representing food in the window..
    pygame.draw.rect(window,red,[foodx,foody,10,10])

    #pygame.draw.rect(window, white, [x1,y1,10,10])
    for segment in snake_body:
        pygame.draw.rect(window, white, [segment[0],segment[1],10,10])
    pygame.display.update()

    # Initial speed of snake starts at 15fps and can go as +5fps after every 5 points scored..
    # We can control it using clock object.
    clock.tick(increasing_speed)