from django.contrib.auth import get_user_model
from django import forms

class RegisterForm(forms.ModelForm):
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password',
    widget = forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields =['username', 'first_name', 'last_name','email']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Password dosen't bot natch.")
        return cd['password2']
