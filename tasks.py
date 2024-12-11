from invoke import task

@task(aliases=['i'])
def install_dependencies(c):
    """Install project dependencies."""
    c.run("pip install -e .[dev]")

@task(aliases=['t'])
def run_tests(c):
    """Run the test suite."""
    c.run("pytest")

@task(aliases=['l'])
def lint(c):
    """Run linters."""
    c.run("ruff check .")

@task(aliases=['f'])
def format_code(c):
    """Format the code."""
    c.run("ruff check --fix .")

@task(aliases=['s'])
def setup(c):
    """Setup the development environment."""
    install_dependencies(c)
    lint(c)
    run_tests(c)

@task(aliases=['b'])
def build_image(c, name="fastapi-reference", tag="latest"):
    """Build the Docker image."""
    c.run(f"docker build -t {name}:{tag} .")

@task(aliases=['r'])
def run_image(c, name="fastapi-reference", tag="latest"):
    """Run the Docker image."""
    c.run(f"docker run -p 8000:8000 {name}:{tag}")

@task(aliases=['p'])
def push_image(c, name="fastapi-reference", tag="latest"):
    """Push the Docker image to the container registry."""
    c.run(f"docker push {name}:{tag}")

@task(aliases=['d'])
def deploy(c):
    """Deploy the application to Kubernetes."""
    c.run("kubectl apply -f k8s/deployment.yaml")
    c.run("kubectl apply -f k8s/service.yaml")