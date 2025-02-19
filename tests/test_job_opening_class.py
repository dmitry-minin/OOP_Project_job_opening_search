import src.job_openings_class as job_opening_module


def test_opening_init(job_opening1):
    """
    Test the JobOpening class initialization
    """
    new_opening = job_opening_module.JobOpening(*job_opening1)
    assert new_opening.job_id == "11"
    assert new_opening.name == "DevOps"
    assert new_opening.url == "https://api.hh.ru"
    assert new_opening.salary_from == 3000
    assert new_opening.salary_to == 5500
    assert new_opening.currency == "USD"
    assert new_opening.salary_is_gross == "Gross"
    assert new_opening.salary_max_mentioned == 5500
    assert new_opening.requirement == "Test requirement"
    assert new_opening.responsibility == "Test responsibility"


def test_opening_str(job_opening1):
    """
    Test the JobOpening string representation
    """
    new_opening1 = job_opening_module.JobOpening(*job_opening1)
    assert str(new_opening1) == (
        f"Id Вакансии: 11\n"
        f"Название: DevOps\n"
        f"Ссылка: https://api.hh.ru\n"
        f"Зарплата: Зарплата от 3000 до 5500 USD. Gross\n"
        f"Требования: Test requirement\n"
        f"Обязанности: Test responsibility"
    )


def test_opening_salary_format_str(job_opening1):
    """
    Test the salary format string representation
    """
    new_opening2 = job_opening_module.JobOpening(*job_opening1)
    assert new_opening2.salary_format_str() == "Зарплата от 3000 до 5500 USD. Gross"


def test_opening_repr(job_opening1):
    """
    Test the JobOpening representation using __repr__
    """
    new_opening3 = job_opening_module.JobOpening(*job_opening1)
    assert repr(new_opening3) == ("JobOpening(id='11', name='DevOps', url='https://api.hh.ru', "
                                  "salary_from='3000', salary_to='5500', currency='USD', "
                                  "salary_is_gross='Gross', salary_max_mentioned='5500', requirement='Test "
                                  "requirement', responsibility='Test responsibility')")


def test_get_by_key_words(job_openings_list1):
    """
    Test the get_openings_by_key_words method
    """
    job_opening_module.JobOpening.openings_list.extend(job_openings_list1)
    assert len(job_opening_module.JobOpening.get_openings_by_key_words("Test")) == 1


def test_openings_in_salary_range(job_openings_list1):
    """
    Test the openings_in_salary_range method
    """
    assert len(job_opening_module.JobOpening.openings_in_salary_range(job_openings_list1,
                                                                      50000, 200000)) == 2


def test_get_top_salaries(job_openings_list1):
    """
    Test the opening_get_top_salaries method
    """
    assert len(job_opening_module.JobOpening.opening_get_top_salaries(job_openings_list1, 2)) == 2
    assert ([repr(i) for i in job_opening_module.JobOpening.opening_get_top_salaries(job_openings_list1, 1)]
            == [repr(job_opening_module.JobOpening('11', 'Java proger ', 'https://api.hh.ru',
                                                   200000, 700000, 'USD',
                                                   'Зарплата указана gross.', 700000,
                                                   'B requirement', 'b responsibility'))
                ])
