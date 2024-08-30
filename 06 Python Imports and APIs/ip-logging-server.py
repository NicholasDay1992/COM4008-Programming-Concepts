from http.server import HTTPServer, BaseHTTPRequestHandler
import logging

# Set up logging
logging.basicConfig(filename='access.log', level=logging.INFO,
                    format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

class IPLoggingHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Log the IP address of the client
        client_ip = self.client_address[0]
        logging.info(f"Access from IP: {client_ip}")
        
        # Send a response
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"Hello, your access has been logged!")

def run_server(port=8000):
    server_address = ('', port)
    httpd = HTTPServer(server_address, IPLoggingHandler)
    print(f"Server running on port {port}")
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()
