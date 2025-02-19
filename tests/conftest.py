import importlib
import requests_mock
import pytest
import src.job_openings_class as job_openings_module
import src.opening_originate_class as originate_opening_module
import tempfile
from src.saver_class import JsonSaver

"""
Fixtures for connector class testing
"""


@pytest.fixture
def mock_api_success():
    with requests_mock.Mocker() as m:
        m.get("https://api.hh.ru/vacancies", json={"items": [{"12": "Python dev"}, {"13": "Java dev"}]},
              status_code=200)
        yield m


@pytest.fixture
def mock_api_incorrect_response():
    with requests_mock.Mocker() as m:
        m.get("https://api.hh.ru/vacancies", status_code=200)
        yield m


@pytest.fixture
def mock_api_400_response():
    with requests_mock.Mocker() as m:
        m.get("https://api.hh.ru/vacancies", status_code=400)
        yield m


@pytest.fixture
def mock_api_empty_response():
    with requests_mock.Mocker() as m:
        m.get("https://api.hh.ru/vacancies", json={}, status_code=200)
        yield m


"""
Fixture for Originate class testing
"""


@pytest.fixture(autouse=True)
def reload_job_opening_class():
    importlib.reload(job_openings_module)
    importlib.reload(originate_opening_module)


@pytest.fixture
def dict_success_origination():
    return [
        {
            'id': '115948521', 'premium': False, 'name': 'DevOps (IGaming)', 'department': None,
            'salary':
                {
                    'from': 3000, 'to': 5500, 'currency': 'USD', 'gross': False
                },
            'published_at': '2025-02-13T16:55:10+0300', 'created_at': '2025-02-13T16:55:10+0300',
            'archived': False, "url": "https://api.hh.ru/vacancies/115760953?host=hh.ru",
            'snippet':
                {
                    'requirement': 'Опыт работы от 5 лет.',
                    'responsibility': 'Создание элементов IaC (ansible, terraform).'
                },
            'accept_temporary': False, 'fly_in_fly_out_duration': [],
            'work_format': [{'id': 'REMOTE', 'name': 'Удалённо'}],
            'working_hours': [{'id': 'HOURS_8', 'name': '8\xa0часов'}],
            'work_schedule_by_days': [{'id': 'FIVE_ON_TWO_OFF', 'name': '5/2'}], 'night_shifts': False,
            'experience': {'id': 'between3And6', 'name': 'От 3 до 6 лет'}
        }]


@pytest.fixture
def dict_missing_value_origination():
    return [
        {
            'id': '', 'premium': False, 'name': 'DevOps (IGaming)', 'department': None,
            'salary':
                {
                    'from': 1000, 'to': 5500, 'currency': 'USD', 'gross': False
                },
            'published_at': '2025-02-13T16:55:10+0300', 'created_at': '2025-02-13T16:55:10+0300',
            'archived': False, "url": "https://api.hh.ru/vacancies/115760953?host=hh.ru",
            'snippet':
                {
                    'requirement': 'Опыт работы от 5 лет.',
                    'responsibility': 'Создание элементов IaC (ansible, terraform).'
                }
        }]


"""
Fixture for job opening and saver classes testing
"""


@pytest.fixture
def job_opening1():
    return [
        "11", "DevOps", "https://api.hh.ru",
        3000, 5500, "USD", "Gross", 5500,
        "Test requirement", "Test responsibility"
    ]


@pytest.fixture
def job_openings_list1():
    return [job_openings_module.JobOpening('11', 'DevOps', 'https://api.hh.ru',
                                           50000, 100000, 'USD',
                                           'Зарплата указана gross.', 100000,
                                           'Test requirement', 'Test responsibility'),
            job_openings_module.JobOpening('11', 'Python proger ', 'https://api.hh.ru',
                                           10000, 200000, 'USD',
                                           'Зарплата указана gross.', 200000,
                                           'A requirement', 'A responsibility'),
            job_openings_module.JobOpening('11', 'Java proger ', 'https://api.hh.ru',
                                           150000, 500000, 'USD',
                                           'Зарплата указана gross.', 500000,
                                           'B requirement', 'b responsibility'),
            job_openings_module.JobOpening('11', 'Java proger ', 'https://api.hh.ru',
                                           200000, 700000, 'USD',
                                           'Зарплата указана gross.', 700000,
                                           'B requirement', 'b responsibility')
            ]


@pytest.fixture
def file_with_json(job_openings_list1):
    """
    Returns a path to temporary json with objects in it
    """
    with tempfile.TemporaryDirectory() as tmpdirname:
        instance = JsonSaver()
        instance.file_directory = tmpdirname
        instance.save_json('test_file_name', job_openings_list1)
        yield instance
