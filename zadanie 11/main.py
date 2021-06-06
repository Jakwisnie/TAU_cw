import logging

def add(x, y):

    return x + y


def subtract(x, y):

    return x - y


def multiply(x, y):

    return x * y


def divide(x, y):

    return x / y


num_1 = 20
num_2 = 10

add_result = add(num_1, num_2)
logging.info('Add: {} + {} = {}'.format(num_1, num_2, add_result))

sub_result = subtract(num_1, num_2)
logging.info('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))

mul_result = multiply(num_1, num_2)
logging.error('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))

div_result = divide(num_1, num_2)
logging.debug('Div: {} / {} = {}'.format(num_1, num_2, div_result))