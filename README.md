# Flat OpenAPI Specification

[![Greenkeeper badge](https://badges.greenkeeper.io/FlatIO/api-reference.svg)](https://greenkeeper.io/)
[![Build Status](https://travis-ci.org/FlatIO/api-reference.svg?branch=master)](https://travis-ci.org/FlatIO/api-reference)

## Links

- Documentation(ReDoc): https://flat.io/developers/api/reference/
- Look full spec:
    + JSON https://flat.io/developers/api/reference/swagger.json
    + YAML https://flat.io/developers/api/reference/swagger.yaml
- Preview spec version for branch `[branch]`: https://flatio.github.io/api-reference/preview/[branch]

**Warning:** All above links are updated only after Travis CI finishes deployment

## Working on specification
### Install

1. Install [Node JS](https://nodejs.org/)
2. Clone repo and `cd`
    + Run `npm install`

### Usage

1. Run `npm start`
2. Checkout console output to see where local server is started. You can use all [links](#links) (except `preview`) by replacing https://flat.io/developers/api/reference/ with url from the message: `Server started <url>`
3. Make changes using your favorite editor or `swagger-editor` (look for URL in console output)
4. All changes are immediately propagated to your local server, moreover all documentation pages will be automagically refreshed in a browser after each change
5. Once you finish with the changes you can run tests using: `npm test`
6. Share you changes with the rest of the world by pushing to GitHub :smile:
