from flask import jsonify
from flask_restful import abort, Resource

from .users import User
from .reqparse_user import parser
from . import db_session


def abort_if_user_not_found(user_id):
    db_sess = db_session.create_session()
    user = db_sess.query(User).get(user_id)
    if not user:
        abort(404, message=f"User {user_id} not found")


class UsersResource(Resource):
    def get(self, user_id):
        abort_if_user_not_found(user_id)
        db_sess = db_session.create_session()
        user = db_sess.query(User).get(user_id)
        return jsonify({'user': user.to_dict(only=('surname', 'name', 'age',
                                                   'position', 'speciality',
                                                   'address', 'email', 'hashed_password'))})

    def delete(self, user_id):
        abort_if_user_not_found(user_id)
        db_sess = db_session.create_session()
        user = db_sess.query(User).get(user_id)
        db_sess.delete(user)
        db_sess.commit()
        return jsonify({'success': 'OK'})


class UsersListResource(Resource):
    def get(self):
        db_sess = db_session.create_session()
        users = db_sess.query(User).all()
        return jsonify({'users': [item.to_dict(only=('surname', 'name', 'age', 'position',
                                                     'speciality', 'address', 'email',
                                                     'hashed_password')) for item in users]})

    def post(self):
        args = parser.parse_args()
        db_sess = db_session.create_session()
        user = User(
            surname=args['surname'],
            name=args['name'],
            age=args['age'],
            position=args['position'],
            speciality=args['speciality'],
            address=args['address'],
            email=args['email']
        )
        user.set_password(args['hashed_password'])
        db_sess.add(user)
        db_sess.commit()
        return jsonify({'id': user.id})
