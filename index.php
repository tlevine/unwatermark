<?php
$out=shell_exec("sed -i '/font color=black.This file is not intended to be viewed directly using a web browser/d' ../*.html");
echo $out;
echo 'The watermarks have been removed.';
?>
