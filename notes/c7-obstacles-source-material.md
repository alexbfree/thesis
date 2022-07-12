### Data Awareness & Understanding

#### Obstacle 1: Illegible Data

As outlined in People struggle to relate to data. It is not relatable because it is complex, not presented as meaningful information, and not easily interpretable as information. They lack tools to gain insights. To overcome this obstacle, more work is needed to make data relatable and to provide tools that can deliver valuable meaning and insights.

#### Insight 1: Life Information Makes Data Relatable

When data is transformed into information that can be related back to moments, people, places or relationships in people's lives, it becomes instantly relatable.
[from BBC: Data becomes meaningful when people are able to associate it with the real substance of their lives - people, places, organisations, causes or topics they care about. Therefore, the more associations you can find in data the more valuable it is.]

We can consider the different types of information in people's lives:

![Figure X: Life Concept Modelling](./src/figs/figX-life-concepts.png)

We need to model life information, not data.



#### Obstacle 2: The Personal Data Diaspora

Every individual's personal data is scattered across multiple providers, devices, apps, held by hundreds of third parties. The complexity of a modern day digital life is unmanageable and overwhelming. People are inevitably ignorant of much of their data and its use. This can lead to resignation and apathy. To overcome this obstacle, approaches must be identified that recognise the scattered, complex reality of each individual's personal data ecosystem and begin to make it visible and understandable.

#### Insight 2: Ecosystem Information is an antidote to Digital Life Complexity

No matter how understandable the data itself is, it is also critical that people can acccess information about their data ecosystem. Without this, there will always be aspects of their data that are beyond their awareness or beyond the reach of what they can access, control or manage. Many tools today do not recognise this, and build for a world that does not exist. It is important that people have tools that allow them to interact with multiple providers and data sources across their digital life.

### Data Useability

#### Obstacle 3: Data is immobile

Almost all data is constrained in some way, limiting its useability. It may be held by a particular provider and inaccessible. It may be stored in a format which is hard to use or change. It may only be visible after a delay. It may be unchangeable. To overcome this obstacle, we need to find ways to extract data from its current constraints and to remove some of these technical or temporal limitations.

#### Obstacle 4: Data that is Unmalleable and Non-Interrogable

Even once an individual has gained possession or access to the relevant parts of their personal data, it can be extremely hard to use. This partly comes from a lack of malleability - the ability to break it down, look at it from different perspectives, reconstitute it in different ways. Put simply, people need to be able interrogate their data - ask questions of it. This requires more than just an ability to view visual representations of data, but an ability to interact with the data and produce new views and insights that can help to answer specific questions. Making some of the PIM and SI capabilities described in 2.2.2 and 2.2.3 can help to address this, but more capabilities can be made available and are needed to fully overcome this obstacle.

#### Insight 3: Life Information & Ecosystem Information should be Useable as a Material

Many computer operating systems and interfaces today treat files as the basic material that an individual can manipulate. To truly empower users to make use of their data, we need to move to a model where pieces of life information -- facts (or assertions) -- can be created, deleted, moved, grouped, annotated, copied, shared, modified, labelled, organised, separated or otherwise manipulated instead. So far, people access data within products. But what they need is a platform, not a product. We need an information operating system.

### Ecosystem transparency

#### Obstacle 5: A Complex and Invisible Data Ecosystem

The first and most obvious barrier that individuals face in managing a complex personal data ecosystem is that, to a great degree, they cannot see it. For example, it is very easy to allow a handful of communication and social media apps access to your address book or contact list, and before you know it you have created a complex and unmanageable network of connections that silently sync and propogate your adddresses and phone numbers across the Internet. And there are deeper layers which are not even slightly visible to users: networks of data brokers, advertisers and digital cookie companies exchanging user identifiers, activity data and personal information about you while you browse or use apps. As Chapter 5 showed, even though people have been granted new rights to access their data and information about provider data sharing activity, the ability to effectively execute those rights to build up a meaningful picture of your personal data ecosystem is severely limited by inconsistent, incomplete or unclear responses. The strong negative practical impacts of today's complex digital lives were already described in section 2.2.4; managing the complexity is an overwhelming, unmanageable task that even personal data experts are not fully able to get a handle on. The ability to provide a user with ecosystem transparency is hindered by the complexity and multiplicity of the data relationships they have been encouraged to set up, and by a lack of tools to provide a meaningful, or indeed any, view of those relationships. A further aspect to this obstacle is that no individual or organisation has the ability to see the whole of a user's ecosystem, and there is little commercial motive to try and solve this problem, as every provider focuses just on their own apps, websites and services.

#### Obstacle 6: A Lack of Metadata

From this complexity an additional obstacle becomes evident. There is scant attention to information **about** your data. Even where data access rights are executed (or data is shared via human means such as in Chapter 4), the attention is on the data itself: what it says. Chapter 5 shows that some of the most desired information was not the data itself, but how it is used and shared and what is inferred from it, yet this was rarely forthcoming. There are many pieces of information that can be quantified about an individual's data, as illustrated in Figure X, which I created during my internship at BBC R&D:

![Figure X: Some of the many aspects of metadata that might exist about a datapoint or dataset](./src/figs/figX-metadata.png)

[ EXPLAIN ASPECTS]

To provide users with meaningful transparency, many of these aspects will need to be tracked and visualised; not an easy task given the complexity and the potential to overwhelm a user, but nonethless a vital first step on the road to giving individuals the ability to have oversight of their personal data ecosystem and take action within it.

[ADD REFERENCE BACK TO 2.2.2 METADATA]

#### Insight 4: Data Needs Provenance

A number of researchers have independently identified the importance of keeping the history of a piece of data with it. Without context, data loses meaning (a phenomenon witnessed in Case Study Two -- see 5.4.3.1). The idea that what has happened to not just an individual but to a piece of data over time is important is a key part of the thinking behind temporal PIM systems, from Lifestreams [@freeman1996] to activity streams [@hartdavidson2012] (see 2.2.2). William Odom, Siân Lindley and colleagues proposed the idea of file biographies, which view the lifetime of a file as something that should remain connected and traversal in order to understand the context of the file at its different interaction points.
Significant research in this space has been undertaken by Professors Mike Martin and Rob Wilson at Northumbria University, formerly Newcastle University, who express the idea of **data with provenance**; in other words that data must carry with it the details of why it exists, how it came to be, and what has happened to it since its inception, and that provenance must be communicated alongside any visualisation of the data, if it is to be fully understood (ie. for its context []). This plays into the ideas of Gitelman, Neff and others, that data is not neutral and in fact is inherently biased, since it was created for a specific purpose with a specific agenda in mind [@gitelman2013;@neff2013]. [ADD MORE DETAIL FROM MIKE MARTIN PAPER AND EMAIL HERE]. While it is not a solution in its own right, it is clear that data with provenance is very likely to be a critical and valuable part of any design that aims to help individuals with managing to get an overview of their complex and invisible personal data ecosystems.

### Ecosystem negotiability

#### Obstacle 7: Provider Hegemony and the Nature of Digital Power

In the pursuit of individual oversight and greater involvement, the power imbalance between individuals and data holders (2.1.2) becomes most clear. While the Internet itself initially held the promise to be a great leveller and to empower individuals, this potential has largely been suppressed. Data is owned and controlled by service providers, who also design and control the interfaces, apps, websites and devices through which individuals access those services, controlling what (if any) of the data stored behind the scenes, and of the internal processes that use that data, is visible, and how such data and processes are represented. In Jasperson _et al._'s detailed metatriangulation review of types of power that affect technology systems [@jasperson2002] we can identify a number of specific types of power that clearly are in effect in today's digital data-centric service provider context:

[ADD TYPES OF POWER FROM JASPERSON WITH CONTEXTUAL EXPLANATIONS]
[structual power,
resource control,
centralisation
etc]

![Figure X: The Panopticon Structure of the Illinois State Penitentiary](./src/figs/figX-panopticon.png)

[@foucault1975]

A helpful analogy for the relationship between provider and user can be seen in the design of Panopticon: A style of prison architecture designed to elevate the power of the prison guards to observe all the prisoners easily at any time and to diminish the ability of prisoners to operate in privacy or to see those in authority. Jeremy Bentham [REF], drawing on the philosophy of Foucault [REF], makes clear that such design is political, and shows that power can be enforced by the environment. This is a useful mental scaffold to keep in mind; as explained below [REF], we can think of today's digital landscape as similarly power-enforcing. Code is law [ADD REF Lessig], and interfaces limit what individuals can do. By holding data behind interfaces shaped to serve their own interests, the landscape is controlled by the data holders.
[UPDATE THIS BASED ON OTHER WRITING ABOUT PANOPTICON]

#### Insight 5: Data Holders Exploit Four Levers of Power to Manipulate the Digital Landscape

Sitra's #digipower investigation [REF], of which I was project leader for Hestia.ai, was a successor to my Case Study Two, but worked with high profile politicians and European influencers and added additional technical audit techniques. Its focus was not on the individual experience of data access, but on using those experiences and acquired datasets to better understand the data ecosystem. Through this research, a model was produced to understand the ways in which service providers (and in particular the larger ecosystem-level platform providers such as Google and Facebook) exert power over individuals and smaller organisations. This model is reproduced in Figure X:

![Figure X: The Four Levers of Infrastructural Power](./src/figs/figX-four-levers-of-power.png)
[TODO: redo this diagram]

[ADD EXPLANATION AND REFERENCE TO THE PIDOUX REPORT]

Through this landscape it is clear that the most powerful data holders exert huge influence over the digital landscape, in terms of what is knowable and what is do-able. Individuals or activists' abilities to balance the landscape are hindered by the fact that they are operating in a landscape that the incumbent platform and service providers effectively control.

A key mechanism to highlight here is that the accumulation of information is implicitly and objectively a form of power. This is consistent with participants' observations in 5.4.4.1 that data holding and limiting access to it is a source of power. In terms of this being an obstacle, we can therefore see that as long as current platforms and service providers are free to collect so much personal information, the information landscape will remain imbalanced and individuals will not be able to acquire ecosystem negotiability.

#### Obstacle 8: Closed, Insular and Introspective Practices

Today's digital landscape is fractured[REF Splinternet]; myriad providers vie to pull users into service relationships or connected ecosystems that will encourage a flow of money and attention to their own products and services, most evident from companies  such as Apple, Amazon, Facebook, Google and Microsoft (the so-called 'big five') that have multiple touchpoints into people's lives through different devices, apps and services. We can think of these different providers' sub-Internets as walled gardens or silos [REF]. Commercial motives encourage them to get users to spend time in their own proprietary spaces (so that resultant ad revenue can be captured) and in order to maintain subscription revenues it is in providers' interests to make it hard for individuals to leave or switch providers. In effect, providers build for a world that does not exist, where every individual is imagined to only interact with that single company's interfaces. There is little incentive to open up the ecosystem when the free flow of information and of users might result in loss of income for the company in question. Users with negotiability would be more able to leave. And this also encourages keeping users in the dark (5.4.2). The less agency and negotiability that users have, the more freedom the provider has to do exactly what they want with their data. In this context, users are, as Lawrence Lessig wrote, _'pathetic dots'_ [ADD REF]. Thus service providers continue to build **proprietary, incompatible silos**.

But it is not only commercial motives that encourage insular attitudes to personal data and user service provision. In the SILVER project [ADD REF] meetings with local authorities and care providers revealed deep organisational and technical barriers within the public sector, with for example health organisations being typically unwilling to share health data with social care services, but also with different councils, community services and charities typically operating separate IT systems, each attempting to construct their own digital pictures within their own databases and very little operability. The problems of this technical reality are explored further in 4.1.2. From what we have observed, the introduction of GDPR and similar regulations has made this problem worse not better, as organisations and departments become increasingly paranoid about storing or sharing data they should not, or about the risks of acting upon data without sufficient consent. We learned of practices such as the sharing of information between care organisations verbally by telephone so that no digital trail was left.

It is clear that throughout society, there is a trend towards organisations being reluctant to work together around people's data, inclined towards collecting their own databases and not sharing them.

Also mention resistance to change

#### Obstacle 9: A Trend of Actively Diminishing Individuals' Agency

As a result of the practices and motives described above, the last decade has seen much reduction in individuals' agency. When software was sold in a box, manufacturers competed based upon which product would let the user take home the greatest range of features and capabilities. New releases with new features drove new product sales. But in the cloud computing era, a smaller set of core features done well is sufficient to guarantee an ongoing subscription revenue from a user. Cost savings in development and support costs can be made by reducing feature sets. The relentless pursuit of increased profits and further cost saving sees products lose, not gain, features. Interfaces are reshaped to serve businesses' interests first and foremost. As described in 2.3.5, the primary concern is about making user behaviours constrained, predictable and profitable, rather than meeting their needs or providing maximal value. One of the most revealing examples is seen in the case of Facebook. Users used to be free to consume their friends' posts in other clients via RSS feeds. These were removed, forcing users to use only Facebook's interfaces, where their eyeballs can be monetized (Twitter closed its APIs too to a great degree, killing off many third party readers). On Facebook users used to have the ability to view the latest updates from a particular list of friends or of news pages. These features too were removed, presumably to increase monetization through the main feed. The 'Friends' page on Facebook currently shows a list of recommended new friends; to access your current friend list requires an extra click. Encouraging users to grow their networks is prioritised over user convenience.

Companies change their practices to limit users' agency (and their own accountability to customers) too. For example, Facebook recently announced they will no longer collect historical location data from users (though they will still use location information). This makes it harder for users to see how their data has been used. Tiktok announced they will rely on legitimate interest rather than consent when it comes to using users' activity data to personalise the app experience, removing users' ability to withdraw consent to such use. Unchecked, it is clear that trends to reduce users' agency and further providers' interests will continue, creating another obstacle to be tackled.

[ANOTHER EXAMPLE: That guy who got banned from Facebook for letting people read their Facebook feed in a different way] [AND the blocking of accessibility readers] [and Chrome getting reinvented] [List of bullets]

#### Obstacle 10: The Inaccessible Data Self

Earlier in this thesis the concept of a data self has been introduced
(4.4.1, 4.4.3, 6.3). We know from both the preliminary study with families [@bowyer2018b] and Case Study Two that data serves as a proxy for direct human involvement of the served individual(s). Put simply, service providers try to minimise interaction with people, by maximising their usage of data to represent people. We are viewed through the distorted lens of our data selves. Despite the inherent challenge of representing people fairly and accurately in data [@bowyer2018b; 4.4.1; 5.4.4.1], this is the default modus operandi for service provision today. This therefore represents a key obstacle to ecosystem negotiability today: how can individuals be given the ability to influence and shape the data self that providers will use to understand them and make decisions?

### Obstacles in the Solution Space

While in the previous four subsections it was possible to identify obstacles relating to specific HDR wants, there are also some readily identifiable obstacles that will affect all our endeavours to improve HDR. Obstacles relating to human challenges are described in this section, and technical challenges are addressed in the following section, 7.3.6.

#### Obstacle 11: A lack of demand and HDR motivation, and perceived hard work

In considering the recommendations of Case Study One (shared data interaction between the state and the individual) and of Case Study Two (new human-centric data practices by service providers), and in exploring possible new human-centric system and interface designs through my work with BBC R&D, it is evident that even if new human-centric types of computer system or service interaction practices can be created, we cannot assume that people will be inclined to use them. Today, data is overwhelming, complex, and 'sounds boring'. There is no denying that currently, engaging with one's personal data economy to any degree more than that of passive consumer, is hard work. People routinely accept data sacrifice, click through T&Cs and cookie banners and are unwilling (or in some cases lack sufficient technical literacy, comprehension or skill) to do the work of asserting control over their digital lives. There is not a clear demand for holistic and novel ways of managing your digital life and exerting agency and negotiability over it. This can be seen as an obstacle that affects all HDR improvement approaches we see, and indeed is why many companies in the emergent PDE economy (2.3.4) struggle to find a business model. But this should not deter disruptive innovation nor does it indicate that such offerings would not be useful. As Henry Ford famously said, "If I had asked people what they wanted, they would have said faster horses." Nonetheless, it is a clear overarching obstacle to overcome.

#### Insight 6: New Life Capabilities and Pain Relievers Drive User Demand

Through work at the BBC R&D exploring how to better connect people with their data, it became clear that there is a way to combat such indifference and apathy of users. It emerges from the realisation that the way people find value in data is to connect it their lives. The more that people see relatable life information and can imagine ways to harness that information in their everyday life, the more motivated they will be.
[include the three concentric circles diagram a bit like the one Rhianne used]

As an example, myself and BBC colleague Jasmine Cox imagined focusing on address books and contact lists as a strong relatable starting point that could easily generate a user demand. Many people face a complexity they cannot easily manage when it comes to the automated syncing and sharing of potentially sensitive contact information between devices, apps and providers, and developing human-centric personal information management capabilities to bring that messy situation under control would offer a clear and tangible benefit to users.

![Figure X: Conceptual Semantic Grouping of Related Data for a Vacation](./src/figs/figX-vacation.png)

Another example that is helpful to consider is my the example from my 2011 article: that of a vacation, as shown in Figure X [@bowyer2011]. Today, all the information around such a holiday is scattered into multiple systems - emails, online provider bookings, chat logs, cloud synced photos, web browser bookmarks, smartphone location logs, etc. It is not hard to imagine that a system that was able to bring all related information about that vacation together in one central place could deliver huge value to users and be very compelling. Such context-targeted human-centric offerings can have a much greater chance of generating interest and impact than offerings that merely allow you to "organise your data" or some other abstract phrasing.

As with any public offering of a product or service, it is important to start with identifying a problem or need, and to demonstrate a potential tool or solution that can help. In particular, there is a need to let people do **new** things that they could not do before. This has been identified as a key ingredient of user empowerment [@schneider2018;@meschtscherjakov2014]. This became a driving influence for design thinking on the BBC R&D Cornmarket project.
It is not enough to believe that "If you build it, they will come."

#### Obstacle 12: A lack of Interoperability

Obstacle 8 (7.3.4.3) already touched on the issues around different companies developing different standalone walled garden or silo user experiences, from a sociotechnical or systemic standpoint. But there is a very specific technical problem that must be acknowledged across all HDR improvement approaches, and that is that it is very difficult to build technical systems that connect and exchange data with each other. This was witnessed first hand by our development team on the SILVER health data interface project [REF] which endeavoured to build a bridge making health data available to Early Help support workers. Not only are there a lack of standards, with each organisation using their own databases and formats for storing data, but often the programming interfaces (APIs) that would be needed to interface between different systems (sometimes legacy systems) do not exist, are insufficient. Furthermore, there can be issues around licensing and consent when data passes from one domain to another. Data sharing agreements must be established, especially in the public sector which is by its nature more liable to scrutiny and accountability. But at an abstract level the technical obstacle, the problem is one that has always faced the tech industry, which is that there often is no universally agreed way to represent important concepts - in this case human-centric information concepts such as events, social media posts, website visits, location history information, app activity, etc. And any entity that does create a standard then faces the challenge of trying to persuade others that their standard is the best one to use. In general, standards work best when established by non-commercial industrial standards bodies (for example the World Wide Web Consortium (W3C) or International Organisation for Standardization (ISO) and then mandated through policy such as European Union law. Such standards much be established with input from industry experts.

#### Obstacle 13: Insufficient machine understanding of human data

Following on from the previous obstacle, but a subtly different point, is that it is technically difficult for machines to handle human information. Without deliberate coding, software can only understand streams of binary data as files or datasets, and does not understand what people, places, events or entities the facts within the data relate to. Therefore, it is necessary to consider how algorithms and systems can be designed to include an understanding of the semantics (meaning) of the information within the files and data records they handle. For example, the data record representing a post on Twitter looks entirely different to the data record representing a post on Facebook. No algorithm can recognise or unify these disparate pieces of data as two instances of the same semantic concept until it the specifics of the data format can be mapped back to a common semantic abstraction of a "social media post".
[find meaning in user's data]

#### Insight 7: Semantic Analysis and Information Standards can Transform Data Storage and facilitate human-centric interface building

![Figure X: Annotating Data with Semantic Context](./src/figs/figX-semantic-annotation.png)

This leads to the next insight: that to build systems and interfaces that are able to deal in human concepts and represent the elements of everyday life requires building systems that store semantic context and semantic associations, not just raw bundles of data. This is advocated by the Web's inventor Tim Berners-Lee in his vision of a Semantic Web [@bernersLee2001] and by proponents of networked PIM systems (2.2.2). There is a need to develop standard ways to digitally model facts and assertions about users' lives, so that those disparate pieces of data can be unified, connected, correlated and compared. Sizable industries have built up around Content Analytics and Enterprise Content Management. Through the capture of metadata at the point of data recording, and through subsequent programmatic analysis of stored data, as illustrated in Figure X [@bowyer2011], we can begin to teach computers what the data we store represent. Machine learning technologies and Artificial Intelligence have pushed machine understanding of human words, images and content to impressive levels in recent years and such technologies can certainly be helpful, but in fact at the core what we are talking about here is somemthing much simpler than AI; It is simply about labelling datapoints in as many different ways as possible so that those datapoints can be associatively retrieved from many different angles, and providing humans with ways to amend incorrect labels and to reclassify data or apply new semantic associations.

#### Insight 8: Better HDR can deliver business value through increased accuracy and consent, and decreased liability.
