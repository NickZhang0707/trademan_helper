import requests
import time

class BunningsAPI:
    def __init__(self, client_id,client_secret , sandbox=True):
        self.base_url = "https://developer.live.bunnings.com.au"
        self.auth_url = "https://authorisation.api.bunnings.com.au/connect/token"
        self.token = None
        self.token_expiry = None
        self.client_id = client_id  # 替换为实际的client_id
        self.client_secret = client_secret  # 替换为实际的client_secret
    
    def _get_token(self):
            """获取OAuth2访问令牌"""
            if self.token and time.time() < self.token_expiry:
                return self.token
                
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded'
            }
            
            body = {
                'client_id': self.client_id,
                'client_secret': self.client_secret,
                'grant_type': 'client_credentials'
            }

            try:
                response = requests.post(
                    self.auth_url,
                    headers=headers,
                    data=body,
                    timeout=10
                )
                response.raise_for_status()
                
                token_data = response.json()
                self.token = token_data["access_token"]
                self.token_expiry = time.time() + token_data.get("expires_in", 3600) - 300  # 提前5分钟过期
                return self.token
                
            except requests.RequestException as e:
                print(f"获取令牌失败: {e}")
                if hasattr(e, 'response') and e.response:
                    print(f"错误详情: {e.response.text}")
                raise

    def get_products(self, max_pages=5, page_size=50):
        """获取商品数据"""
        products = []
        headers = {
            "Authorization": f"Bearer {self._get_token()}",
            "Accept": "application/json"
        }
        
        for page in range(1, max_pages + 1):
            try:
                params = {"page": page, "pageSize": page_size}
                response = requests.get(
                    f"{self.base_url}/products/search",
                    headers=headers,
                    params=params,
                    timeout=10
                )
                response.raise_for_status()
                
                data = response.json()
                if not data.get("items"):
                    break
                    
                for product in data["items"]:
                    products.append({
                        "product_id": product.get("productId"),
                        "sku": product.get("sku"),
                        "name": product.get("name"),
                        "price": product.get("price", {}).get("value"),
                        "currency": product.get("price", {}).get("currency")
                    })
                
                time.sleep(0.5)  # 遵守速率限制
                
            except RequestException as e:
                print(f"获取第 {page} 页失败: {e}")
                if hasattr(e, 'response') and e.response:
                    print(f"错误响应: {e.response.text}")
                break
        
        return products


# 使用示例
if __name__ == "__main__":
    CLIENT_ID = "7Jwzt1hmyHimVNDbUWsO12Ie2oSFZKWo1VXxuLU66RXpoHxR"
    CLIENT_SECRET = "V0TKJ1jGjWjKzZsAGEmQAX3ai82INHPDfkEBKUEVx7A0nHlDDZkfZUUxKqagdiSN"
    # 初始化沙盒环境客户端
    client = BunningsAPI(CLIENT_ID, CLIENT_SECRET, sandbox=True)
    
    # 获取前200个商品
    products = client.get_products(max_pages=4, page_size=50)
    
    # 保存结果
    import json
    with open("bunnings_products.json", "w") as f:
        json.dump(products, f, indent=2)
    
    print(f"成功获取 {len(products)} 个商品数据")