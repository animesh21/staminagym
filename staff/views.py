from django.views.generic import TemplateView, FormView
from django.urls import reverse
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import StaffLoginForm, ContactUsForm


class StaffLoginView(LoginView):
    authentication_form = StaffLoginForm
    template_name = 'staff/index.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse('profile')


class StaffLogoutView(LogoutView):
    def get_next_page(self):
        return reverse('home')


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'staff/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logged_in'] = True
        return context


class AboutView(TemplateView):
    template_name = 'staff/about.html'

    http_method_names = ['get', ]


class GalleryView(TemplateView):
    template_name = 'staff/gallery.html'

    http_method_names = ['get', ]


class MeetTheTeamView(TemplateView):
    template_name = 'staff/interview.html'

    http_method_names = ['get', ]


class ContactUsView(FormView):
    form_class = ContactUsForm
    template_name = 'staff/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['footer_remove'] = True
        return context


class AdminLoginView(LoginView):
    pass


class PageNotFoundView(TemplateView):
    template_name = 'staff/404.html'
