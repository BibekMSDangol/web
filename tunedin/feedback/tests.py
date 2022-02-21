from ast import arg
from django.urls import reverse, resolve
from django.test import Client, SimpleTestCase, TestCase
from feedback.views import feedbackview, feedbackadd, feedbackdelete

class TestUrls(SimpleTestCase):
    def test_case_feedbackview_url(self):
        url=reverse('feedbackview')
        self.assertEquals(resolve(url).func, feedbackview)

    def test_case_feedbackadd_url(self):
        url=reverse('feedbackadd')
        self.assertEquals(resolve(url).func, feedbackadd)

    def test_case_feedbackdelete_url(self):
        url=reverse('feedbackdelete', args=[1])
        self.assertEquals(resolve(url).func, feedbackdelete)

