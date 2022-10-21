from django.shortcuts import redirect, render, get_object_or_404
from .models import Review
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def create(request):
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('reviews:index')
    else:
        review_form = ReviewForm()
    context = {
        'review_form': review_form,
    }
    return render(request, 'reviews/form.html', context)

def index(request):
    reviews = Review.objects.all()
    context = {
        'reviews': reviews,
    }
    return render(request, 'reviews/index.html', context)

def detail(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    context = {
        'review': review,
    }
    return render(request, 'reviews/detail.html', context)

@login_required
def update(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'POST':
        review_form = ReviewForm(request.POST, instance=review)
        if review_form.is_valid():
            review_form.save()
            return redirect('reviews:detail', review_pk)
    else:
        review_form = ReviewForm(instance=review)
    context = {
        'review_form': review_form,
        'review': review,
    }
    return render(request, 'reviews/form.html', context)