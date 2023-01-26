import os

import requests
from picklecache import cache

@cache(os.path.join(os.path.expanduser('~'), '.company'))
def get(country_code, key, unhashed = None):
    '''
    country_code :: Open Corporates country code | None
    key :: str
    unhashed :: Maybe str

    If the company has a weird name, pass another thing as the key and the actual value as the unhashed.
    '''
    query = key if unhashed == None else unhashed
    baseurl = 'https://opencorporates.com/reconcile'
    url = baseurl if country_code == None else base_url + '/' + country_code
    params = {'query': query}
    return requests.get(url, params = params)


def reconcile(country_code, name):
    query = name.replace('/','%2F') # %2F so that pickle_warehouse doesn't make directories
    try:
        response = get(country_code, query)
    except OSError:
        response = get(country_code, hash(query), unhashed = query)
    if response.ok:
        return response.json().get('result')
    else:
        raise ValueError(response)
