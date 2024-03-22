from infra.infra_api.api_wrapper import OtakuAPI


class OtakuReviewItem(OtakuAPI):
   def __init__(self):  # Constructor method to initialize class attributes
        super().__init__()
        self.json = None

   def get_product_page(self,id_product):
       return self.api_get_request(f'{self.url}api/products/{id_product}/')
   def choosing_product(self,rate,review_txt,id_product):
        self.json = {"rating": rate, "comment": review_txt}

        self.response = self.request.post(f'{self.url[:-2]}api/products/{id_product}/reviews/', json=self.json,headers=self.headers)
        return self.response