from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# class SuperUserRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
#
#     def test_func(self):
#         if self.request.user.is_superuser:
#             return self.request.user.is_client
#         else:
#             return self.request.user.is_superuser


class Index(LoginRequiredMixin, TemplateView):
    login_url = '/accounts/login/'
    redirect_field_name = 'home'
    template_name = 'dmca/dashboard_client.html'
