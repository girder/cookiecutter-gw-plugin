from girder_worker.app import app
from girder_worker.utils import girder_job

# TODO: Fill in the function with the correct argument signature
# and code that performs the task.
@girder_job(title='Example Task')
@app.task(bind=True)
def example_task(self):
    pass
