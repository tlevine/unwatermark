import os
import lxml.html

# Single xpath helper
def xpath0(htmlelement, xpath):
    results = htmlelement.xpath(xpath)
    if len(results) == 0:
        return None
    elif len(results) == 1:
        return results[0]
    else:
        raise ValueError('The xpath matched more than one node')
lxml.html.HtmlElement.xpath0 = xpath0
del(xpath0)

PIWIK = lxml.html.fromstring('''<!-- Piwik -->
<script type="text/javascript">
var pkBaseURL = (("https:" == document.location.protocol) ? "https://piwik.thomaslevine.com/" : "http://piwik.thomaslevine.com/");
document.write(unescape("%3Cscript src='" + pkBaseURL + "piwik.js' type='text/javascript'%3E%3C/script%3E"));
</script><script type="text/javascript">
try {
var piwikTracker = Piwik.getTracker(pkBaseURL + "piwik.php", 8);
piwikTracker.trackPageView();
piwikTracker.enableLinkTracking();
} catch( err ) {}
</script><noscript><p><img src="http://piwik.thomaslevine.com/piwik.php?idsite=8" style="border:0" alt="" /></p></noscript>
<!-- End Piwik Tracking Code -->
''')
def add_piwik(html):
    "Add Piwik if it isn't already there."
    if html.xpath0('//img[@src="http://piwik.thomaslevine.com/piwik.php?idsite=8"]') == None:
        body = html.xpath0('//body')
        body.append(PIWIK)
        added = True
    else:
        # Already added
        added = False

    return added, html

def remove_watermark(html):
    watermark = html.xpath0(
      '//div[@style="position:absolute;left:50;top:50;background:white"]'
      '[font[@color="black"]]'
    )
    if watermark is not None:
        watermark.getparent().remove(watermark)
        removed = True
    else:
        removed = False

    return removed, html

def edit_files():
    removed_watermark = []
    added_piwik = []
    for filename in os.listdir(SITE_ROOT):
        if filename[-5:] != '.html':
            continue

        absolute_path = os.path.join(SITE_ROOT, filename)
        f = open(absolute_path, 'r')
        html = lxml.html.fromstring(f.read())
        f.close()

        removed_watermark_from_file, html = remove_watermark(html)
        added_piwik_to_file, html = add_piwik(html)

        if removed_watermark_from_file:
            removed_watermark.append(filename)

        if added_piwik_to_file:
            added_piwik.append(filename)

        f = open(absolute_path, 'w')
        f.write(lxml.html.tostring(html))
        f.close()

    print 'Removed the watermark from these files:'
    print '\n  '.join(removed_watermark)

    print 'Added the piwik analytics snippet to these files:'
    print '\n  '.join(added_piwik)

def cgi_script():
    print 'HTTP/1.1 200 OK'
    print 'Content-Type: text/plain'
    print '\n'
    main()

def main():
    os.system('cd /srv/www.fadelee.com && git init')
    os.system('cd /srv/www.fadelee.com && git commit . -m new\ upload')
    edit_files()
    os.system('cd /srv/www.fadelee.com && git commit . -m removed\ watermark')

# The only bit of configuration: Set this to the site's directory.
SITE_ROOT = os.path.join('/', 'srv', 'www.fadelee.com')
if __name__ == '__main__':
    main()
