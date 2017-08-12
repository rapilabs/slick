from datetime import datetime

from aiohttp import web
from aiohttp_index import IndexMiddleware

messages = [{
    'username': 'shangxiao',
    'time': '11:46pm',
    'content': 'Welcome!',
}]

websockets = []


async def list_messages(request):
    return web.json_response(messages)

async def listen_messages(request):
    ws = web.WebSocketResponse()
    websockets.append(ws)
    await ws.prepare(request)
    print('opened websocket')
    async for msg in ws:
        if msg.type == aiohttp.WSMsgType.TEXT:
            if msg.data == 'close':
                await ws.close()
            else:
                await ws.send_str(msg.data + '/answer')
        elif msg.type == aiohttp.WSMsgType.ERROR:
            print('ws connection closed with exception %s' %
                  ws.exception())
    print('websocket connection closed')
    return ws

async def new_message(request):
    payload = await request.json()
    message = {
        'username': 'shangxiao',
        'time': datetime.now().strftime('%I:%M%p'),
        'content': payload['content'],
    }
    messages.append(message)
    for ws in websockets:
        ws.send_json(message)
    return web.Response()


app = web.Application(middlewares=(IndexMiddleware(),))
app.router.add_post('/messages', new_message)
app.router.add_get('/messages', list_messages)
app.router.add_get('/sub', listen_messages)
app.router.add_static('/js', '../frontend/dist')
app.router.add_static('/', '../frontend/public')
