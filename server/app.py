import os
from flask import Flask, jsonify, request
from flask_cors import CORS

from rq import Queue
from rq.job import Job
from rq.exceptions import NoSuchJobError
from redis import Redis

from .auth import gsuite_authenticate, current_user

redis_url = os.getenv('REDIS_URL', 'redis://localhost:6379/')
redis_conn = Redis.from_url(redis_url)
q = Queue(connection=redis_conn)


# instantiate the app
app = Flask(__name__)
# app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

def _serialize_job(job):
    result = job.result
    _output_sep = '===BEGIN OF COMMAND OUTPUT==='
    if job.is_failed:
        print(job.exc_info)
        print(_output_sep in job.exc_info)
    if job.is_failed and _output_sep in job.exc_info:
        result = job.exc_info.split(_output_sep, 1)[-1]
    task = {
        'id': job.id,
        'status': job.get_status(),
        'enqueuedAt': job.enqueued_at,
        'startedAt': job.started_at,
        'endedAt': job.ended_at,
        'result': result,
    }
    return task


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/task/<task_id>', methods=['GET'])
@gsuite_authenticate
def task_status(task_id):
    user = current_user()
    try:
        job = Job.fetch(task_id, connection=redis_conn)
        print('Status: %s' % job.get_status())
        print(job.meta)
        if job.meta['sub'] != user['sub']:
            print('Error:', 'Subject of task and user do not match')
            raise NoSuchJobError()
        return jsonify(_serialize_job(job))
    except NoSuchJobError:
        return jsonify({
            'message': 'Task not found',
            'code': 404
        }), 404


@app.route('/task', methods=['POST'])
@gsuite_authenticate
def task_post():
    user = current_user()
    post_data = request.get_json()
    target_email = user['email']
    job = q.enqueue(
        'worker.imapsync.imapsync',
        kwargs={
            'source_username': post_data.get('sourceEmail'),
            'source_password': post_data.get('sourcePassword'),
            'target_email': target_email,
        },
        meta={
            'sub': user['sub'],
        },
        job_timeout='4h',
        result_ttl=86400
    )
    task = _serialize_job(job)
    task['task_result'] = None
    return jsonify(task)


if __name__ == '__main__':
    app.run()
