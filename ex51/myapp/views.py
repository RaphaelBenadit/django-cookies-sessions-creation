# myapp/views.py
from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm

def set_cookie_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']

            # Create the HTTP response and set the cookies
            response = HttpResponse(f"Cookie set! Username: {username}, Email: {email}")
            response.set_cookie('username', username, max_age=3600)  # Cookie expires in 1 hour
            response.set_cookie('email', email, max_age=3600)

            return response
    else:
        form = UserForm()

    return render(request, 'myapp/user_form.html', {'form': form})

def get_cookie_view(request):
    # Retrieve cookies
    username = request.COOKIES.get('username', 'No username cookie set')
    email = request.COOKIES.get('email', 'No email cookie set')

    return HttpResponse(f"Username: {username}, Email: {email}")
