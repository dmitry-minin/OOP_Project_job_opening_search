import requests
from src.connector_class import HhAPIConnector
import pytest


def test_hh_connector_init():
    """
    Test HhAPIConnector initializer
    """
    new_connector = HhAPIConnector()
    assert new_connector.endpoint_link == "https://api.hh.ru/vacancies"
    assert new_connector.headers == {"User-Agent": "HH-User-Agent"}
    assert new_connector.body_params == {"text": "", "page": 0, "per_page": 100, "only_with_salary": True}
    assert new_connector.openings_dict == []
    assert new_connector.response_status == []


def test_hh_connector_repr():
    """
    Test HhAPIConnector __repr__ method
    """
    new_connector = HhAPIConnector()
    assert str(new_connector) == (
        "HhAPIConnector(https://api.hh.ru/vacancies, {'User-Agent': 'HH-User-Agent'},"
        " {'text': '', 'page': 0, 'per_page': 100, 'only_with_salary': True}, [], [])"
    )


def test_get_openings_key_word(mock_api_success):
    new_connector = HhAPIConnector()
    new_connector.get_openings("")
    assert new_connector.body_params["text"] == ""


def test_get_openings_successful(mock_api_success):
    new_connector = HhAPIConnector()
    new_connector.body_params["page"] = 19
    new_connector.get_openings("Python")
    assert new_connector.openings_dict == [{"12": "Python dev"}, {"13": "Java dev"}]
    assert new_connector.response_status[-1][19] == 200



def test_get_data_incorrect_response(mock_api_incorrect_response, capsys):
    """
    Response is not in json format or missed.
    """
    new_connector = HhAPIConnector()

    new_connector.get_openings("Python")
    captured = capsys.readouterr()
    assert "Некорректный ответ API, формат не соответствует json" in captured.out
    assert new_connector.openings_dict == []
    assert new_connector.response_status[0][0] == 200


def test_get_data_response_with_error(mock_api_400_response, capsys):
    new_connector = HhAPIConnector()

    with pytest.raises(requests.exceptions.HTTPError):
        new_connector.get_openings("")


def test_get_data_empty_response(mock_api_empty_response):
    new_connector = HhAPIConnector()
    new_connector.get_openings("")
    assert new_connector.openings_dict == [{}]
