from django.contrib.auth import login, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView

from car_collection.account.forms import CreateProfileForm
from car_collection.account.models import Profile
from car_collection.car.models import Car

CarCollectionUserModel = get_user_model()


class SignUpView(CreateView):
    template_name = 'account/profile-create.html'
    form_class = CreateProfileForm
    success_url = reverse_lazy('home page', )

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)
        return result


class UserDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'account/profile-delete.html'
    model = CarCollectionUserModel
    success_url = reverse_lazy('home page')


class UserDetailsView(LoginRequiredMixin, DetailView):
    template_name = 'account/profile-details.html'
    model = CarCollectionUserModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['total_sum'] = sum(c.price for c in Car.objects.all())

        return context


class UserEditView(LoginRequiredMixin, UpdateView):
    template_name = 'account/profile-edit.html'
    model = Profile
    fields = ('first_name', 'last_name', 'age', 'gender', 'profile_image')

    def get_success_url(self):
        return reverse_lazy('details profile', kwargs={
            'pk': self.request.user.pk,
        })
