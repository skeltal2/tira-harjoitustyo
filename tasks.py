from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/index.py")

@task
def test(ctx):
    ctx.run("pytest")

@task
def pylint(ctx):
    ctx.run("pylint src/")

@task
def coverage(ctx):
    ctx.run("coverage report")