from django.urls import path

from .views import ContactPageView, HomePageView, job_detail_view

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('job/<int:pk>', job_detail_view, name='job-detail'),
]