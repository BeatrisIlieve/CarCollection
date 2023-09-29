from django.urls import path, include

from car_collection.account.views import SignUpView, UserDeleteView, UserDetailsView, UserEditView

urlpatterns = (
    path('create/', SignUpView.as_view(), name='create profile'),
    path('<int:pk>/', include(
        [
            path('delete/', UserDeleteView.as_view(), name='delete profile'),
            path('details/', UserDetailsView.as_view(), name='details profile'),
            path('edit/', UserEditView.as_view(), name='edit profile')
        ]
    ))

)
