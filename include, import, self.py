from jinja2 import Environment, FileSystemLoader, FunctionLoader

subs = ["Math", "Lenguage", "Infromation"]

persons = [{'name': 'Misha', 'age': 25, 'weight': 80},
        {'name': 'Vasya', 'age': 30, 'weight': 90},
        {'name': 'Petya', 'age': 35, 'weight': 100}]

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

# tm = env.get_template("page.htm")
tm = env.get_template("about.htm")
msg = tm.render(list_table=subs)
print(msg)

