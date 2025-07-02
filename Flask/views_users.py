from principal import app
from flask import render_template, request, redirect, session, flash, url_for
from models import Usuarios
from rotarecuperaimagem import FormularioUsuario

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    form = FormularioUsuario()
    return render_template('login.html', proxima=proxima, form=form)


@app.route('/autenticar', methods=['POST'])
def autenticar():
    from models import Usuarios  # ⬅️ só carrega quando a função roda
    form = FormularioUsuario(request.form)
    usuario = Usuarios.query.filter_by(nickname=form.nickname.data).first()

    if usuario and form.senha.data == usuario.senha:
        session['usuario_logado'] = usuario.nickname
        flash(usuario.nickname + ' logado com sucesso')
        proxima_pagina = request.form.get('proxima') or url_for('index')
        return redirect(proxima_pagina)

    flash('Usuário não logado')
    return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('index'))
