from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import UserProfile


class UserProfileCreationForm(UserCreationForm):
    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'username', 'email', 'phone_number')


class UserProfileChangeForm(UserChangeForm):
    class Meta:
        model = UserProfile
        fields = ('email', )
