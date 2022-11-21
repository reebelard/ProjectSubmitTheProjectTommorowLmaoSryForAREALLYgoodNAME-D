from time import sleep
from colorama import init, Fore, Back, Style


class style:
    BOLD = "\033[1m"
    END = "\033[0m"
    UNDERLINE = '\033[4m'


init()
1
while True:
    print(Fore.GREEN + "Welcome To The Bangalore Tourism Tour!")
    sleep(1)
    print("Ok so tell me where you want to travel")
    print("1.Lalbagh Botanical Garden")
    print("2.ISKCON")
    print("3.Cubbon Park")
    print("4.Bannerghatta National Park")
    print("5.Turahalli Forest")
    choice = int(input("Enter your choice:"))
    if choice == 1:
        print(
            Fore.LIGHTBLUE_EX
            + f"""Lalbagh is one of Bengaluru’s major attractions. A sprawling garden situated in a 
            240 acres piece of land in the heart of the city, Lalbagh houses India’s largest collection 
            of tropical plants and sub-tropical plants, including trees that are several centuries old. 
            Exhibits like the Snow White and the seven dwarfs, and a topiary park, an expansive lake, a 
            beautiful glasshouse modelled around the Crystal Palace in London adorn the park giving it a 
            surrealistic atmosphere. A watchtower perched on top of a 3000 million years old rocky outcrop 
            (which is a National Geological Monument), built by Kempegowda, the founder of Bengaluru also 
            adorns the picturesque garden.

{style.UNDERLINE}Why visit Lalbagh{style.END}{Fore.LIGHTBLUE_EX}:

Lalbagh Glass House: Lalbagh Glass House is a giant palace like glass and iron structure, inspired by Crystal 
Palace in London’s Hyde Park. Lalbagh glass house was built in 1989 and renovated in 2004 and remains the 
primary attraction for visitors of Lalbagh.

Lalbagh Lake: Lalbagh has a large lake in its southern part, complete with walking trails, a bridge and 
a mini waterfall.

Seasonal attractions at Lalbagh: Lalbagh hosts several events all through the year- Lalbagh flower show 
during Republic Day (26 January) and Independence Day (15 August), Mango/Jackfruit festivals during summer,
cultural shows at Band stand are some of the popular events held in Lalbagh.

Other attractions at Lalbagh:

Bonsai Garden, large rock and Kempegowda watchtower, flower clock, Hibiscus garden are some of 
the other interesting spots to explore inside Lalbagh botanical gardens.

Lalbagh Visiting Hours:

Lalbagh botanical gardens is open daily from 6 AM to 7 PM. Entry is free during early morning and late 
evening (6 to 9 AM and 6 to 7 PM). A nominal fee applies during the day time.

Facilities available at Lalbagh:

Lalbagh has several shops run by the horticulture department of Karnataka Government as well as few private 
vendors. These shops sell fruits, vegetables, fruit juices and various snacks items. 

Public toilets are available near the Glass House. Lalbagh has 4 different entrances one in each direction 
making it easy for visitors to enter and exit as per their convenience. West gate is very close to Lalbagh 
Metro train station while parking is available at the double road entrance.

How to reach Lalbagh:

Lalbagh is located 7 kms south of the city centre (Majestic area) and 38 kms from the Bengaluru airport. 
Lalbagh can be accessed using the Bengaluru metro rail network from different parts of Bengaluru city. 
Buses, auto or taxis are readily available to reach Lalbagh.

Places to stay near Lalbagh:

Budget and luxury hotels are available near Lalbagh, Jayanagara, Basavanagudi and KR Market area which 
are within walking distance from Lalbagh"""
        )
    elif choice == 2:
        print(
            """Situated to the western of Chord Road on the hill lock known as 'Hare Krishna Hill', 
            Iskcon Temple is known not only for its religious significance but also for its architectural 
            beauty. Also known as Hare Krishna this temple has been built in the Neo-Classical style, 
            presenting a beautiful fusion of ultra-contemporary and traditional style and is equipped 
            with all kinds of modern amenities. Like various other Iskcon temples which are spread all 
            across the world, this temple of Bangalore is also dedicated to the Lord Krishna and Radha.

This temple was built to mark the birth anniversary of Sri Prabhupada, the founder of ISKCON. The temple 
has 4 ‘gopurams’ with each being connected to the other illuminating glass canopy. The captivating waterfalls, 
designed arcs along with intricately done ceilings add on to the overall beauty of the temple. The 10,000 
square feet hall, named as the “Hari Naam Kirtan” has also been beautified with exquisite paintings on the 
ceilings.

The Iskcon Vedic Theatre is another popular attraction of the temple. Along with this the temple also 
has vedic museum and area for exhibitions. The lush green garden with mesmerizing flowering plants 
boosts the temple’s beauty even more. The open-air amphitheater which hosts various concerts and festivals 
also makes this temple a unique one.

Well connected to the rest of the city, reaching the Iskcon Temple is a hassle free task. There are many bus 
stands located near to the temple. So apart from usual autos and taxis, you can also one of the many buses 
which go till the temple."""
        )
    elif choice == 3:
        print(
            """A green haven spread across 300 acres, Cubbon Park provides Bengalureans with a refuge 
            from the hustle and bustle of city life right in the middle of the city. The park is home 
            to the State Library housed in the Sheshadri Iyer Memorial Hall, a splendid red Gothic 
            structure. The whole park is peppered with fountains, statues, flowering trees and lush greenery.

Things To Do:

Seshadri Iyer Memorial Hall: Cubbon Park has a central library housed in Seshadri Iyer Memorial Hall. 
Central Library is open daily from 8.30 AM till 7.30 PM, except on Mondays, public holidays and second 
Tuesdays of the month. A well maintained garden with colourful flowers is available right in front of the 
memorial hall.

Children’s play area and Toy Train: Toy train ride inside Jawahar Bal Bhavan is a popular attraction among kids. 

Aquarium: At Government Aquarium, visitors can see aquatic creatures on display in over 3 floors. Open 
from 10 AM to 5 PM on all days except Mondays and alternate Tuesdays.

Entry fee: Entry to Cubbon park is free.

Places to visit near Cubbon Park:

Vidhana Soudha, High Court of Karnataka, Freedom Park, Kanteerava Indoor Stadium and Vishveshwaraya 
Industrial and Technological museum are within a few kms of from the park.

How to reach:

Cubbon Park can be reached using the Bengaluru Metro(BMRCL), bus or taxi from any part of Bengaluru city.
 The Park is 3 kms from Majestic bus stand, 35 kms from Bengaluru airport. Traffic restrictions may apply 
 from time to time."""
        )

    elif choice == 4:
        print(
            """It is not in every city that you find a place bestowed with scenic beauty and full of 
            exquisite flora and fauna. Bannerghatta National Park which is approximately 21 km from 
            the city of Bangalore presents tourists with perfect weekend options. There is nothing 
            like relaxing amidst the refreshing natural setting after hectic work pressure and monotony 
            of daily chores. Excitement of seeing the bravest of all the animals, tigers, from few inches 
            of distance and the pleasure of looking at colourful and exotic plants is unexplainable.

Established in the year of 1971, Bannerghatta National Park is spread across 104. 27 sq.kms and has ten 
reserve forests of Anekal Range of the Bangalore Forest Division under it. Once at the national park, you 
will have more than one option to keep yourself engaged. Along with national park, Bangerghatta has an 
Aquarium, a Zoo, Children's park, Crocodile Farm, Snake park, Prehistoric animals park and a Museum. From 
families with children to adventure lovers, every one has something of their choice here.

The overall beauty of the park gets a boost from the Suvarnamukhi stream, originating in the Suvarnamukhi 
hills and runs through the park. Suvarnamukhi hills spread out to a huge rock and have famous Champaka 
Dhama Swamy temple which belongs to the Hoysala age at the foothill of the rock. The Suvarnamukhi pond that 
is two kms away is believed to have curative powers.

The National Park as a Butterfly Park too. Being first of its kind in India, Butterfly Park is one of the 
major attractions. The park is spread across an area of 7.5 acres, and has a butterfly conservatory, a 
museum and an audio-visual room.

Activity : Bannerghatta National Park
You have umpteen number of options for activities near by the national park. Apart from rides in open 
jeeps, mini buses, vans and elephants, tourists can go for fishing, Coracle boat rides, Bird watching, 
River rafting and Outdoor camping. There are various trekking places as well. Some of these are Uddigebande 
(3.5 kms.), a natural rock formation called Hajjamana Kallu (3 kms.) and Mirza Hill (1.5 kms.)

Fauna : Bannerghatta National Park
Although famous for tigers, Lions, Thamin deer, hog deer, king cobra, Himalayan black bear and Malabar giant 
squirrel you can also spot wild animal such as Elephant, gaur, leopard, jackal, fox, wild pig, sambar, chital, 
spotted deer, barking deer, common langur, bonnet macaque, porcupine, the hare, pangolin, slender loris and huge 
monitor lizards like cobras, pythons, kraits and Russell vipers in the national park. Tiger and Lions can be 
seen across 25,000 acres of the Park which is securely fenced.

The Bannerghatta National Park has amazing population of birds as well adding charming colours to the park. 
Cormorants, white ibis, little green heron, grey heron, paradise flycatcher, Tickell’s Blue Flycatcher, Common 
Grey Hornbill, White bellied Drong, Spotted Owlet, Collared Scop’s owl, Mottled Wood Owl, Eurasian Eagle owl and 
Brown Fish owl are few constituting the avian population on the park.

Flora: Bannerghatta National Park
The Bannerghatta National Park has mainly moist deciduous teak forest. Bamboos are quite common in the park with 
Dendrocalamus strictus being the most commonly found species. Commonly founds species of plants in the park are 
Anogeissus latifolia, Schleichera oleosa, Terminalia tomentosa, sandal, neem, T. arjuna. Grewia tilaefolia, 
Santalum album, tamarind, chujjullu, Shorea talura, Emblica officinalis, Vitex altissima, jalari, Wrightia 
tinctoria, Randia sp. Zizphus sp. and Albizzia sp. There is small area on the park which has mainly plantations 
of Eucalyptus, Bauhinia purpurea, Samanea saman and Peltphorum pterocarpum.

Visiting the Park:
Although the city of Bangalore and its near by areas has moderate climate and mostly ranges from 15°C to 35°C, 
the best time to visit the park is during the months from November - June.

You can reach the Park by opting for bus services running from Bangalore which have high frequency or hiring 
private transportation.

The Park is open for tourists from 9 am and 5 pm. It is closed on every Tuesday of the week. You can buy 
tickets for entry into the Zoo and Safaris at the main entrance."""
        )

    elif choice == 5:
        print(
            """Located at a distance of only 20 km outside Bengaluru, Turahalli is a sprawling verdant 
            forest that is a perfect escapade from the chaos and din of the city into nature. The forest 
            is sprinkled with huge rock boulders that make it a perfect spot not only to sit and relax but 
            also to pose and take great pictures with the forest in the backdrop. Vehicles have been banned 
            inside the forest with the exceptions of cycles. It has excellent cycling trails so you can find 
            a lot of cyclists visiting here especially in the mornings.

Because of the presence of several rock boulders, you can also find adventure enthusiasts here. These climbers 
visit regularly to practice to participate in national as well as international competitions. In addition to that, 
the forest supports a rich and varied wildlife, both in terms of flora and fauna. The trees are mostly eucalyptus 
among other species. Several animals and birds can also be spotted in the jungle. Since there are no eateries or 
food stalls that can be found here, it is best advised to carry food along.

1. Nature Walk

The wilderness provides the best landscape to take a long walk alone or in company. It is the perfect escape that 
is required to wander off from the city life in the lap of nature. Aside from the natural floral beauty, you can 
also spot several fauna species and diverse varieties of birds.


2.Trekking

Trekking is a popular activity at Turahalli. It is considered most ideal for short hikes. You can trek up to any 
of the several hillocks from where you can enjoy a 360 degree view of the township below and gorgeous green 
surroundings around.


3.Cycling

Cycling is the most popular activity at the forest. Turahalli Forest is also known for its very best cycling 
trails in the region. With a picturesque backdrop, these trails are easy to ride on. So along with exercise, 
you can also enjoy the scenery in the background.

4.BirdWatching

The forest is a hub for various avifauna species. And hence, it is most loved by avid bird watchers who come 
here with their binoculars to spot the birds. Some of the birds that can be spotted here include  black drongo, 
white-breasted kingfisher, pond heron, common iora, magpie robin and a lot more.

5.Rock Climbing

Rock Climbing is also a popular activity at the forest because of the presence of a number of huge rock boulders. 
Many climbers come here to practice their skills for several national and international competitions. While some 
also indulge in the activity for recreational purposes.

6.Picnic

Lastly, picnic is a popular activity that people come here for. You can sit down with a basket of food alongside a 
brook and enjoy food amidst bounteous natural beauty.
"""
        )
    repeat = input("Do you want to continue? (y/n)")
    if repeat == "n" or repeat == "N":
        break
