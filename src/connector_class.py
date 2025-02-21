from abc import ABC, abstractmethod
import requests


class BaseAPIConnector(ABC):

    @abstractmethod
    def get_openings(self, *args):
        """
        Abstract method for a get_data method.
        """
        pass


class HhAPIConnector(BaseAPIConnector):
    def __init__(self):
        """
        Initialize the HhAPIConnector.
        """
        self.endpoint_link: str = "https://api.hh.ru/vacancies"
        self.headers: dict = {"User-Agent": "HH-User-Agent"}
        self.body_params: dict = {"text": "", "page": 0, "per_page": 100, "only_with_salary": True}
        self.openings_dict: list[dict] = []
        self.response_status: list = []

    def __repr__(self):
        """
        Return a string representation of the HhAPIConnector instance.
        """
        return (f"{self.__class__.__name__}({self.endpoint_link}, {self.headers}, {self.body_params},"
                f" {self.openings_dict}, {self.response_status})")

    def get_openings(self, keyword: str) -> None:
        """
        Make a GET request with User's keyword in the request to the API endpoint and return
        the response data in python dict format.
        Result of the method is that obtained data recorded to the openings_dict attribute.
        Also processes possible errors
        """
        self.body_params["text"] = keyword if keyword else ""
        while self.body_params.get("page") != 20:
            response = requests.get(self.endpoint_link, headers=self.headers, params=self.body_params, timeout=20)
            self.response_status.append({self.body_params["page"]: response.status_code})
            response.raise_for_status()
            try:
                loaded_openings = response.json().get("items", [])
                if not loaded_openings:
                    self.openings_dict.append({})
                    return
            except ValueError:
                print("Некорректный ответ API, формат не соответствует json")
                return
            self.openings_dict.extend(loaded_openings)
            self.body_params["page"] += 1


if __name__ == "__main__":
    ex = HhAPIConnector()
    ex.get_openings("Python")
    print(ex.openings_dict)
