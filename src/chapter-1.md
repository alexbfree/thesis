<h1 class="title">Section I: Introduction, Background & Approach</h1><a name='section-i'/>

<h2>Introduction to Section I</h2><a name='#section-i-intro'/>

This thesis is divided into five sections:

* Section I: Introduction, Background and Approach
* Section II: Understanding Attitudes and Desires through Participatory Case Studies
* Section III: Defining A New Research Agenda: Human Data Relations
* Section IV: Operationalising the Research Agenda through Design & Practice
* Section V: Conclusions and Outlook

This first section, Section I, provides a thorough background and explanation to the thesis through three chapters:

* [Chapter 1](#chapter-1) introduces the research, explaining the background, context and objectives, then summarises the contributions and publications generated, before outlining the structure of the rest of the thesis.
* [Chapter 2](#chapter-2) contains a literature review, laying out the foundational ideas upon which this research is built; drawing from information theory, data access legislation, personal data interaction system design, and the emergent human-centric paradigm of personal data ecosystems.
* [Chapter 3](#chapter-3) describes the methodology used in the research, from its philosophical foundations to its overall research objectives, and details the specific participatory techniques and data analysis approaches used.

Introduction{#chapter-1}
=======================

> _"My data is everywhere, and I am nowhere."_—Imogen Heap (musician and digital rights advocate), speaking at MyData 2019, encapsulating a core problem with modern digital life.

Background and Motivation for this Research{#1.1}
-------------------------------------------

We live in an increasingly data-centric world, where our direct and indirect interactions with computer systems depend upon the collection, storage and use of personal data about individuals. Motivated to reduce costly human interaction and scale to serve more customers, organisations capture and represent individuals as data and rely increasingly on the interpretation of those datapoints to make decisions—decisions that affect our everyday lives in myriad ways, from determining eligibility to access particular services, benefits or products or targeting advertisements or recommendations to influencing our decisions and behaviour. Data about people has become extremely valuable. It is 'the new oil' [@toonders2014] driving a model of _surveillance capitalism_ [@zuboff2019] that collects data and exploits it for profit.

This multi-party use of data has resulted in a splintering [@lemley2021] of our _digital selves_ across hundreds of different organisations' computer systems, creating 'a chaos of multiplicity' [@bødker2015] where data becomes trapped [@abiteboul2015] and hard to manage. Current data practices cause harm to individuals through anxiety, distraction and a sense of being overwhelmed [@fu2020; @timely2020]. Data use can harm society too, due to the ease with which people's attention and beliefs are manipulated, risking radicalisation and a loss of democratic freedom [@thompson2011; @chan2019]. It is generally accepted that:

> _"There is **a power imbalance** in the amount of information about individuals held by industry and governments, and the lack of knowledge and ability of the same individuals to control the use of that information."_—World Economic Forum [@wef2014context]

To address this power imbalance, people need a more effective relationship with their own data. This has been conceptualised as a lack of _agency_ (the ability to act for oneself), _negotiability_ (the ability to exert influence over data use within the system as things change), and _legibility_ (the ability to understand one's data and its implications) [@mortier2014]. A need is growing for the conscious design of human relationships with data, as these problems cannot be solved through interface design alone but only through the reconfiguration of service relationships that involve data. Currently, users of today's digital services typically experience a _point of severance_ [@luger2013]: they are forced to sacrifice their data and are subsequently cut out of the loop. Without understanding how they are currently seen through data, people face risks of unfair treatment, or physical or psychological harm [@bowyer2018family; @crossley2022]. Left unexplored and unchallenged, the situation will not improve, as the datafication of society grows, and user agency continues to diminish.

This thesis focuses on that power imbalance and seeks to design improvements to information interaction interfaces, processes and service relationships that can improve individual agency, legibility and negotiability. This PhD tackles this design challenge through a hybrid approach that uncovers individual needs through participatory co-design workshops and qualitative interviews, alongside  grounded innovation and development work carried out by the author while embedded in industrial and academic project settings, focusing on operationalising and refining the emerging design objectives through user-centred system design, conceptual modelling, and prototyping.

The two parallel tracks of this research [Figures [1.2](#figure-1.2), [3.2](#figure-3.2)] are described separately in [Section II](#section-ii), which describes Case Studies exploring how people relate to data, and [Section IV](#section-iv), which embraces the commercial realities and lived experiences of today's data-centric world to present the author's grounded learnings from projects that seek better data relations. These tracks ran concurrently, resulting in a perpetual action research feedback cycle [[Figure 3.15](#figure-3.15)] where participant insights and theoretical models informed practical system and process designs while real-world learnings about societal challenges and practical obstacles refined the emerging models.

[Section III](#section-iii) combines Case Study findings into a unified theory that captures six core human desires for data relations as future research goals for empowering individuals through their personal data. Through a new research agenda **Human Data Relations (HDR)**, which incorporates Human Data Interaction (HDI) [@mortier2013; @mortier2014] theory, specifies four objectives for improved HDI and data relations in practice. [Section IV](#section-iv) therefore serves as an operationalisation of that agenda, documenting practical obstacles as well as four distinct approaches to the pursuit of HDR (including _adversarial design_ [@disalvo2012]). [Section V](#section-v) crystallises these novel contributions to knowledge into thirteen design principles to support the generation of actions by future researchers and innovators to pursue the empowerment of individuals and the rebalancing of power over data, equipping them with ideas and understandings they will need to bring about better Human Data Relations at a societal level.

### Personal Motivation and Context{#1.1.1}

This PhD and this thesis represent the culmination of my lifelong passion to help people get more value from our computers. My experience and expectations of computers were shaped by the 1980s home computing revolution, which taught me and a generation of young people that the computer was a machine to program, a tool to be exploited, mastered and bent to your will. Then, in my formative years approaching the turn of the millennium, I lived through the birth of the public Internet and marvelled at the ability for computers to connect people across the world, empower individuals as creators, innovators and broadcasters, level the playing field and transform the way people interact. In my software engineering career, I gradually transitioned from back-end to front-end development and ultimately to User Experience (UX), driven to take a more active role in building software features that directly benefit users and improve their lives. Keenly tracking and embracing the Web 2.0 revolution while observing the digitisation and disruption of so many industries, I became fascinated with the ways in which humans were shaping computer systems which in turn were shaping our habits and our society, phenomena I explored through the Human 2.0 blog which I co-founded [@bowyer2009human].

But then, having seen Internet-era computing give us new capabilities, and knowing the potential of computers to become tools for positive change in society, I bore witness to a changing world, and the balkanisation and commercialisation of the once-free Internet. As companies adapted to the Information Age and shifted to data-driven, cloud-centric business models, our ability to harness computers for our own ends began to slip away. While immersed in the start-up community in Montréal, Canada, I became frustrated at this loss of potential. Driven to explore the reasons for, and implications of, this loss of agency, and the possibilities for more human-centric computing, I published several essays and presentations [@bowyer2009bitnorth; @bowyer2010bitnorth; @bowyer2011filesdie; @bowyer2012bitnorth; @bowyer2012timespace; @bowyer2013bitnorth] which collectively form the seed from which this thesis grew.

By 2014, it was beyond doubt to me that the software industry had lost its way, prioritising business goals over user agency, reducing features and creating technology designed with in-built limits to our capabilities and interfaces optimised to corral users to behave in certain ways. Web 2.0's revolutionary potential of a 'people's internet' had been squashed and withered away in the shadow of new data giants Google, Facebook, Apple and Amazon, who reshaped and usurped Internet, Web and smartphone technologies for profit, at great cost to human wellbeing. Against a backdrop of a social media revolution which was literally breaking society and democracy to drive profit [@tufekci2017; @hall2018], I took the leap to escape corporate IT. I sought to research, design and build a better digital future where computers could be made useful again. This led me to the _Digital Civics_ CDT programme [@digitalCivicsCDT2018], where I was finally able to work full-time on what I consider the most important problem of our age—**Understanding and Improving Human Data Relations**.

### Research Objectives and Purpose{#1.1.2}

The aim of this thesis is to establish how people relate to personal data, how they understand and use it, and what they want from it and its holders in order to thrive and pursue their goals; and from there, to begin to explore how those needs might be met in practice.

The thesis is informed by a constructivist ontology and a pragmatist, individualist epistemology [[3.1](#3.1)], and employs a multi-disciplinary _Digital Civics_ [@vlachokyriakos2016] approach to examine two key Research Questions (RQ):

> **RQ1.** What is the human experience of personal data, and what do people want from their data? [[3.3.1](#RQ1)]

> **RQ2.** What role does data play in people's service relationships, and how could relationships involving data be improved? [[3.3.2](#RQ2)]

This thesis assumes that if the asymmetry over data access and use between individuals and organisations holding data is to be addressed then a greater understanding of current data use issues is needed by all parties; thus the production of knowledge and insights is a vital first step towards the design of a more balanced model of data use that can deliver increased agency and negotiability.

After this Introduction chapter, Section I continues with a review of relevant existing literature and research [[Chapter 2](#chapter-2)] to identify a clear baseline and research gap, then an explanation of the research approach and methodological choices to be used [[Chapter 3](#chapter-3)].

Section II reports on the two Case Studies, which invited participants to 'look behind the curtain' of the opaque data-centric organisations they interact with. These enabled participants to consider more deeply the collection, storage and use of their personal data by service organisations. A participatory research design was employed, collecting interview transcripts to enable qualitative analysis and identify themes that inform a descriptive model of human-centred data empowerment needs. The focus was upon examining current practices, identifying attitudes to those practices, and imagining alternative designs and approaches for data use by service providers and the participants themselves. The participant groups were:

  - **Case Study One**: Supported families, who meet with _Early Help_ support workers (whose role to understand and empower those individuals to improve their lives is currently supplemented through access to myriad civic data records including housing, benefits and educational data) [[Chapter 4](#chapter-4)]; and
  - **Case Study Two**: Ordinary British and European citizens, who gained new legal rights via 2018's _GDPR_ legislation [[2.1.3](#2.1.3)], enabling them to request copies of held personal data along with other relevant information from the companies and service providers in their lives [[Chapter 5](#chapter-5)].

Comparing the two case studies reveals commonalities in individual attitudes and understandings, validating each other's findings and allowing the expression of clear insights about people's relationships to personal data that can answer the two RQs. This synthesis and analysis of interview data enabled the generation of a descriptive model to address the research gap, concluding the core academic research of this PhD [[Chapter 6](#chapter-6)].

This research is situated in the HCI discipline, which means that design (both participatory co-design and expert-informed user-centred design [[3.2](#3.2)]) forms a key part of the approach to exploring the problem space. Examination of individual attitudes and desires around data in a 'whole life' sense is an under-researched area. Where HCI traditionally focuses on the mechanisms by which humans interact with data, the Case Studies, like the thesis as a whole, adopt a more sociotechnical focus on understanding lived experience.

In order to produce workable designs and theories that could be applied in the real world, the remainder of the thesis takes an even broader perspective, recognising that for participants' desired changes in data relations to be realised requires an examination and a recognition of current technical, legal and commercial realities and the multi-party complexities of modern digital life.

The design work presented in Section IV complements the participatory Studies, providing an additional source of learning: real-world explorations, conducted alongside the qualitative Case Studies, of how to design more effective data relationships. This is done through design, modelling and conjecture, drawing upon the author's direct experiences working part-time in related industrial projects that share this thesis's focus on empowering individuals through data.

To support future researchers, activists and innovators in achieving the vision of a more human-centric future, the pursuit of the identified wants are shaped into a defined new research agenda - **Human Data Relations (HDR)**, which represents a broadening of focus from merely understanding the world towards planning how to change it. Motivations and objectives are identified, and in [[Chapter 7](#chapter-7)] HDR is positioned as a broad activist agenda whose practitioners seek to reconfigure society to their own advantage.

Sections IV and V are deliberately open-ended, mapping out the existing landscape of challenges and possibilities for the HDR agenda, deviating from a traditional thesis structure in order to offer more actionable insights. Given the scale of the sociotechnical design challenge society faces, this thesis does not carry out 'in the wild' evaluation of particular data interaction approaches or interface designs. Instead, drawing upon direct experience as well as the work of other researchers and innovators in this space, it documents known obstacles [[Chapter 8](#chapter-8)]. It also maps out four possible change trajectories [[Chapter 9](#chapter-9)] that can inform future design and innovation in human-centric system design.

A series of design principles underpin Chapters 8 and 9, developed by the author based upon the learnings from both the participatory and project-based research tracks. These principles are documented in [[Chapter 10](#chapter-10)], along with reflections, limitations, a summary of contributions, and ideas for future work. The presented strategies and insights (which should be viewed as speculative rather than definitive), can aid the design and implementation of initiatives that recognise and confront the unique challenges of the status quo in pursuit of improving people's agency and negotiability over and through personal data.

Taken together, the two parallel research tracks of this thesis serve as novel and actionable reference material for future research, activism and innovation, solidly grounded in literary theory, participant experience, and industrial reality.

Contributions of the Research{#1.2}
-----------------------------

The contributions of this thesis are summarised in this section, and described in more detail throughout the thesis, in the referenced chapters and subsections.

### An Understanding of what People want from Personal Data{#1.2.1}

Through the qualitative Case Studies in Chapters [4](#chapter-4) and [5](#chapter-5) and the discursive analysis in [Chapter 6](#chapter-6), this thesis establishes a clear picture of what people want from their personal data. In general, people need all of their personal data to be _visible_ [[6.1.1](#6.1.1)], _understandable_ [[6.1.2](#6.1.2)], and _useable_<sup>[11](#fn11)</sup> [[6.1.3](#6.1.3)].

Furthermore, the sociotechnical focus of the research delivers deep qualitative insights into the _relationships_ people have with data holding organisations and services, revealing attitudes and emotions including distrust, fear, frustration, confusion, helplessness and curiosity. Specific insights are drawn for the two Case Study contexts:

- In social care [[Chapter 4](#chapter-4)], families want to be given a voice, and an ability to see and meaningfully interact with their data. They want to be able to influence how they are understood through data, and to be able to explain and discuss their data with authorities. The Case Study (and its pilot study [[4.2.2](#4.2.2); @bowyer2018family; [Appendix A](#appendix-a)] validate prior findings that highlight families' difficulties with civic data, while documenting their ideas for improving the use of their civic data and for improving empowerment and trust within the support context.
- In the service provider relationships of everyday life [[Chapter 5](#chapter-5)], individuals want to be able to understand what companies are collecting about them. They want to see that data, understand what inferences and decisions result from its use, and exert control over how it can be used, kept and shared. These desires (which also explain motives for using GDPR rights) provide novel insights into the lived experience of the data-centric world, and in particular of using the GDPR to access and control one's personal data.

Examined together [[Chapter 6](#chapter-6)], the Case Studies reveal clear common themes for people in service relationships that involve personal data; people want _process transparency_ [[6.2.1](#6.2.1)] when it comes to processes that use their personal data, _individual oversight_ [[6.2.2](#6.2.2)] over how their data is used, and ultimately _involvement in processes and decision making_ [[6.2.3](#6.2.3)].

The Case Studies also establish a more granular view of what we mean by personal data. The pilot study for Case Study One [[4.2.2](#4.2.2); @bowyer2018family; [Appendix A](#appendix-a)] establishes the term _family civic data_ [[ARI4.1](#ari-fcd-types)], which can encompass relationship information, educational records, welfare details, health data, housing data, and civic and legal records. Case Study Two establishes a model of personal data according to its origin; data can be _volunteered_, _observed_, _derived_, _acquired_ or _metadata_ [[Table 5.2](#table-5.2)]. This model has been adopted by others: during design and ideation sessions at BBC R&D, and within Sitra/Hestia.ai's _digipower_ investigation [[ARI7.2OLD](#ARI7.2OLD)] (for explaining data holding to participants and as a frame for data analysis) [@bowyer2022hestia; @pidoux2022].

Through the design and innovation work in [Section III](#section-iii) and beyond, a deeper understanding of the relationship people have with personal data is developed, and of what role data plays in people's lives. This forms part of the research agenda summarised in [1.2.5](#1.2.5) below.

### Methodologies for Participatory Work around Personal Data{#1.2.2}

A significant component of this PhD (the Case Studies and the preceding formative work and pilot studies) involved selecting, designing and executing methods for engaging with individuals and groups around personal data. At the outset, the challenge of getting laypeople to engage with this potentially dry and boring topic seemed significant. However, building on established methodologies such as card sorting [[3.4.2.OLD](#3.4.2)] and ideation decks [[3.4.3](#3.4.3)], a number of novel approaches were developed, which constitute novel contributions of this research:

<strong>Data Cards and Family Design Games</strong>

This approach was pioneered in the pilot study [[4.2.2](#4.2.2)]; @bowyer2018family; [[Appendix A](#appendix-a)]. To serve as _boundary objects_ and _things to think with_ [[3.4.2OLD](#3.4.2OLD)], a tangible set of _Family Civic Data Cards_ [shown in [Figure 3.6](#figure-3.6)] were developed to represent the different types of civic data. These were used in a variety of exercises in both the pilot study and in Case Study One. While these are not formally assessed as a methodology in this thesis, these were very relatable to participants and proved highly effective at getting conversations flowing around data. A similar approach was used during the BBC Cornmarket project, where a set of Data Cards derived from the Family Civic Data cards concept were designed by the author and BBC colleague Chris Gameson to represent different types of data in the 'everyday digital life data' context [see @bowyer2020internreport for mockup]. These cards were successfully used in a 1,500 participant study by BBC R&D [@sharp2021], showing the value of this contribution. As well as the Family Civic Data Cards, a number of other original activities for considering data such as 'Family Facts' [[Figure 3.3](#figure-3.2)] and 'Sentence Ranking' [[Figure 3.5](#figure-3.5)] were developed and used in the Case Studies. Some of these were published by the author as _Family Design Games_ [@bowyer2018family].

<strong>Storyboarding Action Cards</strong>

For the third workshop of Case Study Two, there was a need to explore interpersonal interactions between different parties in a service relationship, without getting caught up on details of interface layouts or software and hardware capabilities. A novel approach was developed consisting of the use of _storyboarding action cards_ [[Figure 3.11](#figure-3.11)] with participants to give them a vocabulary to map out interactions at a sociotechnical, functional level. These cards are documented in [ARI4.3](#ari-storyboarding) and this approach could be useful to others wishing to undertake participatory co-design work at the relationship or service design level.

<strong>A Methodology for Qualitative Interviews that Explore a User's Personal Data</strong>

For Case Study Two, an approach was designed that would allow a researcher to accompany an individual participant on a journey of exploration of their own personal data files, retrieved from companies using GDPR, and to carry out a guided 'deep dive' into that data, in order to reveal attitudes to revealed data storage and use practices. This approach is detailed in [5.2.2](#5.2.2), and focused on using privacy policy promises and GDPR access rights as a frame of reference from which to assess data response quality and usefulness. The methodology was successful, enabling the production of detailed insights which are presented in [Chapter 5](#chapter-5). The methodology was not designed with a view to it being used elsewhere, but in fact the author was engaged by Hestia.ai to replicate this methodology (with some expansion and tweaks) as co-leader of the digipower investigation, which aimed to take 15 high profile European politicians, civil servants and journalists through a similar journey of discovery. The digipower investigation took place in 2021 and was also able to apply the methodology very successfully, resulting in the publication of multiple research reports [[ARI7.2OLD](#ari-digipower-OLD)].

A technological accompaniment to the Case Study Two methodology was originally developed by the author for use in the interviews, the _private data viewing monitor_ [[ARI3.1](#ari-monitor)], but this was not used for the Study due to the infeasibility of face-to-face interviewing during the COVID-19 pandemic in 2020.

### Best Practices and Design Guidelines for Systems and Processes involving Personal Data{#1.2.3}

The findings from the Case Studies allowed clear recommendations to be produced that can be applied by service providers and other stakeholders in the two specific contexts of the Case Studies. These contributions can be applied more broadly to other data-related service interactions:

<strong>Shared Data Interaction in the Context of Care</strong>

Through Case Study One [[Chapter 4](#chapter-4)], a new human-centric approach and set of practices for support workers working with with families in the Early Help context was developed: To treat family civic data as a resource to be looked at, discussed and updated together on a shared screen or tablet, within the context of a support interaction. This _Shared Data Interaction_ approach was considered advantageous by both staff and families, as it would offer families increased negotiability and evidence-based feedback while also provided staff with a more accurate view of families' lives and greater confidence of their consent. The approach was applied in detail to several scenarios as part of the Case Study, and also has the benefit of shifting the _Locus of Decision Making (LDM)_ [[4.5.3](#4.5.3)] closer to the supported family.

In pursuit of Shared Data Interaction, 12 desirable best practices (which could be of value to any service organisation focused on individual development) are laid out through the sub-themes of Case Study One [[4.4](#4.4)]:

- providing understandable information summarises;
- interacting with data together;
- offering direct and unified data access;
- providing ongoing data access and support;
- avoiding treating people like records;
- checking data together;
- accounting for changes in people's lives;
- enabling individuals and families to contribute data;
- providing granular access controls;
- handling personal data transparently and with respect;
- prioritising the acquisition and demonstration of greater understanding; and
- pro-actively challenging data-centric norms.

<strong>Recommendations for Policymakers, Service Providers and Individuals on Data Use</strong>

Through Case Study Two [[Chapter 5](#chapter-5)] (which explores relationships with service providers in everyday life - especially those where GDPR rights apply), recommendations for rethinking the use of data (and especially access to it) in such relationships were produced:

- Policymakers are recommended to regulate and provide guidance to improve GDPR response quality, to improve enforcement and protection of data rights, and to redesign future policies to consider ongoing access to and understanding of data rather than one-time file delivery.
- Data holders are presented with evidence that improving data transparency can improve customer loyalty. Treating data as a co-owned resource could increase engagement, and an untapped demand for personal data ecosystems is identified.
- Individuals are advised of the importance of their personal data, given it contains meaningful and potentially valuable information about their lives. Individuals are recommended to exert their data rights to improve their awareness and make more informed choices.

An additional contribution presented is the evidence of the positive and negative impacts of GDPR: Knowledge and experience of poor data handling practices are shown to harm provider trust and perceived individual power, but both trust and individual power can be improved through transparency and inclusive data processes.

<strong>A Reframing of Data Literacy for the Sociotechnical Context</strong>

Building on existing thinking about _data literacy_ as a set of skills one can acquire to increase one's effectiveness in an increasingly technological world [@gurstein2011; @knight2016; @precisely2022], this thesis offers an expanded definition of data literacy for the context of data-driven service relationships [summarised in [9.5.1](#9.5.1) and explained throughout Chapter 9], including knowledge and appreciation of:

- the intrinsic value of personal data
- the implications of how one's personal data is used and shared by organisations
- the importance of portable data and of separation between platforms and personal data
- how to exercise one's data rights and assess and act upon responses to data access requests
- the need for a free and fair information landscape
- the ability to identify when one's individual agency is being diminished

All of the guidelines and recommendations that have been summarised in 1.2.3 can guide designers and inform individual and organisational choices, but this thesis also contributes specific principles which can be used to generate system, process and interface designs for better data relations. These principles are summarised in the next subsection.

### Principles for Generative Action towards Better Data Relations{#1.2.4}

In Chapters [8](#chapter-8) and [9](#chapter-9), examples and insights drawn from the author's work with BBC R&D and Hestia.ai, as well as from the work of HDI specialists and activists, are shared. The conclusion of this thesis formalises these learnings and insights into thirteen concrete principles for improving our relationships with and through data. These principles, detailed in [10.1](#10.1), go further than interface design guidelines as they address the sociotechnical reality of how personal data is used today. They could be used to generate designs, interfaces, research projects, activist movements, grassroots campaigns, prototypes, user studies and more and serve as the ultimate actionable outputs from this PhD. The principles are:

- [Principle 1](#principle-1) - Life Information Makes Data Relatable.
- [Principle 2](#principle-2) - Data Needs to be United and Unified.
- [Principle 3](#principle-3) - Data Must be Transformed into a Versatile Material.
- [Principle 4](#principle-4) - Ecosystem Information is an Antidote to Digital Life Complexity.
- [Principle 5](#principle-5) - We Must Know Data's Provenance.
- [Principle 6](#principle-6) - Data Holders use Four Levers of Infrastructural Power.
- [Principle 7](#principle-7) - Human-centred Information Systems Must Serve Human Values, Relieve Pain and Deliver New Life Capabilities.
- [Principle 8](#principle-8) - We Need to Teach Computers to Understand Human Information.
- [Principle 9](#principle-9) - Individual GDPR Requests can Compel Companies to Change Data Practices.
- [Principle 10](#principle-10) - Collectives can Compare and Unify their Data and Use it to Demand Change.
- [Principle 11](#principle-11) - Automating the Identification of Entities can enhance Machine Understanding and Unburden Life Interface Users.
- [Principle 12](#principle-12) - The 'Seams' of Digital Services need to be Identified, Exploited and Protected.
- [Principle 13](#principle-13) - It is Possible (and Necessary) to Demonstrate Business Benefits of Transparency and Human-centricity.

### A Detailed and Actionable Research Agenda and Strategy for Empowerment and Systemic Change{#1.2.5}

In order to bring together the learnings of this research and the above contributions into the most actionable form, this thesis (specifically [Section III](#section-iii)) outlines a new research agenda, called **_Human Data Relations (HDR)_** [[Chapter 7](#chapter-7)]. HDR extends the existing theories of Human-Data Interaction (HDI) [@mortier2014], in order to invite and facilitate confrontation of its practical challenges (as well as the challenges of the other desires identified through the Case Studies). This involves discursive and grounded examination of the sociotechnical realities of held data and provider power in today's data-centric world. HDR can be considered as a framework to operationalise HDI, and its practitioners as a _recursive public_ [[7.8](#7.8)].  

Drawing on the information theory background presented in [2.1.1](#2.1.1), [Chapter 7](#chapter-7) differentiates the needs participants expressed from data (the stored artefact) and from information (the set of facts and opinions encoded within that data), modelling two distinct concepts of _life information_ (from which people gain insights and extract value) and _ecosystem information_ (from which people improve awareness and control over the use of their data). Combining these differing motives with the Case Study themes from [Chapter 6](#chapter-6) yields four clear objectives that the HDR research agenda aims to deliver for people:

- _data awareness and understanding_,
- _data useability_<sup>[11](#fn11)</sup>,
- _data ecosystem awareness and understanding_, and
- _data ecosystem negotiability_.

The practical pursuit of these objectives form the basis of [Section IV](#section-iv) of the thesis, with [Chapter 8](#chapter-8) mapping out the HDR landscape, identifying obstacles and insights that might help overcome them. [Chapter 9](#chapter-9)
provides details of four identified trajectories for those who wish to improve Human Data Relations by pursuing systemic changes that can empower individuals with and through their personal data:

- _Discovery-Driven Activism_ [[9.2](#9.2)],
- _Building the Human-centric Future_ [[9.3](#9.3)],
- _Defending User Autonomy and Hacking the Information Landscape_ [[9.4](#9.4)], and
- _Teaching, Championing and Selling the HDR Vision_ [[9.5](#9.5)].

Publications Arising From and Connected to This Research{#1.3}
--------------------------------------------------------

### Pilot Study{#1.3.1}

My Doctoral Training programme at Open Lab began with a Masters in Research in Digital Civics. For my MRes project[^1], I conducted a pilot study, interviewing and exploring issues around data with families who had experience of social care services. During the first months of this PhD, I conducted new analysis of previously collected data, resulting in the synthesis into a full first-author paper published and [presented at](https://chi2018.acm.org/attending/proceedings/) CHI 2018:

- _[Understanding the Family Perspective on the Storage Sharing and Handling of Family Civic Data](https://dl.acm.org/doi/10.1145/3173574.3173710)_ [@bowyer2018family]

This study is given a special status in this thesis; while the research was carried out prior to this PhD and thus does not form a core part of this thesis, it plays a critical role as a pilot study for Case Study One and its findings and insights are built upon in Chapters [4](#chapter-4) and [6](#chapter-6) and in later discussions. The paper is included in full in [Appendix A](#appendix-A).

[^1]: MRes result awarded: Distinction.

### Primary Case Studies{#1.3.2}

<a name="1.3.2.1">**Publications from Case Study One**</a>

The work exploring shared data interaction in Early Help carried out in Case Study One has been initially published as an Extended Abstract at CHI 2019:

- _[Human-Data Interaction in the Context of Care: Co-designing Family Civic Data Interfaces and Practices](https://doi.org/10.1145/3290609.2012998)_ [@bowyer2019]

This work was also presented at the conference in the form of a poster, which is shown in [Figure 1.1](#figure-1.1). A journal paper is in prep.

![Figure 1.1: Poster Presentation of Case Study One at CHI 2019](./src/figs/fig1.1-hdi-in-care-poster.png){#figure-1.1}

<a name="1.3.2.2">**Publication from Case Study Two**</a>

The work exploring the human experience of GDPR data access carried out in Case Study Two has been published [and presented](https://www.youtube.com/watch?v=hf-XjsCgBJY&t=32465s) as a full first-author paper at CHI 2022, where it was awarded an _Honourable Mention_:

- _[Human-GDPR Interaction: Practical Experiences of Accessing Personal Data](https://doi.org/10.1145/3491102.3501947)_ [@bowyer2022gdpr].

I carried out all field research myself. Data analysis and paper writing were jointly executed by myself and Jack Holt.

### Workshop Papers, Presentations & Interviews{#1.3.3}

During the PhD, I gave a number of presentations and interviews and published three workshop papers. These outputs included material from, or directly contributed to, this thesis and its arguments.

  - _[Designing for Human Autonomy: The next challenge that civic HCI must address](https://eprints.ncl.ac.uk/273832)_ [@bowyer2017] - a short talk I presented to my peers at Open Lab in January 2017 laying out the landscape of reduced agency and possible avenues for improving humans' relationships to their data that my PhD would explore;
  - _[Free Data Interfaces: Taking Human-Data Interaction to the Next Level](https://eprints.ncl.ac.uk/273825)_ [@bowyer2018freedata] - a CHI 2018 workshop paper formalising my pre-PhD design thinking and outlining a vision for unconstrained and useful data interaction interfaces;
  - _[A Grand Vision for Post-Capitalist HCI: Digital Life Assistants](https://eprints.ncl.ac.uk/273826)_ [@bowyer2018grandvision] - a CHI 2018 workshop paper where I imagined a form of digital computer assistant that is far more helpful and human-data-centric than the digital voice assistants of today;
  - _[Personal Data Innovation: Sharing Power to Build Trust](https://blog.digi.me/2019/11/14/mydata-blog-personal-data-innovation-sharing-power-to-build-trust/)_ - A guest interview on PDS company digi.me's blog in November 2019;
  - _[Personal Data Use: A Human-centric Perspective](https://eprints.ncl.ac.uk/273834)_ [@bowyer2020lecture] - a lecture about my research that I was invited to give to undergraduate students at both Northumbria University and Newcastle University in early 2020, just prior to the pandemic;
  - _[My Thesis in 3 Minutes: Understanding and Designing Human Data Relations](https://www.youtube.com/watch?v=YFHXc_TfM5c)_ [@bowyer20213MT] - my entry into Newcastle University's 3-minute thesis competition in April 2021, for which I was co-winner of the people's choice prize;
  - _[Human-Data Interaction has two purposes: Personal Data Control and Life Information Exploration](https://eprints.ncl.ac.uk/274297)_ [@bowyer2021twopurposes] - a workshop paper I presented at CHI 2021, introducing my model of the two motivating factors for interacting with personal data;
  - _[Conversation with Alex Bowyer: Understanding and Improving Human Data Relations](https://podcasts.apple.com/gb/podcast/conversation-with-alex-bowyer-understanding-and/id1581554015?i=1000595165881)_ [@bowyer2023tudelft] - a podcast interview in January 2023 with the Data-centric Design Lab at Delft University of Technology about the Case Study Two GDPR paper and my PhD research in general; and
  - _[The Power of Personal Data: How Companies Exploit Your Data to Shape Your World](https://bit.ly/power-personal-data-part-1)_ [@bowyer2022samespace] and _[The Power of Personal Data: Taking Back Control of our Data and Challenging Powerful Corporations](https://bit.ly/power-personal-data-part-2)_ -[@bowyer2023samespace] a two-part series of layperson-friendly talks about my research I gave at my local co-working space in September 2022 and January 2023.

### Secondary Publications{#1.3.4}

During the same timeframe as this PhD and as resulting from the practical design and innovation work undertaken through the external projects [[Section IV](#section-iv)], I contributed to a number of publications [[7.2OLD](#7.2OLD)]:

- As a researcher and developer on the SILVER project [see [Section II Introduction](#section-ii-research-contexts) and [Section IV Introduction](#section-iv-embedded-project-settings)], my work contributed towards an internal report to CHC as well as the [overall impact report](https://web.archive.org/web/20211225192408/https://www.chc-impact-report.co.uk/) [@ConnectedHealthCities2021impact,129-130].
- Also for SILVER, I published [demonstration videos](https://eprints.ncl.ac.uk/273839) [@bowyer2019silvervideo] of a health data interface prototype developed by myself and Stuart Wheater.
- I was co-author on research relating to improving fast food platform interfaces using adversarial design to encourage healthy eating. This was published [at BCS 2021](https://doi.org/10.14236/ewic/HCI2021.16) [@goffe2021] and [in the Interacting with Computers journal](https://doi.org/10.1093/iwc/iwac015) [@goffe2022].
- As a research intern at BBC R&D [[ARI7.1OLD](#ari-bbc-OLD)], I published an internal design research report [@bowyer2020bbcreport] into personal data store design, and wrote and presented a 'stimulus presentation' on personal data design innovation for members the project team, to launch an internal hack week.
- At Hestia.ai, I was a lead author on [a research report auditing the data economy](https://doi.org/10.5281/zenodo.6554177) [@bowyer2022hestia], and co-author on [a research report on power mechanisms in the data economy](https://doi.org/10.5281/zenodo.6554155) [@pidoux2022].

The Structure of this Thesis{#1.4}
----------------------------

The overall structure of this thesis is illustrated in [Figure 1.2](#figure-1.2). Activities from the two tracks of participatory co-design research and grounded project design work are shown at the bottom and top respectively, along with arrows showing how those activities relate to the different parts of the thesis and how some of the chapters relate to each other. The five thesis sections described at the start of Section I above are indicated in distinct columns.

Section I continues from this Introduction chapter with a literature review and a methodology chapter, which also introduces the two Research Questions RQ1 and RQ2. Section II describes the research contexts chosen and details the two Case Studies which constitute the participatory research track of the thesis. In Section III, findings and insights from both Case Studies are synthesised to explain, in answer to RQ1 and RQ2, what people want from data and from data holders. The pursuit of such better relationships is then formalised into a new research agenda, _Human Data Relations (HDR)_, with four specific strategic approaches to change. Section IV describes the grounded industrial/project design work undertaken to operationalise this research agenda, mapping some of the key obstacles to HDR progress before laying out detailed designs and approaches. The thesis concludes in Section V, where findings and insights are distilled into thirteen principles for generative action, before a reflection upon the research in terms of its limitations and pragmatic challenges, and on the PhD in terms of its legacy and the author's personal experience. Further detail on the content of each section is provided below.

![Figure 1.2: The Structure of This Thesis](./src/figs/fig1.2-thesis-structure.png){#figure-1.2}

**Remainder of Section I: Introduction, Background and Approach**

[Chapter 2](#chapter-2) contains a literature review. The first part [[2.1](#2.1)] examines the difference between data and information, outlines the central role data has taken in our society, why people need effective access to their data and how laws have been introduced to try and deliver this. The second [[2.2](#2.2)] serves as history of personal data interaction, from _Personal Information Management_ to the emergence of complex digital lives involving relationships with many data-holding providers. Finally, [2.3](#2.3) charts a path from _HCI_ and _HDI_ foundations through to the embracing of sociotechnical thinking around data and the current bleeding edge [@dictBleedingEdge] of human-centred innovation, leading to the primary Research Question (RQ) of this thesis:

> _**"What relationship do people want with their personal data?"**_ [[2.4](#RQ)]

[Chapter 3](#chapter-3) describes the methodology used in this research, explaining first the constructivist ontology and pragmatist, individualist epistemology behind the approach [[3.1](#3.1)]. Then, the choice of the dual-track participatory co-design research and embedded design and innovation work in line with a _Digital Civics_ agenda is explained [[3.2](#3.2)]. The RQ is split into two—RQ1 and RQ2 [[3.3](#3.3)]. Finally, the specific methods and techniques adopted in the research are explained and illustrated, including workshop activities, sensitisation, stimuli and recruitment [[3.4](#3.4)].

**Section II: Understanding Attitudes and Desires through Participatory Case Studies**

After an [introduction](#section-ii-research-contexts) which explains the research contexts for the participatory work and the choices of Case Studies, Section II begins with [Chapter 4](#chapter-4) which reports on Case Study One. [4.1](#4.1) is a detailed introduction to the UK's Early Help social care context, including its history of data-centrism which inherently contradicts the empowerment goals of Early Help. This makes it an ideal setting to explore the RQs. After explaining activities and methodology in [4.2](#4.2), [4.3](#4.3) introduces prior findings on family and staff perspectives, motivating the _Shared Data Interaction_ vision and workshop design. The key findings are presented [[4.4](#4.4)] then discussed [[4.5](#4.5)] in terms of involving people with their data, effective data access, and shifting the Locus of Decision Making.

[Chapter 5](#chapter-5) reports on Case Study Two. [5.1](#5.1) contextualises data access in light of the GDPR. [5.2](#5.2) summarises the activities and methods adopted, before [5.3](#5.3) explains the human-centric approach to this study. Findings are presented in [[5.4](#5.4)], which shares quantitative outcomes based on analysis of participants' GDPR requests, interview responses and participant-assigned scores. Key themes from qualitative analysis of interviews and observations follow in [[5.5](#5.5)]. The discussion [[5.6](#5.6)] then derives GDPR-improving design guidelines for policymakers, data holders and individuals, in line with a human-centric philosophy.

**Section III: Defining A New Research Agenda: Human Data Relations**

Following its [introduction](#section-iii-introduction), Section III begins with a discussion chapter, [Chapter 6](#chapter-6). This synthesises the two Case Studies, and answers RQ1 [in [6.1](#6.1)] and RQ2 [in [6.2](#6.2)] with clear statements about what people want from data—visibility, understanding and useability<sup>[11](#fn11)</sup>—and from data holders—transparency, oversight and involvement. [6.3](#6.3) concludes the chapter in line with this thesis's purpose to address the power imbalance over personal data; it positions these six 'wants' as desirable _empowerment_ relative to that perspective, motivating their practical pursuit.

[Chapter 7](#chapter-7) builds upon that motivation, shifting the narrative of the remainder of thesis towards a practical focus on how human-centric empowerment might be achieved. The thesis' findings are synthesised, drawing on experience from external work and relevant information theory, to formally define a new research agenda called _Human Data Relations (HDR)_, whose practitioners act as a _recursive public_ [[7.8](#7.8)], pursuing four objectives [[7.7](#7.7)] for increased awareness, understanding and negotiability.

**Section IV: Operationalising the Research Agenda through Design & Practice**

Section IV begins with an [introduction](#section-iv-embedded-project-settings) to the placements and projects undertaken by the author, through which the parallel track of design and innovation work to operationalise the HDR research agenda was progressed; these contexts provided the grounded learning for the insights presented in this section. Then, [Chapter 8](#chapter-8) maps out the landscape for the HDR research space, focusing on identifying obstacles to the pursuit of the HDR objectives.

[Chapter 9](#chapter-9), using a _Theories of Change (ToC)_ framing, introduces opportunities for progress, arranged as four different trajectories of change that could be executed to pursue better HDR. These approaches are illustrated with designs and illustrations from the practical work in order to explain possible strategies.

**Section V: Conclusions and Outlook**

Section V concludes the thesis through [Chapter 10](#chapter-10). First, in [10.1](#10.1), a collection of thirteen design principles for generative action are asserted and illustrated. These principles emerged through the HDR operationalisation work documented in Section IV. [10.2](#10.2) provides a pragmatic discussion of the practicalities of pursuing HDR, identifying some additional pitfalls, assumptions and implications. [10.3](#10.3) takes a critical eye to look back at this body of research, identifying limitations as well as opportunities for future work. To conclude the narrative of this thesis, [10.OLD1](#10.OLD1) first reflects on this researcher's journey, before [10.OLD2](#10.OLD2) summarises the legacy and contributions of this body of work, positioning HDR and this thesis as call to arms for activist research and design innovation to tackle the power imbalance around personal data in society.

---
