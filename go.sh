#!/bin/sh

for file in /srv/www.fadelee.com/*.html
  do
  cat "$file" | /srv/www.fadelee.com/unwatermark/tail-r.py | sed "3c\ $(cat /srv/www.fadelee.com/unwatermark/piwik.html)" | /srv/www.fadelee.com/unwatermark/tail-r.py > "$file".tmp
  cat "$file".tmp > "$file"
  rm "$file".tmp
done
