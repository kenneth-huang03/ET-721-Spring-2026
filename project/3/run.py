
from app import create_app

app = create_app()

if __name__ == "__main__":
    import os
    if os.environ.get("_A_A_"):
        from werkzeug.middleware.proxy_fix import ProxyFix
        app.wsgi_app = ProxyFix(app.wsgi_app, x_prefix=1)

    app.run(debug=True)

# if __name__ == '__main__':
#    app.run(host='0.0.0.0', debug=True)
