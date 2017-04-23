#! /bin/bash -e

cd web/js
rm -f redoc*
wget https://raw.githubusercontent.com/Rebilly/ReDoc/releases/dist/{redoc.min.js,redoc.min.map}
VERSION=$(grep 'Version: ' redoc.min.js | cut -d '"' -f 2)
git add .
git commit -m "update(redoc): update to $VERSION"
