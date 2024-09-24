Feature: Partida a 6 Rondas

  Scenario: Iniciar una nueva partida
    Given players "player1" and "player2" have started a two-player game
    Then the player "player1" has to start a round for "player2"
    Then the scores should be 0-0
    Then the started rounds should be 0-0

  Scenario: Jugador 1 gana por 6-0
    Given players "player1" and "player2" have started a two-player game
    When the current player starts the game for the oponent with word "python"
    When the current player tries the letter "a"
    When the current player tries the letter "b"
    When the current player tries the letter "c"
    When the current player tries the letter "d"
    When the current player tries the letter "e"
    When the current player tries the letter "f"
    When the current player starts the game for the oponent with word "secret"
    When the current player tries the word "secret"
    Then the game result is "ACERTASTE"
    Then the scores should be 6-0

  Scenario: Jugador 1 gana por 4-0
    Given players "player1" and "player2" have started a two-player game
    When the current player starts the game for the oponent with word "python"
    When the current player tries the letter "a"
    When the current player tries the letter "b"
    When the current player tries the letter "c"
    When the current player tries the letter "d"
    When the current player tries the letter "e"
    When the current player tries the letter "f"
    Then the game result is "SE TE ACABARON LOS INTENTOS"
    Then the player "player2" has to start a round for "player1"
    When the current player starts the game for the oponent with word "secret"
    When the current player tries the letter "e"
    When the current player tries the letter "s"
    When the current player tries the letter "c"
    When the current player tries the letter "r"
    When the current player tries the letter "p"
    When the current player tries the letter "x"
    When the current player tries the letter "t"
    Then the game result is "ACERTASTE"
    Then the scores should be 4-0

  Scenario: Jugador 2 gana por 0-6
    Given players "player1" and "player2" have started a two-player game
    When the current player starts the game for the oponent with word "python"
    When the current player tries the letter "p"
    When the current player tries the letter "n"
    When the current player tries the letter "o"
    When the current player tries the letter "t"
    When the current player tries the letter "h"
    When the current player tries the letter "y"
    Then the game result is "ACERTASTE"
    Then the scores should be 0-6

  Scenario: Jugador 2 gana por 0-4
    Given players "player1" and "player2" have started a two-player game
    When the current player starts the game for the oponent with word "python"
    When the current player tries the letter "p"
    When the current player tries the letter "n"
    When the current player tries the letter "o"
    When the current player tries the letter "t"
    When the current player tries the letter "h"
    When the current player tries the letter "a"
    When the current player tries the letter "e"
    When the current player tries the letter "y"
    Then the game result is "ACERTASTE"
    Then the scores should be 0-4
