from flask import Flask, request
import uuid
import base64
import json

app = Flask(__name__)

@app.route('/account/login', methods=['POST'])
def login():
    username = request.values.get('username')
    psswd = request.values.get('password')
    return json_encode({'account': {'id': to_base64(uuid.uuid4()), 'authentication': to_base64(uuid.uuid4())}})


@app.route('/account/register', methods=['POST'])
def register():
    name = request.values.get('name')
    username = request.values.get('username')
    psswd = request.values.get('password')
    return json_encode({'account': {'id': to_base64(uuid.uuid4()), 'authentication': to_base64(uuid.uuid4())}})


@app.route('/users/<uid>', methods=['GET'])
def get_user(uid):
    uid = uuid.UUID(bytes=to_bytes(uid))
    return json_encode({
            'id': to_base64(uid.bytes),
            'name': 'Leandro',
            'username': 'leandro'
        })


@app.route('/users', methods=['GET'])
def get_users():
    users = [
        {
            'id': str(uuid.uuid4()),
            'name': 'Gustavo',
            'username': 'gustavo'
        },
        {
            'id': str(uuid.uuid4()),
            'name': 'André',
            'username': 'andre'
        }
    ]
    if users is not None and len(users) > 0:
        for mp in users:
            uid = uuid.UUID(mp['id'])
            encoded = to_base64(uid.bytes)
            mp['id'] = encoded
        return json_encode({'users': users})
    return json_encode({'error': 'no_users_found', 'message': 'Nenhum usuário foi encontrado.'})


@app.route('/gen', methods=['GET'])
def gen():
    uid = uuid.uuid4()
    code = to_base64(uid.bytes)
    return json_encode({'id': code})


@app.route('/', methods=['GET'])
def home():
    return 'Apollo API<br>Version 1.0.0<br>© 2021'


if __name__ == '__main__':
    app.run()


def json_encode(data):
    return json.dumps(data, ensure_ascii=False).encode('utf8')


def to_base64(bt):
    return base64.urlsafe_b64encode(bt).decode('utf8').rstrip("=")


def to_bytes(bs):
    return base64.urlsafe_b64decode(bs + '==')
