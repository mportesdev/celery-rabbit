from .celery import app


@app.task
def power_sum(collection, power):
    return sum(item ** power for item in collection)


@app.task(ignore_result=True)
def write_to_text_file(value, filename):
    with open(filename, "a") as f:
        print(value, file=f)
