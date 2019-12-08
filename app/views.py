"""
Definition of views.
"""

from datetime import datetime

from django.shortcuts import render
from django.http import HttpRequest
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect


from app.forms import BootstrapUserCreationForm, BootstrapAuthenticationForm


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return redirect('/')


def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'contact.html',
        {
            'title': 'Contact',
            'message': '''For web site technical issues, contact macke@yar.nu\n\n
                For issues w.r.t. the club, events and tasks, contat info@team13.se.''',
            'year': datetime.now().year,
        }
    )


def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'about.html',
        {
            'title': 'About',
            'message': 'Webb app that helps Team 13 manage club activites and tasks that members can take upon themselves.',
            'year': datetime.now().year,
        }
    )


def signup(request):
    if request.method == 'POST':
        form = BootstrapUserCreationForm(request.POST)
        if 'localhost' in request.get_host() and 'captcha' in form.fields:
            del form.fields['captcha']

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            
            user = authenticate(username=username, password=raw_password)

            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.email = username
            user.save()

            login(request, user)
            return redirect('/')
    else:
        form = BootstrapUserCreationForm()
        if 'localhost' in request.get_host() and 'captcha' in form.fields:
            del form.fields['captcha']

    return render(request, 'signup.html', {
        'form': form,
        'year': datetime.now().year
    })


class MyLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = BootstrapAuthenticationForm
    extra_context = {
        'title': 'Logga in',
        'year': datetime.now().year,
    }
    redirect_authenticated_user = True

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        if 'localhost' in self.request.get_host() and 'captcha' in form.fields:
            del form.fields['captcha']
        return form

    def dispatch(self, request, *args, **kwargs):
        self._request = request
        return super().dispatch(request, *args, **kwargs)
