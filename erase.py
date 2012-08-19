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

def remove_excludes(html):
    pass

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

if __name__ == '__main__':
    html = lxml.html.fromstring(open('fixtures/has_watermark.html').read())
    a, b = remove_watermark(html)
    import pdb; pdb.set_trace()
