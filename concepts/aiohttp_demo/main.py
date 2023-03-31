import aiohttp
from aiohttp import web
import asyncio

routes = web.RouteTableDef()


@routes.get("/")
async def hello(request):
    return web.Response(text="Hello, world!")


@routes.get("/j")
async def hello(request):
    return web.json_response({"data": "hello"})

if __name__ == '__main__':
    app = web.Application()  # 创建应用
    app.add_routes(routes)  # 添加路由
    web.run_app(app)  # 运行服务器
