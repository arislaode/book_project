
from django.test import TestCase
from book_register.forms import BookForm

class BookFormTest(TestCase):
    def test_book_form_date_field_name(self):
        form = BookForm()
        self.assertTrue(form.fields['name'].label == None or form.fields['name'].label == 'Full Name')

    def test_book_form_date_field_contact(self):
        form = BookForm()
        self.assertTrue(form.fields['contact'].label == None or form.fields['contact'].label == 'Mobile Phone')

    def test_book_form_date_field_book(self):
        form = BookForm()
        self.assertTrue(form.fields['book'].label == None or form.fields['book'].label == 'Book')

    def test_book_form_date_field_start_date(self):
        form = BookForm()
        self.assertTrue(form.fields['start_date'].label == None or form.fields['start_date'].label == 'Start Date Borrow(mm/dd/2020)')

    def test_book_form_date_field_end_date(self):
        form = BookForm()
        self.assertTrue(form.fields['end_date'].label == None or form.fields['end_date'].label == 'End Date Borrow(mm/dd/2020)')