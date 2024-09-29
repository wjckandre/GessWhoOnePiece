import pygame
import api
import io
import random
import pyperclip

try:
    # Python2
    from urllib3 import urlopen
except ImportError:
    # Python3
    from urllib.request import urlopen

pygame.init()
######## SETTINGS ########
background_colour = (0,0,0)
background = pygame.image.load("background.jpg")
(width, height) = (1800, 1000)
screen_size = (width, height)
background_image = pygame.transform.scale(background, screen_size)
font = pygame.font.Font('freesansbold.ttf', 15)

grid = (8, 6)
nb_case = grid[0]*grid[1]
tile_size = (width/grid[0] - width/(grid[0]+(grid[0]*4)), height/grid[1] - height/(grid[1]+(grid[1]*2.5)) )
cross = pygame.transform.scale(pygame.image.load("cross.png"), tile_size)
print(tile_size)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('One Piece Guess Who')

with open('log.txt', 'r') as fichier:
    # Lis toutes les lignes du fichier
    images = fichier.readlines()
# Supprime les retours à la ligne et autres caractères indésirables
images = [ligne.strip() for ligne in images]
for i in range(len(images)):
    images[i] = (i,images[i])


##############################
image_url = random.sample(images, nb_case)
##############################
# image_url = ["https://static.wikia.nocookie.net/onepiece/images/0/04/X_Drake_Anime_Post_Timeskip_Infobox.png/revision/latest?cb=20200209080003 ,"]*8*6
##############################
images_loaded = []
for k in image_url:
    
    image_str = urlopen((k[1]).replace(' ,', '')).read()
    image_file = io.BytesIO(image_str)
    
    image_file = pygame.image.load(image_file)

    images_loaded.append((k[0],pygame.transform.scale(image_file, tile_size)))

seed = []
for i in images_loaded:
    seed.append(i[0])

############### FUNCTION ###############

def grid_to_screen(grid_pos, screen):
    screen_x = (screen[0] ) * (grid_pos[0]+1)
    screen_y = (screen[1] ) * (grid_pos[1]+1) 
    return screen_x, screen_y


def display(image, coords):
    screen.blit(image, coords)


def choose_target(seed):
    print("(((())))",type(seed))
    for i in range(len(seed)):
        print("############", seed[i])
    return display( pygame.transform.scale( pygame.image.load (io.BytesIO (urlopen(images[int(seed[random.randint(0,len(seed)-1)])][1].replace(' ,', '')).read())) ,tile_size), (0,screen_size[1]-400))


########################################
display(background_image, (0,0))
rects = []
x = 0
for i in range(grid[0]):
    for j in range(grid[1]):
        rects.append(pygame.Rect(grid_to_screen((i,j), tile_size), tile_size))
        screen.blit(images_loaded[x][1], grid_to_screen((i,j), tile_size))
        x += 1
i = 0

tiles = []
for i in range(len(images_loaded)):
    tiles.append([rects[i], images_loaded[i][1]])





seed_display = font.render(str(seed), True, (255,255,255))
seed_button = pygame.Rect((0,screen_size[1]-100),(50,50))
seed_image = pygame.transform.scale(pygame.image.load('copy.png'),(50,50))

seek_button = pygame.Rect((0,screen_size[1]-200),(50,50))
seek_image = pygame.transform.scale(pygame.image.load('red.png'),(50,50))
#########################################################################   GAME LOOP   #########################################################################

running = True
while running:

    display(seed_display, (0,screen_size[1]-50))
    display(seed_image,(0,screen_size[1]-100))
    display(seek_image,(0,screen_size[1]-200))
    for event in pygame.event.get():

        if event.type == pygame.QUIT or len(tiles) == 0:
            running = False

    # Vérifier si un clic de souris est détecté
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
            pos = pygame.mouse.get_pos()  # Obtient la position de la souris
            for rect in tiles:
                if rect[0].collidepoint(pos):  # Vérifie si le rectangle est cliqué
                    display(cross, rect[0].topleft)
            if seed_button.collidepoint(pos):
                pyperclip.copy(seed)
                print("Copied in the Clipboard")
            elif seek_button.collidepoint(pos):
                choose_target( pyperclip.paste().replace('[','').replace(']','').split(', ') )
                print(pyperclip.paste())
        elif event.button == 3:
            pos = pygame.mouse.get_pos()  # Obtient la position de la souris
            for rect in tiles:
                if rect[0].collidepoint(pos):  # Vérifie si le rectangle est cliqué
                    display(rect[1], rect[0].topleft)

    pygame.display.flip()