# Geometric Service

This is library contains a REST API for geometric calculations (so far limited to basic polygon and plane intersection).

## Usage
```bash
docker build -t geometric-service .
docker run -p 5000:5000 geometric-service
```
Send a request to http://localhost:5000/cut with the following body:
```json
{
    "polygon": {
        "vertices": [[-0.5, 0, 0], [0, 1, 0], [0.5, 0, 0]]
    },
    "plane": {
        "point": [0, 0.5, 0],
        "normal": [0, 1, 0]
    }
}
```

## Development

### Requirements
- python > 3.6
- python-venv

### Environment
The following env vars can be export and overwrite the defaults of the makefile:
```
export ALPHA=true
export HOST=localhost
export PORT=5000
export SYSTEM_PYTHON=python3
```

### Deploy and Test
- debug: `make debug`
- release: `make release`
- test: `make test`