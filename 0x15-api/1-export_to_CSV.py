#!/usr/bin/python3
"""
Export the Employees TODO-List data in a CSV format
"""
from argparse import ArgumentParser
from os import path
from requests import get
from sys import argv
from csv import QUOTE_ALL, writer


mockApiUsers = "https://jsonplaceholder.typicode.com/users"
mockApiTodo = "https://jsonplaceholder.typicode.com/todos"

if __name__ == '__main__':

    parser = ArgumentParser(prog=path.basename(argv[0]))
    parser.add_argument('ID', type=int, help="employee ID")
    args = parser.parse_args()
    user = get('/'.join([mockApiUsers, str(args.id)])).json()
    with open('.'.join([str(args.id), 'csv']), 'w', newline='') as ostream:
        writer(ostream, quoting=QUOTE_ALL).writerows(
            [str(args.id), user['username'], task['completed'], task['title']]
            for task in get(mockApiTodo, params={'userId': args.id}).json())
