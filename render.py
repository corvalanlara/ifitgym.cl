from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('templates'))
templates = ['index.html', 'planes.html', 'programas.html']

for template in templates:
    tmp = env.get_template(template)
    out = tmp.render()
    location = "/home/cheshire/gym/gymweb/rendered/{}".format(template)
    with open(location, "w") as f:
        f.write(out)
print("Listo")
