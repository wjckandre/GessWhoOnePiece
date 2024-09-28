import sys
import api

stdoutOrigin=sys.stdout 
sys.stdout = open("log.txt", "w")

characters = api.get_random_characters(773)

for k in range(len(characters)):
    print(api.get_image(characters[k]['name']), ',')

sys.stdout.close()
sys.stdout=stdoutOrigin