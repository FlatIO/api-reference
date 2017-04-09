var FlatApi = require('flat-api');
FlatApi.ApiClient.instance.authentications.OAuth2.accessToken = process.env.FLAT_ACCESS_TOKEN;

// List the scores for the current authenticated user ("me"):
new FlatApi.ScoreApi().getUserScores('me', {}, function (error, data, response) {
  if (error) {
    console.error(error);
  }
  else {
    console.log('Successfully create the document:', data);
  }
});
