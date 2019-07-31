import os
from app import app
from controllers import facts, auth, years

app.register_blueprint(facts.api, url_prefix='/api')
app.register_blueprint(years.api, url_prefix='/api')
app.register_blueprint(auth.api, url_prefix='/api')


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):

    if os.path.isfile('dist/' + path):
        return app.send_static_file(path)

    return app.send_static_file('index.html')