import json

class FileReader:
    """Class for read the file that was transferred """

    def file_reader(self, file):
        try:
            with open(file) as read_file:
                data = json.load(read_file)
            return data

        except FileNotFoundError:
            print("Your file \"" + file + "\" not founding")
            raise SystemExit












