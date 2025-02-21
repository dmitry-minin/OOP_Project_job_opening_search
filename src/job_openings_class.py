from abc import ABC, abstractmethod


class BaseJobOpening(ABC):
    """
    Abstract class for JobOpening.
    """

    @classmethod
    @abstractmethod
    def get_openings_by_key_words(cls, use_keywords: str) -> list:
        """
        Abstract method for retrieving openings by keywords.
        """
        pass

    @staticmethod
    @abstractmethod
    def openings_in_salary_range(data: list, range_a: int, range_b: int) -> list:
        """
        Abstract method for retrieving openings in salary range.
        """
        pass

    @staticmethod
    @abstractmethod
    def opening_get_top_salaries(data: list, top_range: int) -> list:
        """
        Abstract method for retrieving top N salaries.
        """
        pass


class JobOpening(BaseJobOpening):
    """
    JobOpening class represents a job opening.
    """
    openings_list: list["JobOpening"] = []

    __slots__ = ("job_id", "name", "url", "salary_from", "salary_to", "currency", "salary_is_gross",
                 "salary_max_mentioned", "requirement", "responsibility")
    """
    Slot for job_id, name, url, salary_from, salary_to, currency, salary_is_gross, salary_max_mentioned,
    requirement, responsibility.
    To restrict creation of an additional attribute, and optimize memory usage
    """

    def __init__(self, job_id: str, name: str, url: str, salary_from: int, salary_to: int,
                 currency: str, salary_is_gross: str, salary_max_mentioned: int,
                 requirement: str, responsibility: str) -> None:
        self.job_id = job_id
        self.name = name
        self.url = url
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.currency = currency
        self.salary_is_gross = salary_is_gross
        self.salary_max_mentioned = salary_max_mentioned
        self.requirement = requirement
        self.responsibility = responsibility

    def salary_format_str(self) -> str:
        if self.salary_from == 0 and self.salary_to == 0:
            return "Зарплата не указана"
        elif self.salary_from > 0 and self.salary_to > 0:
            return f"Зарплата от {self.salary_from} до {self.salary_to} {self.currency}. {self.salary_is_gross}"
        elif self.salary_from > 0 and self.salary_to == 0:
            return f"Зарплата от {self.salary_from} {self.currency}. {self.salary_is_gross}"
        elif self.salary_from == 0 and self.salary_to > 0:
            return f"Зарплата до {self.salary_to} {self.currency}. {self.salary_is_gross}"
        else:
            return "нет информации"

    def __str__(self):
        """
        Return a string representation of the JobOpening instance in user format.
        """
        return (
            f"Id Вакансии: {self.job_id}\nНазвание: {self.name}\nСсылка: {self.url}\n"
            f"Зарплата: {self.salary_format_str()}\nТребования: {self.requirement}\nОбязанности: {self.responsibility}")

    def __repr__(self):
        """
        Return a string representation of the JobOpening instance.
        """
        return (f"{__class__.__name__}(id='{self.job_id}', name='{self.name}', url='{self.url}',"
                f" salary_from='{self.salary_from}', salary_to='{self.salary_to}', currency='{self.currency}',"
                f" salary_is_gross='{self.salary_is_gross}', salary_max_mentioned='{self.salary_max_mentioned}',"
                f" requirement='{self.requirement}', responsibility='{self.responsibility}')")

    @classmethod
    def get_openings_by_key_words(cls, use_keywords) -> list:
        """
        Return list of JobOpening instances that contain any of the given keywords.
        """
        keywords = use_keywords.lower().split(" ")
        result = []
        for opening in cls.openings_list:
            for keyword in keywords:
                if keyword in opening.name:
                    result.append(opening)
                elif keyword in opening.requirement.lower():
                    result.append(opening)
                elif keyword in opening.responsibility.lower():
                    result.append(opening)
        return result

    @staticmethod
    def openings_in_salary_range(data: list, range_a: int, range_b: int) -> list:
        """
        Sort list of JobOpening instances by salary within the given range.
        """
        result = []
        for opening in data:
            if opening.salary_to is not None:
                if opening.salary_to in range(range_a, range_b + 1):
                    result.append(opening)
            elif opening.salary_from is not None:
                if opening.salary_from in range(range_a, range_b + 1):
                    result.append(opening)
        return result

    @staticmethod
    def opening_get_top_salaries(data: list, top_range: int) -> list:
        """
        Return list of JobOpening instances with the highest salary within the given range.
        """
        top_sorted_in_range = sorted(data, key=lambda x: x.salary_max_mentioned, reverse=True)[:top_range]
        return top_sorted_in_range
