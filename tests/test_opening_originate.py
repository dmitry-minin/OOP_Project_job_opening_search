import src.job_openings_class as job_openings_module
import src.opening_originate_class as originate_opening_module


def test_successfully_originate(dict_success_origination):
    """
    Test the OriginateOpening class with a dictionary of openings
    """
    origin = originate_opening_module.OriginateOpening()
    origin.create_instance(dict_success_origination)
    assert len(job_openings_module.JobOpening.openings_list) == 1
    assert job_openings_module.JobOpening.openings_list[0].job_id == "115948521"
    assert job_openings_module.JobOpening.openings_list[0].name == "DevOps (IGaming)"
    assert job_openings_module.JobOpening.openings_list[0].url == "https://api.hh.ru/vacancies/115760953?host=hh.ru"
    assert job_openings_module.JobOpening.openings_list[0].salary_from == 3000
    assert job_openings_module.JobOpening.openings_list[0].salary_to == 5500
    assert job_openings_module.JobOpening.openings_list[0].currency == "USD"
    assert job_openings_module.JobOpening.openings_list[0].salary_is_gross == "Зарплата указана net."
    assert job_openings_module.JobOpening.openings_list[0].salary_max_mentioned == 5500
    assert job_openings_module.JobOpening.openings_list[0].requirement == "Опыт работы от 5 лет."
    assert job_openings_module.JobOpening.openings_list[0].responsibility == ("Создание элементов IaC (ansible,"
                                                                              " terraform).")



def test_failed_origination(dict_missing_value_origination):
    """
    Test the OriginateOpening class with a dictionary where some required values are missing
    """
    failed_origin = originate_opening_module.OriginateOpening()
    failed_origin.create_instance(dict_missing_value_origination)
    assert len(job_openings_module.JobOpening.openings_list) == 0
