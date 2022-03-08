from invoke import task

@task(optional=["no_ui"])
def start(ctx, no_ui=False):
    if no_ui:
        ctx.run("python src/index_t.py")
    else:
        ctx.run("python src/index_u.py")
    

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