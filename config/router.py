from app import app
from controllers import facts

app.register_blueprint(facts.api, url_prefix='/api')
