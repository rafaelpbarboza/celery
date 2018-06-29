from celery import Celery

app=Celery("example1",backend="amqp://guest@localhost",broken="amqp://localhost")

@app.task()
def tarea(file):
    f = file.objects.get(pk=id)
    print(f.name.name)