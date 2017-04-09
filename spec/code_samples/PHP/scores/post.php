<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure OAuth2 access token
Flat\APIClient\Configuration::getDefaultConfiguration()->setAccessToken($_ENV['FLAT_ACCESS_TOKEN']);

$musicXml = file_get_contents('https://gist.githubusercontent.com/gierschv/938479bec2bbe8c39eebbc9e19d027a0/raw/2caa4fa312184412d0d544feb361f918869ceaa5/hello-world.xml');

try {
    $body = new \Flat\APIClient\Model\ScoreCreation();
    $body->setTitle('Hello world');
    $body->setPrivacy('private');
    $body->setData($musicXml);

    $scoreApi = new Flat\APIClient\Api\ScoreApi();
    $result = $scoreApi->createScore($body);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ScoreApi->createScore: ', $e->getMessage(), PHP_EOL;
}
