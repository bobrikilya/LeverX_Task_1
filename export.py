import json


class JsonExporter:
    """Class for creating new json file"""

    def __init__(self, info_list):
        self.info_list = info_list

    def unloading(self):
        with open("rooms_with_students.json", 'w') as new_file:
            json.dump(self.info_list, new_file)
        return "Mission completed"
