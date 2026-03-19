from flask import Flask
import importlib
import os
import pkgutil

from blueprints.main import bp as main_bp


def load_plugins(app: Flask) -> None:
    package_name = "plugins"
    plugins_dir = os.path.join(os.path.dirname(__file__), package_name)
    if not os.path.isdir(plugins_dir):
        return

    requested = os.getenv("PLUGINS")
    if requested:
        module_names = [name.strip() for name in requested.split(",") if name.strip()]
    else:
        module_names = [module.name for module in pkgutil.iter_modules([plugins_dir])]

    for name in module_names:
        module = importlib.import_module(f"{package_name}.{name}")
        if hasattr(module, "register"):
            module.register(app)
        elif hasattr(module, "bp"):
            app.register_blueprint(module.bp)


def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(main_bp)

    load_plugins(app)
    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)
