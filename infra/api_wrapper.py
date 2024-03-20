import requests
class ExamAPI:
    BASE_URL = "http://127.0.0.1:8000/#/"

    @staticmethod
    def get_exams():
        return requests.get(f"{ExamAPI.BASE_URL}")