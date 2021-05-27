from django.shortcuts import get_object_or_404, render

from apps.portal.models import JobOffer
from django.views.generic import ListView, TemplateView


class ContactPageView(TemplateView):
    template_name = 'portal/contact.html'


class HomePageView(ListView):
    model = JobOffer
    template_name = 'portal/home.html'


def job_detail_view(request, pk):
    job = get_object_or_404(JobOffer, pk=pk)
    return render(request, 'portal/job_detail.html', context={'job': job})
