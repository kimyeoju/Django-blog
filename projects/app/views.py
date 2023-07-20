from django.shortcuts import render
from django.views import View

class IndexMain(View):
    def get(self, request):
        context = {
            'title': '"My Blog"'
        }
        return render(request, 'index.html', context)