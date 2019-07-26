from app import app
from controllers import facts, auth, years

app.register_blueprint(facts.api, url_prefix='/api')
app.register_blueprint(years.api, url_prefix='/api')
app.register_blueprint(auth.api, url_prefix='/api')
