from django.shortcuts import render

from ControlDeAcceso.views.mid_auth import AuthAbsView


class IndexView(AuthAbsView):
    def get(self, request):
        return render(request, 'Index/index.html')
