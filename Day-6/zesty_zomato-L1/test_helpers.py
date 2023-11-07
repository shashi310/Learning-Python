import json

def send_json_request(client, method, url, data):
    return client.open(
        url,
        method=method,
        data=json.dumps(data),
        content_type='application/json'
    )
