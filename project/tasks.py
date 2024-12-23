from .celery import app


@app.task
def power_sum(collection, power):
    return sum(item ** power for item in collection)
