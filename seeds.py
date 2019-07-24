from datetime import datetime
from app import app, db
from models.year import Year
from models.fact import Fact

with app.app_context():
    db.drop_all()
    db.create_all()

year1938 = Year(
    year=1938
)

anschluss = Fact(
    name='Anschluss',
    date_of_fact=datetime.strptime('1938-03-12', '%Y-%m-%d'),
    bio='The union of Austria and Germany was forbidden by the Treaty of Versailles. The treaty was deeply resented by both countries for its allocation of war guilt and imposition of heavy reparations. When the German army marched into Austria in March 1938, they were welcomed by cheering crowds of Austrians.',
    image='image_url',
    year=year1938
 )

kindertransport = Fact(
    name='First refugee children of the Kindertransport arrive in Britain',
    date_of_fact=datetime.strptime('1938-02-12', '%Y-%m-%d'),
    bio='A total of 10,000 Jewish children between the ages of five and 17 were sent from Germany, Austria and Czechoslovakia to Britain between December 1938 and the outbreak of war in September 1939. Many were given homes by British families, or lived in hostels. Very few of them saw their parents again.',
    image='image_url',
    year=year1938
)


db.session.add(year1938)
db.session.add(anschluss)
db.session.add(kindertransport)

db.session.commit()
