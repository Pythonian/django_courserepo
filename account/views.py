from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from repository.models import Material

from .forms import SignupForm, UserForm
from .tokens import account_activation_token


def signup(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)

            if request.is_secure():
                protocol = 'https'
            else:
                protocol = 'http'

            subject = render_to_string(
                'registration/account_activation_subject.txt',
                {'site_name': current_site.name}
            )

            message = render_to_string(
                'registration/account_activation_email.html',
                {'user': user,
                 'domain': current_site.domain,
                 'protocol': protocol,
                 'site_name': current_site.name,
                 'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                 'token': account_activation_token.make_token(user), }
            )
            user.email_user(subject, message)
            return redirect('account:account_activation_sent')
        else:
            messages.error(
                request, "An error occured while trying to create your account.")
            return render(request,
                          'registration/signup.html',
                          {'form': form})
    else:
        form = SignupForm()

    template = 'registration/signup.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def account_activation_sent(request):
    if request.user.is_authenticated:
        return redirect('home')

    template = 'registration/account_activation_sent.html'
    context = {}

    return render(request, template, context)


def activate(request, uidb64, token):
    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_verified = True
        user.save()
        messages.success(request, 'Your profile has been successully created.')
        return redirect('account:login')
    else:
        return render(
            request,
            'registration/activate.html',
            {})


def profile(request):
    materials = Material.objects.filter(user_library=request.user)
    template = 'profile.html'
    context = {
        'materials': materials,
    }

    return render(request, template, context)


def settings(request):
    if request.method == 'POST':
        user_form = UserForm(
            request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Your account was successully updated.')
            return redirect('account:profile')
        else:
            messages.warning(
                request, 'There was an error while updating your account.')
    else:
        user_form = UserForm(instance=request.user)

    template = 'settings.html'
    context = {
        'user_form': user_form,
    }

    return render(request, template, context)


class CustomPasswordChangeView(PasswordChangeView):
    success_url = reverse_lazy('account:profile')

    def form_valid(self, form):
        messages.success(self.request, 'Your password was successfully changed.')
        return super().form_valid(form)
