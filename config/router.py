from app import app
from controllers import facts, auth

app.register_blueprint(facts.api, url_prefix='/api')
app.register_blueprint(auth.api, url_prefix='/api')
