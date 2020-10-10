from server.api.api_server import api_server

if __name__ == '__main__':
    api_server.run(host='0.0.0.0', port=5000, debug=True)