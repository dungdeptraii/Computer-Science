import pgzrun
from random import randint
WIDTH=1200  
HEIGHT=720
score=0
game_over=False
shipper=Actor('shipper')
shipper.pos=100,500
parcel=Actor('parcel')
parcel.pos=300,300
music.play('nhac')
def draw():
    if not game_over:
     screen.blit('background',(0,0))
     shipper.draw()
     parcel.draw()
     screen.draw.text("Score: "+str(score),color="black", fontsize= 40, topleft=(20,20),bold=True)
    else:
        screen.blit('background',(0,0))
        screen.draw.text("Final score: "+ str(score),color="black", fontsize= 40,topleft=(20,20))
def place_parcel():
    parcel.x=randint(20,(WIDTH-20))
    parcel.y=randint(20,(HEIGHT-20))

def reset_game():
    global score, game_over
    score = 0
    game_over = False
    shipper.pos = 100, 500
    place_parcel()
def press_to_restart():
    global game_over
    if keyboard.SPACE and game_over:
        reset_game()

def update():
    global score
    if keyboard.left:
      if shipper.x>120:
        shipper.x=shipper.x-10
    elif keyboard.right:
      if shipper.x<WIDTH-120:        
        shipper.x=shipper.x+10
    elif keyboard.up:
      if shipper.y>120:  
        shipper.y=shipper.y-10
    elif keyboard.down:
      if shipper.y<HEIGHT-120:         
        shipper.y=shipper.y+10
    parcel_collected=shipper.colliderect(parcel)
    if parcel_collected:
        score=score+10
        place_parcel()
def time_up():
    global game_over
    game_over=True
    screen.draw.text("Game Over! Press SPACE to play again.", color="black", fontsize=40, topleft=(20, 60))

clock.schedule(time_up,20.0)
place_parcel()


pgzrun.go()


