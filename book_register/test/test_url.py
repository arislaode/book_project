
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from book_register.views import book_list, book_form, book_delete, review_form, review_list

class TestUrls(SimpleTestCase):

    def test_list_url_book_list(self):
        url = reverse('book_list')
        self.assertEquals(resolve(url).func, book_list)

    def test_list_url_book_form(self):
        url = reverse('book_insert')
        self.assertEquals(resolve(url).func, book_form)

    def test_list_url_book_list(self):
        url = reverse('book_list')
        self.assertEquals(resolve(url).func, book_list)

    def test_list_url_review_form(self):
        url = reverse('review')
        self.assertEquals(resolve(url).func, review_form)

    def test_list_url_review_list(self):
        url = reverse('review_list')
        self.assertEquals(resolve(url).func, review_list)
