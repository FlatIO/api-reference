from pprint import pprint
import os

import flat_api
from flat_api.rest import ApiException

flat_api.configuration.access_token = os.environ['FLAT_ACCESS_TOKEN']

try:
    pprint(flat_api.AccountApi().get_authenticated_user())
except ApiException as e:
    print e
