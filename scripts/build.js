#!/usr/bin/env node
'use strict';
var Path = require('path');

require('shelljs/global');
set('-e');

mkdir('-p', 'web_deploy')

cp('-R', 'web/*', 'web_deploy/');

exec('pnpm run openapi bundle spec/openapi.yaml --format=json --output=web_deploy/openapi.json');
exec('pnpm run openapi bundle spec/openapi.yaml --output=web_deploy/openapi.yaml');
