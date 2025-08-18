from django.shortcuts import render, redirect, get_object_or_404  # Funções para renderizar templates, redirecionar URLs e buscar objetos ou retornar 404
from django.contrib import messages  # Para exibir mensagens de sucesso ou erro aos usuários
from django.contrib.auth.decorators import login_required  # Garante que apenas usuários logados possam acessar determinadas views
from django.urls import reverse_lazy  # Gera URLs a partir do nome das rotas, útil principalmente para CBVs
from django.utils import timezone  # Trabalha com datas e horários, útil para cálculos como dias restantes
from .models import Certificate, VendorVPN, Application  # Importa os modelos do app console
from .forms import CertificateForm, VendorVPNForm, ApplicationForm  # Importa os formulários criados para os modelos

# View da página inicial do console - Dashboard # TODO: Será feito por último


# ===========================
# VIEWS PARA CERTIFICADOS
# ===========================

# Lista de certificados - LIST VIEW
@login_required  # Garante que apenas usuários logados possam acessar
def certificate_list(request):
    # Buscar todos os certificados
    certificates = Certificate.objects.all().order_by('expiration_date')

    # Opcional: filtrar apenas certificados próximos de expirar (menos de 7 dias)
    for cert in certificates:
        cert.days_to_expire = (cert.expiration_date - timezone.now().date()).days
        cert.is_alert = cert.days_to_expire <= 7

    return render(request, 'console/certificate_list.html', {'certificates': certificates})

# Criar certificado - CREATE VIEW
@login_required
def certificate_create(request):
    if request.method == 'POST':
        form = CertificateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('certificate_list')  # Redireciona para a lista após salvar
    else:
        form = CertificateForm()

    return render(request, 'console/certificate_form.html', {'form': form, 'title': 'Adicionar Certificado'})

# Editar certificado - UPDATE VIEW
@login_required
def certificate_update(request, pk):
    certificate = get_object_or_404(Certificate, pk=pk)  # Busca o certificado pelo ID
    if request.method == 'POST':
        form = CertificateForm(request.POST, instance=certificate)
        if form.is_valid():
            form.save()
            return redirect('certificate_list')
    else:
        form = CertificateForm(instance=certificate)

    return render(request, 'console/certificate_form.html', {'form': form, 'title': 'Editar Certificado'})

# Excluir certificado via modal - DELETE VIEW 
@login_required
def certificate_delete(request, pk):
    certificate = get_object_or_404(Certificate, pk=pk)
    if request.method == 'POST':
        certificate.delete()
    return redirect('certificate_list')  # Redireciona sempre para a lista

# ================================
# VIEWS PARA VPNS DE FORNECEDORES
# ================================

# Listar todos os VendorVPN - LIST VIEW
@login_required
def vendorvpn_list(request):
    vendorvpns = VendorVPN.objects.all().order_by('expiration_date')

    # Calcular dias restantes e alerta
    for vpn in vendorvpns:
        vpn.days_to_expire = (vpn.expiration_date - timezone.now().date()).days
        vpn.is_alert = vpn.days_to_expire <= 2  # alerta programado para 2 dias antes da expiração

    return render(request, 'console/vendorvpn_list.html', {'vendorvpns': vendorvpns})

# Criar VendorVPN - CREATE VIEW
@login_required
def vendorvpn_create(request):
    if request.method == 'POST':
        form = VendorVPNForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vendorvpn_list')
    else:
        form = VendorVPNForm()

    return render(request, 'console/vendorvpn_form.html', {'form': form, 'form_title': 'Adicionar VendorVPN'})

# Atualizar VendorVPN - UPDATE VIEW
@login_required
def vendorvpn_update(request, pk):
    vendorvpn = get_object_or_404(VendorVPN, pk=pk)
    if request.method == 'POST':
        form = VendorVPNForm(request.POST, instance=vendorvpn)
        if form.is_valid():
            form.save()
            return redirect('vendorvpn_list')
    else:
        form = VendorVPNForm(instance=vendorvpn)

    return render(request, 'console/vendorvpn_form.html', {'form': form, 'form_title': 'Editar VendorVPN'})

# Deletar VendorVPN via modal - DELETE VIEW
@login_required
def vendorvpn_delete(request, pk):
    vendorvpn = get_object_or_404(VendorVPN, pk=pk)
    if request.method == 'POST':
        vendorvpn.delete()
    return redirect('vendorvpn_list')  # redireciona sempre para a lista

# ============================
# VIEWS PARA APPLICATIONS
# ============================

# Listagem de Applications
@login_required
def application_list(request):
    applications = Application.objects.all().order_by('deadline_date')

    # Calcular atributos temporários para o template
    for app in applications:
        app.days_to_expire = (app.deadline_date - timezone.now().date()).days
        app.is_alert = app.days_to_expire <= 30  # atributo, não método

    return render(request, 'console/application_list.html', {'applications': applications})

# Criar Application
@login_required
def application_create(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('application_list')
    else:
        form = ApplicationForm()
    return render(request, 'console/application_form.html', {'form': form, 'title': 'Add New Application'})

# Editar Application
@login_required
def application_update(request, pk):
    app = get_object_or_404(Application, pk=pk)
    if request.method == 'POST':
        form = ApplicationForm(request.POST, instance=app)
        if form.is_valid():
            form.save()
            return redirect('application_list')
    else:
        form = ApplicationForm(instance=app)
    return render(request, 'console/application_form.html', {'form': form, 'title': 'Edit Application'})

# Deletar Application
@login_required
def application_delete(request, pk):
    app = get_object_or_404(Application, pk=pk)
    if request.method == 'POST':
        app.delete()
        return redirect('application_list')
    return render(request, 'console/application_confirm_delete.html', {'application': app})

# ============================
# VIEW DO DASHBOARD
# ============================

@login_required
def dashboard(request):
    # Certificados
    certificates = Certificate.objects.all().order_by('expiration_date')
    for cert in certificates:
        cert.days_to_expire = (cert.expiration_date - timezone.now().date()).days
        cert.is_in_alert = cert.days_to_expire <= 7

    # VPNs
    vendorvpns = VendorVPN.objects.all().order_by('expiration_date')
    for vpn in vendorvpns:
        vpn.days_to_expire = (vpn.expiration_date - timezone.now().date()).days
        vpn.is_in_alert = vpn.days_to_expire <= 2

    # Aplicações
    applications = Application.objects.all().order_by('deadline_date')
    for app in applications:
        app.days_to_expire = (app.deadline_date - timezone.now().date()).days
        app.is_in_alert = app.days_to_expire <= 30

    # Checar se há alertas
    has_alerts_cert = any(cert.is_in_alert for cert in certificates)
    has_alerts_vpn = any(vpn.is_in_alert for vpn in vendorvpns)
    has_alerts_app = any(app.is_in_alert for app in applications)

    context = {
        'certificates': certificates,
        'vendorvpns': vendorvpns,
        'applications': applications,
        'has_alerts_cert': has_alerts_cert,
        'has_alerts_vpn': has_alerts_vpn,
        'has_alerts_app': has_alerts_app,
    }
    return render(request, 'console/dashboard.html', context)