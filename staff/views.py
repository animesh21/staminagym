from django.views.generic import TemplateView, FormView
from django.urls import reverse
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import Group
from django.shortcuts import redirect
from django.contrib import messages
from .forms import LoginForm, ContactUsForm, AddStaffForm


class StaffLoginView(LoginView):
    authentication_form = LoginForm
    template_name = 'staff/index.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse('profile')


class StaffLogoutView(LogoutView):
    def get_next_page(self):
        return reverse('home')


class ProfileView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'staff/profile.html'

    raise_exception = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logged_in'] = True
        return context

    def test_func(self):
        return self.request.user.groups.filter(name='staff').exists()


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
    authentication_form = LoginForm
    template_name = 'staff/staff_login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse('admin_view')


class AdminAddStaffView(LoginRequiredMixin, UserPassesTestMixin, FormView):
    template_name = 'staff/add_staff.html'
    form_class = AddStaffForm
    raise_exception = True

    def test_func(self):
        return self.request.user.groups.filter(name='admin').exists()

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            group = Group.objects.get(name='staff')
            user = form.save()
            user.groups.add(group)
            user.save()
            messages.add_message(request, messages.SUCCESS, "User was added successfully, pk: {}".format(user.id))
            return redirect(self.get_success_url())
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('admin_view')


class PageNotFoundView(TemplateView):
    template_name = 'staff/404.html'
