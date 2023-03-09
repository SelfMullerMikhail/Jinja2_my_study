from jinja2 import Template

data = "Just some example data and text = {{ name }}"

tm = Template(data)
msg = tm.render(name="Misha")

print(msg)

cities = [{'id':1, 'name':'New York'}, 
        {'id':2, 'name':'London'},
        {'id':3, 'name':'Paris'},
        {'id':4, 'name':'Moscow'},
        {'id':5, 'name':'Berlin'}]
link = """<select name="cities">
{% for c in cities -%}
{% if c.id >2 -%}
<option value = {{c.id}}>{{c.name}}</option>
{% elif c.id == 2 -%}
{{c.name}} = special city
{% else -%}
{{c.name}}
{% endif -%}
 {% endfor -%}
</select>"""

tm = Template(link)
msg = tm.render(cities=cities) 
print(msg)