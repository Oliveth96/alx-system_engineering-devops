<h1>0x15. API</h1>
<br>

<h5>RESOURCES</h5>

<span>Read or watch:</span>
<br>
[Friends don’t let friends program in shell script](https://www.turnkeylinux.org/blog/friends-dont-let-friends-program-shell-script)
[What is an API](https://www.webopedia.com/definitions/api/)
[What is an API? In English, please](https://www.freecodecamp.org/news/what-is-an-api-in-english-please-b880a3214a82/)
[What is a REST API](https://www.sitepoint.com/rest-api/)
[What are microservices](https://smartbear.com/solutions/microservices/)

<br>

<h5>LEARNING OBJECTIVES</h5>
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

<ul>General</ul>
<li>What Bash scripting should not be used for</li>
<li>What is an API</li>
<li>What is a REST API</li>
<li>What are microservices</li>
<li>What is the CSV, JSON format</li>
<li>Pythonic Package and module name style</li>
<li>Pythonic Class, Variable, Function, Constant name style</li>
<li>Significance of CapWords or CamelCase in Python</li>

| TASKS | FILES | DESCRIPTION |
| ----- | ----- | ----------- |
| 0. Gather data from an API | [0-gather_data_from_an_API.py](https://github.com/Oliveth96/0x15-api/0-gather_data_from_an_API.py) | Write a Python script that, using this REST API, for a given employee ID, returns information about his/her TODO list progress.<ul>Requirements</ul><li>You must use urllib or requests module</li><li>The script must accept an integer as a parameter, which is the employee ID</li><li>The script must display on the standard output the employee TODO list progress in this exact format:</li>|
| 1. Export to CSV |[1-export_to_CSV.py](https://github.com/Oliveth96/0x15-api/1-export_to_CSV.py)|<p>Using what you did in the task #0, extend your Python script to export data in the CSV format.</p><span>Requirements:</span><li>Records all tasks that are owned by this employee</li><li>Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"</li><li>File name must be: USER_ID.csv</li>|
| 2. Export to JSON |[2-export_to_JSON.py](https://github.com/Oliveth96/0x15-api/2-export_to_JSON.py)|<p>Using what you did in the task #0, extend your Python script to export data in the JSON format.</p><span>Requirements:</span><li>Records all tasks that are owned by this employee</li><li>Format must be: { "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}</li><li>File name must be: USER_ID.json</li>|
| 3. Dictionary of list of dictionaries |[3-dictionary_of_list_of_dictionaries.py](https://github.com/Oliveth96/0x15-api/3-dictionary_of_list_of_dictionaries.py)|<p>Using what you did in the task #0, extend your Python script to export data in the JSON format.</p><span>Requirements:</span><li>Records all tasks from all employees</li><li>Format must be: { "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ], "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}</li><li>File name must be: todo_all_employees.json</li>|

AUTHOR

[Oliveth Ndubuka](https://github.com/Oliveth96)