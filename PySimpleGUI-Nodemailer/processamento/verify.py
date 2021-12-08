def verify():
    from urllib import request
    import json
    
    print('[!] - Iniciando a verificação.')

    request = request.urlopen('http://127.0.0.1:5001/').read()
    js = json.loads(request)

    if js['verify']:
        return True
    else:
        return False
