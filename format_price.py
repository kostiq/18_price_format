import argparse
import re
import locale


def format_price(input_price):
    loc = locale.getlocale()
    try:
        locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
        price = str(input_price).replace(',', '.')
        price = float(price)
        group_price = locale.currency(price, grouping=True)
        without_sent = re.sub(r'\.00$', '', group_price)
        without_dollar = without_sent.replace('$', '')
        pretty_view = without_dollar.replace(',', ' ')
        locale.setlocale(locale.LC_ALL, loc)
        return pretty_view
    except ValueError:
        return 0
    finally:
        locale.setlocale(locale.LC_ALL, loc)
        

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--price', help="Input price", required=True)
    args = parser.parse_args()
    print (format_price(args.price))
