#! /bin/bash -e
# usage: scripts/update-redoc.sh version
VERSION=$1
cd web/js
rm -f redoc*

wget https://cdn.jsdelivr.net/npm/redoc@${VERSION}/bundles/redoc.standalone.js{,.map}
git add .
git commit -m "update(redoc): update to $VERSION"
