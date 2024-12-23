broker_url = "amqp://guest@localhost:5672"
result_backend = "rpc://"

include = ["project.tasks"]

broker_connection_retry_on_startup = True
