import os, uuid
import matplotlib.pyplot as plt
from datetime import datetime

winOrLoss = input('Enter Win or Loss: ')

from neural_net import csPer5, DATA_DIR

for file in os.listdir(DATA_DIR):
    if file.endswith('.png'):
        os.remove(os.path.join(DATA_DIR, file))

currentDate = str(datetime.date(datetime.now()))

try:
    os.mkdir(os.path.join(DATA_DIR, currentDate))
except:
    pass # ignore exception if folder exists

numGamesForCurrentDate = len(os.listdir(os.path.join(DATA_DIR, currentDate))) + 1

x = list(csPer5.keys())
y = list(csPer5.values())
goal_y = [38, 90, 135, 180, 225, 270]

fig, ax = plt.subplots()
ax.set_title('Game ' + str(numGamesForCurrentDate) + ': ' + winOrLoss)
ax.plot(x, y, label='achieved')
ax.plot(x, goal_y, label='goal')
ax.set_yticks(goal_y + [300])
ax.set_xlabel('Minutes')
ax.set_ylabel('CS')
for i,j in zip(x,y):
    ax.annotate(str(j),xy=(i,j))
plt.legend()
plt.savefig(os.path.join(DATA_DIR, currentDate, str(uuid.uuid4().hex)))
