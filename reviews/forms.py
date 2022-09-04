from django import forms
from  .models  import Review

# class ReviewForm(forms.Form):
#     user_name = forms.CharField(label='your name', max_length=30, error_messages={
# "required": "please enter a username",
# "max_length": "your name seems too long"
#     })
#     review_text = forms.CharField(label='your feedback', widget=forms.Textarea, max_length=50)
#     rating = forms.IntegerField(label='rating', min_value=1, max_value=5)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        # exclude = ['user_name']
        labels = {
            'user_name' :'your name',
            'review_text' : 'your review',
            'rating' : 'rating'
        }
        error_messages = {
            'user_name':{
                "required": "please enter a username",
"max_length": "your name seems too long"
            },
            'review_text':{
                "required": "please enter a review",
"max_length": "your review seems too long"
            }
        }
