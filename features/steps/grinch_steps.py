from behave import given, when, then
from pages.imdb_page import ImdbPage


@given('usuario ingresa a "{url}"')
def step_impl(context, url):
    context.imdb_page = ImdbPage(context.page)
    context.imdb_page.go_to(url)

@when('usuario llena "{campo}" campo con "{valor}"')
def step_impl(context, campo, valor):
    locator_func = context.imdb_page.get_field_by_enum(campo)
    locator = locator_func(context.page)
    locator.fill(valor)

@when("usuario clica en primera pelicula de la lista")
def step_impl(context):
    locator_func = context.imdb_page.get_field_by_enum("first_movie_list")
    locator = locator_func(context.page)
    locator.click()
    context.page.wait_for_load_state("networkidle")

@when('usuario clica en "{campo}"')
def step_impl(context, campo):
    locator_func = context.imdb_page.get_field_by_enum(campo)
    locator = locator_func(context.page)
    locator.click()

@then('director debe ser "{expected_director}"')
def step_impl(context, expected_director):
    locator_func = context.imdb_page.get_field_by_enum("director")
    director_locator = locator_func(context.page)
    director_text = director_locator.inner_text()
    assert expected_director in director_text, f"Se esperaba '{expected_director}' pero se encontró '{director_text}'"

@then('calificacion debe ser mayor a "{min_rating}"')
def step_impl(context, min_rating):
    locator_func = context.imdb_page.get_field_by_enum("rating")
    rating_locator = locator_func(context.page)
    rating_text = rating_locator.inner_text()
    rating = float(rating_text)
    min_rating_float = float(min_rating)
    assert rating > min_rating_float, f"La calificación {rating} no es mayor a {min_rating_float}"
    context.imdb_page.take_screenshot("rating_check")
