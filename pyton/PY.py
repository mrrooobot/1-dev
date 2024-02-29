import http.server
import socketserver
from urllib.parse import urlparse, parse_qs

secret_token = "sexo"

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        query_params = parse_qs(parsed_path.query)

        # Redireciona de "url/385146972" para "01722685/produto"
        if parsed_path.path == '/url/385146972':
            self.send_response(301)
            self.send_header('Location', '/01722685/produto')
            self.end_headers()
            return

        # Verificação do token para acessar "01722685/produto"
        if parsed_path.path == '/01722685/produto':
            if 'token' in query_params and query_params['token'][0] == secret_token:
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'Acesso autorizado a 01722685/produto!')
                return
            else:
                self.send_response(403)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'Acesso não autorizado. Forneça um token válido para 01722685/produto.')
                return

      
        super().do_GET()

# Define a porta para o servidor
port = 8000

# Inicia o servidor
with socketserver.TCPServer(("", port), MyHandler) as httpd:
    print(f"Servidor iniciado na porta {port}")
    httpd.serve_forever()