def app(environ, start_response):
    status = '200 OK'
    headers = [
        ('Content-Type', 'text/plain; charset=utf-8')
    ]
    start_response(status, headers)
    print('\n@1@', type(environ['QUERY_STRING']), environ['QUERY_STRING'], '\n')
    #return [(param + '\n').encode('utf-8') for param in environ['QUERY_STRING']]
    return [environ['QUERY_STRING'].replace('&', '\n').encode('utf-8')]
