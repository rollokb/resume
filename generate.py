import sys

from jinja2 import Template


def generate():
    with open('./resume.md') as f:
        template = f.read()

    tem = Template(template)

    sys.stdout.write(tem.render(**{
        'title': 'Curriculum Vitae',
    }))


if __name__ == '__main__':
    generate()
