<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure OAuth2 access token
Flat\APIClient\Configuration::getDefaultConfiguration()->setAccessToken($_ENV['FLAT_ACCESS_TOKEN']);

$api = new Flat\APIClient\Api\ScoreApi();

try {
    $result = $api->getUserScores();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ScoreApi->getUserScores: ', $e->getMessage(), PHP_EOL;
}
