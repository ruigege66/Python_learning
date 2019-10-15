import threading
#引入异步io包
import asyncio
#使用协程
@asyncio.coroutine
def hello():
    print("Hello World!(%s)"%threading.current_thread())
    print("Start......(%s)"%threading.current_thread())
    yield from asyncio.sleep(5)
    print("Done.....(%s)"%threading.current_thread())
    print("Hello again!(%s)"%threading.current_thread())
#启动消息循环
loop = asyncio.get_event_loop()
#定义任务
tasks = [hello(),hello()]
#asyncio使用wait等待task执行完毕
loop.run_until_complete(asyncio.wait(tasks))
#关闭消息循环
loop.close()

import asyncio
from aiohttp import web

async def index(request):
    await asyncio.sleep(0.5)
    return web.Response(body=b"<h1>Index</h1>")

async def hello(request):
    await asyncio.sleep(0.5)
    text = "<h1>hello,%s!</h1>"%request.match_info["name"]
    return web.Response(body=text.encode("utf-8"))

async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route("GET","/",index)
    app.router.add_route("GET","/hellp/{name}",hello)
    srv = await loop.create_server(app.make_handler(),"127.0.0.1",8000)
    print("Server started at http://127.0.0.1:8000...")
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()

import time
from concurrent.futures import ThreadPoolExecutor

def return_future(msg):
    time.sleep(3)
    return msg

#创建一个线程池
pool = ThreadPoolExecutor(max_workers = 2)#参数是2，代表里面有两个线程干活
#往线程池里面加入两个task
f1 = pool.submit(return_future,"hello")
f2 = pool.submit(return_future,"world")
time.sleep(1)
#等待执行完毕
print(f1.done())
time.sleep(3)
print(f2.done())
#结果
print(f1.result())
print(f2.result())
