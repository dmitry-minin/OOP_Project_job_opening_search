from abc import ABC


class ValuesInspector(ABC):
    """
    Abstract class for validating values of various types.
    """
    pass


class OpeningValuesInspector(ValuesInspector):
    """
    Class for validating values of JobOpening instances.
    """

    @classmethod
    def id_check(cls, job_id):
        """
        Check if id is not empty and contains only alphanumeric characters and hyphens.
        """
        return job_id if job_id else None

    @classmethod
    def name_check(cls, name):
        """
        Check if name is not empty and contains only alphanumeric characters and spaces.
        """
        return name if name else ""

    @classmethod
    def url_check(cls, url) -> str:
        """
        Check if url is not empty and starts with "https://" or "http://".
        """
        return url if url and url.startswith(("https://", "http://")) else ""

    @classmethod
    def salary_check_from(cls, salary_from) -> float or int:
        """
        Check if 'from' salary is not empty and contains only digits.
        """
        return salary_from if isinstance(salary_from, (int, float)) else 0

    @classmethod
    def salary_check_to(cls, salary_to) -> float or int:
        """
        Check if 'to' salary is not empty and contains only digits.
        """
        return salary_to if isinstance(salary_to, (int, float)) else 0

    @classmethod
    def salary_check_currency(cls, salary_currency) -> str:
        """
        Check if currency is not empty.
        """
        return salary_currency if salary_currency and isinstance(salary_currency, str) else ""

    @classmethod
    def salary_check_is_gross(cls, salary_is_gross: bool) -> str:
        """
        Check if salary is_gross is not empty and contains only boolean values.
        """
        if isinstance(salary_is_gross, bool):
            return "Зарплата указана gross." if salary_is_gross else "Зарплата указана net."
        else:
            return f"{salary_is_gross}"

    @classmethod
    def salary_max_mentioned(cls, salary_from, salary_to) -> int:
        """
        Check if 'to' or 'from' salary is not empty, return max specified value.
        """
        if cls.salary_check_to(salary_to):
            return salary_to
        elif cls.salary_check_from(salary_from):
            return salary_from
        else:
            return 0

    @classmethod
    def requirement_check(cls, requirement):
        """
        Check if requirement is not empty.
        """
        return requirement if requirement else ""

    @classmethod
    def responsibility_check(cls, responsibility):
        """
        Check if responsibility is not empty.
        """
        return responsibility if responsibility else ""


class InputValuesInspector(ValuesInspector):
    """
    Class for validating user input.
    """
    @staticmethod
    def check_search_request(search_word: str or int) -> str:
        """
        Check if search_word is not empty. If it's empty, return an empty string.
        """
        if not search_word:
            search_word = ""
            return search_word
        return search_word

    @staticmethod
    def check_key_word(key_words):
        """
        Check if key_words is not empty. If it's empty, return an empty string.
        """
        if not key_words:
            key_words = ""
            return key_words
        return key_words

    @staticmethod
    def check_salary_min(salary_min) -> int:
        """
        Check if salary_min is not empty and contains only digits. If it's empty, return 0.
        """
        if salary_min.isdigit():
            return int(salary_min)
        elif not salary_min.strip():
            salary_min = 0
            return salary_min
        return 0

    @staticmethod
    def check_salary_max(salary_max, salary_min) -> int:
        """
        Check if:
        - salary_max is not empty contains only digits. If it's empty, return 1000000000.
        """
        if salary_max.isdigit():
            return int(salary_max) if int(salary_max) > int(salary_min) else 1000000000
        elif not salary_max.strip():
            salary_max = 1000000000
            return salary_max
        return 1000000000

    @staticmethod
    def check_top_range(top_range) -> int:
        """
        Check if top_range is not empty and contains only digits. If it's empty, return 100.
        """
        if top_range.isdigit():
            return int(top_range)
        else:
            print("Вы указали некорректный диапазон, будет выведено топ 100 по зарплате")
            top_range = 100
            return top_range
