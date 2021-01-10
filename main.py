from file_reader import FileReader
from distribution import Distribution
from export import JsonExporter
from argument_parser import ArgumentParser


def main():
    """Main function for calling others"""
    parsing = ArgumentParser()
    rooms_file, students_file = parsing.args_info()
    example = FileReader()
    rooms = example.file_reader(rooms_file)
    students = example.file_reader(students_file)
    new_info = Distribution(rooms, students).student_distribution()
    result = JsonExporter(new_info).unloading()
    print(result)


main()
