# 🎮 Projeto Flask - Catálogo de Jogos

Este é um projeto simples em **Python** utilizando o **framework Flask**, que implementa um CRUD básico para gerenciar uma lista de jogos. Também há um sistema de **login e autenticação** de usuários com sessões.

---

## 🚀 Funcionalidades

- ✅ Visualização da lista de jogos
- ✅ Cadastro de novos jogos (restrito a usuários autenticados)
- ✅ Sistema de login e logout com sessão
- 🔒 Rotas protegidas para impedir acesso não autorizado
- ⚠️ Funcionalidade de edição e exclusão ainda não implementadas (CRUD incompleto)

---

## 🧩 Tecnologias Utilizadas

- Python 3
- Flask
- HTML (com `render_template`)
- Sessões com Flask
- Flash messages

---

## 🛠️ Estrutura de Classes

### `Jogo`
```python
class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

class Usuario:
    def __init__(self, nome, nickname, senha):
        self.nome = nome
        self.nickname = nickname
        self.senha = senha
```

| Rota          | Método | Descrição                                             |
| ------------- | ------ | ----------------------------------------------------- |
| `/`           | GET    | Exibe a lista de jogos cadastrados                    |
| `/novo`       | GET    | Exibe formulário para adicionar novo jogo (com login) |
| `/criar`      | POST   | Adiciona novo jogo à lista                            |
| `/login`      | GET    | Exibe o formulário de login                           |
| `/autenticar` | POST   | Verifica se o usuário existe e autentica              |
| `/logout`     | GET    | Encerra a sessão do usuário                           |
 
--- 

### 🔐 Acesso e Login
```Usuários são definidos no código com nickname e senha. Exemplo:
usuario1 = Usuario("Dudinha", "DD", "piropiro")
Para acessar a rota de novo jogo (/novo), é necessário estar logado com um desses nicknames e senhas.