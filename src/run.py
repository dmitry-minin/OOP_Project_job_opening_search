from src.connector_class import HhAPIConnector
from src.job_openings_class import JobOpening
from src.opening_originate_class import OriginateOpening
from src.mixin_value_inspector import InputValuesInspector
from src.saver_class import JsonSaver


class Run(InputValuesInspector):
    """
    Class for running the application.
    """

    def start(self):
        connect = HhAPIConnector()
        search_word = self.check_search_request(input("Введите ключевое слово/ слова для поиска: "))
        connect.get_openings(search_word)
        OriginateOpening.create_instance(connect.openings_dict)
        user_keyword: str = self.check_key_word(input("Введите ключевые слова для фильтрации вакансий: "))
        sorted_by_keyword: list = JobOpening.get_openings_by_key_words(user_keyword)
        self.printing_function(sorted_by_keyword)
        salary_range_min: int = self.check_salary_min(input("Введите нижний предел зарплаты: "))
        salary_range_max: int = self.check_salary_max(input("Введите верхний предел зарплаты: "), salary_range_min)
        sorted_by_salary = JobOpening.openings_in_salary_range(sorted_by_keyword, salary_range_min, salary_range_max)
        self.printing_function(sorted_by_salary)
        top_range = self.check_top_range(input("Введите количество вакансий для вывода в топ N: "))
        sorted_by_salary_in_range: list = JobOpening.opening_get_top_salaries(sorted_by_salary, top_range)
        self.printing_function(sorted_by_salary_in_range)
        should_save = input("Хотите сохранить результат (да/нет)? ")
        if should_save.lower() == "да":
            saver = JsonSaver()
            file_name = input("Введите название файла:  ")
            saver.save_json(file_name, sorted_by_salary_in_range)
            print(f"Результат сохранен в {saver.file_path}")
        else:
            print("Результат не сохранен.")
    
    
    @staticmethod
    def printing_function(iter_object: list) -> None:
        for opening in iter_object:
            print(str(opening))


if __name__ == "__main__":
    run_instance = Run()
    run_instance.start()
