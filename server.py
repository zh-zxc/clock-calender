#!/usr/bin/env python3
import http.server
import socketserver
import os
import sys

PORT = 3000

# 定义支持的MIME类型
class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        http.server.SimpleHTTPRequestHandler.end_headers(self)

    def guess_type(self, path):
        mimetype = http.server.SimpleHTTPRequestHandler.guess_type(self, path)
        if mimetype == 'application/octet-stream':
            if path.endswith('.js'):
                mimetype = 'text/javascript'
            elif path.endswith('.json'):
                mimetype = 'application/json'
        return mimetype

# 设置当前目录为服务器根目录
os.chdir(os.path.dirname(os.path.abspath(__file__)))

Handler = CustomHTTPRequestHandler

try:
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"\n服务器正在运行:")
        print(f"地址: http://localhost:{PORT}")
        print(f"按 Ctrl+C 停止服务器\n")
        httpd.serve_forever()
except KeyboardInterrupt:
    print("\n服务器已停止")
    sys.exit(0)
except Exception as e:
    print(f"服务器启动失败: {e}")
    sys.exit(1)