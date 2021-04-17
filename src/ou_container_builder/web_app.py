"""Build containers housing a single web application."""
from jinja2 import Environment


def generate(env: Environment, settings: dict):
    """Generate the Dockerfile for a single web application.

    :param env: The Jinja2 environment to use for loading and rendering templates
    :type env: :class:`~jinja2.environment.Environment`
    :param settings: The settings parsed from the configuration file
    :type settings: dict
    """
    with open('build/Dockerfile', 'w') as out_f:
        if settings['type'] == 'web-app':
            tmpl = env.get_template('dockerfile/web-app.jinja2')
        out_f.write(tmpl.render(**settings))

    with open('build/start-web-app.sh', 'w') as out_f:
        tmpl = env.get_template('start-web-app.sh')
        out_f.write(tmpl.render(**settings))
