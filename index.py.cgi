import os

dir='/home/public'
for file in os.listdir(dir):
  old = open(os.path.join(dir, filename), 'r')
  oldcontents = old.read()
  old.close()
  lines = contents.split('\n')

# Remove third-to-last line
  newcontents = '\n'.join(lines[:-3] + lines[-2:])
  new = open(os.path.join(dir, filename), 'w')
#  new.write(newcontents)
  new.close()
