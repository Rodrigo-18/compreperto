from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Loja, Usuario


class BarraPesquisa(forms.Form):
    name = forms.CharField(label='', max_length= 20,widget=forms.TextInput(attrs={'placeholder': 'Qual produto você deseja?'}))

class NovoUsuarioForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'email']
		labels = {
			'first_name': 'Nome',
			'last_name': 'Sobrenome',
			'email': 'Email',
		}
	
	CHOICES = (('Cliente', 'Fazer minhas compras online'),('Lojista', 'Administrar minha loja online'))
	objetivo = forms.CharField(widget=forms.Select(choices=CHOICES))
	nome_da_loja = forms.CharField(max_length=20, required= False)
	
	def save(self, commit = True):
		user = super(NovoUsuarioForm, self).save(commit=False)
		user.username = self.cleaned_data['email']
		user.email = self.cleaned_data['email']
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']	
		

		if commit:
			user.save()
			usuario = Usuario.objects.create(user = user, tipo_user = self.cleaned_data['objetivo'])
			if self.cleaned_data['objetivo'] == 'Lojista':
				loja = Loja.objects.create(nome =self.cleaned_data['nome_da_loja'], lojista = usuario,
			avaliacao = 0, status = 'Aberto')
		return usuario

