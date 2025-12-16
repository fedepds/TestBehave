Feature: Operacion Grinch

  Scenario: Validar Mi pobre angelito
    Given usuario ingresa a "https://www.imdb.com"
    When usuario llena "search_input" campo con "mi pobre angelito"
    And usuario clica en "search_button"
    And usuario clica en primera pelicula de la lista
    Then director debe ser "Chris Columbus"
    And calificacion debe ser mayor a "7.0"
