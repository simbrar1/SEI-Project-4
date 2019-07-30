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
    fact=anschluss,
    user=sim
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
    bio='On Sunday morning, 7 December 1941, a Japanese war fleet arrived at the American naval base at Pearl Harbor, on Hawaii. The Japanese bombarded the Americans with bombs and torpedoes. When the attack was over, more than 3,500 American were left dead or wounded. Eighteen warships had been sunk and hundreds of aircraft had been destroyed or damaged. Japan attacked the United States to prevent the Americans from thwarting Japanese plans for expansion in Asia. The surprise attack was carried out to perfection, but Japan did not defeat the US. The damage caused was soon repaired and the main American aircraft carriers were in other ports at the time of the attack. The United States were able to retaliate quickly. On that same day, Japan also attacked Singapore, Malaysia, Hong Kong, Thailand, as well as American bases in the Philippines and Guam. As a result, Japan was now at war with Great Britain and Canada. Australia, New Zealand and the Netherlands also declared war on Japan, and the war spread rapidly across the East-Asia.The American population regarded the attack as a cowardly act and stood behind its governments decision to declare war on Japan. In response, Hitler declared war on America on 11 December 1941, for Germany was an ally of Japan. This meant that Hitler had gained another strong opponent. From then on, the United States fought with the Allies against Nazi Germany.',
    image='https://annefrank.freetls.fastly.net/media/filer_public_thumbnails/filer_public/10/97/1097b1d6-5389-433f-8e7c-9073a20890ed/nara_ww2-126.jpg__1536x1536_q85_subsampling-2.jpg',
    year=year1941,
    creator=sim
    )


    year1942 = Year(
    year=1942
    )
    singapore_surrenders = Fact(
    name='British colony of Singapore surrenders to Japanese forces',
    location='Singapore',
    date_of_fact=datetime.strptime('1942-02-15', '%Y-%m-%d'),
    bio='This catastrophic defeat was a fatal blow to British prestige and signalled the fall of the empire in the Far East. The Japanese unexpectedly attacked down the Malay Peninsula instead of from the sea, where Singapores defences were concentrated. About 70,000 men were taken prisoner, many of whom would not survive the war due to the brutal conditions of their incarceration.',
    image='http://2.bp.blogspot.com/-q1OheduX02U/USDtBAaA2aI/AAAAAAAAAB4/mms8own5KYI/s1600/20080218-jsoldiers01+jap+in+shang+tales+of+old+shang.jpg',
    year=year1942,
    creator=sim
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
    midway = Fact(
    name='Battle of Midway',
    location='Midway Attol, Ocean',
    date_of_fact=datetime.strptime('1942-02-15', '%Y-%m-%d'),
    bio='The USA defeated the Japanese navy at the Battle of Midway. Following this victory, the US navy was able to push the Japanese back.',
    image='https://cdn.britannica.com/s:300x300/80/71380-004-B4724C34.jpg',
    year=year1942,
    creator=sim
    )
    stalingrad = Fact(
    name='Battle of Stalingard',
    location='Russia',
    date_of_fact=datetime.strptime('1942-11-12', '%Y-%m-%d'),
    bio='In the summer of 1942, Hitler launched a major offensive into southern Russia, seeking to destroy what was left of the Soviet Army and ultimately capture the Caucasus oilfields. The initial advance went well, and the German Sixth Army under General Friedrich von Paulus was ordered to capture the city. But Stalin demanded it be defended at all costs. Every available soldier and civilian was mobilised. Stalingrad was heavily bombed by the Luftwaffe, and the ruins became the scene for months of bitter street fighting. By October most of the city was in German hands, but the Russians clung onto the banks of the Volga, across which they ferried vital reserves.',
    image='https://cdni.rbth.com/rbthmedia/images/2018.02/article/5a746d7785600a37210db97e.jpg',
    year=year1942,
    creator=sim
    )


    year1943 = Year(
    year=1943
    )
    leave_amsterdam = Fact(
    name='All Jews must leave Amsterdam',
    location='Amsterdam, Netherlands',
    date_of_fact=datetime.strptime('1943-05-20', '%Y-%m-%d'),
    bio='On 20 May 1943, approximately 750 Jews reported to the military police building near Muiderpoort train station in Amsterdam. They complied with a measure taken by Rauter, head of the German SS and the police, that no Jew could stay in Amsterdam without permission. Only Jews carrying a so-called Sperre, a proof of postponement, were allowed to stay on.They arrived in Westerbork in the evening. At least two of them, a couple, were put on transport five days later to the Sobibor extermination camp, where they were gassed on 28 May 1943. We do not know what happened to the others, because their names are not known.Rauter was dissatisfied with the low turnout on this day and so, the Germans held a big raid in the centre of Amsterdam a few days later. They arrested around 3,000 people, who were subsequently deported to Westerbork. The Nazis also forced the Jewish Council to take away the Sperre of a large number of Jews and to select them for transport to Westerbork.',
    image='https://annefrank.freetls.fastly.net/media/filer_public_thumbnails/filer_public/35/09/35093f1e-9e0b-47a0-94f7-7c752d73688b/niod_96789jpg.jpeg__1536x1536_q85_subsampling-2.jpg',
    year=year1943,
    creator=sim
    )
    last_raid = Fact(
    name='Last raid in Amsterdam: 17,000 Jews arrested',
    location='Amsterdam, Netherlands',
    date_of_fact=datetime.strptime('1943-06-20', '%Y-%m-%d'),
    bio='On Sunday, 20 June 1943, the Nazis held a major raid in Amsterdam. The action had been secretly prepared by the Nazis. German and Dutch police officers closed off neighbourhoods in the east and south of Amsterdam. This was where most of the Amsterdam Jews lived.From 3:30 in the morning, loudspeaker cars were driving around, ordering the Jews to report at assembly points. Those who did not come voluntarily were forcibly removed from their homes. The raid lasted well into the night and continued the next day. Approximately 5,500 Jews were arrested.A month later, the occupying forces held a smaller raid. On 29 September 1943, a final major raid was held. Approximately 10,000 Jews were arrested and taken to Camp Westerbork. There were now almost no Jews left in Amsterdam.',
    image='https://annefrank.freetls.fastly.net/media/filer_public_thumbnails/filer_public/e6/45/e64556e2-a51c-4512-976f-86e0d5a57115/niod_96799.jpg__1536x1536_q85_subsampling-2.jpg',
    year=year1943,
    creator=sim
    )
    sicily = Fact(
    name='First Allied troops land in Europe as invasion of Sicily begins',
    location='Sicily, Italy',
    date_of_fact=datetime.strptime('1943-07-10', '%Y-%m-%d'),
    bio='On 10 July 1943, the Allies started their invasion of Sicily, an island located off the southern tip of the Italian mainland. They brought troops and equipment ashore, by air and by sea. The bad weather made the operation difficult but also provided the element of surprise. The Germans and Italians were not expecting an attack in those strong winds.By the end of the first day, the Allies had conquered two ports. This allowed new troops to land quickly. After a fierce battle, the Allies gained ground. By the end of July, Germany and Italy started to withdraw their troops. Two weeks later, all of Sicily was in the hands of the Allies.From Sicily, the British and Americans were able to move into the Italian mainland and start liberating Europe.',
    image='https://annefrank.freetls.fastly.net/media/filer_public_thumbnails/filer_public/e2/cf/e2cf1d3c-5e1d-43c1-a645-68790bfef674/iwm_018.jpg__1536x1536_q85_subsampling-2.jpg',
    year=year1943,
    creator=sim
    )
    italy = Fact(
    name='Italy surrenders',
    location='Italy',
    date_of_fact=datetime.strptime('1943-09-03', '%Y-%m-%d'),
    bio='Mussolini had been thrown out of office and the new government of Italy surrendered to the British and the USA. They then agreed to join the allies. The Germans took control of the Italian army, freed Mussolini from imprisonment and set him up as head of a puppet government in Northern Italy. This blocked any further allied advance through Italy.',
    image='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTOfArG3HjGcj5UOu1AFwFuGFYQNqkxs7_TeSD6BXB34UrNraZjyw',
    year=year1943,
    creator=sim
    )

    year1944 = Year(
    year=1944
    )
    dday = Fact(
    name='D-Day: The Allied Forces land in France',
    location='Normandy, France',
    date_of_fact=datetime.strptime('1944-06-06', '%Y-%m-%d'),
    bio='On 6 June 1944, shortly after midnight, D-Day, a huge military operation, began. Over 5,000 ships transported 150,000 allied soldiers and 1,500 tanks to the coast of Normandy in France.For two years, the Allies had been preparing for Operation Overlord. The purpose of the operation was to set up a landing base on the European mainland. From there, the Allies would be able to liberate the countries that had been occupied by Germany and move on towards Berlin. And if Germany also had to fight in the West, it would make things a bit easier on the Soviet Union.The Allies landed in a few places along the coast of Normandy. The attack was backed up by bombardments and paratroopers. In some places, they were easily able to push back the German defence, but in others, resistance was fierce. On ‘Omaha Beach’, the American bombers did not manage to hit the German line of defence well. There, German troops shot down the soldiers trying to land. Some did not even get that far and drowned as soon as they left their ships.By the end of D-Day, the Allies had established a base on the mainland. The Germans tried to hold out as long as possible It took another two months of fighting in Normandy before the Allies succeeded in moving further into France. On 15 August, the Allies also landed in the south of France. Paris was liberated on 25 August and by mid-September 1944, the German army had almost been forced out of France.',
    image='https://annefrank.freetls.fastly.net/media/filer_public_thumbnails/filer_public/2d/a1/2da15230-bd27-4465-b04b-267ac2cb96a5/iwm_007.jpg__1536x1536_q85_subsampling-2.jpg',
    year=year1944,
    creator=sim
    )
    assassinate = Fact(
    name='German officers attempt to assassinate Hitler (Operation Valkyrie)',
    location='Wolfs Lair, Germany',
    date_of_fact=datetime.strptime('1944-07-20', '%Y-%m-%d'),
    bio='On 20 July 1944, during a meeting with Adolf Hitler, German officer Claus von Stauffenberg placed a bomb under the table. After Von Stauffenberg had left, the bomb went off. As if by a miracle, Hitler survived the attack. He had some burns and abrasions, and the bang had ruptured his eardrums. That very evening, his voice could be heard on German radio to let the people know that he was still alive.The conspiracy of which Von Stauffenberg was a member, had failed. A large number of German army officers had wanted to get rid of Hitler. The people involved each had their own reasons for participating in the conspiracy. Some wanted more influence and power, others wanted to prevent Hitler from destroying Germany in a senseless war.Shortly after the attempt, hundreds of arrests were made. The leaders of the attempt were sentenced to death in a show trial.',
    image='https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/Bundesarchiv_Bild_146-1972-025-10%2C_Hitler-Attentat%2C_20._Juli_1944.jpg/300px-Bundesarchiv_Bild_146-1972-025-10%2C_Hitler-Attentat%2C_20._Juli_1944.jpg',
    year=year1944,
    creator=sim
    )
    majdanek = Fact(
    name='Red Army discovers Majdanek camp',
    location='Lublin, Poland',
    date_of_fact=datetime.strptime('1944-07-22', '%Y-%m-%d'),
    bio='On 22 July 1944, Soviet troops reached the Polish city of Lublin. Here, they discovered the Majdanek labour and extermination camp, which was situated close to the city. The guards had already left.The Nazis had tried to erase their traces. Barracks had been demolished, bodies of murdered people had been burned, and the camp archives had been destroyed. But many barracks were still standing, and the gas chambers and some crematoria were still intact. Many prisoners had been left behind.Around 78,000 people were murdered in the camp, 59,000 of whom were Jews.It was the first concentration camp the Allies discovered. The Russians invited journalists to the camp. A month later, newspapers were writing about the evidence of the mass murder by the Nazis for the first time.',
    image='https://annefrank.freetls.fastly.net/media/filer_public_thumbnails/filer_public/24/38/2438fceb-3ed2-4aa9-aaea-66ba00943b9a/ushmm_754295.jpg__1536x1536_q85_subsampling-2.jpg',
    year=year1944,
    creator=sim
    )
    paris_france = Fact(
    name='Paris liberated',
    location='Paris, France',
    date_of_fact=datetime.strptime('1944-07-22', '%Y-%m-%d'),
    bio='On 25th August 1944 The French capital of Paris was liberated from the Germans, as allied troops stormed in and overthrew the enemy.',
    image='http://binaryapi.ap.org/cf559287f7e6da11af9f0014c2589dfb/preview.jpg?wm=api',
    year=year1944,
    creator=sim
    )

    year1945 = Year(
    year=1945
    )
    yalta = Fact(
    name='Allied leaders shape the post-war world at the Yalta Conference',
    location='Yalta',
    date_of_fact=datetime.strptime('1945-02-04', '%Y-%m-%d'),
    bio='The war leaders agreed that Germany should be forced to surrender unconditionally and would be divided into four zones between Britain, the Soviet Union, France and the United States. It was also agreed that the Soviet Union would enter the war against Japan after Germany was defeated.',
    image='https://upload.wikimedia.org/wikipedia/commons/0/05/Yalta_Conference_%28Churchill%2C_Roosevelt%2C_Stalin%29_%28B%26W%29.jpg',
    year=year1945,
    creator=sim
    )
    march = Fact(
    name='Death marches from the concentration camps',
    location='Germany',
    date_of_fact=datetime.strptime('1945-03-30', '%Y-%m-%d'),
    bio='By the summer of 1944, the Germans were losing more and more territory to the Soviet army. The front was shifting to the west so fast that the Nazis were afraid that their concentration and extermination camps would be discovered. And so, Himmler, head of the SS, decided to bring prisoners from Eastern Europe back to Germany. The camps would be emptier, the prisoners would not be able to tell the enemy anything, and they could still be used as forced labourers.First, the prisoners were brought west by train. But from the autumn onwards, with the Soviets advancing, the prisoners had to walk long distances. The prisoners called these marches death marches. Under severe winter weather conditions, they were made to walk hundreds of kilometres without warm clothes and shoes, food or shelter. Those who were unable to keep up, were shot or beaten to death. Chances of survival were very slim indeed.',
    image='https://annefrank.freetls.fastly.net/media/filer_public_thumbnails/filer_public/71/f9/71f9daae-df01-457e-8d7e-21076d6c5707/dachau-dodenmars.jpg__1536x1536_q85_subsampling-2.jpg',
    year=year1945,
    creator=sim
    )
    belsen = Fact(
    name='British troops liberate the concentration camp at Bergen-Belsen, Germany',
    location='Lower Saxony, Germany',
    date_of_fact=datetime.strptime('1945-04-15', '%Y-%m-%d'),
    bio='The liberation of Bergen-Belsen brought the horrors of Nazi genocide home to the British public when film and photographs of the camp appeared in British newspapers and cinemas. Conditions at Bergen-Belsen were so desperate that more than 10,000 prisoners died in the weeks after the liberation of the camp, despite the best efforts of the Allies to keep them alive. Millions were murdered to satisfy Nazi theories about racial-biological purity, at least six million of whom were Jews.',
    image='https://encyclopedia.ushmm.org/images/large/0de1e3b6-07b0-4bc4-80e5-e8cfe82ebe35.jpg.pagespeed.ce.9VEkIg3rNi.jpg',
    year=year1945,
    creator=sim
    )
    suicide = Fact(
    name='Hitler commits suicide',
    location='Underground Bunker Berlin, Germany',
    date_of_fact=datetime.strptime('1945-04-30', '%Y-%m-%d'),
    bio='The German leader, Adolf Hitler committed suicide in his bombproof shelter together with his mistress, Eva Braun, who he had, at the last minute, made his wife',
    image='https://www.history.com/.image/t_share/MTU3ODc3NjU2NDc3MDUwMTg1/this-day-in-history-04301945---hitler-commits-suicide.jpg',
    year=year1945,
    creator=sim
    )
    conquer = Fact(
    name='The Red Army conquers Berlin',
    location='Germany',
    date_of_fact=datetime.strptime('1945-05-02', '%Y-%m-%d'),
    bio='On 2 May 1945, Soviet troops occupied the Berlin Reichstag and planted the Soviet flag on its roof. It was the culmination of a two-week battle for the German capital. The military operation started on 16 April with a major attack on the Seelow Heights, the German defence line near the river Oder. During this attack, the Soviet army fired one million grenades. All night, the horizon was lit by explosions and the searchlights that dazzled the German army. After two days of heavy fighting, the Red Army broke through the German defence, and on 25 April, the Soviet army had surrounded Berlin. Hitler had ordered his troops to defend the city ‘to the last man’. The streets were barricaded, to stop the tanks and soldiers from coming through. Due to a shortage of soldiers, the boys of the Hitlerjugend and the old men of the Volkssturm were ordered to help defend the city. With their small arms and grenades, they did not stand a chance against the Red Army, and many of them died a pointless death. On 2 May, Helmuth Weidling, the commander of the Berlin defence forces, surrendered. Germany was now almost completely defeated. ',
    image='https://annefrank.freetls.fastly.net/media/filer_public_thumbnails/filer_public/1d/6c/1d6c8250-07fb-404d-907f-1f2709327a9d/sovjet-vlag-op-rijksdag-2-mei-1945-berlijn.jpg__1536x1536_q85_subsampling-2.jpg',
    year=year1945,
    creator=sim
    )
    ve = Fact(
    name='Britain celebrates the end of war on Victory in Europe Day',
    location='Europe',
    date_of_fact=datetime.strptime('1945-05-08', '%Y-%m-%d'),
    bio='German forces had been utterly defeated by the end of April 1945. Adolf Hitler committed suicide on 30 April as Soviet forces closed in on his Berlin bunker. The German Grand Admiral Karl Dönitz surrendered to Allied General Dwight Eisenhower in France on 7 May. The following day was officially celebrated in Britain as Victory in Europe Day. The entire country came to a standstill as people celebrated the end of war.',
    image='https://www.explorica.ca/-/media/Images/Landing%20Page%20Images/canadian-history/VE%20Day%20Image.ashx',
    year=year1945,
    creator=sim
    )
    election = Fact(
    name='Churchill loses election',
    location='Europe',
    date_of_fact=datetime.strptime('1945-07-05', '%Y-%m-%d'),
    bio='Winston Churchill lost the election to Clement Atlee’s Labour Party. The Labour party promised sweeping social reforms including nationalisation of the coal and railway industries and the creation of a welfare state. The Labour party gained 393 seats to the Conservatives 213. It was generally accepted that the landslide victory for Labour was due to the men and women of the armed services who did not want to resume civilian life under the conditions that they had before they entered service.?',
    image='http://www.may2015.com/wp-content/uploads/2014/12/3329137-1024x825.jpg',
    year=year1945,
    creator=sim
    )
    bomb = Fact(
    name='Victory over Japan Day marks the end of World War Two',
    location='Hiroshima, Nagasaki, Japan',
    date_of_fact=datetime.strptime('1945-08-15', '%Y-%m-%d'),
    bio='On 6 August, an atomic bomb was dropped on the Japanese city of Hiroshima by the American bomber Enola Gay. Three days later, a second bomb was dropped on the port city of Nagasaki. In all, 140,000 people perished. Less than a week later, the Japanese leadership agreed to an unconditional surrender, and the Emperor Hirohito broadcast his nations the capitulation over the radio. Victory over Japan day also marked the end of World War Two.',
    image='http://historyconflicts.com/wp-content/uploads/2017/04/hiroshima-bombing-article-about-atomic-bomb.jpg',
    year=year1945,
    creator=sim
    )
    nations = Fact(
    name='United Nations comes into existence with Britain as a founder member',
    location='Europe',
    date_of_fact=datetime.strptime('1945-10-24', '%Y-%m-%d'),
    bio='At the Yalta Conference in early 1945, the Big Three of Britains Winston Churchill, US President Franklin D Roosevelt and Soviet leader Joseph Stalin agreed to establish a new global organisation - the United Nations. The structure and charter of the organisation were established at another conference in San Francisco. Britain became one of the five security council members, with a power of veto. On 24 October, the UN officially came into existence when its members ratified its charter.',
    image='https://www.norway.no/contentassets/b898d76a601844e8b523ec3ce623ccbd/236062.jpg?preset=large&v=38052596',
    year=year1945,
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
    db.session.add(singapore_surrenders)
    db.session.add(midway)
    db.session.add(stalingrad)


    db.session.add(year1943)
    db.session.add(leave_amsterdam)
    db.session.add(last_raid)
    db.session.add(sicily)
    db.session.add(italy)

    db.session.add(year1944)
    db.session.add(dday)
    db.session.add(assassinate)
    db.session.add(majdanek)
    db.session.add(paris_france)

    db.session.add(year1945)
    db.session.add(yalta)
    db.session.add(belsen)
    db.session.add(march)
    db.session.add(suicide)
    db.session.add(conquer)
    db.session.add(ve)
    db.session.add(election)
    db.session.add(bomb)
    db.session.add(nations)

    db.session.commit()
