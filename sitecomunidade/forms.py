from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_wtf.file import FileField
from wtforms import  StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from sitecomunidade.models import Usuario
from flask_login import current_user



class FormCriarConta(FlaskForm):
    username = StringField('Nome de Usuário', validators= [DataRequired()])
    email = StringField('E-mail', validators= [DataRequired(),Email()])
    senha = PasswordField('Senha',validators= [DataRequired(), Length(6,20)])
    confirmacao_senha = PasswordField('Confirmação da Senha',validators= [DataRequired(),EqualTo('senha')])
    botao_submit_criar_conta = SubmitField('Criar Conta')

    def validate_email(self,email):
        usuario = Usuario.query.filter_by(email= email.data).first()
        if usuario:
            raise ValidationError('Email já cadastrado. Cadastre-se com outro Email ou faça Login')



class FormLogin(FlaskForm):
    email = StringField('E-mail', validators= [DataRequired(),Email()])
    senha = PasswordField('Senha',validators= [DataRequired()])
    lembrar_dados = BooleanField("Lembrar Dados")
    botao_submit_login = SubmitField('Fazer Login')


class FormEditarPerfil(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    foto_perfil = FileField('Atualizar foto de Perfil', validators=[FileAllowed(['jpg','png'])])
    curso_ingles = BooleanField("Curso Inglês")
    curso_matematica = BooleanField("Curso Matematica")
    curso_espanhol = BooleanField("Curso Espanhol")
    curso_frances = BooleanField("Curso Frânces")
    curso_alemao = BooleanField("Curso Alemão")
    curso_italiano = BooleanField("Curso Italiano")
    botao_submit_editar_perfil = SubmitField('Confirmar Edição')

    def validate_email(self,email):
        if current_user.email != email.data:
            usuario = Usuario.query.filter_by(email= email.data).first()
            if usuario:
                raise ValidationError('Já existe um usuário com esse email. Cadastre outro Email')


class FormCriarPost(FlaskForm):
    titulo = StringField('Título do Post', validators=[DataRequired(),Length(2,140)])
    corpo =  TextAreaField('Escreva seu Post aqui',validators=[DataRequired()])
    botao_submit = SubmitField('Criar Post')