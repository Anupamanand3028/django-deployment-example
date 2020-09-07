from django import forms
from django.core import validators
from AppTwo.models import ExUser
from django.contrib.auth.models import User
from AppTwo.models import UserProfileInfo

# creating our own custom Validation
# def check_for_z(value):
#     if value[0].lower() != 'z':
#         raise forms.ValidationError("Need to start with Z")

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Please verify your email')
    text = forms.CharField(widget=forms.Textarea)
    # botcatcher = forms.CharField(required=False, widget=forms.HiddenInput,
    #                               validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean_data = super().clean()

        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("There is a mismatch in email field! please correct it.")

class UserForm(forms.ModelForm):
        password = forms.CharField(widget=forms.PasswordInput())

        class Meta:
            model = User
            fields = ('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
        class Meta:
            model = UserProfileInfo
            fields =('portfolio_site','profile_pic')

# instead we are using django builtin validator
    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0:
    #         raise form.ValidationError("Gotcha Bot!")
    #     return botcatcher
class NewUserForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = ExUser
        fields = '__all__'
