from datetime import datetime
from app import app, db
from models.year import Year
from models.fact import Fact, Comment
from models.user import UserSchema

user_schema = UserSchema()

with app.app_context():
    db.drop_all()
    db.create_all()


#USER login

    sim, errors = user_schema.load({
    'username': 'sim',
    'email': 'sim@email',
    'password': 'pass',
    'password_confirmation': 'pass'
    })

    if errors:
        raise Exception(errors)


    year1938 = Year(
    year=1938
    )

    anschluss = Fact(
    name='Anschluss',
    location='Austria',
    date_of_fact=datetime.strptime('1938-03-12', '%Y-%m-%d'),
    bio='The union of Austria and Germany was forbidden by the Treaty of Versailles. The treaty was deeply resented by both countries for its allocation of war guilt and imposition of heavy reparations. When the German army marched into Austria in March 1938, they were welcomed by cheering crowds of Austrians.',
    image='http://3.bp.blogspot.com/-qPePlUTpi0w/UWB-g_fXh7I/AAAAAAAAD5U/f117mRIN7Uo/s1600/Ovation+for+Hitler+in+the+Reichstag+after+announcing+the+successful+Anschluss+-+March+1938.jpg',
    year=year1938,
    creator=sim
    )

    kindertransport = Fact(
    name='First refugee children of the Kindertransport arrive in Britain',
    location='Britain',
    date_of_fact=datetime.strptime('1938-02-12', '%Y-%m-%d'),
    bio='A total of 10,000 Jewish children between the ages of five and 17 were sent from Germany, Austria and Czechoslovakia to Britain between December 1938 and the outbreak of war in September 1939. Many were given homes by British families, or lived in hostels. Very few of them saw their parents again.',
    image='http://ww2forschools.weebly.com/uploads/1/8/3/3/18336943/711957.jpg?398',
    year=year1938,
    creator=sim
    )

    comment_one = Comment(
    content="I did not know this happened. Great fact",
    fact=anschluss
    )

    year1939 = Year(
    year=1939
    )

    britain = Fact(
    name='Britain guarantees territorial integrity of Poland',
    location='Britain',
    date_of_fact=datetime.strptime('1939-03-31', '%Y-%m-%d'),
    bio='This guarantee formally ended the policy of appeasement, and the British government reluctantly began to prepare for war. Conscription was introduced for the first time in peacetime on 27 April, with little protest. On 23 August, the German-Soviet Non-Aggression Pact put paid to British hopes of a Russian ally. Prime Minister Neville Chamberlain warned Adolf Hitler that Britain would support Poland if it was attacked by Germany.',
    image='https://i.pinimg.com/236x/81/41/73/814173b0f34b713ae0d933c37b7ddbb2--appeasement-modern-history.jpg',
    year=year1939,
    creator=sim
    )

    db.session.add(sim)
    db.session.add(year1938)
    db.session.add(anschluss)
    db.session.add(kindertransport)
    db.session.add(comment_one)
    db.session.add(year1939)
    db.session.add(britain)

    db.session.commit()
