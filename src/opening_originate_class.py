from src.mixin_value_inspector import OpeningValuesInspector
from src.job_openings_class import JobOpening


class OriginateOpening(OpeningValuesInspector):

    @staticmethod
    def create_instance(list_of_openings: list[dict]) -> None:
        """
        Factory method for creating instances of JobOpening from a list of dictionaries.
        """
        checker = OpeningValuesInspector
        for opening in list_of_openings:
            job_id = checker.id_check(opening.get("id"))
            name = checker.name_check(opening.get("name"))
            url = checker.url_check(opening.get("url"))

            salary = opening.get("salary", {})
            salary_from = checker.salary_check_from(salary.get("from"))
            salary_to = checker.salary_check_to(salary.get("to"))
            currency = checker.salary_check_currency(salary.get("currency"))
            salary_is_gross = checker.salary_check_is_gross(salary.get("gross"))
            salary_max_mentioned = checker.salary_max_mentioned(salary_from, salary_to)


            snippet = opening.get("snippet", {})
            requirement = checker.requirement_check(snippet.get("requirement"))
            responsibility = checker.responsibility_check(snippet.get("responsibility"))
            if all([job_id, name, url, requirement, responsibility]):
                JobOpening.openings_list.append(JobOpening(job_id, name, url, salary_from, salary_to,
                                                           currency, salary_is_gross, salary_max_mentioned,
                                                           requirement, responsibility))


if __name__ == '__main__':
    originate_opening = OriginateOpening()
    originate_opening.create_instance([
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
        }])
    print(JobOpening.openings_list[0])
