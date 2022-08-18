Introduction{#chapter-1}
=======================

> _"My data is everywhere, and I am nowhere."_ — Imogen Heap (musician and digital rights advocate), speaking at MyData 2019.

Background and Motivation for this Research{#1.1}
-------------------------------------------

We live in an increasingly **data-centric** world, where direct and indirect interactions with computer systems depend upon the collection, storage and use of personal data about individuals. Motivated to reduce costly human interaction and scale to serve more customers, organisations **capture and represent individuals as data** and rely increasingly on the **interpretation of those datapoints to make decisions** - decisions that affect our everyday life in myriad ways, from determining eligibility to access particular services, benefits or products or targeting advertisements or recommendations to influence how people behave. Thus, data about people has become extremely valuable; _'the new oil'_ [@toonders2014] at the core of a model of **surveillance capitalism** [@zuboff2019] that extracts and exploits data for profit.

This multi-party use of data has resulted in a splintering [@lemley2021] of our 'digital selves' across hundreds of different organisations' computer systems, creating _"a chaos of multiplicity"_ [@bødker2015] where data becomes **trapped** [@abiteboul2015] and hard to manage. Current data practices **cause harm to individuals** through anxiety, distraction and a sense of being overwhelmed [@fu2020; @timely2020]. Many people believe **data use harms society too**, due to the ease with which people's attention and beliefs are manipulated, risking radicalisation and a loss of democratic freedom [@thompson2011; @chan2019]. It is generally accepted that there is **a power imbalance** _"in the amount of information about individuals held by industry and governments, and the lack of knowledge and ability of the same individuals to control the use of that information"_ [@wef2014context].

To address this power imbalance, people need to achieve **a more effective relationship with their own data**. This has been conceptualised as a lack of _agency_ (the ability to act for oneself), _negotiability_ (the ability to exert influence over data use within the system as things change), and _legibility_ (the ability to understand one's data and its implications) [@mortier2014]. Currently, users of today's digital services typically experience a _'point of severance'_ [@luger2013]: they are forced to sacrifice their data and are then cut out of the loop. Without understanding of how they are currently seen through data, people **face risks of unfair treatment, or physical or psychological harm** [@bowyer2018family]. Left unexplored and unchallenged, the situation will not improve, as the datafication of society grows, and user agency continues to diminish.

This thesis focuses on the apparent power imbalance and explores ways in which individual agency, legibility and negotiability can be improved. First, through academic inquiry, it makes a novel contribution to knowledge, examining deeply how people relate to data, what capabilities people need, and how they would like service providers to handle their data. The thesis takes a broader perspective than current work in the field of Human-Computer Interaction (HCI), which tends to focus upon the mechanisms by which humans interact with data without considering the problem of asymmetric power over data from a sociotechnical perspective, which is necessary if societal benefits are to be achieved.

### Personal Motivation and Context{#1.1.1}

This PhD and this thesis represent the culmination of my lifelong passion to help people get more value from our computers. My experience and expectations of computers was shaped by the home computing revolution of the 1980s and 1990s, which taught me and a generation of young people that the computer was a machine to program, **a tool to be exploited**, mastered and bent to your will. Then, in my formative years approaching the turn of the millennium, I lived through the birth of the public Internet and marvelled at the ability for computers to connect people across the world, **empower individuals** as creators, innovators and broadcasters, level the playing field and transform the way people interact. I gradually shifted my software engineering career from back-end to front-end development and ultimately to User Experience (UX), so that I might take a more active role in building software features that **directly benefit users and improve their lives**. Keenly tracking and embracing the Web 2.0 revolution while observing the digitisation and disruption of so many industries, I became fascinated with the ways in which **humans were shaping computer systems which in turn were shaping our habits and our society**, phenomena I explored through the Human 2.0 blog which I co-founded [@bowyer2009human].

But then, having seen **Internet-era computing give us new capabilities**, and knowing the potential of computers to become tools for positive change in society, I bore witness to a changing world, where, through the digitalisation of businesses and the shift to data-centric cloud-centric business models, we began, and continue to, **lose the ability to harness computers for our own ends**. I began to explore the reasons and implications of this loss of agency and the possibilities for more human-centric computing, through several published essays and presentations [@bowyer2009bitnorth; @bowyer2010bitnorth; @bowyer2011filesdie; @bowyer2012bitnorth; @bowyer2012timespace; @bowyer2013bitnorth] which collectively form the seed from which this thesis grew.

By 2014, it was beyond doubt to me that the software industry had lost its way, prioritising business goals over user agency, reducing features and creating technology designed to limit and corral users to behave in certain ways. Web 2.0's revolutionary potential of a 'people's internet' was squashed and **withered away in the shadow of new data giants** Google, Facebook, Apple and Amazon and their **reshaping and usurping of Internet and smartphone technologies**. Against a backdrop of a social media revolution which was literally breaking society and democracy to further the pursuit of profit [@tufekci2017; @hall2018], I took the leap to escape corporate, for-profit IT in order to seek ways to research, design and help to build a better digital future, with the objective of making computers useful again. This led me to join the Digital Civics CDT programme [@digitalCivicsCDT2018], where I was finally able to work full-time on what I consider the most important problem of our age -- **Understanding and Improving Human Data Relations**.

### Research Objectives and Purpose{#1.1.2}

The aim of this thesis is to research **how people relate to data**, how they understand and use it, and **what they need from it and its holders** in order to thrive and to meet their own goals.

The thesis is informed by a constructivist ontology and a pragmatist, individualist epistemology [[3.1](#3.1)], and employs a multi-disciplinary _Digital Civics_ [@vlachokyriakos2016] approach, conducting an academic inquiry to answer two key research questions (RQ):

  - **RQ1. What is the human experience of personal data, and what do people want from their data?** [[3.3.1](#RQ1)]
  - **RQ2. What role does data play in people's service relationships, and how could relationships involving data be improved?** [[3.3.2](#RQ2)]

This thesis assumes that if the **asymmetry over data access and use between individuals and organisations holding data is to be addressed**, that a greater understanding of current data use issues is needed by all parties, and that the **production of knowledge and insights** is therefore a vital first step towards the pursuit of a more balanced model of data use that can deliver **increased agency and negotiability**. To acquire this understanding, a participatory research design is employed, collecting interview transcripts from two contexts to enable qualitative analysis that can identify themes to inform a descriptive model of human-centred data empowerment.

The thesis reports on two studies that invited participants to _'look behind the curtain'_ of previously opaque data-centric organisations they interact with, enabling them to consider more deeply the collection, storage and use of their personal data by service organisations. In both cases the focus was upon examining current practices, identifying attitudes to those practices, and imagining alternative designs and approaches for data use by service providers and the participants themselves. The participants of the two studies are:

  - **Case Study One**: Supported families, who meet with _'Early Help'_ support workers (whose role is to access civic data to understand and empower those individuals to improve their lives) [[Chapter 4](#chapter-4)]; and
  - **Case Study Two**: Ordinary British and European citizens, who gained new legal rights via 2018's _GDPR_ legislation [[2.1.3](#2.1.3)], enabling them to request copies of held personal data along with other relevant information from the companies and service providers in their lives [[Chapter 5](#chapter-5)].

Through comparative analysis of the two case studies, commonalities in individual attitudes and understandings serve to validate each other, and allow the expression of clear insights about people's relationships to personal data that can serve as answers to the two RQs. This **synthesis and analysis of interview data** forms the core academic research of this PhD [[Chapter 6](#chapter-6)].

This research is situated in the Human-Computer Interaction (HCI) discipline, which means that **design** (both participatory co-design and expert-informed user-centred design [[3.5](#3.5)]) forms a key part of the approach to exploring the problem space. Within this space, there has been a great deal of focus on direct interaction with data and upon interface design, but more sociotechnical examination of individual attitudes to data and individual needs in a data-centric context is an under-researched area. To support the creation of improved interfaces and processes that can redress the power imbalance, this thesis focuses upon the **generation of a descriptive model to address the research gap**, producing detailed models and insights that recognise the multi-party complexity of data interaction today and thus can be directly of use to inform future design and innovation in the building of systems that recognise the unique challenges of the status quo.

In particular, in [Chapter 7](#chapter-7) this thesis moves beyond academic inquiry and provides **designerly thoughts, models and ideas** that explore how the findings from the academic inquiry could be applied in practice, expanding the scope of the thesis from merely understanding the world towards planning how to change it. Given the scale of the sociotechnical design challenge society faces, this thesis does not carry out _'in the wild'_ evaluation of particular data interaction approaches or interface designs. Instead, drawing upon **direct experience in related industrial research** as well as the work of other researchers and innovators in this space, this thesis prioritises the documentation of obstacles, important insights and opportunities for future work. The primary contribution here, as the thesis concludes, is to **map out current, emergent and future approaches for improving people's agency and negotiability**, enabling future research, design and innovation work to pursue these goals with a more targeted and well-understood approach, both philosophically and in practice.

Nature and Contributions of the Thesis{#1.2}
--------------------------------------

This section lists the 14 major contributions (**Cn**) of this thesis, which can be summarised as:

- an understanding of what people need when they relate to data [[1.2.1](#1.2.1)];
- the establishment of the field of *Human Data Relations* [[1.2.2](#1.2.2)]; and
- additional contributions specific to the Case Study contexts of
  - Early Help [[1.2.3](#1.2.3)], and
  - GDPR/everyday data access [[1.2.4](#1.2.4)].

### An Understanding of what People want from Personal Data{#1.2.1}

Through the concluding sections of Chapters [4](#chapter-4) and [5](#chapter-5), the reader will be able to see that research participants across both studies (and the pilot study) shared common issues around personal data. These commonalities provide the answers to [RQ1](#RQ1) and [RQ2](#RQ2), which form the first two contributions C1 and C2:

**C1: An understanding of What People Want in Direct Data Relations**

Section [6.1](#6.1) answers [RQ1](#RQ1) by explaining people's three specific needs for direct relations with data:

- for data to be **visible** [[6.1.1](#6.1.1)],
- **understandable** [[6.1.2](#6.1.2)], and
- **useable**<sup>[13](#fn13)</sup> [[6.1.3](#6.1.3)].

**C2: An Understanding of What People Want in Indirect Data Relations**

Section [6.2](#6.2) answers [RQ2](#RQ2) by explaining the three things people need when they have an indirect relationship to their data because it is held by someone else, such as a service provider:

- **process transparency** [[6.2.1](#6.2.1)],
- **individual oversight** [[6.2.2](#6.2.2)], and
- **involvement** in processes and decision making [[6.2.3](#6.2.3)].

### Establishing a new field: Human Data Relations{#1.2.2}

**C3: The Synthesis and Formulation of the Field of Human Data Relations (HDR)**.

At the highest level, this thesis contributes a new field of research and innovation, **Human Data Relations (HDR)**. [Chapter 2](#chapter-2) reviews existing literature and prior work to explain the problems of data-centrism and limited access to data [[2.1](#2.1)]; personal information management and interaction [[2.2](#2.2)]; and human-centric perspectives on data [[2.3](#2.3)].
From this baseline, the participatory academic inquiry into the lived realities data relationships described in Chapters [4](#chapter-4), [5](#chapter-5), and [6](#chapter-6), leads to a synthesis of what people need in data relations.
[Chapter 7](#chapter-7) maps out and contextualises both existing work and new designerly insights and models that could service those needs, and formalises the pursuit a defined field of academic and practical endeavour, Human Data Relations [[7.2](#7.2)] as the pursuit of four specific objectives:

  - **data awareness and understanding**
  - **data useability**
  - **ecosystem awareness and understanding**
  - **ecosystem negotiability**

**C4: A clear delineation of two primary motivators for individuals seeking better HDR**

[7.2.3](#7.2.3), informed by both the Case Studies and the peripheral activities [[7.1.2](#7.1.2)], clarifies the two driving motivations for pursuing better HDR:

  - **Life Information Utilisation**, and
  - **Personal Data Ecosystem Control**.

**C5: A map of the HDR landscape, identifying obstacles and insights**

The goal of this thesis is to set the stage for future research and innovation in the newly-defined space of Human Data Relations. Across sections [7.3](#7.3) and [7.4](#7.4), the landscape of HDR is mapped out from multiple perspectives.

[7.3](#7.3) maps out eight obstacles to the pursuit of the HDR objectives, as well as four obstacles that exist in the solution space across all four, including:

  - the personal data diaspora,
  - the intractable data self,
  - immobile, illegible and unmalleable data,
  - hegemony and active diminishing of user agency by data holders,
  - closed, introspective and insular practices,
  - a lack of demand and investment in HDR from individuals and organisations, and
  - insufficient machine understanding of human data

To begin to address these obstacles, [thirteen insights](#hdr-insights) are explained that could seed future research and innovation towards tackling these obstacles:

  [1](#insight-1). Life information makes data relatable.
  [2](#insight-2). Data needs to be united and unified.
  [3](#insight-3). Data must be transformed into a versatile material.
  [4](#insight-4). Ecosystem information is an antidote to digital life complexity.
  [5](#insight-5). We must know data's provenance.
  [6](#insight-6). Data holders exploit four levers of power to manipulate the digital landscape.
  [7](#insight-7). We need new human-centred information systems that serve human values, relieve pain and deliver new life capabilities.
  [8](#insight-8). We need to teach computers to understand human information.
  [9](#insight-9). Individual GDPR requests can compel companies to change data practices.
  [10](#insight-10). Collectives can compare and unify their data and use it to demand change.
  [11](#insight-11). Automating the identification of entities can enhance machine understanding and unburden life interface users.
  [12](#insight-12). The 'seams' of Digital Services need to be identified, exploited and protected.
  [13](#insight-13). It is possible (and necessary) to demonstrate business benefits of transparency and human-centricity.

**C6: Four identified trajectories for advancing Human Data Relations**

Section [7.4](#7.4) explains, with detailed real-world examples and original design work from the author's peripheral work in industry, four distinct approaches for furthering the cause of HDR:

  1. **Discovery-Driven Activism** [[7.4.2](#approach-1)]
  2. **Building the Human-Centric Future** [[7.4.3](#approach-2)]
  3. **Defending User Autonomy and Hacking the Information Landscape** [[7.4.4](#approach-3)]
  4. **Teaching, Championing and Selling the HDR Vision** [[7.4.5](#approach-4)]

**C7: A reframing of data literacy for the HDR space**

Section [7.4.5.1](#7.4.5.1) broadens existing conceptions of _data literacy_ that include critical thinking, numerical analysis and arguing using data, to describe additional skills that people will need to develop if they are to become fully _**HDR literate**_:

  - appreciating the value of personal data;
  - understanding the implications of organisational data use;
  - recognising why portable data and app/data separation is important;
  - knowing how to exercise data rights and evaluate responses;
  - identifying diminishing agency and erosions of a free and fair information landscape.

### Additional contributions in the Early Help and Civic Data Use context{#1.2.3}

**C8: Validation and enumeration of supported families' attitudes and needs around civic data**

The pilot study [[1.3.1](#1.3.1)] and its continuation through Case Study One [[Chapter 4](#chapter-4)] was useful to validate that people do feel the effects of data records about them and, contrary to early expectations, do care about data access. People want **continuing rights, control and visibility over their personal data**, so that it remains **fair, accurate and meaningful**.  Furthermore, the lived experiences of supported families show how **data can become a proxy for human involvement**, and that this can be harmful and disempowering. In particular:

- Supported families need **meaningful interaction** with and through data,
- They need to be **given a voice** to explain, challenge or add context to data, and
- **Transparency over data can improve trust** in support services.

**C9: _Shared Data Interaction_: A proposed model for more efficient and empowering social support relationships that embraces human-centricity**.

Support service providers want to be more data-centric to improve accuracy [[4.1.2](#4.1.2), [4.2.3](#4.2.3)], while supported families want a more human, less data-centric treatment. [[4.2.4](#4.2.4)] describes a novel model that has the potential to address both parties' conflicting needs and enhance the support relationship: _Shared Data Interaction_. While this was not evaluated in the field, it is consistent with emergent practices [[4.3.1](#4.3.1)], and, after thorough exploration by participants [[Table 3.1](#table-3.1)] - was perceived to be beneficial. The benefits (and challenges) of such an approach are explored thoroughly in [[4.4.3](#4.4.3)]. The success of this study's methodology [[3.5.2](#3.5.2)] provides further evidence for the effectiveness of bringing people together around representations of data, echoing other researchers' work on _boundary objects_ [@star1989] and _'things to think with'_ [@brandt2004].

### Additional contributions in the context of GDPR and Everyday Data Access{#1.2.4}

**C10: A model to understand the five different origins of held personal data**

[[Table 5.2](#table-5.2)] describes five different types of data organisations can hold about individuals:

  - **Volunteered Data**
  - **Observed Data**
  - **Derived Data**
  - **Acquired Data**
  - **Metadata**

This model has been used as both during design and ideation sessions at BBC R&D as well as being used and cited within SITRA/Hestia.ai's digipower study, both for explaining data holding to participants and as a frame for data analysis [@bowyer2022hestia; @pidoux2022].

**C11: A rich understanding of the lived experience of accessing data using GDPR rights and of motivations for GDPR data access**

Case Study Two fills a research gap in understanding the human experience of using GDPR to access one's personal data. The findings [[5.4](#5.4)] confirm previous research that compliance is poor and returned data often incomplete [@ausloos2018], and contribute new knowledge by uncovering specific attitudes such as **resignation about data sacrifice**, **disappointment in GPDR handling** by service providers, and **a lack of answers to questions**. Specific motivations for GDPR data access (and hence more widely for HDR) are enumerated, which provides a valuable starting set of requirements for future research and innovation (see [Table 5.5](#table-5.5) and the supplemental materials of [@bowyer2022gdpr]).

**C12: Evidence for the impact of knowledge about data handling practices on provider trust and perceived individual power**

A particularly novel and surprising discovery from Case Study Two was that the use of GDPR rights and privacy policy analyses to scrutinise data-holding service providers often resulted in a **decrease in trust** in those same data holders. At the same time, GDPR use on the whole failed to provide a net increase in perceived individual power; it was **not empowering** people and hence not meeting its own goals. Further analysis of these patterns also showed that **data handling practices are critical to trust and consumer loyalty** [[5.3.4](#5.3.4); [5.5.2](#5.5.2)]].

**C13: Guidance for policymakers, data holders and individuals on how to improve HDR**

Synthesis and analysis of participant experiences in Case Study Two enabled the production of specific guidance [[5.5](#5.5)] for parties involved in data relationships:

  1. Policymakers and DPOs should do better at **enforcing GDPR rights**, and regulate to **improve response quality** and legislate to mandate data holders to **support data subjects in understanding data**.
  2. Data-holding service providers should **improve transparency** over data and data handling process, and could seize the opportunities of **more inclusive and collaborative models of individual data access** to improve trust, empower users and reduce their own liability.
  3. Individuals should recognise the critical role of held personal data in modern life, embrace opportunities to **access and exploit their own data** and **use data access rights to hold service providers to account**.

**C14: A proto-methodology for educating individuals about held data, data access and the data ecosystem**

While it was not designed as a methodological contribution nor formally evaluated as such within the scope of this thesis, the guided-data-retrieval-and-interview approach of Case Study Two [[5.2](#5.2)] has proven to be **highly valuable and replicable** as means to connect people with their held data and conduct research at that intersection point. The creation of this methodology resulted in this author being approached and employed as lead researcher of Hestia.ai/SITRA's digipower investigation [@härkönen2022project], which **adopted Case Study Two's methodology**, with some adaptation and broadening of scope, for an extensive EU study auditing and understanding the power of data holders in the data economy [@bowyer2022hestia; @pidoux2022; @härkönen2022report].

Publications arising from and connected to this research{#1.3}
--------------------------------------------------------

### Pilot Study{#1.3.1}

My Doctoral Training programme at Open Lab began with a Masters in Research in Digital Civics. For my MRes project[^1], I conducted a pilot study, interviewing and exploring issues around data with families who had experience of social care services. During the first months of this PhD, I conducted new analysis of the data collected, resulting in the synthesis into a full first-author paper published and [presented at](https://chi2018.acm.org/attending/proceedings/) CHI 2018:

- "[Understanding the Family Perspective on the Storage Sharing and Handling of Family Civic Data](https://dl.acm.org/doi/10.1145/3173574.3173710)" [@bowyer2018family]

This study is given a special status in this thesis; while it is not officially to be examined, it plays a critical role as a pilot study for Case Study One and its findings and insights are built upon in Chapters [4](#chapter-4), [6](#chapter-6) and [7](#chapter-7). The paper is included in full in [Appendix A](#appendix-A).

[^1]: MRes result awarded: Distinction.

### Primary Case studies{#1.3.2}

#### Publications from Case Study One{#1.3.2.1}

The work exploring shared data interaction in Early Help carried out in Case Study One has been initially published as an Extended Abstract at CHI 2019:

- "[Human-data interaction in the context of care: Co-designing family civic data interfaces and practices](https://doi.org/10.1145/3290607.3312998)" [@bowyer2019]

This work was also presented at the conference in the form of a poster, which is shown in [Figure 1.1](#figure-1.1). A full journal paper of Case Study One is in prep.

![Figure 1.1: Poster Presentation of Case Study One](./src/figs/fig1.1-hdi-in-care-poster.png){#figure-1.1}

#### Publication from Case Study Two{#1.3.2.2}

The work exploring the human experience of GDPR data access carried out in Case Study Two has been published [and presented](https://www.youtube.com/watch?v=hf-XjsCgBJY&t=32465s) as a full first-author paper at CHI 2022, where it was awarded an _Honourable Mention_:

- ["Human-GDPR Interaction: Practical Experiences of Accessing Personal Data"](https://doi.org/10.1145/3491102.3501947) [@bowyer2022gdpr].

I carried out all field research myself. Data analysis and paper writing were jointly executed by myself and Jack Holt.

### Workshop papers & presentations{#1.3.2.3}

During the PhD, I gave a number of additional presentations and published three workshop papers which included material from, or directly contributed to, this thesis and its arguments.

- ["Designing for Human Autonomy: The next challenge that civic HCI must address"](https://eprints.ncl.ac.uk/273832) [@bowyer2017] - a short talk I presented to my peers at Open Lab in January 2017 laying out the landscape of reduced agency and possible avenues for improving humans' relationships to their data that my PhD would explore;
- ["Free Data Interfaces: Taking Human-Data Interaction to the Next Level"](https://eprints.ncl.ac.uk/273825) [@bowyer2018freedata] - a CHI 2018 workshop paper formalising my pre-PhD design thinking and outlining a vision for unconstrained and useful data interaction interfaces;
- ["A Grand Vision for Post-Capitalist HCI: Digital Life Assistants"](https://eprints.ncl.ac.uk/273826) [@bowyer2018grandvision] - a CHI 2018 workshop paper where I imagined a form of digital computer assistant that is far more helpful and human-data-centric than the digital voice assistants of today;
- ["Personal Data Use: A Human-centric Perspective"](https://eprints.ncl.ac.uk/273834) [@bowyer2020lecture] - in early 2020 just prior to the pandemic, I was invited to give lectures on my research to undergraduate students at both Northumbria University and Newcastle University;
- ["My Thesis in 3 Minutes: Understanding and Designing Human Data Relations"](https://www.youtube.com/watch?v=YFHXc_TfM5c) [@bowyer20213MT] - in April 2021, I presented my thesis in Newcastle University's 3-minute thesis competition, and was co-winner of the people's choice prize;
- ["Human-Data Interaction has two purposes: Personal Data Control and Life Information Exploration"](https://eprints.ncl.ac.uk/274297) [@bowyer2021twopurposes] - A workshop paper I presented at CHI 2021, where I first outlined my model of the two motivating factors for interacting with personal data.

### Publications from other work{#1.3.2.4}

During the same timeframe as this PhD, I have also contributed to a number of publications from peripheral work [[Appendix D](#appendix-d)] tangential to my primary research agenda:

- As a researcher and developer on the Connected Health Cities SILVER project [[3.4.1.1](#3.4.1.1)], I contributed to work published through Newcastle University's internal report to CHC (not publicly available) and the [overall impact report](https://web.archive.org/web/20211225192408/https://www.chc-impact-report.co.uk/) [@ConnectedHealthCities2021impact,129-130], and more directly published [demonstration videos](https://eprints.ncl.ac.uk/273839) [@bowyer2019silvervideo] of a health data interface prototype developed by myself and Stuart Wheater.
- As a researcher and developer on DERC's Healthy Eating project, I developed interface prototypes (no longer online) and was co-author to two research publications [at BCS 2021](https://doi.org/10.14236/ewic/HCI2021.16) [@goffe2021] and [in Interacting with Computers](https://doi.org/10.1093/iwc/iwac015) [@goffe2022].
- As a research intern on BBC R&D's Cornmarket project [@sharp2021], I published an internal research report [TODO ADD REF] into personal data store design, as well as a 'stimulus presentation' to launch an internal hack week and a BBC blog article about the work (which was not officially published) [TODO ADD REF].
- As project leader, data access coach and researcher at Hestia.ai, I was a lead author on [a research report auditing the data economy](https://doi.org/10.5281/zenodo.6554177) [@bowyer2022hestia], and co-author on [a research report on power mechanisms in the data economy](https://doi.org/10.5281/zenodo.6554155) [@pidoux2022].

The structure of this thesis{#1.4}
----------------------------
[TODO address JG feedback]

The overall structure of this thesis is illustrated in [Figure 1.2](#figure-1.2). This introduction is followed by a literature review [[Chapter 2](#chapter-2)] and a methodology chapter [[Chapter 3](#chapter-3)]. Both research questions RQ1 and RQ2 are examined in both Case Studies, and these studies are documented as self-contained pieces of research in [[Chapter 4](#chapter-4)] and [[Chapter 5](#chapter-5)] respectively. In [[Chapter 6](#chapter-6)] the findings and insights from the Case Studies are synthesised into common findings as to what people want from data and from data holders, which concludes the academic investigation of the two research questions. [[Chapter 7](#chapter-7)] looks beyond the theoretical to the practical, setting the stage for future research and innovation in the HDR landscape, building on both the research conclusions in Chapter 6 as well as my practical experiences from other related research and development activities conducted outside of this PhD research but during the same timeframe. Each chapter finishes with a summation section. [Chapter 8](#chapter-8) concludes the thesis.

![Figure 1.2: The Structure of This Thesis](./src/figs/fig1.2-thesis-structure.jpg){#figure-1.2}

[Chapter 2](#chapter-2) is a literature review divided into three key sections. The first [[2.1](#2.1)] examines the difference between data and information, outlines the central role data has taken in our society, why people need effective access to their data and how laws have been introduced to try and deliver this. The second [[2.2](#2.2)] serves as history of personal data interaction, from Personal Information Management to the emergence of complex digital lives involving relationships with many data-holding providers. Finally [[2.3](#2.3)] charts a path from HCI and Human-Data Interaction foundations through to the embracing of sociotechnical thinking around data and the current bleeding edge [@dictBleedingEdge] of human-centred innovation, leading to the primary academic Research Question (RQ) of this thesis: _"What relationship do people need with their personal data?"_ [[2.4](#RQ)].

[Chapter 3](#chapter-3) describes the methodology used in this research, explaining first the constructivist ontology and pragmatist, individualist epistemology behind the approach [[3.1](#3.1)]. Then the choice of participatory action research and co-design from a Digital Civics standpoint is explained [[3.2](#3.2)]. The two research questions (RQs) are explained in more detail [[3.3](#3.3)] and the contexts for the Case Studies are introduced from a personal 'what did I do?' perspective [[3.4](#3.4)]. Finally, the specific methods and techniques adopted in the research are explained and illustrated, including sensitisation, workshop activities, recruitment strategies and modelling [[3.5](#3.5)].

[Chapter 4](#chapter-4) is a detailed, self-contained account of Case Study One. This begins [[4.1](#4.1)] with a detailed introduction to the UK's Early Help social care context, including its history of data-centrism and the inherent contradiction between that and the empowerment goals of Early Help which make it an ideal setting to explore my research questions. In [4.2](#4.2), prior findings on family and staff perspectives are introduced, motivating the _'Shared Data Interaction'_ vision and structure of the workshops, whose participants' shared values are introduced. The thematic findings are detailed extensively [[4.3](#4.3)] including participant quotes, and then contextualised in the discussion [[4.4](#4.4)] in terms of the value of involving people with their data, the link between HDI and effective data access, and the implications of shifting the locus of decision-making.

[Chapter 5](#chapter-5) is a thorough and self-contained write-up of Case Study Two. The first section [[5.1](#5.1)] provides additional context on the need for data access, prior GDPR research and the human-centric approach to this study, whose design and configuration is detailed in [5.2](#5.2). Findings are shared: firstly [[5.3](#5.3)] the largely quantitative outcomes of the participants' GDPR requests, interview responses and trust/power scores, then the thematic findings [5.4](#5.4), illustrated with participant quotes. The discussion [[5.5](#5.5)] contextualises and synthesises the findings into human-centric, GDPR-improving guidelines for policymakers, data holders and individuals.

[Chapter 6](#chapter-6) synthesises the two case studies, and answers RQ and RQ2, bringing the thesis's central academic research to a close based on findings and discursive insights from both studies backed by literature references. The answer to RQ1 is provided [[6.1](#6.1)] as people's three wants from direct data relations (for it to be visible, understandable and useable), and the answer to RQ2 is provided [[6.2](#6.2)] as people's three wants from indirect data relations (process transparency, individual oversight, and involvement). The chapter concludes [[6.3](#6.3)] by outlining this thesis's perspective power and positioning the pursuit of these six _'data wants'_ as _empowerment_ relative to that perspective and thus as _'better HDR'_.

[Chapter 7](#chapter-7) looks beyond the original research question, and is a deliberately broad, shallow and open-ended chapter synthesising designerly insights acquired through practical experience. Here I move beyond a traditional thesis structure, with the goal of providing real-world ideas on _how such human-centric empowerment might be achieved in practice_. In tackling this more practical question, the thesis becomes a _valuable and actionable anthology of reference material_ for future researchers, activists and innovators. First [[7.1](#7.1)], the peripheral contexts that I worked in alongside this PhD from with the additional insights arise are introduced. In [[7.2](#7.2)], the findings of the thesis are expanded upon to frame the pursuit of this thesis's _'data wants'_ as a defined field of future research, called _Human Data Relations_ (HDR), whose practitioners act as a _recursive public_, pursuing four _'landscape objectives'_ that could address the data wants in reality.

The landscape of HDR is mapped out in two parts. First [[7.3](#7.3)], I outline the identified _obstacles_ to pursuit of the HDR objectives. Then [[7.4](#7.4)], using a _Theories of Change_ (ToC) framing, my identified _opportunities for progress_ are introduced, divided into _four different trajectories of change_ that could be executed to pursue better HDR. [7.3](#7.3) and [7.4](#7.4) are interspersed with actionable _insights_ that could help tackle the obstacles and pursue the change trajectories. [7.5](#7.5) is a summation of the chapter.

[Chapter 8](#chapter-8) is a brief conclusion of the thesis, summarising its contributions and positioning HDR and this thesis as call to arms for activist research and innovation that can tackle the power imbalance in society.

---
