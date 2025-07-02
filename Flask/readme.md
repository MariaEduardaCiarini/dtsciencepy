# 🎮 Projeto Flask - Gerenciador de Jogos

## ✅ Resumo do Projeto

Este projeto é uma aplicação web desenvolvida com **Flask** que permite cadastrar, listar, editar e excluir jogos, com upload de imagem de capa para cada jogo. Também inclui autenticação de usuários com login e sessão. A aplicação segue o padrão **MVC (Model-View-Controller)** e utiliza **Bootstrap** para estilização da interface.

### Funcionalidades principais:

- ✅ Cadastro de jogos com nome, console e categoria
- 🖼️ Upload de imagem de capa para cada jogo
- 📋 Listagem de jogos cadastrados
- ✏️ Edição e exclusão de jogos
- 🔐 Sistema de login com validação de usuário
- 💬 Flash messages para feedback do usuário
- 🧾 Validação de formulários com **WTForms**

---

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- **Flask**
- **WTForms**
- **Flask-WTF**
- **Flask-SQLAlchemy**
- **Jinja2** (para templates)
- **Bootstrap 5** (estilização)
- **HTML5 + CSS3**

## 📁 Estrutura do Projeto

```text
Flask/
├── static/
│   ├── app.css                # Estilos personalizados
│   └── bootstrap.css          # Estilos do Bootstrap
├── templates/
│   ├── template.html          # Template base
│   ├── login.html             # Tela de login
│   ├── lista.html             # Página de listagem de jogos
│   ├── novo.html              # Formulário para adicionar jogos
│   └── editar.html            # Formulário para editar jogos
├── uploads/                   # Onde são armazenadas as imagens de capa
├── models.py                  # Definição das classes Jogos e Usuarios
├── views_jogos.py             # Rotas relacionadas aos jogos
├── views_usuarios.py          # Rotas relacionadas à autenticação do usuario
├── rotarecuperaimagem.py      # Responsável por exibir imagens de capa
├── principal.py               # Arquivo principal da aplicação Flask

```
