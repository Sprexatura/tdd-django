from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest

from django.template.loader import render_to_string

from lists.views import home_page

import re

class HomePageTest(TestCase):
    @staticmethod
    def remove_csfr(html_code):
        csrf_regex = r'<input[^>]+csrfmiddlewaretoken[^>]+>'
        return re.sub(csrf_regex, '', html_code)

    def assertEqualExceptCSFR(self, html_code1, html_code2):
        return self.assertEqual(
            self.remove_csfr(html_code1),
            self.remove_csfr(html_code2)
        )

    def test_root_url_resolves_to_home_page_view(self):
        resolved = resolve('/')
        self.assertEqual(resolved.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string(
            'home.html',
        )
        self.assertEqualExceptCSFR(response.content.decode(), expected_html)

    def test_home_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new list item'

        response = home_page(request)

        self.assertIn('A new list item', response.content.decode())
        expected_html = render_to_string(
            'home.html',
            {'new_item_text': 'A new list item'}
        )
        self.assertEqualExceptCSFR(response.content.decode(), expected_html)
