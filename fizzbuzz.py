"""
Regras do Fizzbuzz

1- Se a posicao for multipla de 3: fizz
2- Se a posicao for multipla de 5: buzz
3- Se a posicao for multipla de 3 e 5: fizzbuzz
4. Para qualquer outra posicao fale o propio n

"""


# assertionError  = falhar no test
# qualquer outro error e porque o codigo quebrou


def multiple_of_5(num):
    return num % 5 == 0


def multiple_of_3(num):
    return num % 3 == 0


def robot(pos):
    say = str(pos)

    if multiple_of_3(pos) and multiple_of_5(pos):
        say = 'fizzbuzz'

    elif multiple_of_5(pos):
        say = 'buzz'

    elif multiple_of_3(pos):
        say = 'fizz'

    return say


if __name__ == '__main__':
    assert robot(1) == '1'
    assert robot(2) == '2'
    assert robot(4) == '4'

    assert robot(3) == 'fizz'
    assert robot(6) == 'fizz'
    assert robot(9) == 'fizz'

    assert robot(5) == 'buzz'
    assert robot(10) == 'buzz'
    assert robot(20) == 'buzz'

    assert robot(15) == 'fizzbuzz'
    assert robot(30) == 'fizzbuzz'
