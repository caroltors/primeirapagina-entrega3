from django.db import models
from django.utils import timezone

# Create your models here.

# -------------------------------------------------
# Lista de opções para o campo status
# -------------------------------------------------
STATUS_CHOICES = [
    ('active', 'Active'),       # Ativo
    ('renewed', 'Renewed'),     # Renovado
    ('expired', 'Expired'),     # Expirado
    ('pending', 'Pending'),     # Pendente
    ('resolved', 'Resolved'),   # Resolvido
]

# -------------------------------------------------
# Modelo para armazenar informações de certificados digitais
# -------------------------------------------------
class Certificate(models.Model):
    name = models.CharField(max_length=100)  # Nome do certificado
    related_system = models.CharField(max_length=100)  # Sistema ou aplicação associada
    issue_date = models.DateField()  # Data de emissão
    expiration_date = models.DateField()  # Data de expiração
    status = models.CharField(
        max_length=10, 
        choices=STATUS_CHOICES, 
        default='active'
    )  # Status atual do certificado

    def days_to_expire(self):
        """Retorna a quantidade de dias até expirar"""
        return (self.expiration_date - timezone.now().date()).days

    def is_in_alert(self):
        """Retorna True se faltar 7 dias ou menos para expirar"""
        return self.days_to_expire() <= 7

    def __str__(self):
        return f"{self.name} - {self.related_system}"


# -------------------------------------------------
# Modelo para armazenar informações sobre VPNs de fornecedores
# -------------------------------------------------
class VendorVPN(models.Model):
    vendor_name = models.CharField(max_length=100)  # Nome do fornecedor
    issue_date = models.DateField()  # Data de renovação da VPN
    expiration_date = models.DateField()  # Data de expiração da VPN
    status = models.CharField(
        max_length=10, 
        choices=STATUS_CHOICES, 
        default='active'
    )  # Status atual da VPN

    def days_to_expire(self):
        """Retorna a quantidade de dias até expirar"""
        return (self.expiration_date - timezone.now().date()).days

    def is_in_alert(self):
        """Retorna True se faltar 2 dias ou menos para expirar"""
        return self.days_to_expire() <= 2

    def __str__(self):
        return self.vendor_name

# -------------------------------------------------
# Modelo para controlar prazos e requisitos de aplicações
# Exemplo: atualização de SDK, renovação de tokens, etc.
# -------------------------------------------------
class Application(models.Model):
    app_name = models.CharField(max_length=100)  # Nome da aplicação
    description = models.TextField(blank=True)  # Descrição opcional
    deadline_date = models.DateField()  # Data limite para ação
    reference_link = models.URLField(blank=True, null=True)  # Link de referência 
    status = models.CharField(
        max_length=10, 
        choices=STATUS_CHOICES, 
        default='pending'
    )  # Status atual da aplicação

    def days_to_expire(self):
        """Retorna a quantidade de dias até o prazo final"""
        return (self.deadline_date - timezone.now().date()).days

    def is_in_alert(self):
        """Retorna True se faltar 30 dias ou menos para o prazo"""
        return self.days_to_expire() <= 30

    def __str__(self):
        return self.app_name
