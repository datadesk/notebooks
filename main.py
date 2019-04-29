import csv
import jinja2

loader = jinja2.FileSystemLoader(searchpath="./templates/")
env = jinja2.Environment(loader=loader)


def render():
    # Read in the notebook
    object_list = list(csv.DictReader(open("./notebooks.csv", 'r')))

    # Render the template
    template = env.get_template("README.md")
    md = template.render(object_list=object_list, count=len(object_list))

    # Write out the README
    with open("./README.md", "w") as fh:
        fh.write(md)


if __name__ == '__main__':
    render()
