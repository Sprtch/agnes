import yaml
from xmlrpc.client import ServerProxy
from argparse import ArgumentParser
import os

CONFIG = "identifiers.yaml"  # yaml file
FIELD = ['id', 'name']  # name of the fields of the db odoo that we want to fetch


def connections_db(url, db, username, api_key):
    common = ServerProxy('{}/xmlrpc/2/common'.format(url))
    uid = common.authenticate(db, username, api_key, {})
    return uid


def get_articles_list(url, db, uid, api_key):
    models = ServerProxy('{}/xmlrpc/2/object'.format(url))
    products = models.execute_kw(db, uid, api_key, 'product.product', 'search_read', [[]], {'fields': FIELD})
    return products


def read_yaml_config(filename):
    try:
        with open(filename, "r") as stream:
            config = yaml.safe_load(stream)
    except yaml.YAMLError:
        config = False
    return config


def read_command_line(parser):
    parser.add_argument("yaml_filename", help="name of the yaml configuration file", nargs='?', default=CONFIG)
    args = parser.parse_args()
    filename = args.yaml_filename
    dir_path = os.path.dirname(os.path.realpath(__file__))
    return dir_path + '/' + filename


def get_args(parser):
    filename = read_command_line(parser)
    args = read_yaml_config(filename)
    return args


def main():
    parser = ArgumentParser()
    args = get_args(parser)
    url, db, username, api_key = args.values()
    uid = connections_db(url, db, username, api_key)
    articles_list = get_articles_list(url, db, uid, api_key)
    return articles_list


if __name__ == "__main__":
    articles_list = main()
