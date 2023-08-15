from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, WebPage, AccessRecord
from . import forms
# Create your views here.

def index(request):
    registered = False
    if request.method == 'POST':
        user_form = forms.UserForm(data=request.POST)
        profile_form = forms.UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
        return render(request, 'first_app/index.html', context={'registered': registered,
                                                    'profile_form': profile_form,
                                                    'user_form': user_form})
    else:
        user_form = forms.UserForm()
        profile_form = forms.UserProfileInfoForm()
        return render(request, 'first_app/index.html', context={'registered': registered,
                                                                'profile_form': profile_form,
                                                                'user_form': user_form})

def form_view(request):
    form = forms.FormName()
    if request.method == 'POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            print(form.cleaned_data['email'])
            print(form.cleaned_data['text'])

   
    return render(request, 'first_app/form_page.html', {'form': form} )