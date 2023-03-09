from jinja2 import Environment, FileSystemLoader, FunctionLoader

persons = [{'name': 'Misha', 'age': 25, 'weight': 80},
        {'name': 'Vasya', 'age': 30, 'weight': 90},
        {'name': 'Petya', 'age': 35, 'weight': 100}]

def func(path):
    if path == "index":
        return """Name: {{users.name}}, age: {{users.age}}"""
    else:
        return """Data: {{users}}"""

# file_loader = FileSystemLoader('templates')
file_loader = FunctionLoader(func)

env = Environment(loader=file_loader)

# tm = env.get_template('main.htm') #Template
tm = env.get_template('index')

msg = tm.render(users=persons[0])
print(msg)

