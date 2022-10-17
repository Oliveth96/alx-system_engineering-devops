#!/usr/bin/python3
"""
Export the Employees TODO-List data in a JSON format
"""
from requests import get
from json import dump


mockApiUsers = "https://jsonplaceholder.typicode.com/users"
mockApiTodo = "https://jsonplaceholder.typicode.com/todos"

if __name__ == '__main__':
    with open('todo_all_employees.json', 'w') as ostream:
        dump({
            str(user['id']): [{
                "username": user['username'],
                "task": task['title'],
                "completed": task['completed'],
            } for task in get(TODOS, params={'userId': user['id']}).json()]
            for user in get(USERS).json()
        }, ostream)
