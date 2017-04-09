from pprint import pprint
import os, urllib2

import flat_api
from flat_api.rest import ApiException

SCORE_TO_IMPORT='https://gist.githubusercontent.com/gierschv/938479bec2bbe8c39eebbc9e19d027a0/raw/2caa4fa312184412d0d544feb361f918869ceaa5/hello-world.xml'

flat_api.configuration.access_token = os.environ['FLAT_ACCESS_TOKEN']

try:
    # Download a MusicXML "Hello World"
    hello_world = urllib2.urlopen(SCORE_TO_IMPORT).read()

    # The new score meta, including the MusicXML file as `data`
    new_score = flat_api.ScoreCreation(
        title='Hello World',
        privacy='private',
        data=hello_world
    )

    # Create the document and print the meta returned by the API
    pprint(flat_api.ScoreApi().create_score(new_score))
except (ApiException, urllib2.HTTPError) as e:
    print e
