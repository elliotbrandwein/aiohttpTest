#!/usr/bin/python3
import json

import aiohttp
import asyncio
import aiohttp_jinja2
import jinja2
from aiohttp import web
from jinja2 import Environment, PackageLoader
env = Environment(loader=PackageLoader('templates'))
async def handle(request):
    #with open('simple.html', 'r') as file:
    #     x = file.read()
    #return web.Response(body=x.encode('utf-8'))

    #template = env.get_template('simple.html')
    #x = template.render()
    #print(x)
    return

async def handler(request):
    context = {'name': 'elliot'}
    response = aiohttp_jinja2.render_template('simple.jinja2', request,context)
    response.headers['Content-Language'] = 'eng'
    return response

async def handle_post(request):
    x = await request.json()
    response = web.Response()
    response.text = json.dumps(x)
    response.content_type = 'application/json'
    return response

app = web.Application()
aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('/home/elliot/PycharmProjects/aiohttpTest/templates'))
app.router.add_route('GET', '/', handler)
app.router.add_route('POST', '/', handle_post)

web.run_app(app)