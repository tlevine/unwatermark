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

def add_piwik(html):
    pass

if __name__ == '__main__':
    html = lxml.html.fromstring(open('fixtures/has_watermark.html').read())
    a, b = remove_watermark(html)
    import pdb; pdb.set_trace()
