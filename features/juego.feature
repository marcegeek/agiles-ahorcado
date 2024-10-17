Feature: Juego Simple

  Scenario: Iniciar un nuevo juego
    Given I have started the game with a valid word "python"
    Then I should see the progress "______"

  Scenario: Adivinar una letra correcta
    Given I have started the game with a valid word "python"
    When I guess the letter "p"
    Then I should see the progress "p_____"

  Scenario: Adivinar una letra incorrecta
    Given I have started the game with a valid word "python"
    When I guess the letter "z"
    Then the remaining attempts should be 5

  Scenario: Adivinar una palabra incorrecta
    Given I have started the game with a valid word "python"
    When I guess the word "java"
    Then the remaining attempts should be 4

  Scenario: Perder el juego
    Given I have started the game with a valid word "python"
    When I guess the letter "a"
    When I guess the letter "b"
    When I guess the letter "c"
    When I guess the letter "d"
    When I guess the letter "e"
    When I guess the letter "f"
    Then the remaining attempts should be 0
    Then the game result should be "SE TE ACABARON LOS INTENTOS"
