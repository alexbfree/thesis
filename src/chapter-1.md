Introduction{#chapter-1}
=======================

> _"My data is everywhere, and I am nowhere."_—Imogen Heap (musician and digital rights advocate), speaking at MyData 2019, encapsulating a core problem with modern digital life.

Background and Motivation for this Research{#1.1}
-------------------------------------------

We live in an increasingly data-centric world, where our direct and indirect interactions with computer systems depend upon the collection, storage and use of personal data about individuals. Motivated to reduce costly human interaction and scale to serve more customers, organisations capture and represent individuals as data and rely increasingly on the interpretation of those datapoints to make decisions—decisions that affect our everyday lives in myriad ways, from determining eligibility to access particular services, benefits or products or targeting advertisements or recommendations to influencing our decisions and behaviour. Data about people has become extremely valuable. It is 'the new oil' [@toonders2014] driving a model of _surveillance capitalism_ [@zuboff2019] that collects data and exploits it for profit.

This multi-party use of data has resulted in a splintering [@lemley2021] of our _digital selves_ across hundreds of different organisations' computer systems, creating 'a chaos of multiplicity' [@bødker2015] where data becomes trapped [@abiteboul2015] and hard to manage. Current data practices cause harm to individuals through anxiety, distraction and a sense of being overwhelmed [@fu2020; @timely2020]. Data use can harm society too, due to the ease with which people's attention and beliefs are manipulated, risking radicalisation and a loss of democratic freedom [@thompson2011; @chan2019]. It is generally accepted that:

> _"There is **a power imbalance** in the amount of information about individuals held by industry and governments, and the lack of knowledge and ability of the same individuals to control the use of that information."_—World Economic Forum [@wef2014context]

To address this power imbalance, people need a more effective relationship with their own data. This has been conceptualised as a lack of _agency_ (the ability to act for oneself), _negotiability_ (the ability to exert influence over data use within the system as things change), and _legibility_ (the ability to understand one's data and its implications) [@mortier2014]. Currently, users of today's digital services typically experience a _point of severance_ [@luger2013]: they are forced to sacrifice their data and are subsequently cut out of the loop. Without understanding how they are currently seen through data, people face risks of unfair treatment, or physical or psychological harm [@bowyer2018family; @crossley2022]. Left unexplored and unchallenged, the situation will not improve, as the datafication of society grows, and user agency continues to diminish.

This thesis focuses on that power imbalance and explores ways in which individual agency, legibility and negotiability can be improved. In Part One, its participatory Case Studies make a novel contribution to knowledge, producing a deep understanding of how people relate to data, what capabilities people want, and how they would like service providers to handle their data. These understandings, shaped as six core human desires, can drive future research to empower individuals through their personal data.

Part Two, building upon these findings, defines a new, broader frame for this problem space, **Human Data Relations (HDR)**. Building upon Human Data Interaction (HDI) [@mortier2013; @mortier2014] theory, HDR additionally incorporates the sociotechnical and commercial realities of today's data-centric world and defines a clear agenda for change. This new space is mapped out in terms of objectives, obstacles, approaches and designs, based on the author's parallel industrial research experience and _adversarial design_ [@disalvo2012] thinking. These insights and strategies can equip future researchers and innovators with the tools and understandings they will need to pursue the empowerment of individuals and the rebalancing of power over data at a societal level.

### Personal Motivation and Context{#1.1.1}

This PhD and this thesis represent the culmination of my lifelong passion to help people get more value from our computers. My experience and expectations of computers was shaped by the 1980s home computing revolution, which taught me and a generation of young people that the computer was a machine to program, a tool to be exploited, mastered and bent to your will. Then, in my formative years approaching the turn of the millennium, I lived through the birth of the public Internet and marvelled at the ability for computers to connect people across the world, empower individuals as creators, innovators and broadcasters, level the playing field and transform the way people interact. I gradually shifted my software engineering career from back-end to front-end development and ultimately to User Experience (UX), driven to take a more active role in building software features that directly benefit users and improve their lives. Keenly tracking and embracing the Web 2.0 revolution while observing the digitisation and disruption of so many industries, I became fascinated with the ways in which humans were shaping computer systems which in turn were shaping our habits and our society, phenomena I explored through the Human 2.0 blog which I co-founded [@bowyer2009human].

But then, having seen Internet-era computing give us new capabilities, and knowing the potential of computers to become tools for positive change in society, I bore witness to a changing world, and the balkanisation and commercialisation of the once-free Internet. As companies adapted to the Information Age and shifted to data-driven, cloud-centric business models, our ability to harness computers for our own ends began to slip away. While immersed in the start-up community in Montréal, Canada, I became frustrated at this loss of potential. Driven to explore the reasons and implications of this loss of agency and the possibilities for more human-centric computing, I published several essays and presentations [@bowyer2009bitnorth; @bowyer2010bitnorth; @bowyer2011filesdie; @bowyer2012bitnorth; @bowyer2012timespace; @bowyer2013bitnorth] which collectively form the seed from which this thesis grew.

By 2014, it was beyond doubt to me that the software industry had lost its way, prioritising business goals over user agency, reducing features and creating technology designed to limit and corral users to behave in certain ways. Web 2.0's revolutionary potential of a 'people's internet' had been squashed and withered away in the shadow of new data giants Google, Facebook, Apple and Amazon, who reshaped and usurped Internet, Web and smartphone technologies for profit, at great cost to human wellbeing. Against a backdrop of a social media revolution which was literally breaking society and democracy to drive profit [@tufekci2017; @hall2018], I took the leap to escape corporate IT. I sought to research, design and build a better digital future where computers could be made useful again. This led me to the _Digital Civics_ CDT programme [@digitalCivicsCDT2018], where I was finally able to work full-time on what I consider the most important problem of our age—**Understanding and Improving Human Data Relations**.

### Research Objectives and Purpose{#1.1.2}

The aim of this thesis is to research how people relate to data, how they understand and use it, and what they want from it and its holders in order to thrive and to meet their own goals.

The thesis is informed by a constructivist ontology and a pragmatist, individualist epistemology [[3.1](#3.1)], and employs a multi-disciplinary _Digital Civics_ [@vlachokyriakos2016] approach, conducting an academic inquiry to answer two key research questions (RQ):

> **RQ1.** What is the human experience of personal data, and what do people want from their data? [[3.3.1](#RQ1)]

> **RQ2.** What role does data play in people's service relationships, and how could relationships involving data be improved? [[3.3.2](#RQ2)]

This thesis assumes that if the asymmetry over data access and use between individuals and organisations holding data is to be addressed, that a greater understanding of current data use issues is needed by all parties, and that the production of knowledge and insights is therefore a vital first step towards the pursuit of a more balanced model of data use that can deliver increased agency and negotiability.

After reviewing relevant existing literature and research [[Chapter 2](#chapter-2)] to identify a clear baseline and research gap, Part One of the thesis reports on two studies that invited participants to 'look behind the curtain' of the opaque data-centric organisations they interact with. These enabled participants to consider more deeply the collection, storage and use of their personal data by service organisations. A participatory research design was employed, collecting interview transcripts to enable qualitative analysis and identify themes that inform a descriptive model of human-centred data empowerment needs. The focus was upon examining current practices, identifying attitudes to those practices, and imagining alternative designs and approaches for data use by service providers and the participants themselves. The participant groups were:

  - **Case Study One**: Supported families, who meet with _Early Help_ support workers (whose role is to access civic data to understand and empower those individuals to improve their lives) [[Chapter 4](#chapter-4)]; and
  - **Case Study Two**: Ordinary British and European citizens, who gained new legal rights via 2018's _GDPR_ legislation [[2.1.3](#2.1.3)], enabling them to request copies of held personal data along with other relevant information from the companies and service providers in their lives [[Chapter 5](#chapter-5)].

Through comparative analysis of the two case studies, commonalities in individual attitudes and understandings serve to validate each other, and allow the expression of clear insights about people's relationships to personal data that can serve as answers to the two RQs. This synthesis and analysis of interview data enabled the generation of a descriptive model to address the research gap, concluding the core academic research of this PhD [[Chapter 6](#chapter-6)].

This research is situated in the HCI discipline, which means that design (both participatory co-design and expert-informed user-centred design [[3.5](#3.5)]) forms a key part of the approach to exploring the problem space. Design work to examination individual attitudes and desires around data in a 'whole life' sense is an under-researched area. Where HCI traditionally focuses on the mechanisms by which humans interact with data, the academic enquiry in Part One adopts a more sociotechnical focus on understanding lived experience.

Part Two takes an even broader perspective, recognising that for participants' desired changes in data relations to be realised requires an examination and a recognition of current technical, legal and commercial realities and the multi-party complexities of modern digital life. In this second part, the thesis shifts from participatory academic enquiry to real-world explorations that apply its findings in practice. This is done through design, modelling and conjecture, drawing upon the author's direct experiences working (alongside the PhD) in related projects that share this thesis's focus on empowering individuals through data.

To support future researchers, activists and innovators in achieving the vision of a more human-centric future, the pursuit of wants identified in Part One are shaped into a defined new field - **Human Data Relations (HDR)**. Moving from merely understanding the world towards planning how to change it, motivations and objectives are identified, and HDR is positioned as a broad activist agenda whose practitioners seek to reconfigure society to their own advantage [[Chapter 7](#chapter-7)].

The remainder of Part Two, which is deliberately open-ended, maps out the existing landscape of challenges and possibilities for the HDR field, moving away from a traditional thesis structure in order to offer more actionable insights. Given the scale of the sociotechnical design challenge society faces, this thesis does not carry out 'in the wild' evaluation of particular data interaction approaches or interface designs. Instead, drawing upon direct experience as well as the work of other researchers and innovators in this space, it documents known obstacles [[Chapter 8](#chapter-8)] and shares designerly [insights](#inset-boxes). It also maps out four possible change trajectories [[Chapter 9](#chapter-9)] which can inform future design and innovation in human-centric system design. These strategies, which should be viewed as speculative rather than definitive, can also help facilitate initiatives that recognise and confront the unique challenges of the status quo in pursuit of improving people's agency and negotiability through personal data.

Taken together, the two parts of this thesis can serve as novel and actionable reference material for future research, activism and innovation, solidly grounded in literary theory, participant experience, and industrial reality.

Nature and Contributions of the Thesis{#1.2}
--------------------------------------

This section lists the 14 major contributions (**Cn**) of this thesis, which can be summarised as:

- an understanding of what people want when they relate to data [[1.2.1](#1.2.1)];
- the establishment and mapping of the field of _Human Data Relations_ [[1.2.2](#1.2.2)]; and
- additional contributions specific to the Case Study contexts of
  - Early Help [[1.2.3](#1.2.3)], and
  - GDPR/everyday data access [[1.2.4](#1.2.4)].

### An Understanding of what People want from Personal Data{#1.2.1}

Through the concluding sections of Chapters [4](#chapter-4) and [5](#chapter-5), the reader will be able to see that research participants across both studies (and the pilot study) shared common issues around personal data. These commonalities provide the answers to RQ1 [[3.3.1](#RQ1)] and RQ2 [[3.3.2](#RQ2)], which form the first two contributions C1 and C2:

**<a name="c1">C1</a>: An understanding of What People Want in Direct Data Relations**

Section [6.1](#6.1) answers RQ1 by explaining that people have three specific desires for direct relations with data–for data to be:

- visible [[6.1.1](#6.1.1)],
- understandable [[6.1.2](#6.1.2)], and
- useable<sup>[10](#fn10)</sup> [[6.1.3](#6.1.3)].

**<a name="c2">C2</a>: An Understanding of What People Want in Indirect Data Relations**

Section [6.2](#6.2) answers RQ2 by explaining the three things people want when they have an indirect relationship to their data because it is held by someone else, such as a service provider:

- process transparency [[6.2.1](#6.2.1)],
- individual oversight [[6.2.2](#6.2.2)], and
- involvement in processes and decision making [[6.2.3](#6.2.3)].

### Establishing a New Field: Human Data Relations{#1.2.2}

**<a name="c3">C3</a>: The Synthesis and Formulation of the Field of Human Data Relations (HDR)**.

At the highest level, this thesis contributes a new field of research and innovation, _Human Data Relations (HDR)_. [Chapter 2](#chapter-2) reviews existing literature and prior work to explain the problems of data-centrism and limited access to data [[2.1](#2.1)]; personal information management and interaction [[2.2](#2.2)]; and human-centric perspectives on data [[2.3](#2.3)].
From this baseline, the participatory academic enquiry into the lived realities described in Chapters [4](#chapter-4) and [5](#chapter-5) lead to a synthesis [Chapter 6](#chapter-6) of what people want in data relations.
[Chapter 7](#chapter-7) formalises this defined field of academic and practical endeavour, Human Data Relations [[7.3](#7.3)], as the pursuit of four specific objectives:

  - data awareness and understanding
  - data useability
  - data ecosystem awareness and understanding
  - data ecosystem negotiability

**<a name="c4">C4</a>: A clear delineation of two primary motivators for individuals seeking better HDR**

[7.6](#7.6), informed by both the Case Studies and the peripheral activities [[7.2](#7.2)], clarifies the two driving motivations for pursuing better HDR:

  - Life Information Utilisation [[7.6.1](#7.6.1)], and
  - Personal Data Ecosystem Control [[7.6.2](#7.6.2)].

**<a name="c5">C5</a>: A map of the HDR landscape, identifying obstacles and insights**

The goal of this thesis is to set the stage for future research and innovation in the newly-defined space of Human Data Relations. Across sections [8](#8) and [9](#9), the landscape of HDR is mapped out from multiple perspectives.

[8](#8) maps out eight obstacles to the pursuit of the HDR objectives, as well as four obstacles that exist in the solution space across all four, including:

  - the personal data diaspora,
  - the intractable data self,
  - immobile, illegible and unmalleable data,
  - hegemony and active diminishing of user agency by data holders,
  - closed, introspective and insular practices,
  - a lack of demand and investment in HDR from individuals and organisations, and
  - insufficient machine understanding of human data.

To begin to address these obstacles, thirteen [Insights](#inset-boxes) are explained that could seed future research and innovation towards tackling these obstacles:

  - [1](#insight-1). Life information makes data relatable.
  - [2](#insight-2). Data needs to be united and unified.
  - [3](#insight-3). Data must be transformed into a versatile material.
  - [4](#insight-4). Ecosystem information is an antidote to digital life complexity.
  - [5](#insight-5). We must know data's provenance.
  - [6](#insight-6). Data holders exploit four levers of power to manipulate the digital landscape.
  - [7](#insight-7). We need new human-centred information systems that serve human values, relieve pain and deliver new life capabilities.
  - [8](#insight-8). We need to teach computers to understand human information.
  - [9](#insight-9). Individual GDPR requests can compel companies to change data practices.
  - [10](#insight-10). Collectives can compare and unify their data and use it to demand change.
  - [11](#insight-11). Automating the identification of entities can enhance machine understanding and unburden life interface users.
  - [12](#insight-12). The 'seams' of Digital Services need to be identified, exploited and protected.
  - [13](#insight-13). It is possible (and necessary) to demonstrate business benefits of transparency and human-centricity.

**<a name="c6">C6</a>: Four identified trajectories for advancing Human Data Relations**

[Chapter 9](#chapter-9) explains, with detailed real-world examples and original design work from the author's peripheral work in industry, four distinct approaches for furthering the cause of HDR:

  1. Discovery-Driven Activism [[9.2](#9.2)]
  2. Building the Human-Centric Future [[9.3](#9.3)]
  3. Defending User Autonomy and Hacking the Information Landscape [[9.4](#9.4)]
  4. Teaching, Championing and Selling the HDR Vision [[9.5](#9.5)]

**<a name="c7">C7</a>: A reframing of data literacy for the HDR space**

Section [9.5.1](#9.5.1) broadens existing conceptions of _data literacy_ that include critical thinking, numerical analysis and arguing using data, to describe additional skills that people will need to develop if they are to become fully _HDR-literate_:

  - appreciating the intrinsic value of personal data to themselves and others;
  - understanding the implications of organisational data use;
  - recognising why portable data and platform/data separation is important;
  - understanding one's data rights enough to confidently execute and evaluate responses;
  - identifying diminishing agency and erosions of a free and fair information landscape.

### Additional Contributions in the Early Help and Civic Data Context{#1.2.3}

**<a name="c8">C8</a>: Validation and documentation of supported families' attitudes and desires around civic data**

The pilot study [[1.3.1](#1.3.1)] and its continuation through Case Study One [[Chapter 4](#chapter-4)] was useful to validate that people do feel the effects of data records about them and, contrary to early expectations, do care about data access. People want continuing rights, control and visibility over their personal data, so that it remains fair, accurate and meaningful.  Furthermore, the lived experiences of supported families show how data can become a proxy for human involvement, and that this can be harmful and disempowering. In particular:

- Supported families need meaningful interaction with and through data,
- They need to be given a voice to explain, challenge or add context to data, and
- Transparency over data can improve trust in support services.

**<a name="c9">C9</a>: _Shared Data Interaction_: A proposed model for more efficient and empowering social support relationships that embraces human-centricity**.

Providers of care want to be more data-centric to improve accuracy [[4.1.2](#4.1.2), [4.2.3](#4.2.3)], while supported families want a more human, less data-centric treatment. [4.2.4](#4.2.4) describes a novel model that has the potential to address both parties' conflicting needs and enhance the support relationship: _Shared Data Interaction_. While this was not evaluated in the field, it is consistent with emergent practices [[4.3.1](#4.3.1)], and–after thorough exploration by participants [[Table 3.1](#table-3.1)]–was perceived to be beneficial. The expected benefits (and challenges) of such an approach are explored in [4.4.3](#4.4.3). The success of this study's methodology [[3.5.2](#3.5.2)] provides further evidence for the effectiveness of bringing people together around representations of data, echoing other researchers' work on _boundary objects_ [@star1989] and _things to think with_ [@brandt2004].

### Additional Contributions in the GDPR and Everyday Data Context {#1.2.4}

**<a name="c10">C10: A model to understand the five different origins of held personal data**

[Table 5.2](#table-5.2) describes five different types of data organisations can hold about individuals:

  - Volunteered Data
  - Observed Data
  - Derived Data
  - Acquired Data
  - Metadata

This model has been used as both during design and ideation sessions at BBC R&D as well as being used and cited within Sitra/Hestia.ai's _digipower_ investigation [[ARI7.2](#ARI7.2)], both for explaining data holding to participants and as a frame for data analysis [@bowyer2022hestia; @pidoux2022].

**<a name="c11">C11</a>: A rich understanding of the lived experience of accessing data using GDPR rights and of motivations for GDPR data access**

Case Study Two fills a research gap in understanding the human experience of using GDPR to access one's personal data. The findings [[5.4](#5.4)] confirm previous research that compliance is poor and returned data often incomplete [@ausloos2018], and contribute new knowledge by uncovering specific attitudes such as resignation about data sacrifice, disappointment in GPDR handling by service providers, and a lack of answers to questions. Specific motivations for GDPR data access (and hence more widely for HDR) are enumerated, which provides a valuable starting set of requirements for future research and innovation (see [Table 5.4](#table-5.4) and the supplemental materials of [@bowyer2022gdpr]).

**<a name="c12">C12</a>: Evidence for the impact of knowledge about data handling practices on provider trust and perceived individual power**

A particularly novel and surprising discovery from Case Study Two was that the use of GDPR rights and privacy policy analyses to scrutinise data-holding service providers often resulted in a _decrease_ in trust in those same data holders. At the same time, GDPR use on the whole failed to provide a net increase in perceived individual power; it was not empowering people and hence not meeting its own goals. Further analysis of these patterns also showed that data handling practices are critical to trust and consumer loyalty [[5.3.4](#5.3.4); [5.5.2](#5.5.2)]].

**<a name="c13">C13</a>: Guidance for policymakers, data holders and individuals on how to improve HDR**

Synthesis and analysis of participant experiences in Case Study Two enabled the production of specific guidance [[5.5](#5.5)] for parties involved in data relationships:

  1. Policymakers and DPOs should do better at enforcing GDPR rights. Regulators need to legislate to improve response quality and to mandate data holders to support data subjects in understanding data.
  2. Data-holding service providers should improve transparency over data and data handling process, and could seize the opportunities of more inclusive and collaborative models of individual data access to improve trust, empower users and reduce their own liability.
  3. Individuals should recognise the critical role of held personal data in modern life, embrace opportunities to access and exploit their own data and use data access rights to hold service providers to account.

**<a name="c14">C14</a>: A proto-methodology for educating individuals about held data, data access and the data ecosystem**

While it was not designed as a methodological contribution nor formally evaluated as such within the scope of this thesis, the guided-data-retrieval-and-interview approach of Case Study Two [[5.2](#5.2)] has proven to be valuable and replicable as means to connect people with their held data and conduct research at that intersection point. The creation of this methodology resulted in this author being approached and employed as lead researcher of Hestia.ai/Sitra's digipower investigation [@härkönen2022project], which adopted Case Study Two's methodology, with some adaptation and broadening of scope, for an extensive EU study auditing and understanding the power of data holders in the data economy [@bowyer2022hestia; @pidoux2022; @härkönen2022report].

Publications Arising From and Connected to This Research{#1.3}
--------------------------------------------------------

### Pilot Study{#1.3.1}

My Doctoral Training programme at Open Lab began with a Masters in Research in Digital Civics. For my MRes project[^1], I conducted a pilot study, interviewing and exploring issues around data with families who had experience of social care services. During the first months of this PhD, I conducted new analysis of previously collected data, resulting in the synthesis into a full first-author paper published and [presented at](https://chi2018.acm.org/attending/proceedings/) CHI 2018:

- _[Understanding the Family Perspective on the Storage Sharing and Handling of Family Civic Data](https://dl.acm.org/doi/10.1145/3173574.3173710)_ [@bowyer2018family]

This study is given a special status in this thesis; while it is not officially to be examined, it plays a critical role as a pilot study for Case Study One and its findings and insights are built upon in Chapters [4](#chapter-4) and [6](#chapter-6) and in [Part Two](#chapter-7). The paper is included in full in [Appendix A](#appendix-A).

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
- As a research intern at BBC R&D [[ARI7.1](#ari-bbc)], I published an internal research report [@bowyer2020bbcreport] into personal data store design, and wrote and presented a 'stimulus presentation' to launch an internal hack week.
- At Hestia.ai, I was a lead author on [a research report auditing the data economy](https://doi.org/10.5281/zenodo.6554177) [@bowyer2022hestia], and co-author on [a research report on power mechanisms in the data economy](https://doi.org/10.5281/zenodo.6554155) [@pidoux2022].

The structure of this thesis{#1.4}
----------------------------

The overall structure of this thesis is illustrated in [Figure 1.2](#figure-1.2). Clearly evident are its two distinct parts, as described in 1.1.2 above.

Part One, the participatory investigation, begins with a literature review [[Chapter 2](#chapter-2)] and a methodology chapter [[Chapter 3](#chapter-3)]. RQ1 and RQ2 are examined in both Case Studies, separately documented in [Chapter 4](#chapter-4) and [Chapter 5](#chapter-5). In [Chapter 6](#chapter-6) the findings and insights from the Case Studies are synthesised to explain, in answer to RQ1 and RQ2, what people want from data and from data holders, concluding the academic investigation.

Part Two is adversarial design work and strategic planning, expanding the original research question to examine how the desires uncovered might be achieved in practice. The practical pursuit of better data relations is formalised as a new field with clear objectives, _Human Data Relations_, in [Chapter 7](#chapter-7). This _HDR_ space is then mapped out, drawing on industrial experience, starting with the detailing of known obstacles in [Chapter 8](#chapter-8). Four specific strategic approaches to change, including detailed designs, are laid out in [Chapter 9](#chapter-9) as recommendations for future work, before the thesis is concluded in [Chapter 10](#chapter-10), bringing the two parts together.

![Figure 1.2: The Structure of This Thesis](./src/figs/fig1.2-thesis-structure.jpg){#figure-1.2}

[Chapter 2](#chapter-2) contains a literature review. The first part [[2.1](#2.1)] examines the difference between data and information, outlines the central role data has taken in our society, why people need effective access to their data and how laws have been introduced to try and deliver this. The second [[2.2](#2.2)] serves as history of personal data interaction, from _Personal Information Management_ to the emergence of complex digital lives involving relationships with many data-holding providers. Finally, [2.3](#2.3) charts a path from _HCI_ and _HDI_ foundations through to the embracing of sociotechnical thinking around data and the current bleeding edge [@dictBleedingEdge] of human-centred innovation, leading to the primary academic Research Question (RQ) of this thesis:

> _**"What relationship do people want with their personal data?"**_ [[2.4](#RQ)]

[Chapter 3](#chapter-3) describes the methodology used in this research, explaining first the constructivist ontology and pragmatist, individualist epistemology behind the approach [[3.1](#3.1)]. Then the choice of participatory action research and co-design from a _Digital Civics_ standpoint is explained [[3.2](#3.2)]. The RQ above is split into two—RQ1 and RQ2 [[3.3](#3.3)]—and the contexts for the Case Studies are introduced from a 'what did I do?' perspective [[3.4](#3.4)]. Finally, the specific methods and techniques adopted in the research are explained and illustrated, including workshop activities, sentisation, stimuli and recruitment [[3.5](#3.5)].

[Chapter 4](#chapter-4) reports on Case Study One. This begins [[4.1](#4.1)] with a detailed introduction to the UK's Early Help social care context, including its history of data-centrism and its inherent contradiction with the empowerment goals of Early Help, which make it an ideal setting to explore my research questions. In [4.2](#4.2), prior findings on family and staff perspectives are introduced, motivating the _Shared Data Interaction_ vision and workshop design. The key findings are presented [[4.3](#4.3)] then discussed [[4.4](#4.4)] in terms of involving people with their data, effective data access, and shifting the Locus of Decision Making.

[Chapter 5](#chapter-5) reports on Case Study Two. [5.1](#5.1) contextualises data access in light of the GDPR and explains the human-centric approach to this study [[5.2](#5.2)]. Findings are presented in [[5.3](#5.3)] reporting on quantitative outcomes based on analysis of participants' GDPR requests, interview responses and participant-assigned scores. These are followed by presentation of key themes from qualitative analysis of interviews and observations [[5.4](#5.4)]. The discussion [[5.5](#5.5)] builds upon these findings to form GDPR-improving guidelines for policymakers, data holders and individuals, in line with a human-centric philosophy.

[Chapter 6](#chapter-6) synthesises the two Case Studies, and answers RQ1 [in [6.1](#6.1)] and RQ2 [in [6.2](#6.2)], bringing the central academic research of the thesis to a close with clear statements about what people want from data—visibility, understanding and useability—and from data holders—transparency, oversight and involvement. [6.3](#6.3) concludes the chapter and Part One, by outlining this thesis's purpose to address the power imbalance over personal data, positions these six 'wants' as desirable _empowerment_ relative to that perspective, motivating their practical pursuit.

[Chapter 7](#chapter-7) begins Part Two, shifting to a practical focus to explore how human-centric empowerment might be achieved. The thesis' findings are synthesised, drawing on experience from external work, to formally define a field of future research called _Human Data Relations (HDR)_, whose practitioners act as a _recursive public_ [[7.8](#7.8)], pursuing four objectives [[7.7](#7.7)] for increased awareness, understanding and negotiability.

The landscape of HDR is mapped out in two parts. [Chapter 8](#chapter-8) focuses on identifying obstacles to pursuit of the HDR objectives. Interspersed through the chapter as inset boxes are [8 insights](#inset-boxes-c8) that can inform adversarial design approaches.

[Chapter 9](#chapter-9), using a _Theories of Change (ToC)_ framing, introduces opportunities for progress, arranged as four different trajectories of change that could be executed to pursue better HDR. These approaches are illustrated with designs and illustrations to explain possible strategies, and interspersed with a further [5 insights](#inset-boxes-c9) that could seed future actions to tackle the aforementioned obstacles and pursue the change trajectories, improving the HDR landscape.

[Chapter 10](#chapter-10) concludes the thesis, reflecting first on this researcher's journey [[10.1](#10.1)], before summarising the legacy and contributions of this body of work [[10.2](#10.2)], positioning HDR and this thesis as call to arms for activist research and innovation to tackle the power imbalance around personal data in society.

---
