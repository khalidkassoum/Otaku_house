from infra.infra_api.api_wrapper import OtakuAPI


class SearchItem(OtakuAPI):
    def __init__(self):  # Constructor method to initialize class attributes
        super().__init__()
        self.json = None

    def add_item_to_cart(self,id_product):
        return self.api_get_request(f'{self.url[:-2]}api/products/{id_product}/')

    def search_ITEM(self, keyword):
        return self.api_get_request(f'{self.url[:-2]}api/products/?keyword={keyword}')
