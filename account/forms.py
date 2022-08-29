from .models import CustomUser

from django.contrib.auth.forms import UserChangeForm, UserCreationForm

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model=CustomUser
        # fields=UserChangeForm.Meta.fields
        fields = ["username", "email", "age"]


class CustomUserCreateForm(UserCreationForm):
    class Meta:
        model=CustomUser
        # fields=UserCreationForm.Meta.fields + ("age", )
        fields = ["username", "email", "age"]
