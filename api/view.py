import logging
def main(request):
    request_json = request.get_json()
    headers = {
        'Access-Control-Allow-Origin': '*'
    }
    if request.args and 'message' in request.args:
        logging.info(request.args.get('message'))
        logging.info('value is found in requests.args')
        return (request.args.get('message'), 200, headers)
    else:
        return ('Hello World!', 200, headers)