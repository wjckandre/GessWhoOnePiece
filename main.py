import pygame
import api
import io
try:
    # Python2
    from urllib3 import urlopen
except ImportError:
    # Python3
    from urllib.request import urlopen


background_colour = (255,255,255)
(width, height) = (800, 800)
screen_size = (width, height)

grid = (4, 4)
nb_case = grid[0]*grid[1]
tile_size = (width/grid[0] - width/(grid[0]+8), height/grid[1] - height/(grid[1]+8) )
print(tile_size)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('One Piece Guess Who')

characters = api.get_random_characters(nb_case)
# images = []
# for k in range(len(characters)):
#     image_file = io.BytesIO(urlopen(api.get_image(characters[k]['name'])).read())
#     images.append(pygame.image.load(image_file))
#     print(characters[k]['name'])
images = []
for k in range(nb_case):
    image_url = api.get_image(characters[k]['name'])
    image_str = urlopen(image_url).read()
    image_file = io.BytesIO(image_str)
    
    image_file = pygame.image.load(image_file)

    images.append(pygame.transform.scale(image_file, tile_size))
    print(f"Image of {characters[k]['name']} done !")

def grid_to_screen(grid_pos, screen):
    screen_x = (screen[0] ) * (grid_pos[0]+1)
    screen_y = (screen[1] ) * (grid_pos[1]+1) 
    print(f"i =  {grid_pos[0]+1}   ;   j =  {grid_pos[1]+1}")
    print(f"position :  {(screen_x, screen_y)}")
    return screen_x, screen_y

screen.fill(background_colour)

x = 0
for i in range(grid[0]):
    for j in range(grid[1]):
        # pygame.Rect(grid_to_screen((i,j), tile_size), tile_size)
        screen.blit(images[x], grid_to_screen((i,j), tile_size))
        
        # screen.blit(images[x], (i,j))
        x += 1

pygame.display.flip()
running = True
while running:
    
        

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

