from pprint import pprint
import os

import flat_api
from flat_api.rest import ApiException

configuration = flat_api.Configuration()
configuration.access_token = os.environ['FLAT_ACCESS_TOKEN']
flat_api_client = flat_api.ApiClient(configuration)
try:
    pprint(flat_api.AccountApi(flat_api_client).get_authenticated_user())
except ApiException as e:
    print(e)
