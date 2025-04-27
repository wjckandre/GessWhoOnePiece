import re

# Regex mise à jour : on cherche .png, .jpg, etc. n'importe où dans la ligne
valid_ext = re.compile(r'\.(png|jpe?g|webp|gif)\b', re.IGNORECASE)

with open('log.txt', 'r') as f:
    lines = f.readlines()

# On garde TOUTES les lignes où apparaît une des extensions
lines_with_images = [line for line in lines if valid_ext.search(line)]

with open('log_clean.txt', 'w') as out:
    out.writelines(lines_with_images)

print(f"{len(lines_with_images)} lignes contenant une extension d'image ont été conservées dans log_clean.txt")
