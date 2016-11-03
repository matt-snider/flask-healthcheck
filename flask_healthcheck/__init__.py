import functools

from flask import current_app, jsonify

from .extensions import registered_extensions


class Healthcheck:

    def __init__(self, app=None):
        if app:
            self.init_app(app)
        self.healthchecks = {}

    def __call__(self, healthcheck_func, name=None):
        if not name:
            name = healthcheck_func.__name__
        self.healthchecks[name] = healthcheck_func
        return healthcheck_func

    def init_app(self, app):
        rule = app.config.get('HEALTHCHECK_PATH', '/healthcheck')
        app.add_url_rule(rule, view_func=self.do_healthcheck)

    def do_healthcheck(self):
        response = {}
        ok = True

        for name, healthcheck in self.healthchecks.items():
            try:
                result = healthcheck()
                if isinstance(result, tuple):
                    state, message = result
                else:
                    state, message = result, None
            except Exception as e:
                state = False
                message = str(e)
            response[name] = {'healthy': state}
            if message:
                response[name]['message'] = message
            ok &= state
        return jsonify(response), 200 if ok else 500

    def add_extension(self, ext_name, ext_obj):
        if ext_name not in registered_extensions:
            raise ValueError("No built in healthcheck for extension '{}'"
                             .format(ext_name))
        name, func = registered_extensions[ext_name]
        self.healthchecks[name] = functools.partial(func, ext_obj)

