from config import *
import logging

logging.basicConfig(filename='logs.txt', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

convert_amount = float(input('How many dollars are you converting?'))


def dollars():
    output = dollar * convert_amount
    outputfinal = round(output, 2)
    print('$' + str(outputfinal))
    logging.info('$' + str(outputfinal))
    return


def pounds():
    output = pound * convert_amount
    outputfinal = round(output, 2)
    print('£' + str(outputfinal))
    logging.info('£' + str(outputfinal))
    return


def euros():
    output = euro * convert_amount
    outputfinal = round(output, 2)
    print('€' + str(outputfinal))
    logging.info('€' + str(outputfinal))
    return


def pesos():
    output = peso * convert_amount
    outputfinal = round(output, 2)
    print('₱' + str(outputfinal))
    logging.info('₱' + str(outputfinal))
    return


def cads():
    output = cad * convert_amount
    outputfinal = round(output, 2)
    print('C$' + str(outputfinal))
    logging.info('C$' + str(outputfinal))
    return


def rus():
    output = ru * convert_amount
    outputfinal = round(output, 2)
    print('C$' + str(outputfinal))
    logging.info('C$' + str(outputfinal))
    return


def auds():
    output = aud * convert_amount
    outputfinal = round(output, 2)
    print('A$' + str(outputfinal))
    logging.info('A$' + str(outputfinal))
    return


def yens():
    output = yen * convert_amount
    outputfinal = round(output, 2)
    print('¥' + str(outputfinal))
    logging.info('¥' + str(outputfinal))
    return


def none():
    print('would have converted nothing')
    logging.info('would have converted nothing')
    return


currencies = {
    0: none,
    1: dollars,
    2: pounds,
    3: euros,
    4: pesos,
    5: cads,
    6: rus,
    7: auds,
    8: yens
}
again = 'yes'
while again == 'yes':
    def switch(currency):
        currencies.get(currency, none)()
    convert = input('What would you like to convert?')
    (switch(int(convert)))
