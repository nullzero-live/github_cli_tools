import argparse
import os
from __version__ import __version__

def main_parser():
    # Create the parser
    parser = argparse.ArgumentParser(description="Process some flags.")
    
    parser.add_argument('--title', help='The title for the operation', default=None)
    parser.add_argument('--body', help='The body content for the operation', default=None)
    parser.add_argument('--repo', '-r', help='Sets the name of the project', default="my_project_1")
    parser.add_argument('--auto', '-a', action='store_true', help='Sets the AUTO_INSTALL variable to True', default=False)
    parser.add_argument('--debug', '-d', action='store_true', help='Sets the DEBUG variable to True', default=False)
    parser.add_argument('--quiet', '-q', action='store_true', help='Suppresses the output', default=False)
    parser.add_argument('--extract', '-e', action='store_true', help='Adds a custom library', default=False)
    parser.add_argument('--version', '-v', help='Shows the version of the tool', default=f"{__version__}")

    return parser

        









