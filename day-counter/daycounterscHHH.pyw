from nbt import nbt
from time import sleep

def checkDay():
    sb = nbt.NBTFile(r'C:\Users\click\AppData\Roaming\PrismLauncher\instances\Hardcore Fabric\.minecraft\saves\ThisWillBeShortLived\data\scoreboard.dat', 'rb')
    for i in enumerate(sb['data']['PlayerScores']):
        if i[1]['Objective'].value == 'daycount':
            d = i[1]['Score'].value
            return d

while True:
    with open('daycounter.txt','w') as f:
        f.write(f'Day: {checkDay():,}')
    sleep(60)