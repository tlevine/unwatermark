<?php
shell_exec('
  for file in /srv/www.fadelee.com/*.html
    do
    cat "$file" | /srv/www.fadelee.com/unwatermark/tail-r.py | sed \'3c\
<!-- Piwik -->\
<script type="text/javascript">\
var pkBaseURL = (("https:" == document.location.protocol) ? "https://piwik.thomaslevine.com/" : "http://piwik.thomaslevine.com/");\
document.write(unescape("%3Cscript src=\"" + pkBaseURL + "piwik.js\" type=\"text/javascript\"%3E%3C/script%3E"));\
</script><script type="text/javascript">\
try {\
var piwikTracker = Piwik.getTracker(pkBaseURL + "piwik.php", 8);\
piwikTracker.trackPageView();\
piwikTracker.enableLinkTracking();\
} catch( err ) {}\
</script><noscript><p><img src="http://piwik.thomaslevine.com/piwik.php?idsite=8" style="border:0" alt="" /></p></noscript>\
<!-- End Piwik Tracking Code -->\
\' | tail -r > "$file".tmp
    cat "$file".tmp > "$file"
    rm "$file".tmp
  done
');
echo 'The watermarks have been removed.';
?>
