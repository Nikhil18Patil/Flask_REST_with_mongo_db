from flask import Blueprint, request, jsonify
from .models import User

main = Blueprint('main', __name__)

# Helper function to convert MongoDB document to JSON, ---> kind of serializer for me
def user_to_json(user):
    return {
        "id": str(user.id),
        "name": user.name,
        "email": user.email,
    }

@main.route('/users', methods=['GET'])
def get_all_users():
    try:
        users = User.objects()
        return jsonify(message="data retrieved successfully",data=[user_to_json(user) for user in users]), 200
    except Exception as e:
        return jsonify(error=f'{e}'), 500

@main.route('/users/<id>', methods=['GET'])
def get_user(id):
    try:
        user = User.objects.get(id=id)
        return jsonify(message=" user found successfully ",data=user_to_json(user)), 200
    except User.DoesNotExist:
        return jsonify({"error": "User not found"}), 404

@main.route('/users', methods=['POST'])
def create_user():
    try:
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')

        if not name or not email or not password:
            return jsonify({"error": "Name, email, and password are required"}), 400

        user = User(name=name, email=email)
        user.set_password(password)
        user.save()

        return jsonify(message="user data added successfully ",data=user_to_json(user)), 201
    except Exception as e:
        return jsonify(error=f'{e}'), 500

@main.route('/users/<id>', methods=['PUT'])
def update_user(id):
    
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    try:
        user = User.objects.get(id=id)
        if name:
            user.name = name
        if email:
            user.email = email
        if password:
            user.set_password(password)
        user.save()
        return jsonify(message="user data updated successfully",data=user_to_json(user)), 200
    except User.DoesNotExist:
        return jsonify({"error": "User not found"}), 404
       

@main.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    try:
        user = User.objects.get(id=id)
        user.delete()
        return jsonify({"message": "User deleted"}), 200
    except User.DoesNotExist:
        return jsonify({"error": "User not found"}), 404
