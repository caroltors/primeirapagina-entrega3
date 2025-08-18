from django import forms # Importa o módulo de formulários do Django
from .models import Certificate, VendorVPN, Application # Importa os modelos do app console

# Criação de um formulário baseado no modelo Certificate
class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = ['name', 'related_system', 'issue_date', 'expiration_date', 'status']
        labels = {
            'name': 'Nome do Certificado',
            'related_system': 'Sistema ou Aplicação',
            'issue_date': 'Data de Emissão',
            'expiration_date': 'Data de Expiração',
            'status': 'Status'
        }
        # Personalizar os widgets 
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}), # adicionar 'placeholder': 'Teste para aparecer no input'
            'related_system': forms.TextInput(attrs={'class': 'form-control'}),
            'issue_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'expiration_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-control'})
        }

# Criação de um formulário baseado no modelo VendorVPN
class VendorVPNForm(forms.ModelForm):
    class Meta:
        model = VendorVPN
        fields = ['vendor_name', 'issue_date', 'expiration_date', 'status']
        labels = {
            'vendor_name': 'Nome do Fornecedor',
            'issue_date': 'Data de Renovação',
            'expiration_date': 'Data de Expiração',
            'status': 'Status'
        }
        # Personalizar os widgets   
        widgets = {
            'vendor_name': forms.TextInput(attrs={'class': 'form-control'}),
            'issue_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'expiration_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-control'})
        }

# Criação de um formulário baseado no modelo Application
class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['app_name', 'description', 'deadline_date', 'reference_link', 'status']
        labels = {
            'app_name': 'Nome da Aplicação',
            'description': 'Descrição',
            'deadline_date': 'Data Limite',
            'reference_link': 'Link de Referência',
            'status': 'Status'
        }
        # Personalizar os widgets   
        widgets = {
            'app_name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'deadline_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'reference_link': forms.URLInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'})
        }
