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
