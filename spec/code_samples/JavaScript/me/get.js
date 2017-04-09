var FlatApi = require('flat-api');
FlatApi.ApiClient.instance.authentications.OAuth2.accessToken = process.env.FLAT_ACCESS_TOKEN;

flatAccountApi.getAuthenticatedUser(function(error, data, response) {
  if (error) {
    console.error(error);
  }
  else {
    console.log('Successfully retrieved user profile: ', data);
  }
});
