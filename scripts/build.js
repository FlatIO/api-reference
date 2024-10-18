#!/usr/bin/env node
'use strict';

require('shelljs/global');
set('-e');

mkdir('-p', 'web_deploy')

cp('-R', 'web/*', 'web_deploy/');

exec('pnpm run openapi bundle ${API_SPEC_DIR_FILE:-spec/openapi.yaml} --output=web_deploy/openapi.json');
exec('pnpm run openapi bundle ${API_SPEC_DIR_FILE:-spec/openapi.yaml} --output=web_deploy/openapi.yaml');
