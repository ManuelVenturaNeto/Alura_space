from django import forms # type: ignore

class LoginForms(forms.Form):
    nome_login=forms.CharField(
        label="Nome de login",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
            'class': 'form-control',
            'placeholder': 'Ex.: Manuel Ventura',
            } 
        ),
    )
    senha=forms.CharField(
        label="Senha",
        required=True,
        max_length=50,
        widget=forms.PasswordInput(
            attrs={
            'class': 'form-control',
            'placeholder': 'Digite sua senha',
            }
        ),   
    )
    
class CadastroForms(forms.Form):
    nome_login=forms.CharField(
        label="Nome de cadastro",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
            'class': 'form-control',
            'placeholder': 'Ex.: Manuel Ventura',
            } 
        ),
    )
    email=forms.EmailField(
        label="Email de cadastro",
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
            'class': 'form-control',
            'placeholder': 'Ex.: manuel.ventura@gmail.com',
            } 
        ),
    )
    senha_1=forms.CharField(
        label="Senha",
        required=True,
        max_length=50,
        widget=forms.PasswordInput(
            attrs={
            'class': 'form-control',
            'placeholder': 'Digite sua senha',
            }
        ),   
    )
    senha_2=forms.CharField(
        label="Confirme sua senha",
        required=True,
        max_length=50,
        widget=forms.PasswordInput(
            attrs={
            'class': 'form-control',
            'placeholder': 'Digite sua senha novamente',
            }
        ),   
    )