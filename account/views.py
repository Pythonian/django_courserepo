from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render
from django.views.generic import CreateView
from repository.models import Material

from .forms import ProfileForm, SignUpForm, UserForm


class SignUpView(SuccessMessageMixin, CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    success_message = "Your account was created successfully"

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('profile')


def profile(request):
    # materials = Material.objects.filter(favorite=request.user)
    # favorite = bool
    # if Material.objects.filter(favorite=request.user).exists():
    #     favorite = True
    template = 'profile.html'
    context = {
        #'materials': materials, 'favorite': favorite
    }

    return render(request, template, context)


def settings(request):
    if request.method == 'POST':
        user_form = UserForm(
            request.POST, instance=request.user)
        profile_form = ProfileForm(
            request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your account was successully updated.')
            return redirect('profile')
        else:
            messages.warning(
                request, 'There was an error while updating your account.')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

    template = 'settings.html'
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }

    return render(request, template, context)
