from juego import Juego

# Test para el mensaje de victoria y el puntaje final arriesgando letras.
def test_gana_con_letras(monkeypatch, capsys):
    j = Juego("casa")
    
    inputs = iter(['c', 'a', 's', 'a'])
    monkeypatch.setattr('builtins.input', lambda: next(inputs))
    
    puntaje = j.iniciarJuego()
    
    captured = capsys.readouterr()
    assert "GANASTE!" in captured.out
    assert puntaje == j.intentosDisponibles()
    
# Test para el mensaje de derrota y el puntaje final arriesgando letras.
def test_pierde_con_letras(monkeypatch, capsys):
    j = Juego("casa")
    j.maxIntentos = 1
    inputs = iter(['v'])
    monkeypatch.setattr('builtins.input', lambda: next(inputs))
    
    puntaje = j.iniciarJuego()
    
    captured = capsys.readouterr()
    assert "PERDISTE!" in captured.out
    assert puntaje == 0
    
# Test para el mensaje de victoria y el puntaje final arriesgando palabras.
def test_gana_con_palabras(monkeypatch, capsys):
    j = Juego("casa")
    j.maxIntentos = 1
    inputs = iter(['casa'])
    monkeypatch.setattr('builtins.input', lambda: next(inputs))
    
    puntaje = j.iniciarJuego()
    
    captured = capsys.readouterr()
    assert "GANASTE!" in captured.out
    assert puntaje == j.intentosDisponibles()
    
# Test para el mensaje de derrota y el puntaje final arriesgando palabras.
def test_pierde_con_palabras(monkeypatch, capsys):
    j = Juego("casa")
    j.maxIntentos = 1
    inputs = iter(['hola'])
    monkeypatch.setattr('builtins.input', lambda: next(inputs))
    
    puntaje = j.iniciarJuego()
    
    captured = capsys.readouterr()
    assert "PERDISTE!" in captured.out
    assert puntaje == 0

