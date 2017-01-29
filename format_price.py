import argparse
import re
import locale


def format_price(input_price):
    try:
        loc = locale.getlocale()
        locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

        price = str(input_price).replace(',', '.')

        price = float(price)
        price = locale.currency(price, grouping=True)
        price = re.sub(r'\.00$', '', price)
        price = price.replace('$', '')
        price = price.replace(',', ' ')
        locale.setlocale(locale.LC_ALL, loc)
        return price
    except ValueError:
        print ('Please, input number!')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--price', help="Input price", required=True)
    args = parser.parse_args()
    print (format_price(args.price))
