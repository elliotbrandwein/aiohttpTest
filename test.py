#!/usr/bin/python3
import json

import aiohttp_jinja2
import jinja2
from aiohttp import web
from jinja2 import Environment, PackageLoader
from aiohttp.test_utils import AioHTTPTestCase, unittest_run_loop
from aiohttp import web


env = Environment(loader=PackageLoader('templates'))
async def handler(request):
    context = {'name': 'elliot'}
    response = aiohttp_jinja2.render_template('simple.jinja2', request,context)
    response.headers['Content-Language'] = 'eng'
    return response

async def handle_post(request):
    x = await request.json()
    response = web.Response()
    output = x['name']
    output += ' hit the server'
    x['name'] = output
    response.text = json.dumps(x)
    response.content_type = 'application/json'
    return response

# app = web.Application()
# aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('/home/elliot/PycharmProjects/aiohttpTest/templates'))
# app.router.add_route('GET', '/', handler)
# app.router.add_route('POST', '/', handle_post)
# web.run_app(app)

# sample unit test from docs

class MyAppTestCase(AioHTTPTestCase):

    def get_app(self, loop):
        app = web.Application()
        aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('/home/elliot/PycharmProjects/aiohttpTest/templates'))
        app.router.add_route('GET', '/', handler)
        app.router.add_route('POST', '/', handle_post)
        return web.Application(loop=app)

    # the unittest_run_loop decorator can be used in tandem with
    # the AioHTTPTestCase to simplify running
    # tests that are asynchronous
    @unittest_run_loop
    async def test_example(self):
        request = await self.client.request("GET", "/")
        assert request.status == 200
        text = await request.text()
        assert "Hello, world" in text

    # a vanilla example
    def test_example(self):
        async def test_get_route():
            url = "/"
            resp = await self.client.request("GET", url, loop=loop)
            assert resp.status == 200
            text = await resp.text()
            assert "Hello, world" in text

        self.loop.run_until_complete(test_get_route())
