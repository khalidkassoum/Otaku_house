from infra.infra_api.api_wrapper import OtakuAPI
class PlaceOrder(OtakuAPI):
   def __init__(self):
        super().__init__()
        self.json = None

   def get_product_page(self,id_product):
       return self.api_get_request(f'{self.url}api/products/{id_product}/')

   def place_Order(self):
        #self.json = {"itemsPrice":"0.00","orderItems":[],"paymentMethod":"payPal","adress":"sakhnin","city":"sakhnin","postalCode":308100,"shippingPrice":10.00,"taxPrice":0.00,"totalPrice":10.00}
        self.json={"orderItems":[{"product":21,"name":"Bleach - Ichigo Kurosaki Honor T-Shirt","image":"/media/images/ichigo_shirt.jpg","price":"1499.00","countInStock":74,"qty":1}],"shippingAddress":{"address":"sakhnin","city":"sakhnin","postalCode":"308100","country":"israel"},"paymentMethod":"PayPal","itemsPrice":"1499.00","shippingPrice":"0.00","taxPrice":"122.92","totalPrice":"1621.92"}
        self.response = self.request.post(f'{self.url[:-2]}api/orders/add/', json=self.json,headers=self.headers2)
        return self.response