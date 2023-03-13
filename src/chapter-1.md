<h1 class="title">Section I: Background & Approach</h1><a name='section-i'/>

<h2>Introduction to Section I</h2><a name='#section-i-intro'/>

<span class="goodnote">good</span>

This thesis is divided into five sections:

* Section I: Background and Approach
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

<span class="goodnote">good</span>

We live in an increasingly data-centric world, where our direct and indirect interactions with computer systems depend upon the collection, storage and use of personal data about individuals. Motivated to reduce costly human interaction and scale to serve more customers, organisations capture and represent individuals as data and rely increasingly on the interpretation of those datapoints to make decisions—decisions that affect our everyday lives in myriad ways, from determining eligibility to access particular services, benefits or products or targeting advertisements or recommendations to influencing our decisions and behaviour. Data about people has become extremely valuable. It is 'the new oil' [@toonders2014] driving a model of _surveillance capitalism_ [@zuboff2019] that collects data and exploits it for profit.

This multi-party use of data has resulted in a splintering [@lemley2021] of our _digital selves_ across hundreds of different organisations' computer systems, creating 'a chaos of multiplicity' [@bødker2015] where data becomes trapped [@abiteboul2015] and hard to manage. Current data practices cause harm to individuals through anxiety, distraction and a sense of being overwhelmed [@fu2020; @timely2020]. Data use can harm society too, due to the ease with which people's attention and beliefs are manipulated, risking radicalisation and a loss of democratic freedom [@thompson2011; @chan2019]. It is generally accepted that:

> _"There is **a power imbalance** in the amount of information about individuals held by industry and governments, and the lack of knowledge and ability of the same individuals to control the use of that information."_—World Economic Forum [@wef2014context]

To address this power imbalance, people need a more effective relationship with their own data. This has been conceptualised as a lack of _agency_ (the ability to act for oneself), _negotiability_ (the ability to exert influence over data use within the system as things change), and _legibility_ (the ability to understand one's data and its implications) [@mortier2014]. A need is growing for the concious design of human relationships with data, as these problems cannot be solved through interface design alone but only through the reconfiguration of service relationships that involve data. Currently, users of today's digital services typically experience a _point of severance_ [@luger2013]: they are forced to sacrifice their data and are subsequently cut out of the loop. Without understanding how they are currently seen through data, people face risks of unfair treatment, or physical or psychological harm [@bowyer2018family; @crossley2022]. Left unexplored and unchallenged, the situation will not improve, as the datafication of society grows, and user agency continues to diminish.

This thesis focuses on that power imbalance and seeks to design improvements to information interaction interfaces, processes and service relationships that can improve individual agency, legibility and negotiability. This PhD tackles this design challenge through a hybrid approach that uncovers individual needs through participatory co-design workshops and qualitative interviews, alongside  grounded innovation and development work carried out by the author while embedded in industrial and academic project settings, focusing on operationalising and refining the emerging design objectives through user-centred system design, conceptual modelling, and prototyping.

<span class="editnote">ADD DIAGRAM REFERENCE</span>

The two parallel aspects of this research are described separately in sections II and IV, but took place in an concurrent and interleaved fashion, resulting in a perpetual action research feedback cycle where insights from participants and resultant theoretical models continued to inform practical system and process designs in the external projects, while real-world learnings about societal challenges and practical obstacles could be fed back into the participatory research in order to refine the emerging models.

[Section II](#section-ii) presents two Case Studies working with individuals and groups to explore their actual and desired relationships with data. These Studies make a novel contribution to knowledge, producing a deep understanding of how people relate to data, what capabilities people want, and how they would like service providers to handle their data.

In [Section III](#section-iii), the separate understandings from the Case Studies are discussed and unified into a combined theory that captures six core human desires, a set of design goals for data relations that can drive future research to empower individuals through their personal data. These individual goals are formalised into a new research agenda, **Human Data Relations (HDR)**. Building upon Human Data Interaction (HDI) [@mortier2013; @mortier2014] theory with a focus on operationalising the learnings from the Case Studies and HDI, HDR formalises the design goals into four specific objectives for delivering improved HDI and data relations in practice. HDR defines a clear agenda for change.

[Section IV](#section-iv) explores and document that operationalisation in more detail, presenting the author's learnings about the wider societal realities of pursuing the HDR agenda, from his parallel work in project settings. Here the research adopts a sociotechnical perspective that focuses on transforming people's relationships with data in a realistic way that acknowledges and understands the commercial realities and difficult lived experience of today's data-centric world. From this perspective, the HDR space in mapped out in terms of known obstacles to overcome and approaches to the pursuit of HDR (including _adversarial design_ [@disalvo2012]).

in [Section V](#section-v), specific designs and practices that could be helpful if progress is to be made is presented, and pragmatic challenges of pursuing the HDR agenda are discussed in more detail. Limitations of the work are acknowledged and future opportunities identified, before the thesis is concluded with reflections on the author's research journey and upon the concrete contributions and legacy this thesis offer. The insights and contributions of the thesis can equip future researchers and innovators with the tools and understandings they will need to pursue the empowerment of individuals and the rebalancing of power over data at a societal level.

### Personal Motivation and Context{#1.1.1}

<span class="goodnote">good</span>

This PhD and this thesis represent the culmination of my lifelong passion to help people get more value from our computers. My experience and expectations of computers was shaped by the 1980s home computing revolution, which taught me and a generation of young people that the computer was a machine to program, a tool to be exploited, mastered and bent to your will. Then, in my formative years approaching the turn of the millennium, I lived through the birth of the public Internet and marvelled at the ability for computers to connect people across the world, empower individuals as creators, innovators and broadcasters, level the playing field and transform the way people interact. In my software engineering career, I gradually transitioned from back-end to front-end development and ultimately to User Experience (UX), driven to take a more active role in building software features that directly benefit users and improve their lives. Keenly tracking and embracing the Web 2.0 revolution while observing the digitisation and disruption of so many industries, I became fascinated with the ways in which humans were shaping computer systems which in turn were shaping our habits and our society, phenomena I explored through the Human 2.0 blog which I co-founded [@bowyer2009human].

But then, having seen Internet-era computing give us new capabilities, and knowing the potential of computers to become tools for positive change in society, I bore witness to a changing world, and the balkanisation and commercialisation of the once-free Internet. As companies adapted to the Information Age and shifted to data-driven, cloud-centric business models, our ability to harness computers for our own ends began to slip away. While immersed in the start-up community in Montréal, Canada, I became frustrated at this loss of potential. Driven to explore the reasons and implications of this loss of agency and the possibilities for more human-centric computing, I published several essays and presentations [@bowyer2009bitnorth; @bowyer2010bitnorth; @bowyer2011filesdie; @bowyer2012bitnorth; @bowyer2012timespace; @bowyer2013bitnorth] which collectively form the seed from which this thesis grew.

By 2014, it was beyond doubt to me that the software industry had lost its way, prioritising business goals over user agency, reducing features and creating technology designed to limit and corral users to behave in certain ways. Web 2.0's revolutionary potential of a 'people's internet' had been squashed and withered away in the shadow of new data giants Google, Facebook, Apple and Amazon, who reshaped and usurped Internet, Web and smartphone technologies for profit, at great cost to human wellbeing. Against a backdrop of a social media revolution which was literally breaking society and democracy to drive profit [@tufekci2017; @hall2018], I took the leap to escape corporate IT. I sought to research, design and build a better digital future where computers could be made useful again. This led me to the _Digital Civics_ CDT programme [@digitalCivicsCDT2018], where I was finally able to work full-time on what I consider the most important problem of our age—**Understanding and Improving Human Data Relations**.

### Research Objectives and Purpose{#1.1.2}

<span class="goodnote">good</span>

The aim of this thesis is to research how people relate to data, how they understand and use it, and what they want from it and its holders in order to thrive and to meet their own goals.

The thesis is informed by a constructivist ontology and a pragmatist, individualist epistemology [[3.1](#3.1)], and employs a multi-disciplinary _Digital Civics_ [@vlachokyriakos2016] approach, conducting an academic inquiry to answer two key research questions (RQ):

> **RQ1.** What is the human experience of personal data, and what do people want from their data? [[3.3.1](#RQ1)]

> **RQ2.** What role does data play in people's service relationships, and how could relationships involving data be improved? [[3.3.2](#RQ2)]

This thesis assumes that if the asymmetry over data access and use between individuals and organisations holding data is to be addressed, that a greater understanding of current data use issues is needed by all parties, and that the production of knowledge and insights is therefore a vital first step towards the design of a more balanced model of data use that can deliver increased agency and negotiability.

After this Introduction chapter, Section I continues with a review of relevant existing literature and research [[Chapter 2](#chapter-2)] to identify a clear baseline and research gap, then an explanation of the research approach and methodological choices to be used [[Chapter 3](#chapter-3)].

Section II reports on the two Case Studies, which invited participants to 'look behind the curtain' of the opaque data-centric organisations they interact with. These enabled participants to consider more deeply the collection, storage and use of their personal data by service organisations. A participatory research design was employed, collecting interview transcripts to enable qualitative analysis and identify themes that inform a descriptive model of human-centred data empowerment needs. The focus was upon examining current practices, identifying attitudes to those practices, and imagining alternative designs and approaches for data use by service providers and the participants themselves. The participant groups were:

  - **Case Study One**: Supported families, who meet with _Early Help_ support workers (whose role to understand and empower those individuals to improve their lives is currently supplemented through access to myriad civic data records including housing, benefits and educational data) [[Chapter 4](#chapter-4)]; and
  - **Case Study Two**: Ordinary British and European citizens, who gained new legal rights via 2018's _GDPR_ legislation [[2.1.3](#2.1.3)], enabling them to request copies of held personal data along with other relevant information from the companies and service providers in their lives [[Chapter 5](#chapter-5)].

Through comparative analysis of the two case studies, commonalities in individual attitudes and understandings serve to validate each other, and allow the expression of clear insights about people's relationships to personal data that can serve as answers to the two RQs. This synthesis and analysis of interview data enabled the generation of a descriptive model to address the research gap, concluding the core academic research of this PhD [[Chapter 6](#chapter-6)].

This research is situated in the HCI discipline, which means that design (both participatory co-design and expert-informed user-centred design [[3.5](#3.5)]) forms a key part of the approach to exploring the problem space. Examination of individual attitudes and desires around data in a 'whole life' sense is an under-researched area. Where HCI traditionally focuses on the mechanisms by which humans interact with data, the Case Studies, like the thesis as a whole, adopt a more sociotechnical focus on understanding lived experience.

In order to produce workable designs and theories that could be applied in the real world, the remainder of the thesis takes an even broader perspective, recognising that for participants' desired changes in data relations to be realised requires an examination and a recognition of current technical, legal and commercial realities and the multi-party complexities of modern digital life. The design work presented in Section IV complements the participatory Studies, providing an additional source of learning: real-world explorations of how to design more effective data relationships. This is done through design, modelling and conjecture, drawing upon the author's direct experiences working (alongside the PhD) in related industrial projects that share this thesis's focus on empowering individuals through data.

To support future researchers, activists and innovators in achieving the vision of a more human-centric future, the pursuit of wants identified are shaped into a defined new research agenda - **Human Data Relations (HDR)**, which represents a broadening of focus from merely understanding the world towards planning how to change it. Motivations and objectives are identified, and HDR is positioned as a broad activist agenda whose practitioners seek to reconfigure society to their own advantage [[Chapter 7](#chapter-7)].

Section IV and V are deliberately open-ended, mapping out the existing landscape of challenges and possibilities for the HDR agenda, moving away from a traditional thesis structure in order to offer more actionable insights. Given the scale of the sociotechnical design challenge society faces, this thesis does not carry out 'in the wild' evaluation of particular data interaction approaches or interface designs. Instead, drawing upon direct experience as well as the work of other researchers and innovators in this space, it documents known obstacles [[Chapter 8](#chapter-8)]. It also maps out four possible change trajectories [[Chapter 9](#chapter-9)] which can inform future design and innovation in human-centric system design. These chapters are underpinned by a series of design insights, developed by the author based upon the learnings from both the participatory and project-based research tracks. These insights are documented in [[Chapter 10](#chapter-10)], along with reflections, limitations and a summary of contributions and ideas for future work.
These strategies and insights, which should be viewed as speculative rather than definitive, can also help facilitate the desig and implementation of initiatives that recognise and confront the unique challenges of the status quo in pursuit of improving people's agency and negotiability over and through personal data.

Taken together, the two parallel research tracks of this thesis can serve as novel and actionable reference material for future research, activism and innovation, solidly grounded in literary theory, participant experience, and industrial reality.

Contributions of the Research{#1.2}
-----------------------------

<span class="editnote">Shrink Contributions / Make More Abstract & save detail for C10. can break down as</span>

The contributions of this thesis are summarised in this section, and described in more detail in [Chapter 10](Chapter 10).

### An Understanding of what People want from Personal Data{#1.2.1}

Through the qualitative Case Studies in Chapters [4](#chapter-4) and [5](#chapter-5) and the discursive analysis in [Chapter 6](#chapter-6), this thesis establishes a clear picture of what people want from their personal data. In general, people need all of their personal data to be _visible_ [[6.1.1](#6.1.1)], _understandable_ [[6.1.2](#6.1.2)], and _useable_<sup>[10](#fn10)</sup> [[6.1.3](#6.1.3)].

Furthermore, the sociotechnical focus of the research has produced deep qualitative insights into the _relationships_ people have with data holding organisations and services, revealing attitudes and emotions including distrust, fear, frustration, confusion, helplessness and curiosity. Specific insights are drawn for the two Case Study contexts:

- In social care [[Chapter 4](#chapter-4)], families want to be given a voice, an ability to see and influence how they are understood through data, and to be able to explain and discuss their data with authorities. The Case Study (and its pilot study [[Appendix A](#appendix-a)] validate prior findings that highlight families' difficulties with civic data, while documenting in detail the ways that they imagine improving the use of their civic data within an empowerment and support context.
- In the service provider relationships of everyday life [[Chapter 5](#chapter-5)], individuals want to be able to understand what companies are collecting about them. They want to see that data, understand what inferences and decisions result from its use, and exert control over how it can be used, kept and shared. These desires (which also explain motives for using GDPR rights) provide novel insights into the lived experience of the data-centric world and in particular of using the GDPR to seek access and control over one's personal data.

Taken together [[Chapter 6](#chapter-6)], the Case Studies reveal clear common themes for people in service relationships that involve personal data; people want _process transparency_ [[6.2.1](#6.2.1)] when it comes to processes that use their personal data, _individual oversight_ [[6.2.2](#6.2.2)] over how their data is used, and ultimately _involvement in processes and decision making_ [[6.2.3](#6.2.3)].

The Case Studies also establish a more granular view of what we mean by personal data: The pilot study for Case Study One establishes the term _family civic data_ [[ARI4.1](#ari-fcd-types)], which can encompass relationship information, educational records, welfare details, health data, housing data, and civic and legal records. Case Study Two establishes a model of personal data according to its origin; data can be _volunteered_, _observed_, _derived_, _acquired_ or _metadata_ [[Table 5.2](#table-5.2)]. This model has been adopted by others: during design and ideation sessions at BBC R&D, and within Sitra/Hestia.ai's _digipower_ investigation [[ARI7.2OLD](#ARI7.2OLD)] (for explaining data holding to participants and as a frame for data analysis) [@bowyer2022hestia; @pidoux2022].

Through the design and innovation work in [Section 3](#section-3) and beyond, a deeper understanding of the relationship people have with personal data is developed, and of what role data plays in people's lives. Drawing on information theory background laid out in [2.1.1](#2.1.1), [[Chapter 7](#chapter-7)] differentiates the needs participants expressed from data (the stored artefact) and from information (the set of facts and opinions encoded within that data), offering as a model the distinct concepts of _life information_ (from which people gain insights and extract value) and _ecosystem information_ (from which people improve awareness and control over the use of their data). Combining these differing motives with the Case Study themes from Chapter 6 yields four clear objectives people have in data relations: _data awareness and understanding_, _data useability_<sup>[10](#fn10)</sup>, _data ecosystem awareness and understanding_, and _data ecosystem negotiability_. These practical pursuit of these objectives form the basis of the _Human Data Relations_ research agenda detailed below in [1.2.5](#1.2.5) and pursued through the design and practice activities of [Section IV](#section-iv).

### Methodologies for Participatory Work around Personal Data{#1.2.2}

cards & design games
A proto-methodology for educating individuals about held data, data access and the data ecosystem
A reframing of data literacy for the HDR space

### Best Practices and Design Guidelines for Systems and Processes involving Personal Data{#1.2.3}

models and best practice guidelines for data holding orgs in public and private sector.
including
_Shared Data Interaction_: A proposed model for more efficient and empowering social support relationships that embraces human-centricity (not proven in practice but arising from and seen as beneficial by both parties)
alternative data access models (GDPR as flow etc)
business Opportunities - enhanced trust (Evidence for the impact of knowledge about data handling practices on provider trust and perceived individual power) but also
Guidance for policymakers, data holders and individuals on how to improve HDR

all of this informs design but specifically:

### Principles for Generative Action towards Improving Human Data Relations{#1.2.4}

sociotechnical Strategies for
moving beyond interface design or user experience design, moving into

- [Insight 1](#insight-1) - Life Information Makes Data Relatable.
- [Insight 2](#insight-2) - Data Needs to be United and Unified.
- [Insight 3](#insight-3) - Data Must be Transformed into a Versatile Material.
- [Insight 4](#insight-4) - Ecosystem Information is an Antidote to Digital Life Complexity.
- [Insight 5](#insight-5) - We Must Know Data's Provenance.
- [Insight 6](#insight-6) - Data Holders use Four Levers of Infrastructural Power.
- [Insight 7](#insight-7) - Human-centred Information Systems Must Serve Human Values, Relieve Pain and Deliver New Life Capabilities.
- [Insight 8](#insight-8) - We Need to Teach Computers to Understand Human Information.
 [Insight 9](#insight-9) - Individual GDPR Requests can Compel Companies to Change Data Practices.
- [Insight 10](#insight-10) - Collectives can Compare and Unify their Data and Use it to Demand Change.
- [Insight 11](#insight-11) - Automating the Identification of Entities can enhance Machine Understanding and Unburden Life Interface Users.
- [Insight 12](#insight-12) - The 'Seams' of Digital Services need to be identified, exploited and protected.
- [Insight 13](#insight-13) - It is Possible (and Necessary) to Demonstrate Business Benefits of Transparency and Human-centricity.

### A Detailed and Actionable Research Agenda and Strategies for Empowerment and Systemic Change{#1.2.5}

(detailed and actionable research agenda and strategies for empowerment and systemic change)
The Synthesis and Formulation of the research agenda of Human Data Relations (HDR)
HDR research agenda, extending HDI theory to invite and facilitate confrontation of the practical challenges of ld data and provider power
A map of the HDR landscape, identifying obstacles and insights
Four identified trajectories for advancing Human Data Relations


Publications Arising From and Connected to This Research{#1.3}
--------------------------------------------------------

<span class="editnote">Update presentations post-PhD</span>

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

<a name="1.3.2.3">**Workshop Papers & Presentations**</a>

During the PhD, I gave a number of additional presentations and published three workshop papers. These outputs included material from, or directly contributed to, this thesis and its arguments.

  - _[Designing for Human Autonomy: The next challenge that civic HCI must address](https://eprints.ncl.ac.uk/273832)_ [@bowyer2017] - a short talk I presented to my peers at Open Lab in January 2017 laying out the landscape of reduced agency and possible avenues for improving humans' relationships to their data that my PhD would explore;
  - _[Free Data Interfaces: Taking Human-Data Interaction to the Next Level](https://eprints.ncl.ac.uk/273825)_ [@bowyer2018freedata] - a CHI 2018 workshop paper formalising my pre-PhD design thinking and outlining a vision for unconstrained and useful data interaction interfaces;
  - _[A Grand Vision for Post-Capitalist HCI: Digital Life Assistants](https://eprints.ncl.ac.uk/273826)_ [@bowyer2018grandvision] - a CHI 2018 workshop paper where I imagined a form of digital computer assistant that is far more helpful and human-data-centric than the digital voice assistants of today;
  - _[Personal Data Use: A Human-centric Perspective](https://eprints.ncl.ac.uk/273834)_ [@bowyer2020lecture] - a lecture about my research that I was invited to give to undergraduate students at both Northumbria University and Newcastle University in early 2020, just prior to the pandemic;
  - _[My Thesis in 3 Minutes: Understanding and Designing Human Data Relations](https://www.youtube.com/watch?v=YFHXc_TfM5c)_ [@bowyer20213MT] - my entry into Newcastle University's 3-minute thesis competition in April 2021, for which I was co-winner of the people's choice prize;
  - _[Human-Data Interaction has two purposes: Personal Data Control and Life Information Exploration](https://eprints.ncl.ac.uk/274297)_ [@bowyer2021twopurposes] - a workshop paper I presented at CHI 2021, introducing my model of the two motivating factors for interacting with personal data.

<a name="1.3.2.4">**Publications from Peripheral Work**</a>

During the same timeframe as this PhD, I have also contributed to a number of publications through peripheral work [[7.2](#7.2)]:

- As a researcher and developer on the SILVER project [[3.4.1](#3.4.1.1)], my work contributed towards an internal report to CHC as well as the [overall impact report](https://web.archive.org/web/20211225192408/https://www.chc-impact-report.co.uk/) [@ConnectedHealthCities2021impact,129-130].
- Also for SILVER, I published [demonstration videos](https://eprints.ncl.ac.uk/273839) [@bowyer2019silvervideo] of a health data interface prototype developed by myself and Stuart Wheater.
- I was co-author on research published [at BCS 2021](https://doi.org/10.14236/ewic/HCI2021.16) [@goffe2021] and [in Interacting with Computers](https://doi.org/10.1093/iwc/iwac015) [@goffe2022].
- As a research intern at BBC R&D [[ARI7.1OLD](#ari-bbc-OLD)], I published an internal research report [@bowyer2020bbcreport] into personal data store design, and wrote and presented a 'stimulus presentation' to launch an internal hack week.
- At Hestia.ai, I was a lead author on [a research report auditing the data economy](https://doi.org/10.5281/zenodo.6554177) [@bowyer2022hestia], and co-author on [a research report on power mechanisms in the data economy](https://doi.org/10.5281/zenodo.6554155) [@pidoux2022].

The Structure of this Thesis{#1.4}
----------------------------

<span class="editnote">Update Text to remove part A/B split</span>

<span class="editnote">Update Structure Diagram Figure 1.2</span>

The overall structure of this thesis is illustrated in [Figure 1.2](#figure-1.2). Clearly evident are its two distinct parts, as described in 1.1.2 above.

Part One, the participatory investigation, begins with a literature review [[Chapter 2](#chapter-2)] and a methodology chapter [[Chapter 3](#chapter-3)]. RQ1 and RQ2 are examined in both Case Studies, separately documented in [Chapter 4](#chapter-4) and [Chapter 5](#chapter-5). In [Chapter 6](#chapter-6) the findings and insights from the Case Studies are synthesised to explain, in answer to RQ1 and RQ2, what people want from data and from data holders, concluding the academic investigation.

Part Two is adversarial design work and strategic planning, expanding the original research question to examine how the desires uncovered might be achieved in practice. The practical pursuit of better data relations is formalised as a new field with clear objectives, _Human Data Relations_, in [Chapter 7](#chapter-7). This _HDR_ space is then mapped out, drawing on industrial experience, starting with the detailing of known obstacles in [Chapter 8](#chapter-8). Four specific strategic approaches to change, including detailed designs, are laid out in [Chapter 9](#chapter-9) as recommendations for future work, before the thesis is concluded in [Chapter 10](#chapter-10), bringing the two parts together.

![Figure 1.2: The Structure of This Thesis](./src/figs/fig1.2-thesis-structure.jpg){#figure-1.2}

[Chapter 2](#chapter-2) contains a literature review. The first part [[2.1](#2.1)] examines the difference between data and information, outlines the central role data has taken in our society, why people need effective access to their data and how laws have been introduced to try and deliver this. The second [[2.2](#2.2)] serves as history of personal data interaction, from _Personal Information Management_ to the emergence of complex digital lives involving relationships with many data-holding providers. Finally, [2.3](#2.3) charts a path from _HCI_ and _HDI_ foundations through to the embracing of sociotechnical thinking around data and the current bleeding edge [@dictBleedingEdge] of human-centred innovation, leading to the primary academic Research Question (RQ) of this thesis:

> _**"What relationship do people want with their personal data?"**_ [[2.4](#RQ)]

<span class="editnote">remove ref to PAR</span>

[Chapter 3](#chapter-3) describes the methodology used in this research, explaining first the constructivist ontology and pragmatist, individualist epistemology behind the approach [[3.1](#3.1)]. Then, the choice of participatory action research and co-design from a _Digital Civics_ standpoint is explained [[3.2](#3.2)]. The RQ above is split into two—RQ1 and RQ2 [[3.3](#3.3)]—and the contexts for the Case Studies are introduced from a 'what did I do?' perspective [[3.4](#3.4)]. Finally, the specific methods and techniques adopted in the research are explained and illustrated, including workshop activities, sentisation, stimuli and recruitment [[3.5](#3.5)].

[Chapter 4](#chapter-4) reports on Case Study One. This begins [[4.1](#4.1)] with a detailed introduction to the UK's Early Help social care context, including its history of data-centrism which inherently contradicts the empowerment goals of Early Help. This makes it an ideal setting to explore the RQs. In [4.2](#4.2), prior findings on family and staff perspectives are introduced, motivating the _Shared Data Interaction_ vision and workshop design. The key findings are presented [[4.3](#4.3)] then discussed [[4.4](#4.4)] in terms of involving people with their data, effective data access, and shifting the Locus of Decision Making.

[Chapter 5](#chapter-5) reports on Case Study Two. [5.1](#5.1) contextualises data access in light of the GDPR and explains the human-centric approach to this study [[5.2](#5.2)]. Findings are presented in [[5.3](#5.3)] reporting on quantitative outcomes based on analysis of participants' GDPR requests, interview responses and participant-assigned scores. These are followed by presentation of key themes from qualitative analysis of interviews and observations [[5.4](#5.4)]. The discussion [[5.5](#5.5)] builds upon these findings to form GDPR-improving guidelines for policymakers, data holders and individuals, in line with a human-centric philosophy.

[Chapter 6](#chapter-6) synthesises the two Case Studies, and answers RQ1 [in [6.1](#6.1)] and RQ2 [in [6.2](#6.2)], bringing the central academic research of the thesis to a close with clear statements about what people want from data—visibility, understanding and useability—and from data holders—transparency, oversight and involvement. [6.3](#6.3) concludes the chapter and Part One, by outlining this thesis's purpose to address the power imbalance over personal data, positions these six 'wants' as desirable _empowerment_ relative to that perspective, motivating their practical pursuit.

[Chapter 7](#chapter-7) begins Part Two, shifting to a practical focus to explore how human-centric empowerment might be achieved. The thesis' findings are synthesised, drawing on experience from external work, to formally define a field of future research called _Human Data Relations (HDR)_, whose practitioners act as a _recursive public_ [[7.8](#7.8)], pursuing four objectives [[7.7](#7.7)] for increased awareness, understanding and negotiability.

The landscape of HDR is mapped out in two parts. [Chapter 8](#chapter-8) focuses on identifying obstacles to pursuit of the HDR objectives. Interspersed through the chapter as inset boxes are [8 insights](#inset-boxes-c8) that can inform adversarial design approaches.

[Chapter 9](#chapter-9), using a _Theories of Change (ToC)_ framing, introduces opportunities for progress, arranged as four different trajectories of change that could be executed to pursue better HDR. These approaches are illustrated with designs and illustrations to explain possible strategies, and interspersed with a further [5 insights](#inset-boxes-c9) that could seed future actions to tackle the aforementioned obstacles and pursue the change trajectories, improving the HDR landscape.

[Chapter 10](#chapter-10) concludes the thesis, reflecting first on this researcher's journey [[10.OLD1](#10.OLD1)], before summarising the legacy and contributions of this body of work [[10.OLD2](#10.OLD2)], positioning HDR and this thesis as call to arms for activist research and innovation to tackle the power imbalance around personal data in society.

---
