import socket
from urllib.parse import urlparse
from typing import Dict, List, Optional

class HttpClient:
    def __init__(self):
        self.url = None
        self.version = 'HTTP/1.1'
        self.socket = None
        self.response = ''
        self.headers: Dict[str, str] = {}
        self.body: List[str] = []
    
    def connect(self, url: str) -> None:
        """连接目标服务器"""
        # 解析URL
        self.url = urlparse(url)
        host = self.url.hostname
        port = self.url.port or 80
        
        print(f"正在连接到 {host}:{port}...")  # 添加调试信息
        
        # 创建socket连接
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.socket.connect((host, port))
            self.headers['Host'] = host
            print("连接成功!")  # 添加调试信息
        except socket.error as e:
            raise Exception(f"连接失败: {e}")

    def set_header(self, header_line: str) -> None:
        """设置请求头"""
        key, value = header_line.split(': ', 1)
        self.headers[key] = value

    def get(self, url: str) -> str:
        """发送GET请求"""
        self.connect(url)
        
        # 构造请求行
        path = self.url.path or '/'
        if self.url.query:  # 添加查询参数支持
            path = f"{path}?{self.url.query}"
            
        request_line = f"GET {path} {self.version}\r\n"
        
        # 构造请求头
        header_lines = [f"{k}: {v}" for k, v in self.headers.items()]
        header_str = '\r\n'.join(header_lines)
        
        # 组装完整请求
        request = f"{request_line}{header_str}\r\n\r\n"
        
        print(f"\n发送的请求:\n{request}")  # 添加调试信息
        
        # 发送请求
        self.socket.send(request.encode())
        
        # 接收响应
        response = []
        while True:
            try:
                data = self.socket.recv(1024)
                if not data:
                    break
                response.append(data.decode())
            except socket.error as e:
                print(f"接收数据时出错: {e}")
                break
            
        self.close()
        return ''.join(response)
    
    def close(self) -> None:
        """关闭连接"""
        if self.socket:
            self.socket.close()

# 测试代码
if __name__ == "__main__":
    # 创建客户端实例
    client = HttpClient()
    
    # 添加一些常用请求头
    client.set_header('User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36')
    client.set_header('Accept: text/html,application/xhtml+xml,application/xml')
    client.set_header('Connection: close')  # 建议添加这个头以确保服务器关闭连接
    
    # 发送GET请求
    try:
        # 可以测试不同的URL
        test_urls = [
            'http://example.com',
            'http://httpbin.org/get',
            'http://www.baidu.com'
        ]
        
        for url in test_urls:
            print(f"\n\n测试URL: {url}")
            response = client.get(url)
            print("\n收到的响应:")
            print("=" * 50)
            print(response[:500] + "...")  # 只打印前500个字符
            print("=" * 50)
            
    except Exception as e:
        print(f"请求失败: {e}") 