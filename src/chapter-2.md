Literature Review {#chapter-2}
=======================

Data-Centrism
-------------
### What is Data?

Data is an oft-used word that carries multiple meanings. In everyday speech, it might refer to mobile phone bandwidth, a filled application form or a collection of files. Even experts have a variety of definitions of data, as well as the related concepts of information and knowledge[@zim2015]. In this study, we refer to data by its accepted definition as information or knowledge stored in a form suitable for computer processing. Wellisch expressed this as 'the representation of concepts or other entities, fixed in or on a medium in a form suitable for communication, interpretation, or processing by human beings or by automated systems'[@wellisch1996], which is a useful definition as it includes the fact that both humans and algorithms can use data, and that data is something that needs interpretation.

From a strict grammatical stance, 'data' is a plural of the singular 'datum' thus it is more correct to write 'the data are correct' - but this usage is rapidly declining from use[@grammaristData] and throughout this thesis I use the more widely adopted usage of treating data as a singular mass noun, as in 'the data is correct'.

The concepts of 'data' and 'information' are closely related, so much so that they are often used interchangeably. Ackoff presented a model for distinguishing data, information, knowledge, understanding/intelligence and wisdom, in which he describes data as the physical symbols, effectively the 1's and 0's stored in a computer or the ink marks on a page, which becomes useful when humans or algorithms are able to deduce facts from those symbols to answer simple questions - at this point it becomes 'information'. Being able to interpret deeper how and why questions allow information to become knowledge and understanding, towards the ultimate goal of wisdom[@ackoff1989]. This is often represented as the DIKW pyramid (DIKW being shorthand for the data-information-knowledge-wisdom transformation that occurs as you move up through the layers), the origin of which is unknown[@wallace2007]. Figure 1 builds upon a representation by George Pór[@por1997] of the pyramid as a 'wisdom curve', showing how increasing meaning and value can be obtained from data as deeper questions can be asked of it. This theme of obtaining meaning and value from data is an important aspect of my research that I will refer back to.

![REDRAW Figure 1: Making Data into Meaningful Information](./src/figs/fig1-data-into-information.png)

This model that turning data into information can be thought of as using that data to answer questions is consistent with the idea that "information can be thought of as the resolution of uncertainty"[@wikipediaInformation]. The exact origin of this definition is unknown but it is often attributed to mathematician Claude Shannon[@shannon1948]. Indeed from an etymological stance, one who is informed is one who has received knowledge or concepts as a result of what has been communicated to them. Thus we can consider that data is the material from which that information can be received. It follows also that data contains uncertainty that must be resolved in order for it to become meaningful information.

### The Rise of Data-centrism

The earliest computer systems used data to store mathemical and scientific facts. Data processing allowed for previously manual operations to be performed with greater speed and accuracy, most famously the work of Alan Turing and the case of the Enigma code breakers during World War II[@hutton2012]. This work was the advent of general-purpose computing - machines that could be applied to any problem provided you could reduce that problem to data. Businesses over the following decades began to apply computers to myriad new problem areas in all different fields of work and life, and doing so began the encoding of information about people as data, be it for statistical purposes like censuses or research, or simply to enable the more efficient serving of customers by storing databases of customer records.

The personal computer revolution[@britannicaPCrevolution] of the late 1970s and 1980s put computers in every office and eventually every home too, and it soon became commonplace that each individual would have data stored about them in companies' databases. In the subsequent years three factors have combined to accelerate this trend of storing data about people: i) labour costs have remained high and companies have sought ways to automate their businesses and to implement online services and call centres in place of in-person staff interaction, ii) computer processing and storage has become ever cheaper thanks to the advent of cloud computing, meaning that many business processes could be reduced to data processing tasks or entire businesses be moved online, and iii) the rise of smartphones and web-enabled devices have meant that the public are now ready and willing to conduct much of their daily business online through the web and apps. These factors have encouraged both commercial and civic providers to centralise their services and to 'go digital' to the greatest degree possible. In doing so they collect ever more data about people (now 'service users' or just 'users'). Data is now seen as a resource which can be mined for value, and harnessed for profit and business efficiency - 'the new oil'[@toonders2014]. Zuboff, in her 2019 book on 'surveillance capitalism', characterises this new digital world as the collection of human behaviour data so that it can be used as free raw material and converted into profit through hyper-personalised advertising and targeting by software platforms[@zuboff2019]. This philosophy is also known as 'data-ism'[@brooks2013].

As a result of data-ism, the collection of data about people has become an inevitable part of modern life. We live 'digital lives'[@ted2018] where we each interact directly and indirectly with hundreds of digital systems every day - as you shop, socialise, or browse online; as you listen to music or watch TV; as you interact with governments or healthcare services; as you travel, and many more. Every one of those interactions indicates the presence of data about you stored in a company database. Every aspect of our lives involves the input, processing and output of data – either provided by, collected from, or generated about, us. And the digital data we create and consume (whether consciously or not  - data sharing is often unwitting[@tolmie2018]) has a direct influence on our lived experience - from decisions about what we are entitled to and what opportunities we will be offered, to the advertisements and content recommendations we are shown while we browse.

Unfortunately, the large-scale systems which collect data about us now function as 'data traps'[@abiteboul2015] - where data about us is easily gathered but very hard to remove or even to access. This creates a lack of agency for the individuals living in this data-centric world. The World Economic Forum's "Rethinking Personal Data" project recognised the critical role that data - specifically personal data - data created by and about people - now holds, and identified that 'an asymmetry of power exists today [...] created by an imbalance in the amount of information about individuals held by industry and governments, and the lack of knowledge and ability of the same individuals to control the use of that information'[@WEF2011;@WEF2013;@WEF2014context;@WEF2014lens].

### Data Protection & GDPR

Since as early as 1973, the need to protect individuals' rights over their data has been recognised[@USDOHEW1973]. The 37-nation organisation OECD in 1980 stated that
"the right of individuals to access and challenge personal data is [...] the most important privacy protection safeguard" and issued recommendations that individuals should be given basic privacy rights, including the right to be informed whether data is stored about them, and the right to an intelligible copy of that data[@OECD1980].

Over the subsequent decades, lawmakers began to enact laws to deliver these rights to individuals, notably the UK's Data Protection Act 1984 (which set up an independent body, the Data Protection Registrar (now the Information Commissioner's Office) with which organisations were required to register their usage of personal data), Ireland's Data Protection Act 1988 (which introduced the concept of a 'duty of care' for data collectors - that they are expected to avoid causing damage or distress to data subjects), the EU's Data Protection Directive in 1995 and the UK's Data Protection Act in 1998. However, such laws were generally found to be ineffective - in 2002 Simon Davies, director of Privacy International said that the UK's DPA was "almost useless in limiting the growth of surveillance"[@millar2002].

It was only in 2018, when the EU's General Data Protection Regulation (GDPR) came into force, carrying with it significant designed-to-hurt fines for non-compliance[@kelly2020;@zdnet2021], that individuals have been able to practically exercise their data rights to any meaningful degree[@atebits2020]. The GDPR -- which gives individuals key rights including rights to timely data access, explanation, erasure and correction[@ico2018] -- can be seen as the first serious attempt to rebalance the aforementioned power imbalance over data between citizens and organisations and is generally regarded as a landmark piece of legislation and a strong template for individual data protection. Around the world, companies have overhauled their privacy policies and updated their business practices to comply with the GDPR and other similar legislation, such as Japan's 2017 Act on the Protection of Personal Information, India's 2019 Personal Data Protection Bill and the 2020 California Consumer Protection Act. In the USA, there has been no national privacy law yet, but the GDPR's influence is being felt in court rulings[@hoofnagle2019].

Also in 2018, the Cambridge Analytica scandal[@wikipedia2018cambAna] broke; the personal data of 87 million people, acquired from Facebook, was exploited with the apparent intent of influencing voting outcomes including the UK's 2016 Brexit referendum and the USA's 2017 election of Donald Trump. This combined with widespread public information campaigns about GDPR have led to a heightened awareness of personal data rights[@EUAFR2020] and at the time of writing in 2021, personal data protection laws and individual digital rights remain a rapidly evolving area.

From the GDPR and its antecedents, a number of key terms have been established which I will adopt in this thesis, specifically [@ico2014;@GDPR2016]:

- _Personal data_ means any information relating to an identifiable natural person - one who can be identified directly or indirectly by reference to an identifier such as a name, identification number or location or to one or more factors specific to the physical, physiological, genetic, mental, economic, cultural or social identity of that person.
- The _data subject_ is the identified individual, living or deceased, who the personal data relates to.
- A _data controller_ is the legal entity (company, public authority, agency, individual or other body) which collects or stores personal data about an individual and determines the means and purposes for which it is processed. Liability for data protection compliance rests with the data controller.
- A _subject access request_ is the right to a copy of your personal data.
- _Data portability_ is the right to receive a copy of all stored data about you, not just that which you provided, in an accessible and machine-readable format such as a CSV file, so that you can transport it to another service or make use of it.

### The Need for Practical and Effective Data Access
[Target 400 words]

Para 1 - to tackle the imbalance, need transparency, control, trust and value.
Larsson, to assess value people need awareness

Para 2 - effective access and what it entails

Para 3 - what is missing in terms of ability to use our data. distributed data - need for associativity, can't do that due to silos etc.
time, timelines -
the needs of filtering, data detail. etc.

it's about finding meaning. there is today no interface that offers such functionality over our digital data.

### Research Gap: The Human Experience of Data
[Target 400 words]

so the gap is - what value and meaning fo people find of their data. what mental models do they have around data. what is data to them, what is their relationship to it (and what would they like it to be).
what is data to people living in a data centric world?


Personal Data Interaction
-------------------------
[Target 2,500 words]

### Computers as General Purpose Information Tools
[Target 300 words]

### Personal Information Management
[Target 600 words]

### Personal Informatics & The Quantified Self
[Target 650 words]

### The Emergence of Complex Digital Lives
[Target 600 words]

### Research Gap: The Data Beyond The Individual
[Target 350 words]

Human-Centric Computing
-----------------------
[Target 2,500 words]

### Human Computer Interaction Foundations
[Target 400 words]

### Data Transcendence & Human Data Interaction
[Target 600 words]

### People In Context: Human-Centred Design
[Target 600 words]

### The Personal Data Economy
[Target 600 words]

### Defining the Research Agenda for Human-Centricity in Practice
[Target 350 words]


Research Gap
------------
[Target 500 words]
