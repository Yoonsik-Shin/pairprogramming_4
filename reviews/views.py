from django.shortcuts import render
from .models import Review
from .forms import ReviewForm

# Create your views here.
def create(request):
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review_form.save()
    else:
        review_form = ReviewForm()
    context = {
        'review_form': review_form,
    }
    return render(request, 'reviews/form.html', context)