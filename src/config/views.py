from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'account/profile.html'


def index(request):
    return redirect('account_login')
