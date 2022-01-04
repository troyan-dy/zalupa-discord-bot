from aiohttp import web


async def hello(request):
    return web.Response(text="Hello, world")


app = web.Application()
app.add_routes([web.get("/", hello)])
health_check = web._run_app(app)
