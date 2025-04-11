from flask import Blueprint, request
from models.models import Task
from utils.db import db
import datetime 
from flask_jwt_extended import jwt_required

tasks_blueprint = Blueprint('tareas', __name__)

@tasks_blueprint.route('/tareas', methods=['GET', 'POST'])
@jwt_required()
def list_or_create_tasks():
    if request.method == 'POST':
        try:
            request_data = request.get_json() if request.is_json else request.form.to_dict()     
            description = request_data.get('description', '')       
            new_task = Task(request_data['title'], description, request_data['priority'], request_data['status'], request_data['expiration_time'])
            new_task.creation_time = datetime.datetime.now()
            db.session.add(new_task)
            db.session.commit()
            return {'message': 'Task created successfully'}, 201
        except KeyError as e:
            return {'message': f'Missing parameter: {str(e)}'}, 400
    elif request.method == 'GET':
        try:
            contacts = Task.query.all()
            if not contacts:
                return {'message':'No tasks found'}, 404
            return [task.to_dict() for task in contacts], 200
        except:
            return {'message':'Error retrieving tasks'}, 500
    else:
        return {'message':'Method not allowed'}, 405
    
@tasks_blueprint.route('/tareas/<id>', methods=['GET', 'PUT', 'DELETE'])
@jwt_required()
def single_task(id):
    if request.method == 'GET':
        try: 
            task = Task.query.get(id)
            if not task:
                return {'message':'Task not found'}, 404
            return task.to_dict(), 200
        except:
            return {'message': 'Error retrieving task'}, 500

    elif request.method == 'PUT':
        try:
            request_data = request.get_json() if request.is_json else request.form.to_dict()
            task = Task.query.get(id)
            if not task:
                return {'message':'Task not found'}, 404
            task.title = request_data['title']
            task.description = request_data['description']
            task.priority = request_data['priority']
            task.status = request_data['status']
            task.expiration_time = request_data['expiration_time']
            db.session.commit()
            return {'message':'Task updated successfully'}, 200
        except KeyError as e:
            return {'message':f'Missing parameter: {str(e)}'}, 400
        except:
            return {'message':'Error updating task'}, 500
    
    elif request.method == 'DELETE':
        try:
            task = Task.query.get(id)
            if not task:
                return {'message':'Task not found'}, 404
            db.session.delete(task)
            db.session.commit()
            return {'message':'Task deleted successfully'}, 200
        except:
            return {'message':'Error deleting task'}, 500
        
    else:
        return {'message':'Method not allowed'}, 405
    