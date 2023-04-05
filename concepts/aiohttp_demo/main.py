import aiohttp
from aiohttp import web
import asyncio
import os

routes = web.RouteTableDef()
webs = None
web_root = "concepts/aiohttp_demo"


@routes.get("/")
async def hello(request):
    return web.FileResponse(os.path.join(web_root, "index.html"))


@routes.get("/j")
async def hello(request):
    return web.json_response({"data": "hello"})


@routes.get("/ws")
async def websocket_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)
    sid = request.rel_url.query.get('clientId', '')
    print(sid)

    async for msg in ws:
        if msg.type == aiohttp.WSMsgType.TEXT:
            if msg.data == 'close':
                await ws.close()
                print("oh, closed")
            else:
                print(msg.data)
                await ws.send_str(msg.data + '/answer')
        elif msg.type == aiohttp.WSMsgType.ERROR:
            print('ws connection closed with exception %s' %
                  ws.exception())

    print('websocket connection closed')
    return ws

if __name__ == '__main__':
    app = web.Application()  # 创建应用
    app.add_routes(routes)  # 添加路由
    web.run_app(app, host="127.0.0.1", port=8080)  # 运行服务器
    print("hello")
