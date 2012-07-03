#!/usr/bin/env python
import os

dir='/home/public'

print '<p>Watermarks have been removed from these files:</p><ul>'
for filename in os.listdir(dir)[:4]:
  # Check that it's an HTML file
  if filename.split('.')[-1] != 'html':
    continue

  old = open(os.path.join(dir, filename), 'r')
  oldcontents = old.read()
  old.close()
  lines = oldcontents.split('\n')

  if len(lines) < 3 or not 'This file is not intended to be viewed directly using a web browser.' in lines[-3]:
    continue

# Remove third-to-last line
  newcontents = '\n'.join(lines[:-3] + lines[-2:])
  new = open(os.path.join(dir, filename), 'w')
#  new.write(newcontents)
  new.close()
  print '<li>%s</li>' % filename
print '</ul>'