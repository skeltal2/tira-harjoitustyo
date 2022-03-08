from invoke import task, Responder

@task(optional=["no_ui"])
def start(ctx, no_ui=False):
    if no_ui:
        r = Responder(pattern=r"ui", response="N\n")
    else:
        r = Responder(pattern=r"ui", response="Y\n")
    ctx.run("python src/index.py",watchers=[r])

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
def perf(ctx):
    ctx.run("python src/performance.py")