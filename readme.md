Unwatermark
======
**erase.py** is a removes Yahoo SiteBuilder's watermarks
from [Fade Lee's website](http://www.fadelee.com).

Specify the SITE_ROOT in erase.py as the place where you
have the website. Then run erase.py to remove watermarks.
While it's at it, it adds Piwik tracking (you'll need to
change the snippet for different sites) and commits to a
git repository.

It runs every two minutes, but not when sftp is running.
But I do forsee problems if it happens to run when sftp
is running. But those should be fixed by uploading the
site again.
