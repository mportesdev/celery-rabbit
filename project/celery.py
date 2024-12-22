from celery import Celery

app = Celery("project")
app.config_from_object("celeryconfig")
