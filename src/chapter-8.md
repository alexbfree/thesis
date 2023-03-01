<h1 class="title">Section IV: Operationalising the Research Agenda through Design & Practice</h1>

<h2>Introduction to Section IV</h2>

<span class="editnote">write text introducing overall placement work and outline for chapter 8 and 9 here</span>
<span class="movenote">integrate pasted subsections from ARI7</span>
<span class="editnote">add a subsection about SILVER development</span>
<span class="editnote">include something more thesis-structure based, looking ahead to what we will do in C8 and C9 and Why</span>

<h3>ARI7.1.OLD BBC R&D's Cornmarket Project</h3><a name='ari-bbc-OLD'/>

<span class="editnote">edit this for its new context</span>
<span class="editnote">renumber this as IV.1</span>

I took a three-month sabbatical from my PhD in the summer of 2020. I was remotely embedded within a full-time research internship at **BBC R&D** - the British Broadcasting Corporation (BBC)'s Research and Development (R&D) department [@bbc1997rd], working with specialists, designers, researchers and developers on an exploratory research project codenamed _Cornmarket_. I continued this involvement as a part-time research consultant and critical friend for a further 5 months after the conclusion of the initial three-month placement.

As part of its Royal Charter, one of the BBC's lesser known obligations is to maintain a centre of excellence for research and development in broadcasting and electronic media, and to this end it employs over 200 researchers in its R&D department looking at everything from AV engineering and production tools to new forms of media, virtual reality, digital wellbeing and human data interaction [@bbc1997rd]. The Cornmarket project, launched in 2019, is a BBC-internal human-data interaction research project which explores a possible role for the BBC as it moves beyond broadcast television, using its public service responsibility to guide citizens to a position of empowerment within today's digital landscape - encompassing not just entertainment but health, finance and self-identity. Due to its unique funding from UK-wide TV licensing and its duties to not only entertain but to inform and educate the general public, the BBC is uniquely placed to take a more human-centred approach than commercial innovators in this space as it needs only to deliver value, not profit. The project is exploring the use of Solid [@bernersLee2022inruptSolid] technology to build a working Personal Data Store (PDS) prototype [[2.3.4](#2.3.4)] while also developing, iterating and trialling user interface designs and conducting participatory research interviews and activities all to explore what for a BBC PDS might take and what features its potential users might value.

The proposed BBC Cornmarket product, internally called _My PDS_, would allow people to populate a PDS with personal data from APIs and data downloads from a variety of services including BBC iPlayer, Netflix, All4, Spotify, Instagram, Strava, Apple Health, banks and finance companies, as well as social media companies such as Facebook, LinkedIn and Twitter, and then to use these combined data sources to create personal _profiles_ for Health, Finance, and Media (i.e. entertainment) as well as a Core profile. Within these profiles various data insights, visualisations, capabilities would be delivered. One feature the work explores in depth as potentially valuable to users is the ability to include and exclude certain datapoints from the imported viewing history data in order to present a more accurate, curated view of oneself that could then be fed back to other applications such as BBC Sounds to give better content recommendations.

With a cross-disciplinary team of around 20 people including architects, developers, user experience designers, product designers, innovators, participatory researchers and marketers, and funding to outsource public engagement research to agencies, this project represents, at the time of writing (late 2020), a significant player in the emerging personal data economy [[2.3.4](#2.3.4)]. As such the Cornmarket project is a fertile ground in which to learn more from practitioners in the PDE space and to test the learnings of this thesis in practice while also finding deeper insights in response to my research questions - in particular RQ3 which is concerned with the building of more human-centric personal data interfaces in practice.

Much of the work I did during this extended internship can be seen in the designs within [9.3](#9.3), as well as the research report I wrote [@bowyer2020bbcreport] and internship writeup [@bowyer2020internreport]. My work with the Cornmarket project can be seen as the concluding part of one of several action research cycles within my PhD [[3.2.2](#3.2.2)].

An additional Figure from my time on Cornmarket that was not featured in the main body of the thesis is shown in Figure 7.1 below. This shows a screenshot from a functional prototype tool I produced during a hack week that allows the user to upload data retreived via GDPR or download portal, and proved the concept of programmatically identifying key entities [9.3.3](#9.3.3) and identifying time-labelled events for display as life information to users.

![Figure ARI7.1: Prototype Entity Extractor and Time-Event Extractor](./src/figs/figARI7.1-prototype-gdpr-interface.png){#figure-ari7.1}

A number of articles relating to the Cornmarket project have been published:

  - Personal data stores: building and trialling trusted data services - BBC R&D [@sharp2021]
  - Building trusted data services and capabilities (explainer videos) [@sharp2022bbcvideos]
  - The BBC’s radical new data plan takes aim at Netflix (Wired) [@orphanides2021]
  - Sir Tim Berners-Lee and the BBC stage a very British coup to rescue our data from Facebook and friends (The Register) [@goodwins2021]
  - BBC and Sir Tim Berners-Lee app mines Netflix data to find shows viewers like (The Times) [@kanter2021]
  - Stronger Together: Cross Service Media Recommendations (research paper) [@ibc2021]
  - BBC wages war on online echo chambers with ‘unbiased’ tech (The Telegraph) [@woods2022]
  - Richard Sharp (BBC Chairman) discusses Data management & privacy (video) [@parl2022bbc]

<h3>ARI7.2.OLD Hestia.ai, and Sitra's _digipower_ Project</h3><a name='ari-digipower-OLD'/>

<span class="editnote">edit this for its new context</span>
<span class="editnote">renumber this as IV.2</span>

Following the conclusion of the funded period of my PhD, I took up a near-full-time position as Project Leader and Personal Data Coach at **Hestia.ai** [@dehaye2019]), a startup based in Geneva, Switzerland. Hestia.ai is a company conducting research, developing technologies, and delivering training, in the emergent MyData/PDE space [[2.3.4](#2.3.4)]. In essence, the company's mission is to help individuals and especially collectives to more easily obtain and understand data held about them, and to help them visualise, aggregate and make use of that data. It is an example of a **data access and understanding services** company as described in [9.5.3](#9.5.3).

I was specifically hired to co-lead the _digipower_ project [@härkönen2022project], for Hestia.ai's client, **Sitra** [@sitra1967]. Sitra is a non-profit organisation in Finland, funded by the Finnish Parliament and accountable to the Finnish people. The goal of the digipower project was to guide 15 European politicians, civil servants and journalists, through the process of obtaining and exploring their own data. The participants were high-profile VIPs, including the former Prime Minister of Finland and former European Commission Vice President, Jyrki Katainen. The goal was to empower those individuals to better understand the workings of the data economy, so that they might be able to influence others and effect change. One of Sitra's goals is to establish a fairer data economy [@sitra2018fairdata].  Methodologically, the project drew heavily on my own Case Study Two [[Chapter 5](#chapter-5)], adopting a similar method of guiding individuals through the process of making GDPR requests and scrutinising the returned data; I was employed on the project for this expertise. Where it differs from my own Case Study is that the focus of the research was outward, on the data economy and the practices of service providers, rather than inward, on the lived experience of the participants. Other differences included the building and use of software interfaces to provide participants with data visualisations, the use of TrackerControl software to audit mobile phone apps [[Insight 12](#insight-12)], and the direct analysis of participants' retrieved personal data by the Hestia.ai research team (whereas my Case Study explicitly avoided handling participants' personal data). The project resulted in three reports:

- Sitra's official project report [@härkönen2022report]; and
- Two technical research reports by Hestia.ai:
  - A high-level interpretation of models of power and influence in the data economy [@pidoux2022]; and
  - A detailed auditing of provider practices, evidenced by examples from participants' data [@bowyer2022hestia].

At the time of publication of this thesis (August 2022), I continue to be employed by Hestia.ai, working on the research, design and development of tools to help collectives [[Insight 10](#insight-10)] with data, make data easier to understand [[6.1.2](#6.1.2); [7.7](#7.7)], and exploring methods to help people 'hack the seams' of digital platforms and services [[9.4](#9.4)].

Where the [BBC internship](#ari-bbc-OLD) has helped me to understand the practicalities of connecting people with their personal data in pursuit of Life Information Utilisation [[7.6](#7.6.1)], my work with Hestia.ai has helped me understand the practicalities of how people might acquire greater Personal Data Ecosystem Control [[7.6](#7.6.1)]. In this sense, both peripheral activities have been highly complementary to developing an overview of the pursuit of HDR in practice.

<h3>ARI7.3.OLD DERC's Healthy Eating Web Augmentation Project</h3><a name='ari-derc-OLD'/>

<span class="editnote">edit this for its new context</span>
<span class="editnote">renumber this as IV.3</span>

As a software developer I have been aware for a long time that one of the biggest challenges in building new data interfaces is to gain programmatic access to the necessary data. As part of the trend towards cloud-based services and data-centric business practices, it has become increasingly difficult to access all of the data held about users by service providers. Application Programming Interfaces (APIs) are a technical means for programmers to access a user's data so that third-party applications may be built using that data. Unfortunately, as a result of commercial incentives to lock users in and keep data trapped [@abiteboul2015; @bowyer2018freedata], much of users' data can no longer be accessed via APIs [[8.4](#8.4.2)]. While GDPR data portability requests do open up a new option for the use of one's provider-collected data in third-party applications, this is an awkward and time-consuming route for both users and developers. **Web augmentation** provides a third possible technical avenue for obtaining data from online service providers. It relies on the fact that a user's data is loaded to the user's local machine and displayed within their web browser every time a website is used, and therefore it is possible to extract that data from the browser using a browser extension; this as another **seam** that can be hacked—see [9.4](#9.4) and [Insight 12](#insight-12). Similarly, once loaded into the browser, a provider's webpage can be modified to display additional data or useful human-centric functionality that the provider failed to provide.

![Figure ARI7.2: Screenshot from a Web-Augmented version of the _Just Eat_ Website,<br/>showing hygiene information and offering additional sorting](./src/figs/figARI7.2-justeat-webaug.jpg){#figure-ari7.2}

In order to better understand what is and is not possible using this technique, I participated part-time from 2018 to 2020 as the sole software engineer in a DERC (Digital Economy Research Centre) project. This project was using the web augmentation technique to explore how researchers could improve the information given to users of Just Eat, a takeaway food ordering platform in the UK. Hygiene Rating information for each outlet was added, as well as a feature to enable user to sort by hygiene rating, as shown in [Figure ARI7.1](#figure-ari7.1). The theoretical basis for this research was published in [@goffe2021; @goffe2022]. While this particular use case does not concern personal data, the technology and techniques being used by the project to exploit the browser seam were considered highly relevant to the exploration of HDR-improving possibilities, and the goals of the research project were also human-centric, and consistent with this thesis's research goals - tackling the hegemony of service providers in order to better serve individual needs.

<h3>Developing a Health Data Interface within the SILVER project</h3><a name='IV.4'/>

<span class="editnote">Write a section about SILVER dev</span>

<h3>ARI7.4 Special Attribution Note for Part Two</h3><a name='IV.5'/>

<span class="editnote">renumber this section and its link</span><a name='ari-attribution'>
<span class="editnote">decide which parts this is most about, and update accordingly</span><a name='ari-attribution'>

This is a note about the attribution of insights within Chapters [7](#chapter-7), [8](#chapter-8) and [9](#chapter-9), as the ideas originate quite differently than from the rest of the thesis.

This thesis is my own work. All ideas synthesised in Part Two are original. Some of the specific details, theories and ideas presented in Part Two arose or were developed or augmented through my close collaboration, discussion and ideation with other researchers both alongside and prior to the PhD timeframe, including:

  - Jasmine Cox, Suzanne Clarke, Tim Broom, Rhianne Jones, Alex Ballantyne and others at BBC R&D;
  - Paul-Olivier Dehaye, Jessica Pidoux, Francois Quellec aand others at Hestia.ai;
  - Stuart Wheater of Arjuna Technologies and Kyle Montague of Open Lab during the SILVER project;
  - Louis Goffe of Open Lab on the DERC Healthy Eating project;
  - earlier innovation work with Alistair Croll at Rednod, Montréal, Canada (circa 2011); and
  - earlier innovation work with Megan Beynon and Dean Upton at IBM Hursley, UK (circa 2006).

Due to these collaborations and the ongoing and parallel nature of many of these projects to my PhD research, it is impossible to precisely delineate the origin of each idea or insight. In practice, ideas from my developing thesis and own thinking informed the projects' trajectories and thinking, and vice-versa. These ideas would not have emerged in this form without my participation, so they are not the sole intellectual property of others, but equally I would not have reached the same conclusions alone, so the ideas are not solely my own either. All diagrams and illustrations were produced by me, except where specified, and the overall synthesis and framing presented in this chapter is my own original work. Where this chapter includes material from the four peripheral projects [[7.2](#7.2)], that material is either already public, or permission has been obtained from the corresponding individuals or project teams.

Mapping the Human Data Relations Landscape {#chapter-8}
==========================================

> _"There are certain things you do not in good conscience do to humans. To data, you can do whatever you like."_
>—Nikhil Sonnad (data journalist and technology commentator)

<span class="editnote">Make sure it makes sense without the insights, edit as needed</span>

In this chapter, we begin to engage with the expanded research question laid out in [7.1](#exRQ). Considering how better HDR might be achieved in practice generates further questions. Like SI's _barriers cascade_ [@li2010], what barriers exist that inhibit the building or adoption of human-centric technologies? What opportunities might overcome these barriers? How can we catalyse progress toward _MyData_'s human-centric agenda [@mydata2017declaration]? What challenges are faced when attempting to build human-centric technologies for today's world? Building on an understanding of human experience of the data-centric world, can we more provide an outlook for PDE design & development and define a _research agenda_ for the next step of tackling the PDE challenge?

Focusing on the four objectives [[7.7](#7.7)], and informed by the peripheral work [[7.2](#7.2)], I can identify specific _obstacles_. Analogous to Li's _barriers cascade_ [[2.2.3](#2.2.3); @li2010], these are the challenges that individuals or system designers must be empowered to overcome. These obstacles are documented in the following sections, accompanied by _insights_ that might help adversarial designers or strategists to tackle them. [Figure 8.1](#figure-8.1) depicts an HDR-specific barriers cascade: a route of overcoming obstacles through which individuals might be empowered and by which organisations might become more HDR-friendly. The concepts on this diagram will be refined and explained across this chapter and the next. The last of these (corresponding to the 'solution space' box) covers some of more pervasive obstacles that apply to all four HDR objectives.

![Figure 8.1: Obstacles and Resulting Insights in the HDR Opportunity Landscape](./src/figs/fig8.1-obstacles-insights-hdr-landscape.jpg){#figure-8.1}

Obstacles to the HDR Objective of Data Awareness & Understanding{#8.1}
----------------------------------------------------------------

### Invisible, Inaccessible or Unrelatable Data{#8.1.1}

In pursuit of visible, understandable data [[6.1.1](#6.1.1); [6.1.2](#6.1.2)], the first obstacle encountered is that most personal data is **invisible**, **inaccessible** or **unrelatable**. It is trapped in service providers' databases, or on different devices or hard drives, or by software limitations and proprietary file formats [@abiteboul2015; @bowyer2018freedata]. My research participants spoke of 'not knowing' what data exists and of being 'in the dark'. Case Study Two showed that even where data is accessible, it is not **relatable** (_legible_ [@mortier2014]; [2.3.2](#2.3.2)). The objective here, addressed in [Insight 1](#insight-1), is to ensure that people not only have awareness of their data, but can understand ('make sense' [@gurstein2011; [2.1.4](#2.1.4)]) of what it means.

<span class="editnote">Add ref to Insight 1 here</span>

### The Personal Data Diaspora {#8.1.2}

Another important obstacle to consider here is what I call the **Personal Data Diaspora**[^16]. As illustrated by Imogen Heap's quote opening [Chapter 1](#chapter-1), an individual's personal data is typically very widely dispersed, and there is no central, holistic view of one's data. For example, if I consider just my movement tracking data, I have over time accumulated activity logs from walking, running, cycling, and driving which are stored by Nike+, MyFitnessPal, Strava, Google Fit, Fitbit, Apple Health and Google Maps, not to mention the records remaining on my different smart watches, smartphones, hard drives and insurer black boxes. This is the SI problem of _Integration_ [@li2010] [[2.2.3](#2.2.3)]. As well as the challenge of managing one's data ecosystem [[2.2.4](#2.2.4)], this makes it impossible to view physical activity history in one place, to spot patterns over time or make comparisons. To overcome this, we need interfaces that recognise the scattered reality of each individual's personal data, and begin to make that ecosystem visible and understandable [see [8.3](#8.3) and [8.4](#8.4) below].

Data awareness and understanding is a problem of representation. Invisible data should be visibly represented. All data should be represented as contextually relatable life information.

[^16]: The word _'diaspora'_ is typically used with reference to populations, but is an apt term, derived from the Greek 'diaspeirein' meaning 'scattered about' or 'dispersed'.

Obstacles to the HDR Objective of Data Useability<sup>[10](#fn10)</sup>{#8.2}
-------------------------------------------------

### Immobile, Inaccessible or Unmalleable Data {#8.2.1}

To improve the useability of data, let us consider what properties of data make it hard to use. Most personal data is immobile, inacessible, unmalleable and not interrogable.

Data is **immobile** in that is very difficult to move it out of its environment. Most data exists in organisations' internal databases, where it is tightly coupled to technology stacks, interfaces and business processes. Separating one's data from the service that holds it is difficult and often impossible. It is **inaccessible** to individuals (in the sense of _effective access_ [@gurstein2011]). Data access requests such as GDPR are typically satisfied by creating a copy of the data, creating problems of delay, divergence and understanding. Even then, returned data is incomplete [[5.4.2](#5.4.2.2)]. Its accessibility is also hindered by the technical nature of data. Data is often stored in complex proprietary structures which are designed for the algorithmic efficiency of the specific business operations rather than for general-purpose re-use.

People need to be able to ask questions of their data [[Table 5.4](#table-5.4); [4.3.2](#4.3.2.4)]. But data is **not interrogable**. It must stand for itself, yet there is no obvious way to ask a question about the meaning of the data or its ability to answer a particular question. To ask questions of data requires either the co-operation of the data holder or advanced technical skills in data querying and analysis (assuming the data is complete and contextualised). Data needs to be **malleable**—capable of being broken down, looked at from different perspectives, and reconstituted in different ways. This goes beyond visually representing the data, and implies an ability to interact with the data to produce new interpretations and insights to investigate specific questions.

To overcome these obstacles, data must be freed from its current constraints and moved into environments where it can be freely examined and reconstituted without restriction. This leads to Insight 2:

<span class="editnote">Add ref to Insight 2 and 3 here</span>

As [Insight 3](#insight-3) show, data will only become useable once we change its nature. Since the 1970s, drawing on the then-common metaphor of a filing cabinet, computers have considered _files_ as the basic material that users will interact with. Where we do interact with data as information instead of files, that information is typically presented in limited contexts within certain products or apps [[Insight 1](#insight-1)]. To move up the DIKW pyramid [[2.1](#2.1)], we need smarter computer systems, that move beyond files [@bowyer2011filesdie]. We need systems whose basic material is not files, but pieces of human information.

**<a name="info-os">We</a> need a human information operating system**.

Obstacles to the HDR Objective of Ecosystem Awareness & Understanding{#8.3}
---------------------------------------------------------------------

### Complex and Invisible Personal Data Ecosystems {#8.3.1}

Crabtree and Mortier highlighted that users need their whole personal data ecosystem to be visible [@crabtree2016]. As established [[2.2.5](#2.2.5); [2.3](#2.3); [6.2](#6.2); [7.2](#7.2)], HDR cannot be made effective without a sea change in the way that individuals are able to interact with the complex ecosystem of personal data they each inhabit. Our PDEs are incredibly complex and largely invisible. For example, it is easy to allow a handful of messaging and social media apps to access your contact list. Before you know it, you have created a complex and unmanageable network of connections that silently sync and propagate your addresses and phone numbers across the Internet. And there are deeper layers which are even less evident to users: networks of data brokers, advertisers and digital cookie companies exchange user identifiers, activity data and personal information about you while you browse or use apps [@pidoux2022]. The ability to build up a meaningful picture of your personal data ecosystem is completely absent [[4.3.4](#4.3.4.1)] or severely limited. People remain 'in the dark', leading to fear [@bowyer2018family], overload [[2.2.4](#2.2.4)] and resignation [[5.4.4](#5.4.4.1)]. Managing one's personal data ecosystem is an **overwhelming, unmanageable task** that even personal data experts are not fully able to get a handle on. We do not feel 'in control' [@teevan2001; [2.2.2](#2.2.2.6)]. The ability to provide a user with ecosystem transparency is hindered by the complexity and multiplicity of data relationships they have been encouraged to set up. People lack tools to provide a meaningful, or indeed any, view of those relationships. In both Case Study contexts, we saw that no one individual or organisation has the ability to see the whole of a user's data ecosystem [[4.3.4](#4.3.4.3); @cornford2013]. There is little commercial motive to try and solve this problem, as each provider focuses on their own apps, websites and services. Making one's ecosystem visible, transparent and understandable is therefore an essential objective for better HDR, as Insight 4 shows.

<span class="editnote">add reference to insight 4 here</span>

### A Lack of Metadata{#8.3.2}

As we start to consider _what the data is about_, new possibilities are unlocked. A PDS-type system could built that is not only a repository of personal data, but (using proxy representations), a collection of ecosystem information and _contextually-situated_ life information too. This could include information about relationships with data holders or other entities. Builders of such a system would face a further challenge—**a lack of metadata** [[2.2.2](#2.2.2.2)]. Typically, most data on our hard drives lacks context about its origin, and how it relates to the individual in a holistic life/ecosystem sense. Where data access rights are executed (or data is personally shared [[4.3.2](#4.3.2.2)]), the attention is on the data itself: what it says. But as Case Study Two showed, some of the most desired information was not the data itself, but handling information and inferences—information that can only come from metadata, which was rarely forthcoming [[Table 5.3](#table-5.3)]. Metadata could include many facets that could be quantified and recorded, as illustrated in [Figure 8.5](#figure-8.5), which I created at BBC R&D:

![Figure 8.5: Some of the Many Aspects of Metadata that Might Exist About a Datapoint or Dataset](./src/figs/fig8.5-metadata.png){#figure-8.5}

These facets can be mapped back to the 5 W's that collectively make up the user's _context_ [@abowd2000; [2.2.2](#2.2.2.5)]. Many of these facets are not explicitly recorded today, or would take significant work to capture. Nonetheless, this exploration shows how data can be better contextualised, supporting contextual and associative approaches [[2.2.2](#2.2.2.5)]. This leads to [Insight 5](#insight-5):

<span class="editnote">add reference to insight 5 here</span>

Paying attention to ecosystem information, metadata and provenance  facilitates a new space that, at the time of writing in 2022, almost no-one is building for. For people to manage their digital world, **they need a map**. This is the first step on the road to giving individuals oversight of their personal data ecosystem.

Obstacles to the HDR Objective of Ecosystem Negotiability{#8.4}
---------------------------------------------------------

There are three distinct obstacles to ecosystem negotiability:

  - the intrinsic structures that give data holders power [[8.4.1](#8.4.1)],
  - the trend of actively diminishing user agency [[8.4.2](#8.4.2)], and
  - the intractable data self [[8.4.3](#8.4.3)].

### Hegemony through Data Holding {#8.4.1}

It is in the pursuit of oversight [[6.2.2](#6.2.2)] and involvement [[6.2.3](#6.2.3)] that the impact of the power imbalance [[2.1.2](#2.1.2)] becomes most clear; unlike the other HDR objectives, individuals cannot act to claim ecosystem negotiability for themselves. Negotiability means having the power to act, and in the context of systems and interfaces owned and designed by service providers, **that power can only be given**. The hegemony of data holders is therefore is the greatest obstacle to this objective, so it is vital to examine the nature of that power if we are to confront it. Where does it come from?

![Figure 8.6: The Panopticon Structure of the Illinois State Penitentiary](./src/figs/fig8.6-panopticon.png){#figure-8.6}

A helpful analogy for the relationship between provider and user can be seen in the design of Jeremy Bentham's _panopticon_ [@bentham1791], a real-world version of which is pictured in [Figure 8.6](#figure-8.6). The panopticon is an 18th-century prison architecture that elevates the power of the (hidden) prison guards to observe all the prisoners easily at any time while removing prisoners' privacy and providing them no ability to observe those in power. As in Orwell's _Nineteen Eighty-Four_, individuals are unable to know when they are being watched (in this case, because the guards are hidden from view by one-way screens). This enforces compliance. Structuralist philosopher Foucault interpreted the panopticon as a political design, recognising that human environments can be configured to influence or regulate behaviour, in order to defend the power of the ruling class [@foucault1975]. Such designs embody his four principles:

  - **Pervasive Power**: the guards see everything all the prisoners do, all the time
  - **Obscure Power**: the guards can see into any cell at any time, but the prisoners can't know when, how or why they are being observed
  - **Direct Violence Made Structural**: the structure motivates the prisoners to self-regulate their behaviour without being coerced (through beating or punishment)
  - **Structural Violence Made Profitable**: having been made compliant by the structure, the prisoners can be put to work for the benefit of those in power, as it is the only option available to them.

We can see at least three of these traits in modern Internet platforms such as Facebook today. These platforms monitor users' behaviour without their knowledge (pervasive power), and without accountability (obscure power). Interfaces are designed to offer only those actions that benefit the platforms (e.g. clicking ads, sharing content or spending more time on site) (structural violence made profitable). This has happened through the processes of _platformisation_ and _infrastructurisation_ [@helmond2015; @plantin2018], which have supplanted the Web 2.0-era promise of a free, open Internet that could have been more empowering to individuals.

Through the control of data and of interface design—the only channels through which they can be observed—**service providers and platforms assert a structural power over the digital landscape**. Just as the design of the panopticon regulates the behaviour of the prisoners, so the configuration of platforms, apps and service interfaces we use regulate and limit our behaviour as users. As Lessig wrote, _'code is law.'_ [@lessig2000]. This infrastructural power is explained further in [[Insight 6](#insight-6)] below.

Structural power is not the only form of power which modern-day data-centric service providers hold. Jasperson _et al._'s extensive review of types of power in the context of technology organisations [@jasperson2002] identifies 23 different power paradigms, of which at least 13 can be, and are, asserted by data-centric organisations today:

- _**authority**_: ownership of technology or infrastructure (e.g. of websites, servers and code)
- _**resource control**_: controlling the flow of resources (in this case of information/data)
- _**systems/structural power**_ structural manipulation of others (as detailed above)
- _**rational power**_: controlling decision-making processes (such as banning users)
- _**disciplinary power**_: using an influential position to affect others' mental models (e.g. positioning location tracking as theft resilience)
- _**zero sum power**_: winning a battle for ownership/resource control at the other party's expense (e.g. losing control of your sacrificed data)
- _**behavioural influence**_: persuading others to carry out the desired behaviour (e.g. restricting features to motivate subscription payments, or promoting certain content or actions)
- _**interpretative influence**_: determining how reality is externally represented (e.g. Facebook determining the way in which your social network is represented to you)
- _**network centrality**_: becoming an indispensable hub of a wider ecosystem (e.g. Facebook/Google dominance in online ad-brokering)
- _**processual power**_: changing processes for competitive advantage (e.g. platforms offering preferential APIs or rates to compliant partners)
- _**socially shaped power**_: influencing a wide audience to settle upon a preferred interpretation (e.g. using dominant market position to dominate debates e.g. about privacy norms)
- _**interpretive power**_: creating the internal representations of reality within an organisation (e.g. presenting unpopular attitudes to data privacy to staff as normal/acceptable/beneficial for business)

<span class="editnote">Add ref to Insight 6 here</span>

### The Active Diminishing of User Agency {#8.4.2}

The second major obstacle to ecosystem negotiability is that platformisation and power exertion are not a one-off transition, but rather an ongoing process. Today's platforms exhibit **a continuing trend of actively diminishing individuals' agency**, especially in the last decade. When software was sold in a box, manufacturers competed based upon which product would let the user take home the greatest range of features and capabilities. New releases with new features drove new product sales. But in the cloud computing era, a smaller set of core features done well is sufficient to guarantee an ongoing subscription revenue from a user. Cost savings in development and support costs can be made by reducing feature sets. Constrained, compliant users are easier to manage. The relentless pursuit of increased profits and further cost saving sees products lose, not gain, features. Interfaces are reshaped to serve businesses' interests first and foremost. Providers' focus on making user behaviours constrained, predictable and profitable, more than meeting their needs or providing maximal value [[2.3.5](#2.3.5)]. Plantin _et al._ describe the particular harmful influence on the ecosystem of Facebook's power exertions:

> _"Facebook is a formidable force in a profit-motivated platformisation which is beginning to eat away at the Open Web.  This entails moving away from published URIs and open HTTP transactions in favour of closed apps that undertake hidden transactions with Facebook through a Facebook-controlled API."_—@plantin2018

Here are just a few examples of the ways in which users' agency has been, and continues to be, diminished:

- Facebook closed their RSS feeds, and later parts of their APIs, meaning that users could no longer consume their friends' posts in any other environment than the ad-filled and manipulated Facebook main feed. Later, they eliminated feeds of friends' posts and favourite pages [@perez2018], removing users' ability to compartmentalise their content viewing to certain friends groups. The 'Friends' page on Facebook currently shows a list of recommended new friends. To access your current friend list requires an extra click. Encouraging users to grow their networks is prioritised over user convenience.
- Twitter closed the parts of its APIs that allowed real-time notifications and access to one's home feed, killing off primary functionality for a healthy ecosystem of third-party Twitter clients that increased user choice [@newton2018]. TweetDeck, a major third-party Twitter client was acquired, and later shut down, as was Twitter's own desktop client. Eventually, the only option left to users was to use the web interface. [@gayomali2015; @hatmaker2018; @siegal2022]
- Apple has been diminishing users' agency for a long time. Users cannot open up iPhones even to change the battery without invalidating their warranty. Apple have removed disk drives, headphone ports, SD card slots and other ports. Certain parts of the hard drive on macOS devices are now read-only and non-writeable by users.
- Facebook recently announced they will no longer store users' historical location data (though they will still use location information) [@pegoraro2022]. This means users will lose the capability to access historical location records. I would argue this makes it harder for users to see how their location data will be used in future, as there will be no historical log to examine. Data-centric companies can change their practices to limit agency and reduce accountability.
- Online news and discussion site Reddit has removed content access for non-logged in users, and uses deceptive techniques to present advertisements that look like posts from users, and to discourage users from appearing offline. These patterns have been described as _disrespectful design_ [@regoje2021].
- In an example from the public sector, through my work on the SILVER project [[3.4.1](#3.4.1.1)] just prior to the introduction of the GDPR in 2018, I heard whispers in at least one local authority of plans to 'shift from getting data collection consent from supported families towards simply informing them of our practices' (in other words, removing their choice). The instinct to further organisational interests over those of the individual appears not to be limited to commercial data holders.
- In a similar vein, TikTok recently announced that it would rely on _legitimate interest_ rather than consent when it comes to using users' activity data to personalise the app experience. This removing users' ability to withdraw consent to such use. This plan has subsequently been paused after warnings that this might breach GDPR [@lomas2022].

Unchecked, trends to reduce users' agency and further providers' interests at the expense of human autonomy are likely to continue. Today's data-centric systems suffer from a lack of consideration to individual welfare. Data centricity encourages neglect of the human end user perspective, creating potential for harm, as the quote atop this chapter illustrates.

The trend to diminish users' agency is needs explicit targeting if data interfaces are to become more free-flowing [@bowyer2018freedata], and if ecosystem negotiability is to be realised. Somehow, the trend needs to be halted, before it can be reversed. The TikTok example suggests this may only be achievable through regulatory changes.

### The Intractable Data Self{#8.4.3}

The third obstacle to ecosystem negotiability is **the intractable data self**. Data about individuals serves as their _proxy_ [[@bowyer2018family; [5.4.4](#5.4.4.1)]. This is their _data self_ [[4.4.1](#4.4.1.3)]. If it is incomplete, inaccurate or unfair—highly likely given the difficulties of representing people in data [@cornford2013; @martin2007]—this can cause harm [@bowyer2018family; @crossley2022]. Yet currently, although some legal rights to data correction exist [@ico2018], people cannot practically modify or assert control over this most important version of themselves—the version of them that exists in data. Even when data can be seen, people lack the ability to **exert influence** over their data self [[5.5.2](#5.5.2); @cornford2013], which is necessary for _individual self-determination_ [@fisch2015]. To address this obstacle, HDR reformers should explore giving people a role in the curation of their data self [[4.4.3](#4.4.3); [5.5.2](#5.5.2)] and [6.3](#6.3)].

To date, research and innovation on ecosystem negotiability has been very limited. It is easier to find business models and research funding for narrow and well-defined contexts. Without a business motive, only non-profit socially-focussed research organisations such as BBC R&D and Sitra have found themselves well-equipped to explore this problem space. Nonetheless, there is an urgent societal need for individual oversight over one's data self [[6.3](#6.3)]. People need to reclaim their data selves, and be given control over their digital lives at the broadest level.

Obstacles to the HDR Objective of Effective, Commercially-Viable and Desirable Systems{#8.5}
---------------------------------------------------------------------------------------

The previous four subsections considered the obstacles to the HDR objectives [[7.7](#7.7)]. However, through pursuit of these objectives, and through observation of public and business responses to human-centricity, I observed additional obstacles that affect _all_ efforts to make progress towards improving HDR. The main challenge is around building such disruptive systems that are so different from the status quo:

**Businesses and individuals will not readily invest time and money in HDR, because it is unfamiliar**.

### A Lack of Individual Demand{#8.5.1}

Customers are not demanding HDR capabilities in their lives, and, all but the most socially-responsible businesses do not see value in an approach that runs so contrary to current business models, based as they are on data accumulation and the constraining of customer experiences.

Data is overwhelming, complex, and 'sounds boring'. Engaging with your personal data economy to any degree more than that of passive consumer is hard work. People routinely accept data sacrifice, click through T&Cs and cookie banners and are unwilling (or in some cases lack sufficient technical literacy, comprehension or skill) to do the work of asserting control over their digital lives. There is not a clear demand for holistic digital life management and control. Research in this this and at Cornmarket suggests that even if human-centric information systems and more inclusive service interaction practices emerged, people would not be inclined to use them in great numbers. It could seem like hard work or not worthwhile. Just as some people (who can afford it) hire an accountant to manage their finances, we can imagine that some would prefer not to have to manage their own data. This obstacle affects all HDR improvement approaches. Indeed, this is why many companies in the emergent PDE economy [[2.3.4](#2.3.4)] struggle to find a business model. There are clear benefits, but better HDR does not appear to something a mainstream audience will pay for. This should not deter disruptive innovation nor diminish the potential value for such tools. As automobile pioneer Henry Ford famously said, _"If I had asked people what they wanted, they would have said faster horses."_ Nonetheless, it is a clear overarching obstacle, which [Insight 7](#insight-7) attempts to confront.

<span class="editnote">Add ref to Insight 7 here</span>

### Closed, Insular and Introspective Practices{#8.5.2}

The kind of life-spanning, unifying interfaces described in the insight above are nothing like the interfaces that are built today, as they span across different providers' data and services. This highlights the secondary obstacle that all HDR system builders will face, whichever objective they wish to target: **closed, self-interested organisations** with **a lack of interoperability**. Building an HDR system will necessarily involve connecting to systems of different providers that have different touchpoints into an individual's life and world. Yet most companies act in closed, introspective and non-cooperative ways to further their own interest. Companies like Apple, Amazon, Microsoft, Facebook and Google (the so-called _'big five'_) build **proprietary, incompatible silos** or _'walled gardens'_—sub-Internets that pretend that the alternatives do not even exist, in order to encourage a flow of money and attention to their own products and services. In doing so, they fail to recognise users' holistic needs [[2.3](#2.3); [6.1.3](#6.1.3)].

Commercial motives encourage them to get users to spend time in their own proprietary spaces (so that resultant ad revenue can be captured) and in order to maintain subscription revenues it is in providers' interests to make it hard for individuals to leave or switch providers. In effect, providers build for a world that does not exist, where every individual is imagined to only interact with that single company's interfaces. I would argue, for example, that Google's venture into social networking with Google+ did not succeed because it failed to build for a reality where most people and their friends were already on Facebook.

### A Lack of Organisational Investment in HDR{#8.5.3}

One can understand why companies are not motivated to build holistic, open experiences. There is little incentive to open up the ecosystem when the free flow of information and of users might result in loss of income. Users with negotiability would be more able to leave. And this also encourages keeping users in the dark [[5.4.2](#5.4.2)]. The less agency and negotiability that users have, the more freedom the provider has to do exactly what they want with their data. In this context, users are _'docile bodies'_ [@foucault1975] or _'pathetic dots'_ [@lessig2000].

The tendency of organisations to work in closed, introspective ways and to be resistant to opening up data or services is not solely motivated by commercial reasons: the public sector has a vastly complex, closed and fragmented ecosystem [@pollock2011; @copeland2015; [4.1.2](#4.1.2)]. Our efforts to build a system to share health data with support workers for the SILVER project [[3.4.1](#3.4.1.1)] proved hugely challenging. Sometimes the challenge was a technical one–incompatible data formats that are hard to reconcile, or data being stored in legacy systems with no public API that would allow programmatic access to that data, or issues around licensing. But data sharing agreements also have be established, especially in the public sector which is by its nature more liable to scrutiny and accountability. More than these technical or procedural issues, there was _resistance to change_ data processes and an unwillingness to share data between agencies, often motivated by a fear of legal repercussions. **Data-centrism encourages insular thinking**: it encourages organisations to codify the world into their own systems, processes and formats for their own use (e.g. [Figure 9.12](#figure-9.12)).

### A Lack of Interoperability{#8.5.4}

Yet, for effective HDR, **data needs to be separable from services**. The more users' data is tightly coupled to specific services, the less agency users have and the harder it is to build life-centric systems. In BBC R&D's Cornmarket project, attempts to build an interface for users to import data from multiple popular Internet services proved to be a hugely complicated endeavour, requiring access to many different APIs or manual exports and imports of data by users. There needs to be greater interoperability and greater establishment and adoption of **standard formats for exchanging human information** (as distinct from establishing standards for data or service-specific APIs). As mentioned above, platformisation breaks the Open Web [@plantin2018]. To overcome this, companies must be persuaded that human-centric thinking, interoperability and transparency has not just social benefits, but business benefits too. In the absence of such openness, a subculture of _adversarial interoperability_ has arisen, where activists, facing a lack of support, force connections to providers' systems in ways that are not approved [@doctorow2019].

### Insufficient Machine Understanding of Human Information{#8.5.5}

At an abstract level, the technical obstacle is one that has always faced the tech industry, which is that there often is no universally agreed way to represent important concepts–in this case human-centric information concepts such as events, social media posts, website visits, location history information, app activity, etc. And any entity that does create a standard then faces the challenge of trying to persuade others that their standard is the best one to use. In general, standards work best when established by non-commercial industrial standards bodies (for example the World Wide Web Consortium (W3C) or International Organisation for Standardization (ISO)) and then mandated through policy such as European Union law. Such standards much be established with input from industry experts.

<span class="editnote">Add ref to Insight 8 here</span>

Even after addressing the obstacles of end-user buy-in and the technical complexities of building human-centric systems, data-driven corporations, motivated as they are by profit and business success (and smaller online organisations too) need to be persuaded of the business value of transparency, interoperability and human-centricity. This is explored further in [9.5](#9.5).

In summary, whichever of the above four HDR objectives are targeted, all HDR reformers involved in building HDR systems must:

  1. create, adopt and co-ordinate around **new standards** for human information storage and management
  2. invest in systems that elevate computers from data-processing machines to **human-information-processing machines**, and
  3. make a persuasive case to both businesses and individuals that the new approach offers **tangible, previously unavailable value**.

Summation of Chapter 8: From Obstacles to Opportunities{#8.6}
----------------------

This chapter has presented, in effect, **a map** of the HDR landscape. It has described the major obstacles to better HDR including invisible, inaccessible, scattered, immobile, unmalleable, or unrelatable data; the complexity of current personal data ecosystems; a lack of metadata and machine understanding; the ongoing exertion of power by introspective data holders to diminish user agency; and a lack of demand and investment in HDR. [Figure 8.1](#figure-8.1) showed an overview of how these different obstacles might be understood to relate.

This chapter can enable HDR reformers to 'hit the ground running' with an understanding of some of the challenges that exist, and insights that may suggest possible strategies to tackle them. A good high-level understanding of the landscape combined with some specific ideas should be valuable for anyone working in the HDR space. Therefore, [Chapter 9](#chapter-9) expands further on these understandings and insights, presenting four specific and detailed strategic approaches to tackling the obstacles in this chapter.

-----
