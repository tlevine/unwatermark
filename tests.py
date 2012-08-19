#!/usr/bin/env python
import os
import nose.tools as n
from lxml.html import fromstring
from erase import remove_excludes, remove_watermark, add_piwik

def _load_fixture(name):
    f = open(os.path.join('fixtures', name + '.html'))
    html = fromstring(f.read())
    f.close()
    return html

html_orig = _load_fixture('has_watermark')

def test_no_excludes():
    'remove_excludes should remove all excludes'
    html_observed = remove_excludes(html_orig)
    html_expected =_load_fixture('no_excludes')
    n.assert_equal(html_observed, html_expected)

def test_no_watermark():
    'remove_watermark should remove the watermark'
    html_observed = remove_watermark(html_orig)
    html_expected =_load_fixture('no_watermark')
    n.assert_equal(html_observed, html_expected)

def test_piwik():
    'add_piwik should add the piwik stuff.'
    html_no_watermark =_load_fixture('no_watermark')
    html_observed = add_piwik(html_no_watermark)
    html_expected =_load_fixture('piwik')
    n.assert_equal(html_observed, html_expected)


