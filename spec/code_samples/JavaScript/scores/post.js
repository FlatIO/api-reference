var request = require('request');
var FlatApi = require('flat-api');

FlatApi.ApiClient.instance.authentications.OAuth2.accessToken = process.env.FLAT_ACCESS_TOKEN;

var scoreToImport = 'https://gist.githubusercontent.com/gierschv/938479bec2bbe8c39eebbc9e19d027a0/raw/2caa4fa312184412d0d544feb361f918869ceaa5/hello-world.xml';

// Download a MusicXML "Hello World"
request(scoreToImport, function (error, response, body) {
  // Create the document and print the meta returned by the API
  new FlatApi.ScoreApi().createScore({
    title: 'Hello world',
    privacy: 'private',
    data: body
  }, function (error, data, response) {
    if (error) {
      console.error(error);
    }
    else {
      console.log('Successfully create the document:', data);
    }
  });
});
