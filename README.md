# README - Projeto Apasi Ambiental

## Visão Geral

Este projeto é um site institucional desenvolvido para a **Apasi Ambiental**, uma empresa especializada em coleta, transporte e gestão de resíduos perigosos (Classe I). O site foi criado como um guia funcional para apresentar os serviços, áreas de atuação, canais de atendimento e outras informações relevantes da empresa. Embora o projeto ainda não esteja concluído, ele já é funcional e atende aos principais requisitos iniciais.

O site foi construído utilizando **Django** no backend, **Bootstrap 5** para o frontend, e integrações com APIs externas, como o **Leaflet** para mapas interativos e o **ViaCEP** para preenchimento automático de endereços. O foco é oferecer uma interface amigável, responsiva e acessível, com funcionalidades que destacam a atuação da empresa em 6 estados brasileiros.

## Funcionalidades Principais

- **Home**: Página inicial com seções destacando os serviços, diferenciais, áreas de atuação e um CTA (Call to Action) para contato.  
- **Sobre Nós**: Informações sobre a história da empresa, presença nacional e números relevantes.  
- **Canais de Atendimento**: Lista de contatos por setor (telefone, WhatsApp, e-mail) e endereço físico.  
- **Contato**: Formulário de contato com validação, máscaras de input (CPF/CNPJ, telefone, CEP) e integração com o ViaCEP. Envia e-mails para a equipe comercial.  
- **Áreas de Atuação**: Mapa interativo (Leaflet) com filtros por estado e busca por cidade, exibindo as cidades atendidas e sedes/escritórios.  
- **Licenças e Certificados**: Lista das principais licenças e certificações da empresa.  
- **FAQ**: Perguntas frequentes sobre os serviços e operações.  
- **Política de Privacidade**: Modal com informações sobre conformidade com a LGPD.

## Tecnologias Utilizadas

### Backend
- **Django 4.x**
- **Django REST Framework**
- **Python 3.x**
- **SQLite** (padrão para desenvolvimento)

### Frontend
- **Bootstrap 5.3**
- **Leaflet 1.9.4**
- **jQuery 3.6.0**
- **jQuery Mask Plugin**
- **Bootstrap Icons**

### APIs Externas
- **ViaCEP**: preenchimento automático de endereços.  
- **OpenStreetMap**: tiles para o mapa Leaflet.

### Outras Ferramentas
- **HTML5**, **CSS3**, **JavaScript (ES6)**
- **Django Templates**
- **Arquivos Estáticos (CSS, JS, imagens)**

## Como Executar o Projeto

### Pré-requisitos
- Python 3.8+
- pip
- Git
- Navegador moderno

### Passos para Configuração

```bash
# Clone o repositório
git clone https://github.com/seu_usuario/apasi_ambiental.git
cd apasi_ambiental

# Crie e ative um ambiente virtual
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate       # Windows

# Instale as dependências
pip install django djangorestframework

# Configure as variáveis de ambiente (opcional)
# Exemplo de .env:
# EMAIL_HOST=smtp.gmail.com
# EMAIL_PORT=587
# EMAIL_USE_TLS=True
# EMAIL_HOST_USER=seu_email@gmail.com
# EMAIL_HOST_PASSWORD=sua_senha
# DEFAULT_FROM_EMAIL=seu_email@gmail.com

# Aplique as migrações
python manage.py makemigrations
python manage.py migrate

# Crie um superusuário (opcional)
python manage.py createsuperuser

# Inicie o servidor
python manage.py runserver
```

Acesse `http://localhost:8000` no navegador.

## Funcionalidades Pendentes

- Autenticação de usuários (login restrito para clientes).  
- Painel administrativo customizado.  
- Upload de arquivos no formulário de contato.  
- Internacionalização (i18n).  
- Testes automatizados.  
- Otimizações de performance.  
- Integração com ferramentas de analytics.

## Contribuições

Contribuições são bem-vindas!  
1. Fork o repositório  
2. Crie uma branch: `git checkout -b feature/sua-feature`  
3. Commit: `git commit -m "Descrição clara"`  
4. Push: `git push origin feature/sua-feature`  
5. Abra um Pull Request

## Contato

Para dúvidas ou sugestões:

- **E-mail**: ambientallix.comercial01@gmail.com  
- **WhatsApp**: +55 (63) 99928-2888

## Licença

Este projeto é de propriedade da **Apasi Ambiental** e não possui uma licença pública definida.  
O uso ou distribuição do código sem autorização expressa é proibido.

---

Nota: A publicação deste projeto no portfólio pessoal foi autorizada pela empresa Apasi Ambiental, com finalidade exclusivamente demonstrativa e sem fins comerciais.

---

**Desenvolvido por João Pedro de Oliveira Paulino para a Apasi Ambiental**  
**Última atualização: 12 de junho de 2025**
