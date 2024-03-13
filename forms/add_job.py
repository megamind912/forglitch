from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class AddJobForm(FlaskForm):
    job = StringField('Название работы', validators=[DataRequired()])
    team_leader = IntegerField('Id руководителя', validators=[DataRequired()])
    work_size = IntegerField('Продолжительность', validators=[DataRequired()])
    collaborators = StringField('Список id исполнителей', validators=[DataRequired()])
    is_finished = BooleanField('Закончена?')
    submit = SubmitField('Добавить')
