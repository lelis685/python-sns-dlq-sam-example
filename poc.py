import uuid

job_names = ['job_1', 'job_2', 'job_3']


def handler():
    job_run = []
    for job_name in job_names:
        run_id = start_job(job_name)
        job_run.append(dict(job_name=job_name, run_id=run_id))

    print(job_run)
    print(list(map(lambda x: x['run_id'], job_run)))
    print(get_job_ids(job_run))

def start_job(job_name):
    print('start_job ', job_name)

    return str(uuid.uuid4())

def stop_job(job_name, run_ids):
    print('stop_job ', job_name, run_ids)

def get_job_ids(job_run: list):
    job_ids = []
    for job in job_run:
        job_ids.append(job['run_id'])
    return job_ids

if __name__ == '__main__':
    handler()
