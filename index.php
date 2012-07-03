<?php
shell_exec("
  d=$(mktemp -d)
  for file in /home/public/index.html
    do
    cat "$file" | tail -r | sed 3d | tail -r > "$d/$file"
    cat "$d/$file" > "$file"
  done
  rm -R "$d"
);
echo 'The watermarks have been removed.';
?>
