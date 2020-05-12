import os
from shutil import copyfile

for i in range(201):
    path = os.path.join('Training', str(i))
    for img in os.listdir(path):
        copyfile(os.path.join(path, img), os.path.join('Testing', f'{i}.png'))