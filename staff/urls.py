from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.StaffLoginView.as_view(), name='home'),
    url(r'^profile/?$', views.ProfileView.as_view(), name='profile'),
    url(r'^logout/?$', views.StaffLogoutView.as_view(), name='logout'),
    url(r'^about/?$', views.AboutView.as_view(), name='about'),
    url(r'^gallery/?$', views.GalleryView.as_view(), name='gallery'),
    url(r'^meettheteam/?$', views.MeetTheTeamView.as_view(),  name='meettheteam'),
    url(r'^contact/?$', views.ContactUsView.as_view(), name='contact_us'),
    # wildcard url pattern for page not found
    url(r'^.*$', views.PageNotFoundView.as_view(), name='not_found')
]
