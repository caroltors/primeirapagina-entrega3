# Console Admin — Pré-Entrega 3

&#x20;

## 📌 Objetivos da Aplicação

O **Console Admin** é uma plataforma web desenvolvida em Django que centraliza o gerenciamento de **certificados**, **VPNs de fornecedores** e **aplicações**, facilitando o controle de alertas de expiração e requisitos de manutenção.

### Funcionalidades principais:

1. **Login obrigatório**

   - Somente usuários autenticados podem acessar o sistema.

2. **Dashboard inicial**

   - Apresenta notificações e alertas de forma consolidada.
   - Mostra os itens próximos da expiração com contadores e alertas visuais.

3. **Console de Certificados**

   - Cadastro, edição, exclusão e visualização de certificados.
   - Alerta configurado para **7 dias antes da expiração**.

4. **Console de VPNs de Fornecedores**

   - Cadastro, edição, exclusão e visualização de VPNs.
   - Alerta configurado para **2 dias antes da expiração**.

5. **Console de Aplicações**

   - Controle de requisitos específicos das aplicações.
   - Alerta configurado para **30 dias antes da expiração** de qualquer requisito.

6. **TODO: Expansão futura**

   - Cronograma de férias.
   - Escala de sobreaviso com alertas automáticos.
   - Sistema de monitoramento de aplicações ou operações.

---

## 🛠 Tecnologias utilizadas

- Django (padrão MVT)
- SQLite (banco de dados local para desenvolvimento)
- Bootstrap 5 (layout responsivo e estilização moderna)
- HTML/CSS/JS (templates e scripts do dashboard)
- Git/GitHub (versionamento do código)

---

## 🧩 Estrutura do Projeto

```
root/
│
├── console/
│   ├── templates/
│   │   └── console/
│   │       ├── base.html
│   │       ├── dashboard.html
│   │       ├── certificate_list.html
│   │       ├── vendorvpn_list.html
│   │       └── application_list.html
│   ├── views.py
│   ├── urls.py
│   └── forms.py
│
├── console_admin/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── manage.py
├── requirements.txt
├── db.sqlite3
└── README.md
```

---

## ⚙️ Instalação e execução

1. Clone o repositório:
   ```bash
   git clone https://github.com/caroltors/primeirapagina-entrega3.git
   ```
2. Entre no diretório do projeto:
   ```bash
   cd console_admin
   ```
3. Crie e ative o ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```
4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
5. Rode as migrações do Django:
   ```bash
   python manage.py migrate
   ```
6. Crie um superusuário para login:
   ```bash
   python manage.py createsuperuser
   ```
7. Execute o servidor local:
   ```bash
   python manage.py runserver
   ```
8. Acesse a aplicação em `http://127.0.0.1:8000/`.

---

## 📝 Ordem recomendada para testes / navegação

1. **Login**
   - Testar acesso com usuário válido.
2. **Dashboard**
   - Conferir contadores de itens e alertas.
   - URLs relacionadas: `/dashboard/`
3. **Console de Certificados**
   - Criar e visualizar certificados.
   - Edição e exclusão são realizadas via modal diretamente na lista.
   - URLs relacionadas:
     - Lista: `/certificates/`
     - Criar: `/certificates/create/`
4. **Console de VPNs**
   - Criar e visualizar VPNs.
   - Edição e exclusão via modal.
   - URLs relacionadas:
     - Lista: `/vendorvpn/`
     - Criar: `/vendorvpn/create/`
5. **Console de Aplicações**
   - Adicionar e visualizar aplicações.
   - Edição e exclusão via modal.
   - URLs relacionadas:
     - Lista: `/applications/`
     - Criar: `/applications/create/`
6. **Logout**
   - Conferir botão de logout e ícone.
   - URL relacionada: `/logout/`
7. **Responsividade**
   - Abrir em diferentes resoluções (desktop, tablet, mobile).
   - Conferir comportamento do menu e dashboard.

---

## 📌 Observações importantes

- Todos os alertas são baseados na data atual (`timezone.now()`) e nas regras definidas na view do dashboard.
- O dashboard utiliza **cards brancos com sombreado azul**, e alertas visuais em **badge amarela**.
- O layout da navbar e footer utiliza **azul escuro**, com títulos e badges contrastantes.
- Manter padrão visual e responsivo em futuras expansões.

---

**Desenvolvido por Caroline Torres para o curso de Python da CoderHouse.**

