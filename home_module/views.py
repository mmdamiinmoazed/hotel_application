from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpRequest as Request
# Create your views here.
class HomeView(TemplateView):
    template_name = "home_module/home.html"

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
class AboutView(TemplateView):
    template_name = "home_module/about.html"

def home_footer(request:Request):
    return render(request,template_name="home_module/includes/home_footer.html" , context={})

def home_header(request:Request):
    return render(request,template_name="home_module/includes/home_header.html" , context={})