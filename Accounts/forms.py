from django import forms


class LoginForm(forms.Form):
    class Meta:
        
        fields = ('username', 'password')
   
        widget = {
            'username': forms.TextInput(attrs={'class': 'mb-4 p-2 appearance-none block w-full bg-gray-200 placeholder-gray-900 rounded border focus:border-teal-500'}),
            'password': forms.PasswordInput(attrs={'class': 'mb-4 p-2 appearance-none block w-full bg-gray-200 placeholder-gray-900 rounded border focus:border-teal-500'})
        }