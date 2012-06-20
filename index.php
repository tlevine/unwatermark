<?php
echo 'hi';
$out=shell_exec("cd ..; sed -i '/font color=black.This file is not intended to be viewed directly using a web browser/d' ../*.html");
echo $out;
?>
