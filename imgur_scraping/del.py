from pathlib import Path
import os
from time import sleep

p = Path.cwd() / 'imgurdownloader'
print('Image Deleter..')
delist = list(p.glob('*.jpg'))
Total_items = len(delist)
if delist:
    for item in delist:
        print(f'Deleting {item}')
        os.unlink(item)
    print(f'Total items deleted were {Total_items}')
else:
    print('Nothing left to Delete', end='')
