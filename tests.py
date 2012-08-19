#!/usr/bin/env python
import os
import nose.tools as n
import lxml.html
from erase import remove_excludes, remove_watermark, add_piwik

def assert_xml_equal(got, want):
    got = lxml.html.tostring(got)
    want = lxml.html.tostring(want)
    checker = LXMLOutputChecker()
    if not checker.check_output(want, got, 0):
        message = checker.output_difference(Example("", want), got, 0)
        raise AssertionError(message)

def _load_fixture(page_name, fixture_name):
    f = open(os.path.join('fixtures', page_name, fixture_name + '.html'))
    html = lxml.html.fromstring(f.read())
    f.close()
    return html

html_orig = _load_fixture('has_watermark')

class TestRemoveWatermark:
    def test_start_with_watermark(self):
        'remove_watermark should remove the watermark'
        removed, html_observed = remove_watermark(html_orig)
        html_expected =_load_fixture('no_watermark')
        n.assert_true(removed)
        assert_xml_equal(html_observed, html_expected)

    def test_start_without_watermark(self):
        'remove_watermark should do nothing if the watermark isn\'t there.'
        html_expected =_load_fixture('no_watermark')
        removed, html_observed = remove_watermark(html_expected)
        n.assert_false(removed)
        assert_xml_equal(html_observed, html_expected)

class TestPiwik:
    def test_start_with_piwik(self):
        'add_piwik should do nothing if the piwik stuff is already there.'
        html_no_watermark_yes_piwik =_load_fixture('no_watermark_yes_piwik')
        added, html_observed = add_piwik(html_no_watermark_yes_piwik)
        html_expected =_load_fixture('no_watermark_yes_piwik')
        n.assert_false(added)
        assert_xml_equal(html_observed, html_expected)

    def test_start_without_piwik(self):
        'add_piwik should add the piwik stuff.'
        html_no_watermark =_load_fixture('no_watermark')
        added, html_observed = add_piwik(html_no_watermark)
        html_expected =_load_fixture('no_watermark_yes_piwik')
        n.assert_true(added)
        n.assert_in(
            'http://piwik.thomaslevine.com/piwik.php?idsite=8',
            lxml.html.tostring( html_observed)
        )


