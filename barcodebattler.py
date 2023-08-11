#Barcode Battler

#Import modules
from sys import argv
import zbar, random, pygame, time

#Pygame init
pygame.init()
pygame.mixer.init()

#Variable
global player, HP,enemyHP, enemy_name, weapon, equip, code

#Functions
def picture(img,w,h):
    pic = pygame.image.load(img)
    background = (0, 0, 0)
    screen = pygame.display.set_mode((w,h))
    screen.fill((background))
    screen.blit(pic,(0,0))
    pygame.display.flip()
    time.sleep(3)
    pygame.display.quit()

def audio(music):
    pygame.mixer.init()
    pygame.mixer.music.load(music)
    pygame.mixer.music.play(1)

def scanner():
    global code
    proc = zbar.Processor()
    proc.parse_config('enable')
    device = '/dev/video1'
    if len(argv) > 1:
        device = argv[1]
    proc.init(device)
    proc.visible = True
    proc.process_one()
    proc.visible = False
    for symbol in proc.results:
        code = symbol.data

#Choose player, this is handled via QR codes.
def player():
        global code,player,HP
        if code == "Andrew":
                print("Andrew is your warrior")        
                HP = random.randint(10,100)
                player = "Andrew"
                print(player+" has "+str(HP)+" HP")
        elif code == "Ben":
                print("Ben is your warrior")
                HP = random.randint(10,100)
                player = "Ben"
                print(player+" has "+str(HP)+" HP")
        elif code == "Graham":
                print("Graham is your warrior")
                HP = random.randint(10,100)
                player = "Graham"
                print(player+" has "+str(HP)+" HP")
        elif code == "Mike":
                print("Mike is your warrior")
                HP = random.randint(10,100)
                player = "Mike"
                print(player+" has "+str(HP)+" HP")
        else:
                print("Player not recognised, please scan one of the cards to continue")

#Generate an enemy.
def enemy():
        global enemy_name
        global enemyHP
        enemy_names = ["Windows10","MegaDave","OpenSourcerer"]
        enemy_name = random.choice(enemy_names)
        enemyHP = random.randint(10,100)
        print("Your enemy is "+enemy_name)
        if enemy_name == "OpenSourcerer":
                audio("os.mp3")
                picture("wizard-penguin.png",616,800)
                print("They have "+str(enemyHP)+" HP")
        elif enemy_name == "MegaDave":
                audio("megadave.mp3")
                picture("openmouthrobot.png",606,719)
                print("They have "+str(enemyHP)+" HP")
        elif enemy_name == "Windows10":
                audio("win10.mp3")
                picture("clippy.jpg",620,465)
                print("They have "+str(enemyHP)+" HP")
              

#Equip player with a weapon
def weapon():
        global code
        global weapon
        scanner()
        print(code)
        value = int(code) / 13000000000 / random.randint(1,10)
        if value > 0 and value < 39:
                print("You have a basic wooden sword")
                weapon = ("wooden_sword")
                audio("wood_sword.mp3")
                picture("bokken.png",800,354)
        elif value > 39 and value < 56:
                print("You have a steel sword")
                weapon = ("steel_sword")
                audio("steel_sword.mp3")
                picture("nello-sword.png",800,771)
        elif value > 56 and value < 400:
                print("You have no sword...you will have to use your fists of fury!")
                weapon = ("fists")
                audio("fists_of_fury.mp3")
                picture("fist-265.png",539,800)
        else:
                print("You have an enchanted sword of mega power")
                weapon = ("enchanted_sword")
                audio("mega_sword.mp3")
                picture("lilking-Jeweled-Sword.png",800,556)

def equip():
        global code
        global equip
        scanner()
        print(code)
        value = int(code) / 13000000000 / random.randint(1,10)
        if value > 0 and value < 39:
                print("You have a basic wooden shield")
                equip = ("wood_shield")
                audio("wood_shield.mp3")
                picture("Shield-ClassicViking.png",800,800)
        elif value > 39 and value < 56:
                print("You have an iron shield")
                equip = ("iron_shield")
                audio("iron_shield.mp3")
                picture("Shield-ClassicMedieval.png",586,800)
        elif value > 56 and value < 400:
                print("You have no shield...that sucks")
                equip = ("nothing")
                audio("no_shield.mp3")
                picture("fist-265.png",539,800)
        else:
                print("You have a seriously powerful mirrored shield")
                equip = ("mirror_shield")
                audio("mirror_shield.mp3")
                picture("Peileppe-Magic-Shield.png",791,800)

def player_attack():
        global enemy_name
        global enemyHP
        chance = ["attack","miss"]
        chance = random.choice(chance)
        if chance != "miss":
                damage = random.randint(0,10)
                print("DAMAGE:",damage)
                enemyHP = enemyHP - damage
                print("You cause "+str(damage)+" damage to "+(enemy_name)+" they now have "+str(enemyHP)+" HP")
        elif HP < 1:
                print("YOU'RE DEAD")
                game_over()
                
        else:
                print("Player misses the opponent")
        
                
def enemy_attack():
        global player
        global HP      
        chance = ["attack","miss"]
        chance = random.choice(chance)
        if chance != "miss":
                damage = random.randint(0,10)
                print("DAMAGE:",damage)
                time.sleep(2)
                HP = HP - damage
                print("Your enemy causes "+str(damage)+" damage to "+(player)+" they now have "+str(HP)+" HP")
        elif enemyHP < 1:
                print("ENEMY DEAD")
        else:
                print("Opponent misses the player")

def prepare():
        red = 255
        green = 255
        blue = 255
        pygame.font.init()
        screen = pygame.display.set_mode( (800,600) )
        for i in range(127):
            red -= 2
            green -= 2
            blue -= 2
            screen.fill( (red,green,blue) )
            myfont = pygame.font.Font(None, 60)
            info1 = myfont.render("PREPARE FOR BATTLE",1,(0,0,0))
            screen.blit(info1, (150,300))
            pygame.display.flip()
            #pygame.display.flip()
            pygame.time.delay(32)

        pygame.display.quit()

def warrior():
        global player
        red = 255
        green = 255
        blue = 255
        pygame.font.init()
        screen = pygame.display.set_mode( (800,600) )
        for i in range(127):
            red -= 2
            green -= 2
            blue -= 2
            screen.fill( (red,green,blue) )
            myfont = pygame.font.Font(None, 60)
            info1 = myfont.render("Your warrior is "+(player),1,(0,0,0))
            screen.blit(info1, (150,300))
            pygame.display.flip()
            pygame.display.flip()
            pygame.time.delay(32)
    
        pygame.display.quit()

def battle_graphics():
    global enemyHP, HP, player, enemy_name
    pygame.font.init()
    screen = pygame.display.set_mode( (800,600) )
    screen.fill( (255,255,255) )
    myfont = pygame.font.Font(None, 60)
    warriorpower = myfont.render(player+" has "+str(HP)+"HP",1,(0,0,0))
    enemypower = myfont.render(enemy_name+(" has ")+str(enemyHP)+"HP",1,(0,0,0))
    screen.blit(warriorpower, (0,200))
    screen.blit(enemypower, (0, 400))
    pygame.display.flip()
    pygame.time.delay(32)
    time.sleep(2)
    pygame.display.quit()


#T E S T I N G

audio("Marieva_s_Project_-_la_marche_des_infideles.mp3")
picture("masthead.gif",500,229)
time.sleep(15)
audio("choose.mp3")
picture("choose.png",800,600)
scanner()
player()
warrior()
enemy()
time.sleep(5)
weapon()
time.sleep(5)
equip()
audio("battle.mp3")
prepare()
while True:
        if HP <= 0 or enemyHP <= 0:
                print("G A M E  O V E R")
                if HP < 1:
                        print("Your enemy has won!")
                        audio("defeat.mp3")
                else:
                        print("You have vanquished your enemy")
                        audio("enemy_vanquished.mp3")
                break

        else:
                audio("fight_music.mp3")
                player_attack()
                battle_graphics()
                time.sleep(1)
                enemy_attack()
                battle_graphics()
