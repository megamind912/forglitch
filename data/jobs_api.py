from flask import Blueprint, jsonify, make_response, request

from . import db_session
from .jobs import Jobs

blueprint = Blueprint(
    'jobs_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/jobs')
def get_jobs():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return jsonify(
        {
            'jobs':
                [item.to_dict(only=('id', 'job', 'team_leader', 'work_size',
                                    'collaborators', 'start_date', 'end_date',
                                    'is_finished'))
                 for item in jobs]
        }
    )


@blueprint.route('/api/jobs/<int:jobs_id>', methods=['GET'])
def get_one_jobs(jobs_id):
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).get(jobs_id)
    if not jobs:
        return make_response(jsonify({'error': 'Not found'}), 404)
    return jsonify(
        {
            'job': jobs.to_dict(only=('id', 'job', 'team_leader', 'work_size',
                                      'collaborators', 'start_date', 'end_date',
                                      'is_finished'))
        }
    )


@blueprint.route('/api/jobs', methods=['POST'])
def create_jobs():
    if not request.json:
        return make_response(jsonify({'error': 'Empty request'}), 400)
    elif not all(key in request.json for key in ['team_leader', 'job', 'collaborators']):
        return make_response(jsonify({'error': 'Bad request'}), 400)
    db_sess = db_session.create_session()
    if 'id' in request.json:
        jobs = db_sess.query(Jobs).get(request.json['id'])
        if jobs:
            return make_response(jsonify({'error': 'Jobs_id exists'}), 400)
    jobs = Jobs(
        team_leader=request.json['team_leader'],
        job=request.json['job'],
        collaborators=request.json['collaborators']
    )
    if 'work_size' in request.json:
        jobs.work_size = request.json['work_size']
    if 'is_finished' in request.json:
        jobs.is_finished = request.json['is_finished']
    db_sess.add(jobs)
    db_sess.commit()
    return jsonify({'id': jobs.id})


@blueprint.route('/api/jobs/<int:jobs_id>', methods=['DELETE'])
def delete_jobs(jobs_id):
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).get(jobs_id)
    if not jobs:
        return make_response(jsonify({'error': 'Not found'}), 404)
    db_sess.delete(jobs)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/jobs/<int:job_id>', methods=['POST'])
def edit_jobs(job_id):
    if not request.json:
        return make_response(jsonify({'error': 'Empty request'}), 400)
    elif not all(key in request.json for key in ['id', 'team_leader', 'job', 'collaborators']):
        return make_response(jsonify({'error': 'Bad request'}), 400)
    db_sess = db_session.create_session()
    jobs = Jobs(
        id=request.json['id'],
        team_leader=request.json['team_leader'],
        job=request.json['job'],
        collaborators=request.json['collaborators']
    )
    if 'work_size' in request.json:
        jobs.work_size = request.json['work_size']
    if 'is_finished' in request.json:
        jobs.is_finished = request.json['is_finished']
    print(jobs)
    job_to_edit = db_sess.query(Jobs).filter(Jobs.id == job_id).first()
    if not job_to_edit:
        return make_response(jsonify({'error': 'Not found'}), 404)
    job_to_edit.id = jobs.id
    job_to_edit.job = jobs.job
    job_to_edit.team_leader = jobs.team_leader
    job_to_edit.collaborators = jobs.collaborators
    job_to_edit.work_size = jobs.work_size
    job_to_edit.is_finished = jobs.is_finished
    db_sess.commit()
    return jsonify({'id': job_to_edit.id})
