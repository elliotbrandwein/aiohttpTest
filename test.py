#!/usr/bin/python3

import asyncio
import aiohttp
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

async def handlePost(request):
    response = aiohttp_jinja2.render_template('simple.jinja2', request, context)
    response.headers['Content-Language'] = 'eng'
    return response
app = web.Application()
aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('/home/elliot/PycharmProjects/aiohttpTest/templates'))
app.router.add_route('GET', '/', handler)
app.router.add_route('POST', '/', handlePost)

web.run_app(app)