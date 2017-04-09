from pprint import pprint
import os

import flat_api
from flat_api.rest import ApiException

flat_api.configuration.access_token = os.environ['FLAT_ACCESS_TOKEN']

print flat_api.configuration.access_token

try:
    # `user` path parameter, `me` for the current user
    pprint(flat_api.UserApi().get_user_scores('me'))
except ApiException as e:
    print e
