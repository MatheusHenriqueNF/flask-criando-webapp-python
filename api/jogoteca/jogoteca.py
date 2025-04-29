from flask import Flask, render_template, request, redirect, session
from flask import flash


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


jogo1 = Jogo('The Last of Us', 'Ação', 'PS4')
jogo2 = Jogo('God of War', 'Aventura', 'PS4')
jogo3 = Jogo('Halo Infinite', 'Tiro', 'Xbox')
lista = [
        jogo1,
        jogo2,
        jogo3
    ]
app = Flask(__name__)
app.secret_key = 'Alura'

@app.route('/')
def index():
          
    return render_template('lista.html', titulo='Jogos', jogos=lista)

@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo Jogo')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect('/')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if 'alohomora' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash(session['usuario_logado'] + 'Usuário logado com sucesso!')
        return redirect('/')
    else:
        flash('Usuário ou senha inválidos!')
        return redirect('/login')

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Usuário deslogado com sucesso!')
    return redirect('/')

app.run(debug=True)