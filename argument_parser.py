import argparse


class ArgumentParser:
    """Class for the ability to enter parameters from the command line"""
    def __init__(self):
        self.args = None
        self.parser_creating()


    def parser_creating(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('arg_rooms', type=str, help='Write path to rooms file')
        parser.add_argument('arg_students', type=str, help='Write path to students file')
        self.args = parser.parse_args()


    def args_info(self):
        return self.args.arg_rooms, self.args.arg_students




