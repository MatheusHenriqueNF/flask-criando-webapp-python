from flask import Flask, render_template


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


app = Flask(__name__)


@app.route('/inicio')
def ola():
    jogo1 = Jogo('The Last of Us', 'Ação', 'PS4')
    jogo2 = Jogo('God of War', 'Aventura', 'PS4')
    jogo3 = Jogo('Halo Infinite', 'Tiro', 'Xbox')

    lista = [
        jogo1,
        jogo2,
        jogo3
    ]
        
    return render_template('lista.html', titulo='Jogos', jogos=lista)

app.run()