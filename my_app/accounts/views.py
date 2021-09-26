from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, RedirectView, UpdateView, View

from accounts.forms import SignUpForm
from accounts.models import User

# Create your views here.


class MyProfileView(LoginRequiredMixin, UpdateView):
    queryset = User.objects.all()
    fields = ('first_name', 'last_name', 'avatar')
    success_url = reverse_lazy('index')
    template_name = 'my_profile.html'

    # def get_queryset(self):
    #    queryset = super().get_queryset()
    #    queryset = queryset.filter(id=self.request.user.id)
    #    return queryset

    def get_object(self, quetyset=None):
        return self.request.user


class SignUpView(CreateView):
    model = User
    template_name = 'sign_up.html'
    success_url = reverse_lazy('index')
    form_class = SignUpForm

    def form_valid(self, form):
        messages.info(self.request, 'Thank for sign up! Please, check your email.')
        return super().form_valid(form)


class ActivateUserView(RedirectView):
    pattern_name = 'index'

    def get_redirect_url(self, *args, **kwargs):
        username = kwargs.pop('username')
        user = get_object_or_404(User, username=username, is_active=False)
        # breakpoint()

        user.is_active = True
        user.save(update_fields=('is_active', ))
        messages.info(self.request, 'Account is activated.')

        return super().get_redirect_url(*args, **kwargs)
