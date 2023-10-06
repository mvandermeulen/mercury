
import os
from routes import health
import middleware.auth_guard as auth_guard
from routes.user import user

v = os.environ['API_VERSION']

def import_resources(app):
    app.include_router(health.router, tags=['Information'], prefix=f'/{v}')
    app.include_router(auth_guard.router, tags=['Access Token'], prefix=f'/{v}')
    app.include_router(user.router, tags=['User'], prefix=f'/{v}/user')