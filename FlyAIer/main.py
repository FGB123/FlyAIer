import pygame
import sys
import random

background_colour = (0, 0, 0)

line1 = ""
line2 = ""
line3 = ""
line4 = ""
line5 = ""
line6 = ""
line7 = ""
line8 = ""
line9 = ""
line10 = "FlyAIer booted, control gived. START!"

command = ""
output = ""

speed = 0
height = 0
rotation = 0

SCREENX = 1920
SCREENY = 1280
screen = pygame.display.set_mode((SCREENX, SCREENY))
  
pygame.display.set_caption('FlyAIer')
  
screen.fill(background_colour)

clock = pygame.time.Clock()

pygame.display.flip()

pygame.font.init()
base_font = pygame.font.SysFont("calibri", 64)
user_text = ''

input_rect = pygame.Rect(100, 1050, 1100, 64)

color_active = pygame.Color('gray')

color_passive = pygame.Color('gray')
color = color_passive

active = False
running = True
engine = False
ascend = 0
autospeed = False
inspeed = 0
progress = 0
airport = False
airportangle = random.randint(-2, 2)
output = "Landing angle: " + str(airportangle)
landed = False
fuel = 100
chance = 0

while running:
    screen.fill(background_colour) 
    
    chance = random.randint(0, 1200)
    if chance == 65:
        output = "[SET ANGLE TO " + str(random.randint(-2, 2)) + "!]"

    if fuel < 0: fuel = 0

    #if height > 1: speed += 0.2

    if speed == 0 and height > 0: 
        ascend = False
        height -= 0.5

    if engine:
        fuel -= 0.01
        fuel = round(fuel, 3)

    if progress < 100:
        progress += round(speed, 2) / 4000
        progress = round(progress, 2)

    if progress > 80 and airport == False and landed == False:
        output = "[AIRPORT NEAR! START DESCENDING, LANDING ANGLE = " + str(airportangle) + "]"
        airport = True

    if airport and height == 0 and speed == 0 and round(rotation) == airportangle:
        output = "[LANDED SUCCESFULLY]"
        airport = False
        landed = True

    if speed == inspeed:
        autospeed = False
        inspeed = 0

    if autospeed:
        if speed < inspeed:
            engine = True
        else:
            engine = False

    if speed > 20:
        height += 0.02

    if ascend == 1:
        height += 0.07
    if ascend == -1:
        height -= 0.07

    if height > 150:
        output = "[TOO HIGH! DECLINE]"

    if engine and fuel != 0:
        speed += 0.05
    if engine == False and speed > 0:
        speed -= 0.02
    if speed < 0:
        speed = 0
    
    if height < 0:
        height = 0

    if speed < 1.7 and height > 0:
        height -= 0.07

    if speed > 150:
        output = "[SPEED TOO HIGH! SLOWDOWN!]"

    if output != "":
        line10 = line9
        line9 = line1
        line1 = line2
        line2 = line3
        line3 = line4
        line4 = line5
        line5 = line6
        line6 = line7
        line7 = line8
        line8 = output
        output = ""

    for event in pygame.event.get():      
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True
            else:
                active = False
  
        if event.type == pygame.KEYDOWN:
  
            if event.key == pygame.K_BACKSPACE:
  
                user_text = user_text[:-1]

            elif event.key == pygame.K_RETURN:

                line10 = line9
                line9 = line1
                line1 = line2
                line2 = line3
                line3 = line4
                line4 = line5
                line5 = line6
                line6 = line7
                line7 = line8
                line8 = user_text
                command = user_text
                user_text = ""

            elif event.key == pygame.K_LEFT:
                rotation -= 0.25
            
            elif event.key == pygame.K_RIGHT:
                rotation += 0.25

            else:
                user_text += event.unicode
  
    if active:
        color = color_active
    else:
        color = color_passive

    if ":ascend" in command:
        if ascend == 1:
            ascend = 0
        else:
            ascend = 0
            ascend = 1

    if ":decline" in command:
        if ascend == -1:
            ascend = 0
        else:
            ascend = 0
            ascend = -1


    if ":engine" in command:
        if engine:
            engine = False
        else:
            engine = True
        command = ""
        
    if ":setspeed" in command:
        if autospeed:
            autospeed = False
            engine = False
        elif autospeed == False:
            command = command.replace(":setspeed ", "")
            inspeed = int(command)
            autospeed = True
        command = ""


    if ":speed_up" in command:
        speed += 1
        command = ""
        output = "[SPEED INCREASED]"
    if ":height_up" in command:
        height += 1
        command = ""
        output = "[HEIGHT INCREASED]"
    if ":speed_down" in command:
        speed -= 1
        command = ""
        output = "[SPEED DECREASED]"
    if ":height_down" in command:
        height -= 1
        command = ""
        output = "[HEIGHT DECREASED]"
    if ":rotation+" in command:
        rotation += 0.5
        command = ""
        output = "[ROTATION CHANGED]"
    if ":rotation-" in command:
        rotation -= 0.5
        command = ""
        output = "[ROTATION CHANGED]"

    pygame.draw.rect(screen, color, input_rect)
  
    text_surface = base_font.render(user_text, True, (255, 255, 255))

    textline1 = base_font.render(line1, True, (255, 255, 255))
    textline2 = base_font.render(line2, True, (255, 255, 255))
    textline3 = base_font.render(line3, True, (255, 255, 255))
    textline4 = base_font.render(line4, True, (255, 255, 255))
    textline5 = base_font.render(line5, True, (255, 255, 255))
    textline6 = base_font.render(line6, True, (255, 255, 255))
    textline7 = base_font.render(line7, True, (255, 255, 255))
    textline8 = base_font.render(line8, True, (255, 255, 255))
    textline9 = base_font.render(line9, True, (255, 255, 255))
    textline10 = base_font.render(line10, True, (255, 255, 255))

    rotationtext = base_font.render("Rotation: " + str(rotation), True, (255, 255, 255))
    speedtext = base_font.render("Speed: " + str(round(speed, 2)), True, (255, 255, 255))
    heighttext = base_font.render("Height: " + str(round(height, 2)), True, (255, 255, 255))
    enginetext = base_font.render("Engine: " + str(engine), True, (255, 255, 255))
    aspeedtext = base_font.render("Auto-Speed: " + str(autospeed), True, (255, 255, 255))
    progresstext = base_font.render("Progress: " + str(progress) + "%", True, (255, 255, 255))
    fueltext = base_font.render("Fuel: " + str(fuel) + "%", True, (255, 255, 255))

    screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
    screen.blit(textline1, (100, 400))
    screen.blit(textline2, (100, 480))
    screen.blit(textline3, (100, 560))
    screen.blit(textline4, (100, 640))
    screen.blit(textline5, (100, 720))
    screen.blit(textline6, (100, 800))
    screen.blit(textline7, (100, 880))
    screen.blit(textline8, (100, 940))
    screen.blit(textline9, (100, 320))
    screen.blit(textline10, (100, 240))

    screen.blit(speedtext, (1400, 240))
    screen.blit(heighttext, (1400, 300))
    screen.blit(rotationtext, (1400, 360))
    screen.blit(enginetext, (1400, 420))
    screen.blit(aspeedtext, (1400, 480))
    screen.blit(progresstext, (1400, 540))
    screen.blit(fueltext, (1400, 600))
    
    input_rect.w = max(100, text_surface.get_width()+10)

    pygame.display.update()

    clock.tick(60)