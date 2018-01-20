from wsgiref.simple_server import make_server


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>hi weixinjiaaaa</h1>']


server = make_server('', 8000, application)
server.serve_forever()
