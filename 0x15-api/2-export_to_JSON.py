#!/usr/bin/python3
"""
Export the Employees TODO-List data in a JSON format
"""
from argparse import ArgumentParser
from os import path
from requests import get
from sys import argv
from json import dump


mockApiUsers = "https://jsonplaceholder.typicode.com/users"
mockApiTodo = "https://jsonplaceholder.typicode.com/todos"

if __name__ == '__main__':

    parser = ArgumentParser(prog=path.basename(argv[0]))
    parser.add_argument('ID', type=int, help="employee ID")
    args = parser.parse_args()
    user = get('/'.join([mockApiUsers, str(args.id)])).json()
    with open('.'.join([str(args.id), 'json']), 'w') as ostream:
        dump({
            str(args.id): [{
                "task": task['title'],
                "completed": task['completed'],
                "username": user['username'],
            } for task in get(TODOS, params={'userId': args.id}).json()]
        }, ostream)
