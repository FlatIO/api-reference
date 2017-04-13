## Flat API Specification

The public API specification is available in `swagger.yml`. You can find [a complete changelog on our API Documentation](https://flat.io/developers/docs/api/changelog.html).

Some indications if you want to make some changes:
- Before making large changes, please open an issue in this repository.
- Before opening a PR, please lint the YAML specification:

```bash
virtualenv .venv && source .venv/bin/activate
pip install -r requirements-dev.txt
./spec-lint.py
````
