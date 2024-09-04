from flask import Flask, render_template, request, redirect, url_for, session
from juego import Juego

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/iniciar', methods=['POST'])
def iniciar():
    palabra = request.form['palabra']
    try:
        juego = Juego(palabra=palabra)
        session['juego'] = juego.to_dict()
        return redirect(url_for('jugar'))
    except ValueError as e:
        return render_template('index.html', error=str(e))

def arriesgar(juego):
    intento = request.form['intento']
    if len(intento) == 1:
        resultado = juego.arriesgarLetra(intento)
    else:
        resultado = juego.arriesgarPalabra(intento)
    return resultado

@app.route('/jugar', methods=['GET', 'POST'])
def jugar():
    if 'juego' not in session:
        return redirect(url_for('index'))

    juego = Juego(data=session['juego'])
    resultado = None

    if request.method == 'POST':
        resultado = arriesgar(juego)
        session['juego'] = juego.to_dict()
    return render_template('jugar.html', juego=juego.informacionJuego(), resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
