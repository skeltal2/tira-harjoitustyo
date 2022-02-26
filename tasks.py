from invoke import task

@task(optional=["no_ui"])
def start(ctx, no_ui=False):
    if no_ui:
        ctx.run("python3 src/index.py")
    else:
        ctx.run("python3 src/ui.py")

#@task
#def start_ui(ctx):
#    ctx.run("python3 src/ui.py")

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