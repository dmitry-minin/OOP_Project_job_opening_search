from src.job_openings_class import JobOpening
from src.saver_class import JsonSaver
import os
import tempfile
import json



def test_save_json_(job_openings_list1):
    """
    Test the save_json method file wit correct structure of job_openings_list created
    """
    with tempfile.TemporaryDirectory() as tmpdirname:
        instance = JsonSaver()
        instance.file_directory = tmpdirname
        instance.save_json('test_file_name', job_openings_list1)
        assert os.path.exists(instance.file_path)

        with open(instance.file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        expected = [
            {
                "job_id": "11", "name": "DevOps", "url": "https://api.hh.ru", "salary_from": 50000, "salary_to": 100000,
                "currency": "USD", "salary_is_gross": "Зарплата указана gross.", "salary_max_mentioned": 100000,
                "requirement": "Test requirement", "responsibility": "Test responsibility"
            },
            {
                "job_id": "11", "name": "Python proger ", "url": "https://api.hh.ru", "salary_from": 10000,
                "salary_to": 200000, "currency": "USD", "salary_is_gross": "Зарплата указана gross.",
                "salary_max_mentioned": 200000, "requirement": "A requirement",
                "responsibility": "A responsibility"
            },
            {
                "job_id": "11", "name": "Java proger ", "url": "https://api.hh.ru", "salary_from": 150000,
                "salary_to": 500000, "currency": "USD", "salary_is_gross": "Зарплата указана gross.",
                "salary_max_mentioned": 500000, "requirement": "B requirement", "responsibility": "b responsibility"
            },
            {
                "job_id": "11", "name": "Java proger ", "url": "https://api.hh.ru", "salary_from": 200000,
                "salary_to": 700000, "currency": "USD", "salary_is_gross": "Зарплата указана gross.",
                "salary_max_mentioned": 700000, "requirement": "B requirement", "responsibility": "b responsibility"
            }
        ]
        assert data == expected


def test_add_opening_to_json(file_with_json):
    """
    Test the add_opening_to_json method
    """
    new_opening = JobOpening(
        '12', 'I WAS ADDED', 'https://api.hh.ru', 10, 200, 'USD', 'Зарплата указана gross.',
        200000, 'A requirement', 'A responsibility')
    file_with_json.add_opening_to_json(new_opening)
    assert os.path.exists(file_with_json.file_path)

    with open(file_with_json.file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    expected = [
        {
            "job_id": "11", "name": "DevOps", "url": "https://api.hh.ru", "salary_from": 50000, "salary_to": 100000,
            "currency": "USD", "salary_is_gross": "Зарплата указана gross.", "salary_max_mentioned": 100000,
            "requirement": "Test requirement", "responsibility": "Test responsibility"
        },
        {
            "job_id": "11", "name": "Python proger ", "url": "https://api.hh.ru", "salary_from": 10000,
            "salary_to": 200000, "currency": "USD", "salary_is_gross": "Зарплата указана gross.",
            "salary_max_mentioned": 200000, "requirement": "A requirement",
            "responsibility": "A responsibility"
        },
        {
            "job_id": "11", "name": "Java proger ", "url": "https://api.hh.ru", "salary_from": 150000,
            "salary_to": 500000, "currency": "USD", "salary_is_gross": "Зарплата указана gross.",
            "salary_max_mentioned": 500000, "requirement": "B requirement", "responsibility": "b responsibility"
        },
        {
            "job_id": "11", "name": "Java proger ", "url": "https://api.hh.ru", "salary_from": 200000,
            "salary_to": 700000, "currency": "USD", "salary_is_gross": "Зарплата указана gross.",
            "salary_max_mentioned": 700000, "requirement": "B requirement", "responsibility": "b responsibility"
        },
        {
            "job_id": "12", "name": "I WAS ADDED", "url": "https://api.hh.ru", "salary_from": 10,
            "salary_to": 200, "currency": "USD", "salary_is_gross": "Зарплата указана gross.",
            "salary_max_mentioned": 200000, "requirement": 'A requirement', "responsibility": 'A responsibility'
        }
    ]
    assert data == expected


def test_add_opening_with_no_file_exists(file_with_json):
    """
    Test the add_opening_to_json method with missed file
    """
    with tempfile.TemporaryDirectory() as tmpdirname:
        instance = JsonSaver()
        instance.file_directory = tmpdirname
        instance.file_path = os.path.join(tmpdirname, "test_file.json")
        new_opening = JobOpening(
            '12', 'I WAS ADDED', 'https://api.hh.ru', 10, 200, 'USD', 'Зарплата указана gross.',
            200000, 'A requirement', 'A responsibility')
        instance.add_opening_to_json(new_opening)
        assert os.path.exists(instance.file_path)

        with open(instance.file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        compare_with = [
            {
                'currency': 'USD', 'job_id': '12', 'name': 'I WAS ADDED', 'requirement': 'A requirement',
                'responsibility': 'A responsibility', 'salary_from': 10, 'salary_is_gross': 'Зарплата указана gross.',
                'salary_max_mentioned': 200000, 'salary_to': 200, 'url': 'https://api.hh.ru'
            }]
        assert data == compare_with


def test_delete_opening_from_json(file_with_json):
    """
    Test the delete_opening_from_json method
    """
    object_to_delete = JobOpening('11', 'DevOps', 'https://api.hh.ru', 50000,
                                  100000, 'USD', 'Зарплата указана gross.',
                                  100000, 'Test requirement',
                                  'Test responsibility')
    file_with_json.delete_opening_from_json(object_to_delete)
    assert os.path.exists(file_with_json.file_path)
    with open(file_with_json.file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    assert len(data) == 3


def test_objects_to_dict(job_openings_list1):
    """
    Test the objects_to_dict method
    """
    result = JsonSaver.format_objects_to_dict(job_openings_list1)
    assert result == [
        {
            'currency': 'USD', 'job_id': '11', 'name': 'DevOps', 'requirement': 'Test requirement',
            'responsibility': 'Test responsibility', 'salary_from': 50000, 'salary_is_gross': 'Зарплата указана gross.',
            'salary_max_mentioned': 100000, 'salary_to': 100000, 'url': 'https://api.hh.ru'
        },
        {
            'currency': 'USD', 'job_id': '11', 'name': 'Python proger ', 'requirement': 'A requirement',
            'responsibility': 'A responsibility', 'salary_from': 10000, 'salary_is_gross': 'Зарплата указана gross.',
            'salary_max_mentioned': 200000, 'salary_to': 200000, 'url': 'https://api.hh.ru'
        },
        {
            'currency': 'USD', 'job_id': '11', 'name': 'Java proger ', 'requirement': 'B requirement',
            'responsibility': 'b responsibility', 'salary_from': 150000, 'salary_is_gross': 'Зарплата указана gross.',
            'salary_max_mentioned': 500000, 'salary_to': 500000, 'url': 'https://api.hh.ru'
        },
        {
            'currency': 'USD', 'job_id': '11', 'name': 'Java proger ', 'requirement': 'B requirement',
            'responsibility': 'b responsibility', 'salary_from': 200000, 'salary_is_gross': 'Зарплата указана gross.',
            'salary_max_mentioned': 700000, 'salary_to': 700000, 'url': 'https://api.hh.ru'
        }
    ]
