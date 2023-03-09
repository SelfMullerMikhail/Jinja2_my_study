from jinja2 import Template

cars = [
        {'model': 'BMW', 'price': 100000},
        {'model': 'Mercedes', 'price': 200000},
        {'model': 'Audi', 'price': 300000},
        {'model': 'Lada', 'price': 400000},
        {'model': 'Volvo', 'price': 500000},
]

digs = [1, 2, 3, 4, 5]

# tpl = "Summ of price for auto {{ cs | sum(attribute = 'price')}}"
# tpl = "Summ of price for auto {{ cs | max(attribute = 'price')}}"
# tpl = "Summ of price for auto {{ cs | random }}"
tpl = "Summ of price for auto {{ cs | replace('o', 'O') }}"
tm = Template(tpl)
msg = tm.render(cs = cars)
# print(msg)

persons = [{'name': 'Misha', 'age': 25, 'weight': 80},
        {'name': 'Vasya', 'age': 30, 'weight': 90},
        {'name': 'Petya', 'age': 35, 'weight': 100}]

tpl = """ 
{%- for u in users -%}
{% filter upper %}{{u.name}}{% endfilter %}
{% endfor %}
"""
tm = Template(tpl)
msg = tm.render(users = persons)
# print(msg)

html = """
{%- macro input(name, value='', type='text', size=20) -%}
    <input type='{{ type }}' name='{{ name }}' value='{{ value|e }}' size='{{ size }}'>
{%- endmacro %}

<p>{{ input('username') }}
<p>{{ input('mail') }}
<p>{{ input('password') }}
"""

tm = Template(html)
msg = tm.render()
# print(msg)



html = """
{% macro list_users(list_of_user) -%}
<ul>
{% for u in list_of_user -%}
 <li>{{u.name}} {{caller(u)}}
{%- endfor %}
</ul>
{%- endmacro -%}

{% call(user) list_users(users) %}
<ul>
<li>age: {{user.age}}
<li>weight: {{user.weight}}
</ul>
{% endcall %}
"""

tm = Template(html)
msg = tm.render(users=persons)
print(msg)