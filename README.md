# fastapi-reference-api

## Setup

Upgrade Pip

```shell
pip install --upgrade pip
```

Install Invoke

```shell
pip install invoke
```

Install the development dependencies

```shell
pip install -e .[dev]
```

Build and deploy the image

```shell
invoke build_image --tag v1.0
invoke push_image --tag v1.0
invoke deploy
```

A reference application for a FastAPI instance.


## References

- [Getting started with Testcontainers for Python](https://testcontainers.com/guides/getting-started-with-testcontainers-for-python/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Docker](https://www.docker.com/)
- [Testcontainers Python](https://testcontainers-python.readthedocs.io/en/latest/)
- [Testcontainers with FastAPI](https://lricardo.space/posts/seamless-containerized-tests-python/)
