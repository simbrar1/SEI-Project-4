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

    kindertransport = Fact(
    name='First refugee children of the Kindertransport arrive in Britain',
    location='Britain',
    date_of_fact=datetime.strptime('1938-02-12', '%Y-%m-%d'),
    bio='A total of 10,000 Jewish children between the ages of five and 17 were sent from Germany, Austria and Czechoslovakia to Britain between December 1938 and the outbreak of war in September 1939. Many were given homes by British families, or lived in hostels. Very few of them saw their parents again.',
    image='http://ww2forschools.weebly.com/uploads/1/8/3/3/18336943/711957.jpg?398',
    year=year1938,
    creator=sim
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

    comment_one = Comment(
    content="I did not know this happened. Great fact",
    fact=anschluss
    )

    munich_agreement = Fact(
    name='The Treaty of Munich',
    location='Europe',
    date_of_fact=datetime.strptime('1938-09-28', '%Y-%m-%d'),
    bio='The Munich Conference between Britains Neville Chamberlain, Germanys Adolf Hitler, Italys Benito Mussolini and Edouard Daladier of France agreed that the Czechoslovakian territory of the Sudetenland and its three million ethnic Germans should be joined with Germany. Chamberlain returned to Britain claiming he had achieved peace in our time. In fact, it would come to be a clear demonstration that appeasement did not work, as by March 1939 Hitler had seized the rest of Czechoslovakia.',
    image='https://www.thoughtco.com/thmb/McvXOi5YG-s6Qe3PUpSU7DdwEgw=/768x0/filters:no_upscale():max_bytes(150000):strip_icc()/munich-agreement-large-56a61c5c3df78cf7728b64ee.jpg',
    year=year1938,
    creator=sim
    )

    kristallnacht = Fact(
    name='The Kristallnacht proves that Jews have no future in Germany',
    location='Germany',
    date_of_fact=datetime.strptime('1938-11-09', '%Y-%m-%d'),
    bio='On 9 and 10 November 1938, Nazis throughout Germany, Austria, and Sudetenland (in the current Czech Republic) took action against Jews. They humiliated Jews in parades, abused them and put them in concentration camps. They also destroyed Jewish property. Such violent attacks on Jews are called pogroms.Because of the many broken windows, this particular pogrom is called the Kristallnacht, the Night of Broken Glass. Synagogues were set on fire and the fire department was not allowed to put the fires out. The Jews had to pay for the damage themselves and were fined a total of 1 billion Reichsmark by the government.The Kristallnacht showed how the Nazi hatred of the Jews had turned into aggression and persecution - and how hardly anyone stood up for the Jews.',
    image='https://360.rollins.edu/assets/images/uploads/made/assets/images/uploads/posts/Kristallnacht-Commemoration_717_478_s.jpg',
    year=year1938,
    creator=sim
    )

    year1939 = Year(
    year=1939
    )

    poland = Fact(
    name='Nazis Invades Czechoslovakia',
    location='Czechoslovakia',
    date_of_fact=datetime.strptime('1939-03-03', '%Y-%m-%d'),
    bio='Despite the assurances given by Hitler in the Treaty of Munich (Sept 1938), he marched into Czechoslovakia and occupied the country.',
    image='http://extravaganzafreetour.com/wp-content/uploads/2017/03/Bundesarchiv_Bild_183-2004-1202-505_Prag_Burg_Besuch_Adolf_Hitler.jpg',
    year=year1939,
    creator=sim
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
    britain_declare_war = Fact(
    name='Britain declares war on Germany',
    location='Britain',
    date_of_fact=datetime.strptime('1939-09-03', '%Y-%m-%d'),
    bio='On 1 September, German forces invaded Poland. Prime Minister Neville Chamberlain still hoped to avoid declaring war on Germany, but a threatened revolt in the cabinet and strong public feeling that Hitler should be confronted forced him to honour the Anglo-Polish Treaty. Britain was at war with Germany for the second time in 25 years. France also declares war in Germany and marches with Britain',
    image='https://images.immediate.co.uk/production/volatile/sites/7/2018/01/0111709WW2Timeline-ed1f70d.jpg?quality=90&resize=620,413',
    year=year1939,
    creator=sim
    )

    year1940 = Year(
    year=1940
    )
    denmark_norway_invasion = Fact(
    name='The German invasion of Denmark and Norway',
    location='Denmark and Norway',
    date_of_fact=datetime.strptime('1940-04-09', '%Y-%m-%d'),
    bio='Under the code name Operation Weserübung, Nazi Germany attacked Denmark and Norway on 9 April 1940. On that same day, Denmark surrendered and was occupied. The country was a useful base of operations for the fight against Norway. The Norwegians resisted for two months but surrendered on 9 June 1940. France and Britain helped Norway but were forced to withdraw when they were attacked themselves.At the time of the German attack, Denmark and Norway were neutral. Germany still attacked the countries because it feared that Great Britain and France planned to occupy Norway. With Denmarks access to the Baltic Sea in German hands, Swedish iron ore could be transported undisturbed to Germany. Sweden remained neutral.',
    image='https://assets.sutori.com/user-uploads/image/1921b43d-a493-4d2b-b188-1c842869eb83/8b78017f6a391273ab6676ab157027f3.jpeg',
    year=year1940,
    creator=sim
    )
    churchill = Fact(
    name='Winston Churchill becomes prime minister of the coalition government',
    location='England',
    date_of_fact=datetime.strptime('1940-05-10', '%Y-%m-%d'),
    bio='Following the disastrous Norwegian campaign, Prime Minister Neville Chamberlain faced heavy criticism at home. By early May, Chamberlain had lost the confidence of the House of Commons. Labour ministers refused to serve in a national coalition with Chamberlain as leader, so he resigned. Churchill became prime minister on 10 May, the same day Germany invaded Holland and Belgium.',
    image='https://assets.sutori.com/user-uploads/image/1921b43d-a493-4d2b-b188-1c842869eb83/8b78017f6a391273ab6676ab157027f3.jpeg',
    year=year1940,
    creator=sim
    )
    europe_invasion = Fact(
    name='Germany invades the Netherlands, Belgium, and France',
    location='Europe',
    date_of_fact=datetime.strptime('1940-05-10', '%Y-%m-%d'),
    bio='On 10 May 1940, Germany invaded the Netherlands, Belgium, Luxembourg, and France. Luxembourg was occupied that same day. The Netherlands surrendered on 15 May, Belgium on the 28th. At first, Great Britain supported the Netherlands, Belgium, and France, but it withdrew later.On 5 June, the Wehrmacht, the German army, launched a major attack on France. On 14 June, the German army occupied Paris. The French government and many Parisians had already fled the city by then. The French government failed to lead its army properly and they lost the trust of their people. The French Prime Minister resigned and was succeeded by Marshal Philippe Pétain.On 22 June, the French army signed the capitulation in a railway carriage near Compiègne, a small town 60 kilometres to the north of Paris. The location bore special significance for the Germans. This was the place where Germany had signed its surrender in 1918, at the end of the First World War. Many Germans had considered it a great humiliation.Germany did not occupy all of France. South of the front line, there was a new French government led by Marshal Pétain. This Vichy regime, named after the health resort where the government was based, collaborated with the Germans. Not all French people accepted the new situation. Some joined the resistance and others fled to London. General Charles de Gaulle founded the Free French there, with the aim of fighting the German occupation of France.',
    image='https://annefrank.freetls.fastly.net/media/filer_public_thumbnails/filer_public/73/b3/73b39df2-bafe-4b8e-a093-809af4664852/ba_183-r99057.jpg__1536x1536_q85_subsampling-2.jpg',
    year=year1940,
    creator=sim
    )
    dunkirk = Fact(
    name='Thousands of Allied troops are evacuated from Dunkirk, France',
    location='France',
    date_of_fact=datetime.strptime('1940-05-26', '%Y-%m-%d'),
    bio='Allied forces were utterly overwhelmed by the German blitzkrieg in France. Thousands of soldiers were trapped in a shrinking pocket of territory centred around the French seaside town of Dunkirk. The Royal Navys Operation Dynamo succeeded in evacuating approximately 338,000 British and French troops in destroyers and hundreds of little ships - volunteers who sailed to France in their own vessels - over a period of ten days, while under constant attack from the Luftwaffe (German air force).',
    image='https://timedotcom.files.wordpress.com/2017/05/dunkirk.jpeg',
    year=year1940,
    creator=sim
    )
    battle_britain = Fact(
    name='The Battle of Britain',
    location='Britain',
    date_of_fact=datetime.strptime('1940-08-13', '%Y-%m-%d'),
    bio='Shortly after the conquest of Western Europe, Germany attacked the United Kingdom. It had to do so by air because the British Navy was stronger than the German Navy. In July 1940, Germany started making air raids on ports and ships, airports, and places along the coast of England. Hitler had planned to invade England with an army, but this turned out to be impracticable because the German Air Force was unable to gain the upper hand. On 25 August 1940, the British Air Force bombed Berlin. This counter-attack did not cause much damage, but it did change the German plans.Starting on 7 September, London was bombed for 57 consecutive days, and other English cities were hit hard as well. The German air raids continued into the autumn of 1941. They are collectively called "The Blitz", after the German word for lightning.The Battle of Britain cost 27,450 lives and even more people were wounded. More than a million houses were destroyed. But the United Kingdom did not succumb, and Germany lost the Battle of Britain.',
    image='https://upload.wikimedia.org/wikipedia/commons/8/82/Heinkel_He_111_during_the_Battle_of_Britain.jpg',
    year=year1940,
    creator=sim
    )
    destroyers = Fact(
    name='Destroyers for bases agreement gives Britain 50 US destroyers',
    location='Britain',
    date_of_fact=datetime.strptime('1940-09-02', '%Y-%m-%d'),
    bio='In September 1940, US President Franklin Roosevelt signed an agreement to give Britain 50 obsolete American destroyers in exchange for the use of naval and air bases in eight British possessions. The lease was guaranteed for the duration of 99 years free from all rent and charges. Nonetheless, the US showed no sign yet of entering the war on the Allied side, as many in Britain hoped they would.',
    image='https://timedotcom.files.wordpress.com/2017/05/dunkirk.jpeg',
    year=year1940,
    creator=sim
    )

    year1941 = Year(
    year=1941
    )
    raids = Fact(
    name='Mass raids in Amsterdam. The first deportations of Dutch Jews',
    location='Amersterdam',
    date_of_fact=datetime.strptime('1941-02-22', '%Y-%m-%d'),
    bio='On Saturday 22 and Sunday 23 February 1941, the Ordnungspolizei (German police) rounded up Jewish men at Jonas Daniël Meijerplein in Amsterdam. 427 men between the ages of 18 and 35 were arrested, forcibly pushed into lorries and deported. The razzia was Nazi punishment for fights that had occurred between Jews, antisemitic thugs, and the German police. In the weeks prior to the raid, the atmosphere in Amsterdam had been turbulent. Assault groups of the NSB (the Dutch National-Socialist Movement) had constantly been looking to confront Jews. This had caused a lot of fighting. On 11 February, an NSB member was so badly injured that he died a few days later. The anti-Semitic press blamed it all on the Jews.The Jews who were arrested were taken to Camp Schoorl. From there, they were deported to the Mauthausen concentration camp in Austria, where all but one of them died.',
    image='https://annefrank.freetls.fastly.net/media/filer_public_thumbnails/filer_public/7b/75/7b7502eb-8bf7-4043-ab16-e4ae2cdee46c/4097_newline.jpg__1536x1536_q85_subsampling-2.jpg',
    year=year1941,
    creator=sim
    )
    barbarossa = Fact(
    name='Hitler attacks Russia – Operation Barbarossa',
    location='Russia',
    date_of_fact=datetime.strptime('1941-06-22', '%Y-%m-%d'),
    bio='Hitler sent 3 million soldiers and 3,500 tanks into Russia. The Russians were taken by surprise as they had signed a treaty with Germany in 1939. Stalin immediately signed a mutual assistance treaty with Britain and launched an Eastern front battle that would claim 20 million casualties. The USA, which had been supplying arms to Britain under a ‘Lend-Lease’ agreement, offered similar aid to USSR.',
    image='https://cdn.britannica.com/s:500x350/30/180230-049-FD9B1A51.jpg',
    year=year1941,
    creator=sim
    )
    pearl_harbour = Fact(
    name='Pearl Harbour',
    location='Hawaii',
    date_of_fact=datetime.strptime('1941-12-07', '%Y-%m-%d'),
    bio='On Sunday morning, 7 December 1941, a Japanese war fleet arrived at the American naval base at Pearl Harbor, on Hawaii. The Japanese bombarded the Americans with bombs and torpedoes. When the attack was over, more than 3,500 American were left dead or wounded. Eighteen warships had been sunk and hundreds of aircraft had been destroyed or damaged.Japan attacked the United States to prevent the Americans from thwarting Japanese plans for expansion in Asia. The surprise attack was carried out to perfection, but Japan did not defeat the US. The damage caused was soon repaired and the main American aircraft carriers were in other ports at the time of the attack. The United States were able to retaliate quickly.On that same day, Japan also attacked Singapore, Malaysia, Hong Kong, Thailand, as well as American bases in the Philippines and Guam. As a result, Japan was now at war with Great Britain and Canada. Australia, New Zealand and the Netherlands also declared war on Japan, and the war spread rapidly across the East-Asia.The American population regarded the attack as a cowardly act and stood behind its governments decision to declare war on Japan. In response, Hitler declared war on America on 11 December 1941, for Germany was an ally of Japan. This meant that Hitler had gained another strong opponent. From then on, the United States fought with the Allies against Nazi Germany.',
    image='https://annefrank.freetls.fastly.net/media/filer_public_thumbnails/filer_public/10/97/1097b1d6-5389-433f-8e7c-9073a20890ed/nara_ww2-126.jpg__1536x1536_q85_subsampling-2.jpg',
    year=year1941,
    creator=sim
    )


    year1942 = Year(
    year=1942
    )
    yellow_badge = Fact(
    name='The introduction of the yellow badge in the Netherlands',
    location='Netherlands',
    date_of_fact=datetime.strptime('1942-05-03', '%Y-%m-%d'),
    bio='On 29 April 1942, the Nazis introduced another humiliating measure that concerned the Dutch Jews. From 3 May onwards, they would have to start wearing a badge on their clothes: a six-pointed yellow Star of David with the word Jew in the middle.The badge made it possible to identify people in the street as Jews. The Nazis wanted to further isolate the Jews from the non-Jewish Dutch. Not wearing the badge was severely punished. You could even be sent to a concentration camp if you didn’t.The Jewish Council was ordered to distribute the badges among the Dutch Jews within three days. The Jews were forced to buy four each at four cents a piece. Children from the age of 6 had to wear them, too. In total, 569,355 yellow badges were distributed.Some Jews wore them with pride, many others felt humiliated. Some non-Jewish Dutch responded to the new measure as well. Some protested by wearing homemade stars with the words Catholic or Aryan. Others made a point of greeting Jews in the street or giving up their seats on the trams. But over time, the indignation diminished and the gap between Jews and non-Jews widened.',
    image='https://annefrank.freetls.fastly.net/media/filer_public_thumbnails/filer_public/14/7b/147b04fa-5f25-4184-be7d-942770f173fe/jodenster_1942_nederland.jpg__1536x1536_q85_subsampling-2.jpg',
    year=year1942,
    creator=sim
    )


    db.session.add(sim)
    db.session.add(comment_one)
    db.session.add(year1938)
    db.session.add(kristallnacht)
    db.session.add(anschluss)
    db.session.add(kindertransport)
    db.session.add(munich_agreement)



    db.session.add(year1939)
    db.session.add(poland)
    db.session.add(britain)
    db.session.add(britain_declare_war)

    db.session.add(year1940)
    db.session.add(denmark_norway_invasion)
    db.session.add(churchill)
    db.session.add(europe_invasion)
    db.session.add(dunkirk)
    db.session.add(battle_britain)
    db.session.add(destroyers)

    db.session.add(year1941)
    db.session.add(raids)
    db.session.add(barbarossa)
    db.session.add(pearl_harbour)

    db.session.add(year1942)
    db.session.add(yellow_badge)

    db.session.commit()
