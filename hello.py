def app(environ, start_response):
    status = '200 OK'
    headers = [
        ('Content-Type', 'text/plain')
    ]
    start_response(status, headers)
    print('\n@1@', environ['QUERY_STRING'], '\n')
    return iter([(param + '\r\n').encode('utf-8') for param in environ['QUERY_STRING']])
