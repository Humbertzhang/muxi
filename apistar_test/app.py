from apistar import App, Route

def hello(name=None) -> dict :
    if name is None:
        return {'msg': 'Hello, World'}
    return {'msg': 'Hello, %s!' % name}

routes = [
    Route('/', method = 'GET', handler=hello)        
]

app = App(routes=routes)

if __name__ == '__main__':
    app.serve('127.0.0.1', 5000, debug = True)
