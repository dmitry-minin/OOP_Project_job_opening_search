from src.mixin_value_inspector import OpeningValuesInspector, InputValuesInspector


def test_correct_values_inspector():
    """
    Test the correctness of OpeningValuesInspector methods, with existing or correct values
    """
    inspector = OpeningValuesInspector()
    job_id = 11
    name = "Python Developer"
    url = "https://hh.ru/"
    salary_from = 20000
    salary_to = 30000
    salary_currency = "RUB"
    salary_is_gross = True
    requirement = "Python, Django, PostgreSQL"
    responsibility = "Develop, maintain and optimize Python web applications."
    assert inspector.id_check(job_id) == 11
    assert inspector.name_check(name) == "Python Developer"
    assert inspector.url_check(url) == "https://hh.ru/"
    assert inspector.salary_check_from(salary_from) == 20000
    assert inspector.salary_check_to(salary_to) == 30000
    assert inspector.salary_check_currency(salary_currency) == "RUB"
    assert inspector.salary_check_is_gross(salary_is_gross) == "Зарплата указана gross."
    assert inspector.requirement_check(requirement) == "Python, Django, PostgreSQL"
    assert inspector.responsibility_check(responsibility) == "Develop, maintain and optimize Python web applications."
    assert inspector.salary_max_mentioned(salary_from, salary_to) == 30000


def test_incorrect_values_inspector():
    """
    Test the correctness of OpeningValuesInspector methods, with missed or incorrect values
    """
    inspector = OpeningValuesInspector()
    job_id = None
    name = None
    url = "htt"
    salary_from = "33"
    salary_to = None
    salary_currency = None
    salary_is_gross = False
    requirement = None
    responsibility = None
    assert inspector.id_check(job_id) is None
    assert inspector.name_check(name) == ""
    assert inspector.url_check(url) == ""
    assert inspector.salary_check_from(salary_from) == 0
    assert inspector.salary_check_to(salary_to) == 0
    assert inspector.salary_check_currency(salary_currency) == ""
    assert inspector.salary_check_is_gross(salary_is_gross) == "Зарплата указана net."
    assert inspector.requirement_check(requirement) == ""
    assert inspector.responsibility_check(responsibility) == ""
    assert inspector.salary_max_mentioned(salary_from, salary_to) == 0


def test_input_values_inspector():
    """
    Tests of InputValuesInspector methods
    """
    search_word = None
    key_words = None
    salary_min1 = ""
    salary_min2 = "100"
    salary_min3 = "txt"
    salary_max1 = "1000"
    salary_max2 = "txt"
    salary_max3 = "50"
    top_range1 = "10"
    top_range2 = "tt3"

    assert InputValuesInspector.check_key_word(search_word) == ""
    assert InputValuesInspector.check_key_word(key_words) == ""
    assert InputValuesInspector.check_salary_min(salary_min1) == 0
    assert InputValuesInspector.check_salary_min(salary_min2) == 100
    assert InputValuesInspector.check_salary_min(salary_min3) == 0
    assert InputValuesInspector.check_salary_max(salary_max1, salary_min2) == 1000
    assert InputValuesInspector.check_salary_max(salary_max2, salary_min2) == 1000000000
    assert InputValuesInspector.check_salary_max(salary_max3, salary_min2) == 1000000000
    assert InputValuesInspector.check_top_range(top_range1) == 10
    assert InputValuesInspector.check_top_range(top_range2) == 100
