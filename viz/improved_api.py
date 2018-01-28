''' still testing the api  '''

from datetime import datetime

from todoist.api import TodoistAPI

PROJECT_TITLES = {}


def get_project_title(task, api):
    ''' takes in a task and returns the project title '''
    
    # check if the id exists first
    if 'parent_project_id' not in task: 
        return "Deleted Project"
    
    # get project id
    project_id = task['parent_project_id']

    # if the id is not in dictionary, look it up using api
    if project_id not in PROJECT_TITLES:

        try:
            project = api.projects.get_by_id(project_id)
        except:
            project = None

        if project is None:
            return "Deleted Project"

        project_title = project['project']['name']

        # add it to the dictionary
        PROJECT_TITLES[project_id] = project_title

        return project_title

    return PROJECT_TITLES[project_id]


def format_date(task):
    ''' takes a task and created a python date instead of the string date '''

    if 'event_date' not in task:
        return None

    # create a date object
    task_date = task['event_date']
    task_date = task_date[0:23]
    task_date = datetime.strptime(task_date, "%a %d %b %Y %H:%M:%S")

    return task_date


def get_title(task):
    ''' takes a task and returns the content '''

    # check if the task has extras
    if 'extra_data' not in task:
        return "NONE"

    extra_data = task['extra_data']
    title = extra_data['content']

    return title


def get_all_tasks():
    ''' entry function: gets all the tasks from the api '''

    api_key = "none"

    with open("api_key.txt", 'r') as api_file:
        api_key = api_file.read()

    api = TodoistAPI(api_key)

    all_tasks = []

    #todo this is terrible, find something better
    for page in range(0, 1000, 100):
        tasks = api.activity.get(
            limit=100, offset=page, object_type="item", event_type='added')
        for task in tasks:
            # clean it up
            cleaned = {}
            cleaned['date'] = format_date(task)
            cleaned['title'] = get_title(task)
            cleaned['project_title'] = get_project_title(task, api)

            all_tasks.append(cleaned)

    return all_tasks



print(get_all_tasks())
