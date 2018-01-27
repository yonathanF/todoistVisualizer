''' still testing the api  '''

from datetime import datetime

from todoist.api import TodoistAPI


def get_project_id(task):
    ''' takes in a task and returns the project id '''

    return task['parent_project_id']


def format_date(task):
    ''' takes a task and created a python date instead of the string date '''

    # create a date object
    task_date = task['event_date']
    task_date = task_date[0:23]
    task_date = datetime.strptime(task_date, "%a %d %b %Y %H:%M:%S")

    return task_date


def get_title(task):
    ''' takes a task and returns the content '''

    # check if the task has extras
    if 'extra_data' not in task.keys():
        return "NONE"

    extra_data = task['extra_data']
    title = extra_data['content']

    return title


def get_all_tasks():
    ''' entry function: gets all the tasks from the api '''

    api = TodoistAPI('662882fe83d6daf04c70205cad0eca0d4c29d1cd')

    all_tasks = []

    for page in range(0, 1000, 100):
        tasks = api.activity.get(
            limit=100, offset=page, object_type="item", event_type='added')
        for task in tasks:
            # clean it up
            cleaned = {}
            cleaned['date'] = format_date(task)
            cleaned['title'] = get_title(task)
            cleaned['project_id'] = get_project_id(task)

            all_tasks.append(cleaned)

    return all_tasks


print(get_all_tasks())
