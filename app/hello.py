from flask import Flask, render_template, request
import uuid
app = Flask(__name__)

usuarios = ['Mikael', 'Yasmin']
senha = ['123', '456']
musicas = {}
@app.route('/', methods=['GET', 'POST'])
def TelaLogin():
    error = None
    if request.method == 'POST':
        verificar_usuario = request.form.get('usuario') 
        verificar_senha = request.form.get('senha')
        if verificar_usuario in usuarios:
            #Pegando a posição de usuario na lista
            index = usuarios.index(verificar_usuario)
            # vincula a posição de usuario com a da senha
            if senha[index] == verificar_senha:
                return render_template('tela_usuario.html')
            else:
                error = 'Usuário não encontrado. Tente novamente.'
    return render_template('validacao.html', error = error)

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro_usuario():
    if request.method == 'POST':
        cadastrar_usuario = request.form.get('usuario')
        cadastrar_senha = request.form.get('senha')
        usuarios.append(cadastrar_usuario)
        senha.append(cadastrar_senha)
        return render_template('validacao.html')
    return render_template('cadastro.html')


@app.route('/TelaUsuario', methods=['GET', 'POST'])
def cadastrarMusicas():
    if request.method == 'POST':
        cantor = request.form.get('cantor_banda') 
        musica = request.form.get('musica')
        musica_id = str(uuid.uuid4())
        musicas[musica_id] = {
                'nome': cantor,
                'musica': musica
        }

    return render_template('tela_usuario.html', musicas = musicas)

@app.route('/logout')
def logout():
    return render_template('validacao.html')