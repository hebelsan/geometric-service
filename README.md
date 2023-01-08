# Geometric Service

This is library contains a REST API for geometric calculations (so far limited to basic polygon and plane intersection).

## Usage
TODO

```python


cut_polygon = polygon.cut(plane)
```

## Development

### Requirements
- python > 3.6
- python-venv

### Environment
The following env vars can be export and overwrite the defaults of the makefile:
```
export FLASK_APP=app.py
export FLASK_RUN_HOST=localhost
export FLASK_RUN_PORT=5000
export ALPHA=true
```

### Deploy and Test
- debug: `make debug`
- release: `make release`
- test: `make test`