from invoke import task

@task(optional=["no_ui"])
def start(ctx, no_ui=False):
    ctx.run("python3 src/index.py")

@task
def pylint(ctx):
    ctx.run("pylint src/")

@task
def test(ctx):
    ctx.run("coverage run -m pytest")

@task
def coverage(ctx):
    ctx.run("coverage report")
    ctx.run("coverage html")

@task
def performance(ctx):
    ctx.run("python3 src/performance/performance.py")