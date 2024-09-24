import re

from behave import given, then, when
from environment import arriesgar, post

from app import app


@given('players "{player1}" and "{player2}" have started a two-player game')
def step_impl(context, player1, player2):
    context.client = app.test_client()
    context.player1 = player1
    context.player2 = player2
    context.url = "/partida"
    post(context, data={"jugador1": player1, "jugador2": player2})


@then('the player "{current}" has to start a round for "{oponent}"')
def step_impl(context, current, oponent):
    m = re.search(r"<p\b.*?>(.+), ingresa la palabra para (.+):</p>", context.html, re.IGNORECASE)
    p1 = m.group(1)
    p2 = m.group(2)
    assert p1 == current
    assert p2 == oponent


@then("the scores should be {score1:d}-{score2:d}")
def step_impl(context, score1, score2):
    m = re.search(rf"{context.player1} vs. {context.player2}: (\d+)\w*-\w*(\d+)\b", context.html, re.IGNORECASE)
    s1 = int(m.group(1))
    s2 = int(m.group(2))
    assert s1 == score1
    assert s2 == score2


@then("the started rounds should be {rounds1:d}-{rounds2:d}")
def step_impl(context, rounds1, rounds2):
    m = re.search(r"\bRondas iniciadas: (\d+) vs. (\d+)\b", context.html, re.IGNORECASE)
    r1 = int(m.group(1))
    r2 = int(m.group(2))
    assert r1 == rounds1
    assert r2 == rounds2


@when('the current player starts the game for the oponent with word "{word}"')
def step_impl(context, word):
    post(context, data={"palabra": word})


@when('the current player tries the letter "{letter}"')
def step_impl(context, letter):
    arriesgar(context, letter)


@when('the current player tries the word "{word}"')
def step_impl(context, word):
    arriesgar(context, word)


@then('the game result is "{result}"')
def step_impl(context, result):
    assert re.search(rf"\b{result}\b", context.html, re.IGNORECASE)
