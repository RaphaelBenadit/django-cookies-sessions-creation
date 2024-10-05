from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserForm

def user_session_view(request):
    if request.method == 'POST':  # If the form is submitted
        form = UserForm(request.POST)
        if form.is_valid():  # If the form is valid
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']

            # Store the data in session
            request.session['username'] = username
            request.session['email'] = email

            # Return a response displaying the username and a confirmation message
            return HttpResponse(f"Session created! Username: {username}")
    else:
        form = UserForm()  # If it's a GET request, display a blank form

    return render(request, 'myapp/user_form.html', {'form': form})
