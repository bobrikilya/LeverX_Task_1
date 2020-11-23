from file_reader import FileReader
from distribution import Distribution
from export import JsonExporter


def main():
    """Main function for calling others"""
    example = FileReader()
    rooms = example.file_reader('rooms.json')
    students = example.file_reader('students.json')
    new_info = Distribution(rooms, students).student_distribution()
    result = JsonExporter(new_info).unloading()
    print(result)


main()

