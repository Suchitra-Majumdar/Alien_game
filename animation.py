import pgzrun
import random

WIDTH = 500
HEIGHT = 500

lives = 5

color_score = "white"

game_status = 0

speed = 5

score = 0

on_edge = False

alien_status = " "

alien = Actor("alien")
alien.pos = (90,90)

def draw():
    global alien_status, color_score, lives, game_status
    if game_status == 0:
        screen.blit("images",(150,120))
        #screen.draw.text("Press ENTER to start",center=(WIDTH/2,HEIGHT/2))
    if game_status == 1:
        screen.blit("space3", (0,0))
        alien.draw()
        screen.draw.text(f"Score: {score}",(75,50),color = color_score)
        screen.draw.text(f"Lives: {lives}", (75, 75))
        if alien_status == "Hit":
            screen.draw.text("You hit me",center=(WIDTH/2,HEIGHT/2),fontname="jackie",color="yellow")
        elif alien_status == "Miss":
            screen.draw.text("You missed me",center=(WIDTH/2,HEIGHT/2),fontname="jackie",color="yellow")
        if lives <= 0:
            screen.clear()
            screen.blit("download",(120,HEIGHT/4))
            #screen.draw.text(f"Game Over! Your score: {score}",center=(WIDTH/2,HEIGHT/5),color="red")
               

def update():
    global on_edge, speed, score, game_status
    if game_status == 0:
        if keyboard.RETURN:
            game_status = 1
    if game_status == 1:
        if alien.left > 500:
            on_edge = True
            alien.y = random.randint(50,450)
        if on_edge == False:
            alien.left += speed
        else:
            alien.left -= speed
            if alien.left < 0:
                on_edge = False
                alien.y = random.randint(50,450)
        if score < 0:
            score = 0


def on_mouse_down(pos):
    global speed, alien_status, score, color_score, lives, game_status
    if game_status == 1:
        if alien.collidepoint(pos):
            score += 1
            color_score = "yellow"
            sounds.splat.play()
            alien.image = "alien_hurt"
            clock.schedule_unique(set_alien_normal,0.5)
            print("You hit me.")
            alien_status = "Hit"
            speed += 1
        else:
            print("You failed!")
            score -= 1
            color_score = "red"
            alien_status = "Miss"
            speed -= 0.5
            lives -= 1
        
def set_alien_normal():
    alien.image = "alien"

pgzrun.go()
