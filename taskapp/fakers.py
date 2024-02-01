from faker import Faker
from  .models import Tasks, Projects, User
fake = Faker()

def generate_fake_tasks(num_tasks):
    tasks = []

    projects = Projects.objects.all()
    users = User.objects.all()

    for _ in range(num_tasks):
        task_data = {
            'name': fake.name(),
            'description': fake.text(),
            'status': fake.random_element(['PENDING', 'COMPLETED', 'CANCELLED']),
            'start_date': fake.date_this_decade(),
            'end_date': fake.date_this_decade(),
            'project': fake.random_element(projects),
            'created_by': fake.random_element(users),
        }
        tasks.append(Tasks(**task_data))

    return tasks


