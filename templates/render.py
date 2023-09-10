from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('templates'))
templates = ['index.html', 'planes.html', 'programas.html']

for template in templates:
    tmp = env.get_template(template)
    out = tmp.render()
    location = "C:\\Users\\Virginia\\Documents\\GitHub\\ifitgym.cl\\{}".format(template)
    with open(location, "w", encoding="utf-8") as f:
        f.write(out)
print("Listo")
