import os, re

p = re.compile('\d+')

for dir in os.listdir('Training'):
    currDir = os.path.join('Training', dir)
    img = os.listdir(currDir)[0]
    if p.match(img).group() != dir:
        print(f'{p.match(img).group()} does not match {dir}')
