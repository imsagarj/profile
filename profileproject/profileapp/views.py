from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from .models import Profile

class ProfileClassView(TemplateView):
    template_name = 'profiles.html'
    def get_context_data(self, *args ,**kwargs):
        # context = super().get_context_data(**kwargs)
        profiles = Profile.objects.all()
        context = {'profiles':profiles}
        return context

def home(request):
    """ To retrieve all profiles """
    try:
        # profiles = Profile.objects.all()
        return render(request, 'profiles.html',{'profiles': Profile.objects.all()})
    except Exception as e:
        print(e)
        return render(request, 'profiles.html', {'msg': "Something Went Wrong."})

def profile(request):
    """ To Create new profile """
    try:
        if request.method == 'GET':
            return render(request, 'profile.html')
        elif request.method == 'POST':
            try:
                import json
                profile = Profile()
                profile.first_name = request.POST.get('first_name')
                profile.last_name = request.POST.get('last_name', 'Test')
                profile.city = request.POST.get('city')
                profile.state = request.POST.get('state')
                profile.save()
                return redirect('home')
            except Exception as ex:
                print(ex)
                return render(request, 'profile.html', {"msg":"Something Went Wrong When Create Profile."})
        else:
            return render(request, 'profile.html', {"msg":"Method not found."})
    except Exception as ex:
        print(ex)
        return render(request, 'profile.html', {"msg": "Something Went Wrong."})

def edit_profile(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    if request.method == 'POST':
        profile.first_name = request.POST['first_name']
        profile.last_name = request.POST['last_name']
        profile.city = request.POST['city']
        profile.state = request.POST['state']
        profile.save()
        return redirect('home')
    return render(request, 'profile.html', {'profile': profile})

def delete_profile(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    profile.delete()
    return redirect('home')






