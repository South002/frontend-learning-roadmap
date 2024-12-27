import socket
from urllib.parse import urlparse
from typing import Dict, Optional
import json

class HttpPostClient:
    def __init__(self):
        self.socket = None
        self.version = 'HTTP/1.1'
        self.headers: Dict[str, str] = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml',
            'Connection': 'close'
        }

    def post(self, url: str, data: dict, content_type: str = 'application/json') -> str:
        """发送POST请求
        
        Args:
            url: 目标URL
            data: POST的数据，字典格式
            content_type: 内容类型，默认为application/json
        """
        # 解析URL
        parsed_url = urlparse(url)
        host = parsed_url.hostname
        port = parsed_url.port or 80
        path = parsed_url.path or '/'
        
        print(f"正在连接到 {host}:{port}...")
        
        # 创建socket连接
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((host, port))
        print("连接成功!")
        
        # 设置Host和Content-Type头部
        self.headers['Host'] = host
        self.headers['Content-Type'] = content_type
        
        # 处理请求体
        if content_type == 'application/json':
            body = json.dumps(data)
        else:  # application/x-www-form-urlencoded
            body = '&'.join(f"{key}={value}" for key, value in data.items())
            
        # 设置Content-Length
        self.headers['Content-Length'] = str(len(body))
        
        # 构造请求
        request_line = f"POST {path} {self.version}\r\n"
        header_lines = [f"{k}: {v}" for k, v in self.headers.items()]
        header_str = '\r\n'.join(header_lines)
        request = f"{request_line}{header_str}\r\n\r\n{body}"
        
        print(f"\n发送的请求:\n{request}")
        
        # 发送请求
        self.socket.send(request.encode())
        
        # 接收响应
        response = []
        while True:
            data = self.socket.recv(1024)
            if not data:
                break
            response.append(data.decode())
            
        self.socket.close()
        return ''.join(response)

def test_json_post():
    """测试JSON POST请求"""
    client = HttpPostClient()
    
    # 准备测试数据
    test_data = {
        "name": "张三",
        "age": 25,
        "interests": ["编程", "读书", "运动"]
    }
    
    try:
        # 发送POST请求到httpbin（一个用于测试HTTP请求的服务）
        response = client.post(
            'http://httpbin.org/post',
            data=test_data,
            content_type='application/json'
        )
        
        print("\n收到的响应:")
        print("=" * 50)
        print(response)
        print("=" * 50)
        
    except Exception as e:
        print(f"请求失败: {e}")

def test_form_post():
    """测试表单 POST 请求"""
    client = HttpPostClient()
    
    # 准备表单数据
    form_data = {
        "username": "zhangsan",
        "password": "123456",
        "remember": "true"
    }
    
    try:
        response = client.post(
            'http://httpbin.org/post',
            data=form_data,
            content_type='application/x-www-form-urlencoded'
        )
        
        print("\n收到的响应:")
        print("=" * 50)
        print(response)
        print("=" * 50)
        
    except Exception as e:
        print(f"请求失败: {e}")

if __name__ == "__main__":
    print("测试1：JSON POST请求")
    test_json_post()
    
    print("\n\n测试2：表单 POST请求")
    test_form_post()