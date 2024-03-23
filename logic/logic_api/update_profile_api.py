from infra.infra_api.api_wrapper import OtakuAPI

class UpdateProfile(OtakuAPI):
   def __init__(self):
        super().__init__()
        self.json = None

   def profileUpdating(self, id, name, mail, password):
    self.json_data = {"id": id, "name": name, "email": mail, "password": password}
    self.response = self.request.put(f'{self.url[:-2]}api/users/profile/update/', json=self.json_data,
                                     headers=self.headersUpdate)
    return self.response