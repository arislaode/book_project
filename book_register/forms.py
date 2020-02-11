from django import forms
from .models import Book, Review

class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('name', 'contact', 'book', 'start_date', 'end_date')
        labels = {
            'name': 'Full Name',
            'contact': 'Mobile Phone',
            'book': 'Book',
            'start_date': 'Start Date Borrow(mm/dd/2020)',
            'end_date': 'End Date Borrow(mm/dd/2020)'
        }
    
    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.fields['book'].empty_label = "Select Book"
        self.fields['start_date'].required = True
        self.fields['end_date'].required = True



class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['user_name', 'book', 'rating', 'comment']
        widgets = {
            'comment': forms.Textarea(attrs={'cols': 40, 'rows': 15})
        }
        labels = {
            'user_name' : 'Full Name',
            'book' : 'Choose Book',
            'rating': 'Rating',
            'comment': 'Review'
        }
    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.fields['book'].empty_label = "Select"
        # self.fields['rating'].empty_label = "Select"
