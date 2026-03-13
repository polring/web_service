from flask import Flask
import importlib
import os
import pkgutil


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

    @app.get("/")
    def home():
        return """
        <!doctype html>
        <html lang="ko">
          <head>
            <meta charset="utf-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1" />
            <title>소개</title>
            <style>
              :root {
                color-scheme: light;
              }
              body {
                margin: 0;
                font-family: "Georgia", "Times New Roman", serif;
                background: linear-gradient(140deg, #f7f0e8 0%, #e8f0f7 100%);
                color: #1a1a1a;
              }
              .wrap {
                max-width: 860px;
                margin: 0 auto;
                padding: 72px 24px 96px;
              }
              h1 {
                font-size: 44px;
                line-height: 1.1;
                margin: 0 0 16px;
              }
              p {
                font-size: 18px;
                line-height: 1.7;
                margin: 0 0 16px;
              }
              .card {
                background: #ffffffcc;
                border: 1px solid #e6e6e6;
                border-radius: 16px;
                padding: 28px;
                box-shadow: 0 12px 30px rgba(0, 0, 0, 0.06);
              }
              ul {
                margin: 12px 0 0 18px;
                padding: 0;
                font-size: 17px;
              }
              li {
                margin-bottom: 8px;
              }
              @media (max-width: 600px) {
                h1 {
                  font-size: 34px;
                }
              }
            </style>
          </head>
          <body>
            <div class="wrap">
              <h1>안녕하세요, 저는 전민제입니다.</h1>
              <div class="card">
                <p>이 페이지는 Flask로 만든 간단한 자기소개 홈 화면입니다.</p>
                <p>관심 분야와 사용 기술을 아래에 정리했습니다.</p>
                <ul>
                  <li>관심 분야: 웹 개발, 자동화, 오픈소스</li>
                  <li>기술: Java,Spring,jpa,mysql</li>
                  <li>현재 목표: 깔끔하고 유지보수 쉬운 서비스 만들기</li>
                </ul>
              </div>
            </div>
          </body>
        </html>
        """

    load_plugins(app)
    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)
