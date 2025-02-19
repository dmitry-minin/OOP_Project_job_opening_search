from abc import ABC, abstractmethod
import json
import os

from src.job_openings_class import JobOpening


class DataSaver(ABC):

    @abstractmethod
    def __init__(self):
        """
        Abstract method for Initializer
        """
        pass

    @abstractmethod
    def save_json(self, filename: str, data: dict) -> None:
        """
        Abstract method for save_json method
        """
        pass


class JsonSaver(DataSaver):
    def __init__(self):
        """
        Initialize the JsonSaver with the given file directory.
        """
        self.file_path = None
        self.file_directory = os.path.abspath("../data")


    def save_json(self, filename: str, obj_list: list) -> None:
        """
        save_json method saves data to a JSON file with the given name.
        """
        self.file_path = f"{self.file_directory}/{filename}.json"
        converted_file = self.format_objects_to_dict(obj_list)
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(converted_file, f, indent=4, ensure_ascii=False)

    @staticmethod
    def format_objects_to_dict(obj_list: list) -> list[dict]:
        """
        Helper method to convert list of objects to a dictionary of objects.
        """
        return [obj.__dict__ for obj in obj_list]

    def add_opening_to_json(self, obj) -> None:
        """
        Add a job opening to the json file with openings.
        """

        convert_object = self.format_objects_to_dict([obj])
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except FileNotFoundError:
            data = []

        data.extend(convert_object)
        with open(self.file_path, 'w', encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def delete_opening_from_json(self, obj) -> None:
        """
        Delete a job opening from the json file with openings.
        """
        convert_object = self.format_objects_to_dict([obj])
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except FileNotFoundError:
            return print("There is no file to modify")

        for item in convert_object:
            for idx, obj in enumerate(data):
                if obj == item:
                    del data[idx]
                    break

        with open(self.file_path, 'w', encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    json_saver = JsonSaver()
    obj_list = [
        JobOpening('11', 'DevOps', 'https://api.hh.ru', 50000, 100000,
                   'USD', 'Зарплата указана gross.', 100000,
                   'Test requirement', 'Test responsibility'),
        JobOpening('11', 'DevOps', 'https://api.hh.ru', 60000, 200000,
                   'USD', 'Зарплата указана gross.', 200000,
                   'Test requirement', 'Test responsibility'),
        JobOpening('11', 'DevOps', 'https://api.hh.ru', 70000, 300000,
                   'USD', 'Зарплата указана gross.', 300000,
                   'Test requirement', 'Test responsibility')
    ]
    json_saver.save_json("new_test_file", obj_list)
    json_saver.add_opening_to_json(JobOpening('12', 'I WAS ADDED', 'https://api.hh.ru', 10, 200, 'USD', 'Зарплата указана gross.', 200000, 'A requirement', 'A responsibility'))
    # json_saver.delete_opening_from_json(
    #     JobOpening('11', 'DevOps', 'https://api.hh.ru', 50000, 100000,
    #                'USD', 'Зарплата указана gross.', 100000,
    #                'Test requirement', 'Test responsibility')
    # )
