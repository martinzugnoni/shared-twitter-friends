import os
import json
from itertools import permutations, combinations

import twitter
from flask import Flask, render_template


app = Flask(__name__)
api = twitter.Api(
    # don't have an API key? check https://apps.twitter.com/

    consumer_key='YOUR_CONSUMER_KEY',
    consumer_secret='YOUR_CONSUMER_SECRET',
    access_token_key='YOUR_ACCESS_TOKEN_KEY',
    access_token_secret='YOUR_ACCESS_TOKEN_SECRET',
    sleep_on_rate_limit=True)


ACCOUNTS = [
    'santiagobasulto',
    'martinzugnoni',
    'ivanzugnoni',
    'yosoymatias',
    'jperelli',
    'bruno_dimartino',

    # add more friends here.
]
FOLLOWERS_CACHE = {}


@app.route('/', methods=['GET'])
def shared_followers():
    # warm up followers cache.
    # requesting Twitter followers (depending on the amount) might be very slow
    # save them in a local cache to avoid successive requests of the same data.
    for account in ACCOUNTS:
        if not account in FOLLOWERS_CACHE:
            FOLLOWERS_CACHE[account] = api.GetFollowerIDs(screen_name=account)

    data = []
    for i in range(1, len(ACCOUNTS) + 1):
        # compute combinations of all accounts listed above.
        # the result should look something like:
        #    ('santiagobasulto',)
        #    ('santiagobasulto', 'martinzugnoni')
        #    ('santiagobasulto', 'martinzugnoni', 'ivanzugnoni')
        #    ('santiagobasulto', 'martinzugnoni', 'ivanzugnoni', 'yosoymatias')
        #    ...
        for comb in combinations(ACCOUNTS, i):
            sets = [set(FOLLOWERS_CACHE[account]) for account in comb]
            # when the set contains more than one account, compute the followers
            # intersection. Otherwise count the amount of followers it has.
            if len(sets) > 1:
                intersec = sets[0].intersection(*sets[1:])
                data.append({'sets': list(comb), 'size': len(intersec)})
            else:
                data.append({'sets': list(comb), 'size': len(sets[0])})

    return render_template('venn_friends.html', data=data)


if __name__ == '__main__':
    app.debug = True
    host = os.environ.get('IP', '0.0.0.0')
    port = int(os.environ.get('PORT', 8080))
    app.run(host=host, port=port)
