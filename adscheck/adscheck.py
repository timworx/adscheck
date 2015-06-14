""" Grab a page and check for ads. """
import requests
import yaml

with open('networks.yml', 'r') as n_file:
    networks = yaml.load(n_file)

class DidIAd:
    """ 
    Checks a given URL for ads from known Ad networks.
    Returns network name if a network is found, else None
    """
    def __init__(self):
        """Does nothing for now"""
        pass        

    def format_url(self, url):
        if url[:7] != 'http://'
            return url = 'http://{}'.format(url)
        else:
            return url

    def get_page_text(self, url, **kwargs):
        """ Use requests to get the page """
        if kwargs:
            request = requests.get(url, **kwargs)
        else:
            request = requests.get(url)
        try:
            request
        except ConnectionError:
            raise
        else:
            return r.text

    def find_networks(self, data):
        """ Find Ad networks in page data """
        found_networks = {}
        found_networks_append = found_networks.append
        for network, id in networks.items():
            if data.find(id) < 0:
                continue
            else:
                found_networks_append(network)
        return found_networks

    def check(self, url):
        url = self.format_url(url)
        page = self.get_page_text(self.url)
        found_networks = self.find_networks(page)
        return found_networks