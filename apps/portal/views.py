from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'portal/home.html'


class AboutPageView(TemplateView):
    template_name = 'portal/about.html'
