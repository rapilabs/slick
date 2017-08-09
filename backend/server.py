from aiohttp import web
from aiohttp_index import IndexMiddleware


async def hello(request):
    return web.Response(text='Hello, world')


app = web.Application(middlewares=(IndexMiddleware(),))
app.router.add_static('/js', '../frontend/dist')
app.router.add_static('/', '../frontend/public')
