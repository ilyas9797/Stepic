def app(environ, start_response):
    status = '200 OK'
    headers = [
        ('Content-Type', 'text/plain')
    ]
    start_response(status, headers)
    return [(param + '\r\n').encode('utf-8') for param in environ['QUERY_STRING']]
