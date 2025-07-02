import os

from nbformat.validator import validators
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length

from Flask.principal import app
from flask_wtf import FlaskForm


class FormularioJogo(FlaskForm):
    nome = StringField('Nome do Jogo', validators=[DataRequired(), Length(max=50)])
    categoria = StringField('Categoria', validators=[DataRequired(), Length(max=50)])
    console = StringField('Console', validators=[DataRequired(), Length(max=10)])
    salvar = SubmitField('Salvar')


class FormularioUsuario(FlaskForm):
    nickname = StringField('Nome do Usuario', validators=[DataRequired(), Length(max=8)])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(max=50)])
    login = SubmitField('Login', validators=[DataRequired(), Length(max=50)])


def recupera_imagem(id):
    for nome_arquivo in os.listdir(app.config['UPLOAD_PATH']):
        if f'capa{id}' in nome_arquivo:
            return nome_arquivo

    return 'interrogação.jpg'


def deleta_arquivo(id):
    arquivo = recupera_imagem(id)
    if arquivo != 'capa_padrao.jpg':
        os.remove(os.path.join(app.config['UPLOAD_PATH'], arquivo))
