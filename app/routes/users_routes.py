from flask import Blueprint, request, jsonify
from app.services.users_service import create_user, get_user_by_email, get_all_users, check_password

bp = Blueprint('users', __name__, url_prefix='/api/users')

@bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    role = data.get('role', 'user')
    mobile = data.get('mobile')

    # Check if user already exists
    if get_user_by_email(email):
        return jsonify({'message': 'User already exists'}), 400

    user = create_user(email, password, role, mobile)
    return jsonify({'message': 'User created successfully', 'user': {'email': user.email, 'role': user.role}}), 201

@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = get_user_by_email(email)
    if user and check_password(user, password):
        return jsonify({'message': f'Welcome, {user.email}!', 'role': user.role}), 200
    return jsonify({'message': 'Invalid credentials'}), 401

@bp.route('/', methods=['GET'])
def get_users():
    users = get_all_users()
    return jsonify([{'email': user.email, 'role': user.role, 'mobile': user.mobile} for user in users]), 200
