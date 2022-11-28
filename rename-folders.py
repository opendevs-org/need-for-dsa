import os

start = 0
increment = 0

folders = [x for x in os.listdir('./') if os.path.isdir(x) and x != '.git']
folders.sort()

for folder in folders:
  index = int(folder.split('-')[0])
  name = "-".join(folder.split('-')[1:])
  if index < start:
    continue
  new_index = index + increment
  os.rename(folder, f'{new_index:02}-' + name)
