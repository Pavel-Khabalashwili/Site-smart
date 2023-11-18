from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = 'home'),
    path('course', views.course, name = 'course'),
    path('about', views.about, name = 'about'),
    path('contacts', views.contatcs, name = 'contacts'),
    path('course/<int:pk>', views.CourseDetailView.as_view(), name = 'course-detail')
]

