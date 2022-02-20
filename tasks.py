from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/index.py")

@task
def start_ui(ctx):
    ctx.run("python3 src/ui.py")

#@task
#def test(ctx):
#    ctx.run("pytest")

@task
def pylint(ctx):
    ctx.run("pylint src/")

@task
def test(ctx):
    ctx.run("coverage run -m pytest")

@task
def coverage(ctx):
    ctx.run("coverage report")

@task
def performance(ctx):
    ctx.run("python3 src/performance.py")