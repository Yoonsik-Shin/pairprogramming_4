from django.shortcuts import render, redirect
from accounts.forms import CustomUserCreationForm, CustomUserChangeForm

# Create your views here.
def signup(request):
    if request.method == 'POST':
        signup_form = CustomUserCreationForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            return redirect('accounts:signup')
    signup_form = CustomUserCreationForm()
    context = {
        'signup_form': signup_form,
    }
    return render(request, 'accounts/signup.html', context)