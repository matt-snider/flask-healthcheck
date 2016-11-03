registered_extensions = {}


def register_extension(healthcheck_name=None):
    def decorator(healthcheck_func):
        ext_name = healthcheck_func.__name__
        registered_extensions[ext_name] = (healthcheck_name, healthcheck_func)
        return healthcheck_func

    # If called without parameters
    if callable(healthcheck_name):
        healthcheck_func = healthcheck_name
        healthcheck_name = healthcheck_func.__name__
        decorator = decorator(healthcheck_func)
    return decorator


@register_extension('sql')
def sqlalchemy(db):
    with db.engine.connect() as connection:
        connection.execute('SELECT 1;')
    return True


@register_extension('mongodb')
def pymongo(mongo):
    mongo.db.command('ping')
    return True


@register_extension('mongodb')
def mongoengine(mongo):
    mongo.connection.command('ping')
    return True


@register_extension
def redis(db):
    db.ping()
    return True

