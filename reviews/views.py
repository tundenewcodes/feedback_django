from decimal import Clamped
from pipes import Template
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from .models import Review
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView



# Create your views here.
# def reviews(request):
#     if request.method == 'POST':
#         existing_data = Review.objects.get(pk=1)
#         form = ReviewForm(request.POST, instance=existing_data)
#         if form.is_valid():
#             form.save()
#             # review = Review(user_name=form.cleaned_data['user_name'], review_text=form.cleaned_data['review_text'], rating=form.cleaned_data['rating'])
#             # review.save()  call  form.save() directly if you are using modelForm

#             return HttpResponseRedirect('/thanks')
#     else:
#         form = ReviewForm()  #recreeate form
#     return render (request, 'reviews/index.html',{'form':form})



# def thank_you(request):
#     return render(request, 'reviews/thank-you.html')

# class based views

# class ReviewView(View):
#     def get(self, request):
#         form = ReviewForm()  #recreeate form
#         return render (request, 'reviews/index.html',{'form':form})

#     def post(self, request):
#         form = ReviewForm(request.POST)  #recreeate form
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/thanks')
#         return render (request, 'reviews/index.html',{'form':form})

# form view - no need of writing get and post method
# class ReviewView(FormView):
#     form_class = ReviewForm
#     template_name  = 'reviews/index.html'
#     success_url = '/thanks'

#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)

# createview - no need of writing get and post method also can work without forms.py and no need of saving

class ReviewView(CreateView):
    model = Review
    form_class  = ReviewForm  # using this because of the configuration
    success_url = '/thanks'
    template_name  = 'reviews/index.html'





# class ThankYou(View):
#     def get(self, request):
#         return render(request, 'reviews/thank-you.html')

#template view - for redirect
class ThankYou(TemplateView):
    template_name = 'reviews/thank-you.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'it works'
        return context

class ListThankYou(ListView):
    template_name = 'reviews/thank-you.html'
    model = Review



#
# class Review_Lists(TemplateView):
#     template_name =  'reviews/review_lists.html'
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         reviews = Review.objects.all()
#         context['reviews'] = reviews
#         return context

#list view - to get all data
class Review_Lists(ListView):
    template_name =  'reviews/review_lists.html'
    model = Review
    context_object_name  = 'reviews'
#to narrow down querry
    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query.filter(rating__gt=7)
        return data


# class single_review(TemplateView):
#     template_name= 'reviews/single-review.html'
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         review_id = kwargs['id']
#         selected_review = Review.objects.get(pk=review_id)
#         context['review'] = selected_review
#         return context


# detail view to return an item

class single_review(DetailView):
    template_name= 'reviews/single-review.html'
    model= Review


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_review = self.object  # the current review being displayed
        request = self.request # the current request of the loaded review
        favorite_id = request.session.get('favorite_review') #returns a string
        context['fav_review'] = favorite_id == str(loaded_review.id) #add fav_id to context data
        return context

    # just make sure the value you are returning is  pk - int:pk




class Favorite(View):
    def post(self, request):
        review_id = request.POST['review_id']
        #fav_review = Review.objects.get(pk=review_id)
        request.session['favorite_review'] = review_id
        return HttpResponseRedirect(f'/reviews/{review_id}')