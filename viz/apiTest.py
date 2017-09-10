from todoist.api import TodoistAPI
import requests

#api=TodoistAPI('a3a70d4305c98b4654d2d33008a50d525c6f2bd1')
#api.sync()

#print(api.state['tasks'])

response=requests.get('https://todoist.com/API/v7/completed/get_all', params={'token':'a3a70d4305c98b4654d2d33008a50d525c6f2bd1'}).json()

days=[]
projects=[]
tasks=[]

for task in response['items']:
    tasks.append(task['content'])
    projects.append(task['project_id'])
    date=task['completed_date']
    days.append(date)

projectCount={}
for projectId in projects:
    for project in response['projects'].values():
        if project['id'] == projectId:
            if project['name'] in projectCount.keys():
                projectCount[project['name']]+=1
            else:
                projectCount[project['name']]=1


print(projectCount)
    
    
