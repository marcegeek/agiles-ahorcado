"""Aplicación web Flask del juego del ahorcado."""

from __future__ import annotations

import os

from flask import Flask, Response, flash, redirect, render_template, request, session, url_for

from ahorcado import Juego, Partida

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "default_secret_key")


@app.route("/")
def index() -> str:
    """Devuelve la página principal."""
    return render_template("index.html")


def iniciar_juego() -> None:
    """Inicia un juego simple con la palabra ingresada."""
    palabra = request.form["palabra"]
    try:
        juego = Juego(palabra=palabra)
        session["juego"] = juego.to_dict()
    except ValueError as e:
        flash(str(e), category="error")


def arriesgar(juego: Juego) -> str:
    """Arriesgar letra o palabra en el juego actual."""
    intento = request.form["intento"]
    metodo = juego.arriesgar_letra if len(intento) == 1 else juego.arriesgar_palabra
    return metodo(intento)


@app.route("/juego", methods=["GET", "POST"])
def juego() -> str:
    """Permite arriesgar en el juego actual o iniciar uno nuevo y devuelve la vista."""
    if "juego" not in session:
        if request.method == "POST":
            iniciar_juego()
            return redirect(url_for("juego"))
        return render_template("juego-inicio.html")
    juego = Juego(data=session["juego"])
    resultado = None
    if request.method == "POST":
        resultado = arriesgar(juego)
        session["juego"] = juego.to_dict()
    return render_template("juego.html", juego=juego, resultado=resultado)


def url_redireccion(fallback: str | None = None) -> str:
    """Obtiene la URL a la que redirigir."""
    if fallback is None:
        fallback = url_for("index")
    redirecciones = request.values.get("redirect_to"), request.referrer, fallback
    return next(r for r in redirecciones if r)


@app.route("/finalizar", methods=["POST"])
def finalizar() -> Response:
    """Finaliza el juego y/o partida actual."""
    session.pop("juego", None)
    session.pop("jugadores", None)
    session.pop("partida", None)
    return redirect(url_redireccion())


def iniciar_partida() -> None:
    """Inicia una nueva partida con los jugadores ingresados."""
    keys = ["jugador1", "jugador2"]
    session["jugadores"] = [request.form[k] for k in keys]
    p = Partida()
    session["partida"] = p.to_dict()


def iniciar_ronda(partida: Partida) -> None:
    """Inicia una nueva ronda en la partida actual con la palabra ingresada."""
    palabra = request.form["palabra"]
    partida.comenzar_ronda(palabra)
    session["partida"] = partida.to_dict()


@app.route("/partida", methods=["GET", "POST"])
def partida() -> str:
    """Permite arriesgar en la partida actual, iniciar una nueva o iniciar una ronda y devuelve la vista."""
    jugadores = session.get("jugadores")
    partida = Partida(data=session["partida"]) if "partida" in session else None
    if not partida:
        if request.method == "POST":
            iniciar_partida()
            return redirect(url_for("partida"))
        return render_template(
            "partida-inicio.html",
            jugadores=jugadores,
            partida=partida,
        )

    hay_que_iniciar_ronda = partida.id_jugador_actual is None or partida.ronda_finalizo()
    jugador_palabra = 0 if partida.id_jugador_actual is None else partida.id_jugador_actual
    jugador_adivina = (jugador_palabra + 1) % 2
    if request.method == "POST":
        if not partida.finalizo():
            if hay_que_iniciar_ronda:
                iniciar_ronda(partida)
            else:
                arriesgar(partida.juego)
                partida.actualizar_puntos()
                session["partida"] = partida.to_dict()
        else:
            flash("La partida ya finalizó", category="error")
        return redirect(url_for("partida"))
    return render_template(
        "partida.html",
        jugadores=jugadores,
        partida=partida,
        iniciar_ronda=hay_que_iniciar_ronda,
        jugador_palabra=jugador_palabra,
        jugador_adivina=jugador_adivina,
    )


if __name__ == "__main__":
    # ruff: noqa: S201: ignorar uso de debug=True
    app.run(debug=True)
