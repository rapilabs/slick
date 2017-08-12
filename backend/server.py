import json
from base64 import urlsafe_b64decode
from datetime import datetime
from io import BytesIO

from aiohttp import WSMsgType, web
from aiohttp_index import IndexMiddleware
from aiohttp_session import get_session, setup
from aiohttp_session.cookie_storage import EncryptedCookieStorage
from cryptography import fernet

from generate_avatar import generate_avatar

messages = []
users = {}
websockets = []


async def list_messages(request):
    return web.json_response(messages)


async def listen_messages(request):
    ws = web.WebSocketResponse()
    websockets.append(ws)
    await ws.prepare(request)
    print('opened websocket')
    async for msg in ws:
        if msg.type == WSMsgType.TEXT:
            if msg.data == 'close':
                await ws.close()
            else:
                await ws.send_str(msg.data + '/answer')
        elif msg.type == WSMsgType.ERROR:
            print('ws connection closed with exception %s' %
                  ws.exception())
    print('websocket connection closed')
    return ws


async def new_message(request):
    session = await get_session(request)
    payload = await request.json()
    message = {
        'username': session['username'],
        'time': datetime.now().strftime('%I:%M%p'),
        'content': payload['content'],
    }
    messages.append(message)
    for ws in websockets:
        ws.send_json(message)
    return web.Response()


async def whoami(request):
    session = await get_session(request)
    if 'username' in session:
        return web.Response(body=json.dumps({
            'username': session['username']
        }))
    return web.Response(status=401)


async def register(request):
    payload = await request.json()
    if payload['username'] in users:
        return web.Response(status=400, body='Username taken')

    avatar = BytesIO()
    avatar_image = generate_avatar()
    avatar_image.save(avatar, format='PNG')
    user = {
        'avatar': avatar.getvalue(),
    }
    users[payload['username']] = user

    session = await get_session(request)
    session['username'] = payload['username']

    return web.Response()


def get_avatar(request):
    username = request.rel_url.query['username']
    if username in users:
        return web.Response(body=users[username]['avatar'], content_type='image/png')
    return web.Response(status=404)


app = web.Application(middlewares=(IndexMiddleware(),))
fernet_key = fernet.Fernet.generate_key()
secret_key = urlsafe_b64decode(fernet_key)
setup(app, EncryptedCookieStorage(secret_key))

app.router.add_post('/messages', new_message)
app.router.add_get('/messages', list_messages)
app.router.add_get('/sub', listen_messages)
app.router.add_get('/whoami', whoami)
app.router.add_post('/register', register)
app.router.add_get('/avatar', get_avatar)
app.router.add_static('/js', '../frontend/dist')
app.router.add_static('/', '../frontend/public')
