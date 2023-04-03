from helpers import get_rand_month, get_rand_year

def make_person(name, favColor):
    return {
        'name': name,
        'favColor': favColor,
        'birthYear': get_rand_year(),
        'birthMonth': get_rand_month()
    }