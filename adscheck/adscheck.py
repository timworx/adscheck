""" Grab a page and check for ads. """
import os
import requests
import yaml

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))

def get_networks():
    with open(os.path.join(CURRENT_DIR, 'networks.yml'), 'r') as n_file:
        return yaml.load(n_file)

class DidIAd:
    """
    Checks a given URL for ads from known Ad networks.
    Returns network name if a network is found, else None
    """
    @staticmethod
    def format_url(url):
        """ Make sure url has http """
        if url[:7] != 'http://':
            return 'http://{}'.format(url)
        else:
            return url

    @staticmethod
    def get_page_text(url, **kwargs):
        """ Use requests to get the page """
        try:
            if kwargs:
                request = requests.get(url, **kwargs)
            else:
                request = requests.get(url)
        except requests.ConnectionError:
            raise
        else:
            return request.text

    @staticmethod
    def find_networks(data):
        """ Find Ad networks in page data """
        found_networks = []
        found_networks_append = found_networks.append
        for network, footprint in get_networks().items():
            if data.find(footprint) < 0:
                continue
            else:
                found_networks_append(network)
        return found_networks

    @classmethod
    def check(cls, url):
        """ Check the given url for ad_networks """
        ready_url = cls.format_url(url)
        page = cls.get_page_text(ready_url)
        found_networks = cls.find_networks(page)
        return found_networks
