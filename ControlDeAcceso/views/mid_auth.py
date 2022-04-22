from django.shortcuts import redirect
from django.urls import reverse
from django.views import View


class AuthAbsView(View):
    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return super(AuthAbsView, self).dispatch(*args, **kwargs)
        else:
            return redirect(reverse('iniciar-sesion'))