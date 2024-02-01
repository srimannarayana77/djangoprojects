def sort_users(sortBY,sortType,users):
    if sortType.lower() == 'desc':
        users = users.order_by(f'-{sortBY}')
    else:
       users = users.order_by(sortBY)

    return users
    

def sort_projects(sortBY,sortType,projects):
    if sortType.lower() == 'desc':
        projects = projects.order_by(f'-{sortBY}')
    else:
       projects = projects.order_by(sortBY)

    return projects

def sort_tasks(sortBY,sortType,tasks):
   if sortType.lower() == 'desc':
        tasks = tasks.order_by(f'-{sortBY}')
   else:
        tasks = tasks.order_by(sortBY)

   return tasks

def sort_projectmembers(sortBY,sortType,project_members):
   if sortType.lower() == 'desc':
        project_members = project_members.order_by(f'-{sortBY}')
   else:
        project_members = project_members.order_by(sortBY)

   return project_members