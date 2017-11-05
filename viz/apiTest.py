from todoist.api import TodoistAPI

api=TodoistAPI('662882fe83d6daf04c70205cad0eca0d4c29d1cd')


formatted=[]

for page in range(0,1000,100):
    tasks=api.activity.get(limit=100, offset=page, event_type='added')

    for task in tasks:
        if(task['parent_project_id'] is not None):
            formatted.append([task['parent_project_id'], task['extra_data']['content'], task['event_date']])


project_ids=[]
project_names={}
for task in formatted:
    if task[0] not in project_ids:
        try:
            project=api.projects.get(task[0])
            if project is not None:
                project_names[task[0]]=project['project']['name']
        except AttributeError:
            pass
        finally:
            project_ids.append(task[0])
