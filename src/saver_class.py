from abc import ABC, abstractmethod
import json
import os


class DataSaver(ABC):

    @abstractmethod
    def save_json(self, filename: str, data: list) -> None:
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
        self.file_directory = os.path.abspath(os.path.join(__file__, os.pardir, os.pardir, "data"))


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
        result = []
        for obj in obj_list:
            obj_dict = {}
            if hasattr(obj_list, '__dict__') and obj_list.__dict__:
                obj_dict.update(obj_list.__dict__)

            slots = getattr(obj.__class__, "__slots__", None)
            if slots:
                for slot in slots:
                    obj_dict[slot] = getattr(obj, slot)
            result.append(obj_dict)
        return result

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
