<h1 class="title">Section II: Understanding Attitudes and Desires through Participatory Case Studies</h1><a name='#section-ii'/>

<h2>Introduction to Section II</h2><a name='#section-ii-intro'/>

Section II will describe the participatory co-design work undertaken to explore [RQ1](#RQ1) (what people want from data) and [RQ2](#RQ2) (what people from relationships involving data). These RQs are both explored across two contexts. Following a short introduction to these two contexts and their rationales, [Chapter 4](#chapter-4) will describe Case Study One, which examines current and imagined data use approaches in Early Help in the UK, and [Chapter 5](#chapter-5) will describe Case Study Two, a study involving the exercise of GDPR data access rights by participants. Each chapter describes findings from each piece of participatory research and includes a discussion to draw insights from each Case Study. Findings and insights will then be examined for commonalities across the two Case Studies in Section III, in order to answer RQ1 and RQ2.

### The Two Research Contexts: _Early Help_ and GDPR{#section-ii-research-contexts .unnumbered}

As described in [3.2.2](#3.2.2), a two-track research approach was chosen to both explore people's viewpoints and explore reconfiguration of data relations in light of sociotechnical realities. For the participatory track, I was keen to examine the 'everyday digital life' where I had first observed problems of agency and lost human potential [[1.1](#1.1)]. However, at the start of this PhD in 2016, it was hard to see how to frame a study around this. An opportunity arose to take an embedded role as a researcher and developer within Connected Health Cities' SILVER project [@ConnectedHealthCities2017silver]. This presented an ideal context for something more focused on a particular demographic and type of personal data: namely the relationship that families have with their civic data while receiving _Early Help_ social support from their local authority. The SILVER project ran from 2017 to 2019 and was a UK-government-funded "care pathways" project involving University departments, local authorities, NHS trusts and private technology firms in the North of England. It sought to conduct participatory research and technical prototyping to explore the viability of creating an intervention that would allow professionals across many agencies to access better data about supported families while also exploring and addressing the need to ensure such families' consent to data sharing.

The SILVER project its Early Help context in general became the setting for Case Study One. This choice to focus on Early Help to explore RQs around data is contextualised in [Chapter 4](#chapter-4) below, but let us first explain the term: Early Help is a particular type of social support offered by UK local authorities as voluntary help to families who are considered to be at risk of falling into poverty, crime, truancy, addiction or other issues which are both problematic for the individuals and costly to the state. Families enrolled in the scheme meet a social worker (called a _support worker_ in this context) regularly who can provide advice and connect the family with appropriate health, lifestyle and social services to their needs. As part of this, the support worker has access to a variety of data from civic sources: school records, employment and benefits data, social housing data, criminal records, and more, so that they might be better informed about the family's situation. However, the families do not have any access to this data, and thus despite this being a scheme that is on the face of it intended to empower families to help themselves, it runs the risk of _disempowering_ the families through a data-centric power imbalance, exactly the phenomenon identified in the background research [[2.1.2](#2.1.2)]. Therefore, this context would be ideal for the exploration of both RQ1 [[3.3.1](#RQ1)] (finding out how these supported families feel about their data) and RQ2 [[3.3.2](#RQ2)] (examining the impacts of data use within a service relationship) as well as to explore how the families could imagine their data relations being improved. An important aspect of this context was that the SILVER project and local authority contacts gave me as a researcher access to support workers and other local authority contacts, allowing both sides of the Early Help data relationship to be explored, a goal I had already identified in [3.3.2](#3.3.2).

The coming into effect into EU law of the _GDPR (General Data Protection Regulation)_ in May 2018 presented a pragmatic research vector for both participatory research and self-experimentation into the wider aforementioned 'everyday digital life' problem space explored in [Chapter 2](#chapter-2). GDPR rights would give researcher and participants would a means to examine what data was held by service providers, which would provide a suitable basis for investigation and discussion. This data would not be limited to the civic data context but potentially could include any service that an individual might use in their everyday life. This seemed an ideal and complementary context to the Early Help context—focused a little closer to individuals' own lives and personal goals, and this time focused on the average citizen or layperson rather than a specific demographic. Thus, access to digital life data using GDPR became the context for Case Study Two, which is introduced in more detail in [Chapter 5](#chapter-5). Initially, I designed a study in this space which would allow exploration of both sides of the GDPR relationship, by working with my University's Data Protection Office and having students or staff (including myself) request their own data while also conducting interviews with those staff who would handle those requests. This study was approved by the University's Ethics Board but had to be cancelled as a result of changing working practices and increased staff workload at the start of the COVID-19 pandemic. Unfortunately therefore this context was not able to be explored from both sides of the GDPR relationship; nonetheless it was still considered a very useful research context, and Case Study Two was designed—which, after carrying out GDPR requests of my own as sensitisation, would take 10 participants on a journey of exploration of their own personal data and service provider relationships. Post-SILVER project, new opportunities arose for myself to take on an embedded role first in BBC R&D's personal data locker project, and later in Hestia.ai's _digipower_ project. These two external projects were also embedded in the same research context, enabling something closer to a multi-perspective exploration of this research context than Case Study Two would have allowed by itself. These project activities are detailed in [Section IV](#section-iv).

In both Early Help and GDPR research contexts, a variety of preliminary activities and preparatory activities were carried out to ensure full sensitisation and to validate existing understandings and research study designs prior to the start of the primary Case Study workshops and interviews. These are described in [4.3](#4.3), [5.2](#5.2) and [3.4.5](#3.4.5).

This section will now continue with Chapter 4, which describes the Early Help context and Case Study One, before concluding with Chapter 5, which describes the GDPR context and Case Study Two.

Case Study One: Access to Civic Data in Early Help {#chapter-4}
==================================================

> _"If you can see the invisible, then you can see the possible and provide the opportunities for trust, commitment and ways of empowering others to manage their past, present and future."_
>—Ken Wyatt (Australian politician, teacher and equal rights campaigner)

<span class="editnote">add callbacks to early on, making clear how it relates back to my lit review chapter esp wrt HDR and HCI</span>
<span class="editnote">add reflections on process of feedback between industrial experiences, development of HDR framework as that is why you approached problems the way you did. </span>
<span class="editnote">other changes per notes</span>
<span class="editnote">add forward refs where useful</span>
<span class="editnote">make stronger references to Design, and talk about what is feasible / implementable</span>

This chapter describes Case Study One, which involved four 2-hour participatory co-design workshops with local authority support workers, parents and children from supported families involved with _Early Help (EH)_ programmes [see [Section II Introduction](#section-ii-research-contexts)]. Its objectives were to understand family and staff attitudes to civic data holding (RQ1 [[3.3.1](#RQ1)]) and to explore the role of data within the support relationship (per RQ2 [[3.3.2](#RQ2)]). A model of _shared data interaction_, was explored, where supported families would interact with data together with their support workers.

Section [4.1](#4.1) explains the EH context in England. [4.3](#4.3) brings together prior findings from the pilot study [[4.2.2](#4.2.2)] and SILVER [see [Section II Introduction](#section-ii-research-contexts)], and explains how these understandings were used in sensitisation to establish a common ground for participants. [4.4](#4.4) reports qualitative thematic findings: that families want to be given a voice [[4.4.1](#4.4.1)], that trust can be earned through data and process transparency [[4.4.2](#4.4.2)], and that families need _meaningful_ data interaction [[4.4.3](#4.4.3)]. [[4.5](#4.5)] discusses these findings in the context of prior literature, focusing on the value of data involvement [[4.5.1](#4.5.1)], the need for human interaction [[4.5.2](#4.5.2)], and the pros and cons of the shifting of the _Locus of Decision Making (LDM)_ towards the family [[4.5.3](#4.5.3)].

Context: Data Use in Early Help{#4.1}
-------------------------------

### Data-centric Family Intervention in UK Social Care{#4.1.1}

The UK's social care system has been shaped by a series of efforts to improve the lives of children through data-driven interventions: _Every Child Matters_, _ContactPoint_, and the _Common Assessment Framework (CAF)_ [@everychildmatters2006; @gheera2011; @caf2012; @cornford2013]. These interventions later took a broader family focus [@wilson2011; @malomo2017] through programmes such as _Think Family_  which focused on _family intervention_ [@cornford2013; @parr2016] as a primary approach. Social workers learn about and get directly involved with the lives of targeted young people and their families in order so that they might overcome specific difficulties.

2012 saw the introduction of the _Troubled Families Programme (TFP)_ in England, which argued that £9 billion of civic spending was due to just 120,000 families and thus these families should be _'turned around'_. Local authorities had to identify _troubled families_[^6]—those _'at risk'_ families experiencing multiple issues from a list including unemployment, overcrowded housing, poor education, mental health issues, disability, low income, poverty, truancy, crime and domestic violence. For each family where impact could be proven, funding could be reclaimed from central government [@bate2018]. This encouraged extensive collection and use of data about each supported family to track and demonstrate progress and impact.

This shift towards using data mirrors the societal rise of data-centrism [[2.1](#2.1)], but also a wider public sector trend: Pressed to to demonstrate performance and deliver measurable, consistent results, human services including social care, health care and education have all prioritised the collection and use of data about their clients or service users. This use of data by the state to represent and think about families is considered problematic [@cornford2013; @barbosa2018], as records can include both objective facts as well as subjective information such practitioners' observations or numerically-quantified measurements of risk. This increases risks of inaccurate data or unfair judgement. Individuals typically have limited access to verify this data. While families can ask about their data, few do, and the service organisations become de-facto _gatekeepers_ to family data [@corra2002]. The situation has exacerbated as data-driven approaches to family care have been encouraged through policy and reports about improving quality of the sector [@bate2018; @dfe2018; @field2010; @ofsted2015].

[^6]: The term 'Troubled Families', popularised by the TFP, has fallen from use, as it was considered to be negative and judgemental. A latter term 'vulnerable families' has also been criticised for being disempowering. Most councils now refer simply to 'families' or sometimes 'supported families', and the rest of this thesis adopts this convention.

### Current Practice: Early Help Case Records as a Source of Truth{#4.1.2}

Through the 2010s, _Early Help (EH)_ programmes became a key social care offering from most UK local authorities, aiming to intervene in families' lives before costly additional help is needed. To meet the proof requirements of TFP, new processes were established. Support workers would now carry out an _Early Help Assessment_ (a guided enrolment questionnaire) to create an _Early Help Record_ for each supported individual and their family, stored in case management or _eCAF_ systems supplied by companies such as CareFirst and LiquidLogic. To gain a holistic perspective of a family's situation, a process of information gathering and family-centric inter-agency collaboration is adopted. The record is supplemented on a periodic basis by data from other agencies. Through contact with local authorities as part of its work, the SILVER project [see [Section II Introduction](#section-ii-research-contexts)] learned that such data is collected ad hoc, via emailed spreadsheets, phone conversations, and in-person meetings. One such meeting is the _Team Around the Family (TAF)_ – a bespoke grouping with representatives from other agencies such as police, schools or housing agencies. EH data is used to measure family progress relative to the CAF [@caf2012].

Support workers are encouraged to use data as evidence at all stages. A 2015
Ofsted report recommended further evidence-centric standardisation to address inconsistencies and deliver better care [@ofsted2015], triggering the transformation of EH into a data-driven service, where professionals seek more and more data about 'at risk' individuals. This belief that better data can drive better care is baked into national policies:

> _"IT systems are most valuable when practitioners use the shared_ [between agencies] _data to make more informed decisions about how to support and safeguard a child."_—@dfe2018

The technical reality of pursuing data sharing in cared is problematic. The information ecosystem is vastly complex [@copeland2015] with each part of the system having its own ICT arrangements. Teams work in isolation, using different systems and apps. Limited arrangements are in place to facilitate information sharing between data-holding authorities (which can include local charities to which care services are outsourced). Administrative boundaries differ for different authorities and agencies, complicating matters further. With each local authority procuring their own IT systems in the absence (despite recommendations [@harbird2006]) of any centralised systems or information sharing standards, the ecosystem has become severely fragmented.

Support workers face barriers to accessing needed data. Care workers can rarely access health data from GPs and have to rely on school nurses, health visitors, or the individual's own word. Information is often shared informally through telephone conversations, meetings or emails, not supported by technical integration. No one team, agency or authority can have a full picture of an individual's data [@malomo2017]. Different operating policies, consent agreements, privacy regulations, technical access levels, system functions and staff competences result in different interpretations that further limit what data is shared [@malomo2017]. Data should flow freely through the system in the service of individual care, but it does not. The public sector has a closed and fragmented ecosystem [@pollock2011].

Processes such as TAF meetings and the attempt to unify all information onto a single EH record can be seen as a recognition of this failure in the system to produce a single source of truth or understanding of individuals from a 'whole life' perspective. Attempts to create and expand the EH record as a central representation of truth about the family can be seen as data-centric solutionism [@morozov2013], being applied to a problem that was created by a data-centric approach in the first place.

### Rethinking the Role of Data in Early Help Support Relationships{#4.1.3}

Families' only awareness of EH data occurs when support workers or TAF professionals choose to share elements with them. Such sharing is usually verbal, unrecorded and rarely complete. Critiques suggest the acquisition of additional data consolidates power in practitioners' hands and undermines the families they are meant to be supporting [@neff2013; @white2010; @crossley2017tfp]. The scattering of data across so many different systems and organisations, combined with informal processes for sharing, presents serious risk of privacy breaches or mishandling of people's personal data.

Consent may be violated if data, collected for a specific purpose, passes to another authority for some new purpose without explicit consent. The idea that the EH record is a source of truth risks disempowering families further, countering the empowerment goals of the programme itself. Erroneous data is likely, and this may cause prejudice or unfair decisions being made against families. Individual privacy could be violated, or individuals put at risk, if a domestic abuser or criminal gained access to the data. The failure of such systems to properly represent families [@cornford2013] produces further risk. Information shared by one individual in confidence could easily be seen by another family member, with potential severe psychological consequences, such as an adopted child finding out in the wrong way that they are adopted.

Data is not neutral [@gitelman2013; @neff2013]. Collecting data for a specific purpose (rather than objectively) undermines local professionals' ability to deliver care [@cornford2013; @lowe2015]. The collection and use of data may, instead of helping a family, reinforce the existing asymmetry of power that exists between them and data-holding organisations [@cornford2013].

This presents an ideal context to explore RQ2 [[3.3.2](#RQ2)], specifically the impact of data use upon service relationships. Following preliminary sensitisation research [[4.3](#4.3)], a study was designed to work with both families and support staff involved in EH. This study examined individual perspectives per RQ1 [[3.3.1](#RQ1)] but also looked at the power imbalance and the effectiveness of the support relationship as a whole, in terms of its goal to empower families to build better lives for themselves and get them to a point where they no longer need support. As part of RQ2 [[3.3.2](#RQ2)], the study also explored possible alternative models for the use of data within EH relationships. The design and approach of the study is described in more detail in the next section.

Activities and Methodology for this Context{#4.2}
-------------------------------------------

Within this context I carried out three research activities between 2017 and 2019:

### Embedded Research and Development Placement in CHC's SILVER Project{#4.2.1}

From March 2017 to March 2019, I joined Connected Health Cities' _SILVER_ project [@ConnectedHealthCities2017silver] as a part-time research engineer alongside my PhD. This research project was funded by the UK's Department for Health (now the Department of Health and Social Care) and brought together local authorities, health authorities, University researchers and technology partners in the North East of England, in the Early Help context. Its goal was to explore how to unify civic data about a supported family, with their consent, to allow support workers to provide better care to those families. This made it an ideal place to explore my research objectives. It used direct research with families and support workers to inform the system requirements. This also provided an opportunity to deepen understanding of the use of data within Early Help support relationship (RQ2), and both parties' attitudes to this highly personal and real civic data (RQ1). My role was two-fold: as a software engineer, to design and develop user interfaces that would be used to view this unified data, and as a participatory researcher, to assist with the design and execution of focus groups and workshops with staff and supported families that could inform the proof-of-concept data system being built. It is that work as a researcher that forms part of the Case Study in this chapter. The embedded development work is not considered part of this Case Study, but rather as the first embedded research setting [[7.2OLD](#7.2OLD)] and will be referenced in the subsequent chapters, especially Chapters [4](#chapter-4), [8](#chapter-8) and [9](#chapter-9). The final report from the SILVER project was not published but a public summary is available [@NorthernHealthScienceAlliance2020].

### Pilot: Understanding Family Civic Data Study{#4.2.2}

In the summer of 2017, in the MRes year of this doctoral training programme (alongside my involvement with the SILVER project), I carried out an initial participatory field study in order to deepen my understanding of data use and attitudes within this context and to develop appropriate research methods. This study consisted of home visits to four different families in the North East who had interacted in the past with social care & support services [[Table 3.1](#table-3.1)]. During the course of these two-hour visits, I carried out participatory co-design activities and interviewed the families (both adults and children) about their civic data, and in particular their views on how risky different types of data were and how that data should be handled. Fieldwork took place prior to the start of this PhD; however, the data analysis and publication of the findings took place within the scope of this PhD, and directly inform the main Case Study, both through its methodology and as prior work to build upon. This pilot study is given special status in this thesis (as described in [1.3.1](#1.3.1)) and was published as a first author paper [@bowyer2018family], included in full in [Appendix A](#appendix-A).

Within the four pilot study home visits [see photograph in [Figure 3.8](#figure-3.8)] the following activities were carried out:

- 'Family Facts' Sensitisation [[3.4.1](#3.4.1)]
- Data Card Sorting [[3.4.2](#3.4.2)]
- Discussion stimulated by Example Data, News Articles and Interface Mockups

### Case Study One Workshops: Data Interaction in Early Help{#4.2.3}

In the summer of 2018, informed by the SILVER project and the pilot study, I designed and conducted my first major case study of this thesis: a series of four participatory co-design workshops with people directly involved in _Early Help_ relationships in North East England. The workshops were funded by CHC, and were led by myself. They were designed with a dual purpose: to inform the design of the SILVER system but also to serve RQ1 [[3.3.1](#RQ1)] and RQ2 [[3.3.2](#RQ2)] of this thesis. These workshops sought initially to validate findings from SILVER's earlier research and my pilot study.

The study comprised two phases:

  - First in phase 1, to work with families and support workers as two distinct groups, to identify their different needs [[Table 3.1](#table-3.1); [4.3.5](#4.3.5)],
  - then, in phase 2, to work with both groups together in an attempt to address their unified needs through novel approaches to data interaction.

The objective for Phase 1 was to develop a deeper understanding of what supported families (workshop A) and support workers (workshops B1 and B2) perceive as problems with data use in the Early Help context, and to explore perceived solutions to these problems. Phase 1 served to revalidate earlier findings of early work, working with each group separately. A further objective was to understand existing data practices and whether they work, or need improving, and to identify known issues.

A second phase workshop (workshop C) was designed to specifically focus on the use of data _within the support relationship_ [[4.3.4](#4.3.4)]. This was a joint workshop involving staff and parents working together to explore the _Shared Data Interaction_ concept that emerged in Phase 1 [[4.3.4](#4.3.4)]. In Phase 2, the two groups would collaborate to design imagined data practices and interactions. The objective was to understand how _in practice_ staff and families could imagine themselves using data together.

Across both phases, various participatory methods were used, as detailed below. Workshops were audio recorded and transcribed. Transcripts were analysed thematically, and in some cases quantitatively [[3.4.5](#3.4.5)]. Thematic findings are documented in [4.4](#4.4). This Case Study's findings are documented in this chapter, but also contribute to the general findings about RQ1 [[3.3.1](#RQ1)] and RQ2 [[3.3.2](#RQ2)] presented in [Chapter 6](#chapter-6). The workshops are summarised in Table 4.2:

| <a name="table-4.1">Workshop</a> | Engagement | Phase | Number of Participants |
|:---------:|------------------|:--:|----------------|
| Workshop A | Design Workshop for Families | 1 | 8 adults and 9 children from 5 supported families |
| Workshop B<br/>(2 instances) | Design Workshop for Staff | 1 | 36 support workers & related staff (in total) |
| Workshop C | Combined Staff and Parents' Design Workshop | 2 | 3 support workers and 4 parents from supported families |

Table: Table 4.1 - Case Study One Group Design Workshops.

Within the workshops, the following activities were carried out:

**Phase 1: Co-Designing Civic Data Access for Early Help**

_Workshop A (Co-designing with Families):_

- Data Card Sorting [[3.4.2](#3.4.2)]
- Sentence Ranking [[3.4.1](#3.4.1), [4.3.5](#4.3.5)]
- Ideation Decks [[3.4.3](#3.4.3)]
- Poster Design [[3.4.3](#3.4.3)]
- Scenario Discussions [[3.4.2](#3.4.2)]

_Workshops B1 and B2 (Co-designing with Staff):_

- Sentence Ranking [[3.4.1](#3.4.1), [4.3.5](#4.3.5)]
- Ideation Decks [[3.4.3](#3.4.3)]
- Poster Design [[3.4.3](#3.4.3)]
- Scenario Discussions [[3.4.2](#3.4.2)]
- Discussion of Interface Mockup [[3.4.2](#3.4.2)]

**Phase 2: Exploring Shared Data Interaction**

_Workshop C (Combined Parent/Staff Workshop):_

- Sentence Ranking [[3.4.1](#3.4.1), [4.3.5](#4.3.5)]
- Storyboarding Training [[ARI4.3](#ari-4.3)]
- Scenario-based Storyboarding [[3.4.3](#3.4.3)]

The next section goes into more detail into how the preliminary work with the pilot study and SILVER established a baseline for families' and support workers' attitudes to civic data use and access. Section [4.3.5](#4.3.5) details the commonalities and discrepancies in attitudes between the different participant groups, including details of how these baseline attitudes were validated and captured using the Sentence Ranking method.

Preliminary Explorations of Family Civic Data: Families' and Support Workers' Perspectives{#4.3}
-----------------------------------------------------------------------------

The first step in study design was to achieve sensitisation [[3.4.1](#3.4.1)] as a researcher, specifically three ways:

  - to understand what data is stored about families [[4.3.1](#4.3.1)];
  - to understand the family perspective [[4.3.2](#4.3.2)]; and
  - to understand the support worker perspective [[4.3.3](#4.4.3)]

### What is Family Civic Data?{#4.3.1}

In order to communicate effectively with participants, an understanding of what data is held in an EH context was needed. Through the pilot study [[4.2.2](#4.2.2); @bowyer2018family; [Appendix A](#appendix-a)] and a grey literature review within CHC's SILVER project [see [Section II Introduction](#section-ii-research-contexts)], a taxonomy of _Family Civic Data_ was established [@bowyer2018family], as shown in [Table ARI4.1](#table-ari4.1).

Early recruitment attempts revealed that data is seen as an abstract concept in people's daily lives—a dry, technical topic that many families felt unqualified to talk about. The concepts needed to be made relatable. Drawing on the work of Brandt and Messeter [@brandt2004] in creating _design games_ (which observes that game pieces can be used to create common ground and as _things to think with_ [@brandt2004; @papert1980], a set of _data cards_ [[Figure 3.7](#figure-3.7)] were created. These cards made family civic data categories visual and tangible. Serving as _boundary objects_ [@bowker2016; @star2010] the cards aimed to bring researcher and participants' worlds closer together, and to make data relatable to life experience. The design approach for the data cards is documented in [[Appendix A](#appendix-a); @bowyer2018family].

The cards were used as research stimuli [[3.4.2](#3.4.2)] within the pilot study, which involved participatory design activities and design games in family homes. Once families understood data as _stored information about their lives_ they were able to very effectively engage and talk about it. The use of the games and the cards was very successful, keeping a light and playful environment and making the topic relatable. The cards enabled families to talk freely about their own lives and views without feeling personally interrogated, as they were dissociated from the participants' lives.

### What is the Family Perspective on Their Civic Data and its Use?{#4.3.2}

Families participating in the pilot study and in SILVER's early research cared very much about what happened to their civic data, contrary to peers' expectations. They perceived a variety of risks due to data mishandling including identity fraud, criminal targeting and psychological harm. Families felt that data could easily misrepresent them through errors, prolonged storage of data beyond its need, or the recording of unfair judgements and opinions. Families wanted to view the data stored about them. They wanted a set of basic rights—to be informed, involved and accurately represented, with the ability to see, explain and correct their data to ensure it is fair and accurate. They wanted to know that their data will be handled sensitively and only by those that need to know. They believe that having such capabilities would help them to be able to work together with representatives of the state in a more positive relationship.

The SILVER project [see [Section II Introduction](#section-ii-research-contexts)] conducted qualitative interviews with EH-supported families, and unpublished findings from these interviews reinforced the need for a more consultative role for families in data handling. Participating families identified that while there was a willingness to consent to information being shared in order to improve their care, they had very little understanding of how it was used and could not be deemed to have given informed consent to the way their data is currently used.

### What is the Staff Perspective on Family Civic Data and its Use?{#4.3.3}

SILVER worked closely with local authority staff, providing an understanding of support worker and staff perspectives. SILVER conducted a series of 'Amy's Page' [@wilson2020] focus groups/workshops with support workers and other local authority representatives, where staff mapped out information needs. They desired greater access to health information, particularly mental health indicators. The participants revealed a desire to gather as much data as possible about the families they were working with. It was viewed as a useful raw material that enabled them to do their job better.

Collectively, findings from the pilot study and from SILVER showed a conflict between the desires from families and support workers. Families wanted more involvement and less reduction to data. Support workers wanted to amass more and better data. In part due to its funding and what I would consider _solutionist_ [@morozov2013] framing, the SILVER project gave priority to the support worker perspective as key requirements. It continued to pursue the building of a richer data interface for support workers. At this point, my research objectives and those of the SILVER project diverged. I was not ready to 'take sides' nor to pursue a purely data-centric solution. I wanted to explore whether it might be possible to satisfy the needs of both parties and to maintain focus on human-centricity and the need for a balanced relationship.

### Shared Data Interaction: An Equitable and Mutually Beneficial Data Use Model{#4.3.4}

In attempting to reconcile the conflicting desires of families and support workers, **Shared Data Interaction** was conceived. What if, instead of workers gatekeeping data access and using it by themselves, data could be looked at, examined, and updated together, during the face-to-face encounters between families and their support workers? This could potentially bring the benefits of HDI (increased agency, negotiability and legibility) [@mortier2014] to families (and also to workers), while also serving as a boundary object that might improve the relationship itself [@bowker2016]. I theorised that this would allow families to access unseen data while also enabling support workers to 'fill the gaps' in the data by simply asking questions.

This concept emerged in part from phase 1 participants in the research engagement, and became a main focus for the second phase. In this regard, the workshops would not only explore current practice, but also motivate participants to imagine new practices that could serve their needs better. This would allow a preliminary assessment of shared data interaction—whether it might address both groups' needs and whether it would be perceived to benefit the support relationship. Even if the model was not well-regarded, such an exploration would still help to put participants in a speculative, co-design mindset that could elicit deeper insights about how civic data _should_ be used.

### Sensitising Participants and Discovering Shared Values{#4.3.5}

In all workshops, it was important to ensure participants arrived at a common understanding of their 'design brief'. To achieve this, and to validate if these participants' perspectives matched those observed previously, an activity called _Sentence Ranking_ was conducted. Participants considered a number of opinionated statements and ranked them according to:

 - (a) whether they agreed, disagreed or were neutral on that statement, and
 - (b) whether or not they felt that statement was important.

An example statement is:

> _'Families should always be able to talk to someone about their data.'_

The complete list of sentences is in [ARI4.2](#ari-sentences). These sentences were collated from family and staff perspectives observed during the pilot study, in SILVER's research engagements, and from researcher observations from the SILVER project [see [Section II Introduction](#section-ii-research-contexts)].

Through discussing and reaching consensus on these opinions, families and staff would be in effect _agreeing requirements_ that could inform their thinking during design activities. By conducting this same activity across all participant groups and across both phases, this would also allow comparison between the different groups, to identify differences and find shared values.
Within each workshop, groups of participants sat at tables of 4 to 6 people, and each table provided its own sentence rankings.

The resultant rankings were analysed as described in [ARI4.2](#ari-sentences). The visualisation of these findings on shared values is shown in [Figure 4.1](#figure-4.1).

As the figure shows, there was universal consensus that:

- families should be able discuss their data with someone from the authorities,
- public sector officials cannot make good judgements solely by looking at families' data,
- data cannot adequately represent a family,
- families should be treated as more than just what their database record says,
- information stored about them must be fair and accurate,
- families must have rights to see it and how it is used, and that
- support workers really need to know mental health details of family members.

Participants felt it important to address that current consent practices were inadequate. There was also strong consensus that families did not want to be responsible for looking after their own data, though this was felt to be an unimportant matter.

Participants showed considerable contention over whether or not support workers should be able to access historical family records [[4.4.3](#4.4.3.1)], about how families would feel about the collection of data about them and about having responsibility to managing access to it. There was moderate consensus over most other sentences.

![Figure 4.1 - Participants' Shared Values Deduced from Sentence Rankings Data](./src/figs/fig4.1-sentence-ranking-results.png)

After this exercise, participants were considered sensitised and went on to carry out the other co-design activities [[Table 4.1](#table-4.1)]. Transcripts of these activities were analysed to produce thematic findings, which are detailed in the next section.

Thematic Findings{#4.4}
-----------------

The 120,000-word corpus from audio recordings of workshops A, B and C was divided by activity, group, and family/staff focus into 85 different source texts. Each text was thematically coded. The coded texts were analysed through four cycles of analysis [@huberman2002]. During this reductive process, participant creations, activity outputs and ranking data were referenced for context. Results of the thematic analysis are presented below. In [4.4.1](#4.4.1) the three main themes and subthemes are introduced. Each theme is detailed in [4.4.2](#4.4.2) to [4.4.4](#4.4.4), including participant quotes. Notation for quotes is explained in [ARI4.4](#ari-quote-notation).

### Themes & Subthemes{#4.4.1}

Since workshop discussions were framed as explorations of data use within the EH relationship, thematic findings are expressed as desirable best practices. These best practices are divided into three themes:

  1. Meaningful Data Interaction [[4.4.2](#4.4.2)],
  2. Giving a Voice to the Family [[4.4.3](#4.4.3)], and
  3. Earning Trust through Transparency [[4.4.4](#4.4.4)].

Explicit and implicit statements from participants, contextual clues, and accumulated knowledge allowed a judgement to be made as to whether each discussed best practices was:

- commonly in use ('current'),
- happening occasionally/partially ('emergent') , or
- not yet occurring at all ('imagined')[^7].

Tables [4.4](#table-4.3), [4.5](#table-4.4) and [4.5](#table-4.5) show subthemes, illustrated with participant quotes, as well as the current, emergent or imagined status of each subtheme. Structuring the themes makes the findings actionable for social care organisations.

[^7]: As judged at the time of the workshops—Summer 2018.

| <a name="table-4.2">Subtheme</a> | Description & Quote | Status |
|:--------|:-------------------------------------------|:------:|
| Understandable Information Summaries|To maximise understanding, simple summaries of the information within families' data should be available to both families and support workers. Visualisations should be used to ease comprehension, and information should be contextualised at different levels (individual, family, community).<br/><br/>_'There's so much data that's stored. For me, for a parent [I want] to understand that through a text or email but just in point form. […] The less written, the better for the parent. [What we need is] a small synopsis […] like a summary view.'_ [Parent, SQ44]<br/><br/>_'Some families will go, "Well you know that information because it's all there somewhere." We're like, "Yes, but we don't want to trawl back to eight years ago." There's reams and reams and reams of it [data].'_ [Worker, SQ40]|Emergent|
| Interact with Data Together|Support workers should work to actively counter the knowledge imbalance by informing families what their data says. They should make use of specific datapoints as talking points to aid planning conversations.<br/><br/>_'You could have a table, you'd look at where they are and where they could be. [You could say] "This is where you are now but if you [take these specific steps], even though you've got a criminal record, you could progress to this level."'_ [Worker, SQ29]|Emergent / Imagined|
| Direct and unified data access|Individuals should be able to directly access their civic data through a personal interface; this should be a single, common place where all of an individual or family's data is brought together to give a complete and consistent overview to all parties with a need to know.<br/><br/>_'[I'm imagining an] online database of personal family info accessible [only] by people, practitioners that have permission […] I would say that it's only who you want [to give access to, that can see it]. You would have your private code which you could hand out, like the doctors give you appointments.'_ [Parent, FQ8]|Imagined|
| Ongoing Data Access and Support|It is not sufficient simply to give access to data. Families should be able to access information in their own time and should be supported in understanding it. Most importantly they should be able to ask questions, challenge data records or start a conversation to discuss their data at will.<br/><br/>_'[The families would have] a little app which they can log into and read all their information - what's recorded about themselves, […] who we share the information with […]. If they're not happy […] they can fire off an email to us and let us know what they disagree with or if they want their information taken down or their consent.'_ [Worker, SQ51]|Imagined|

Table: Table 4.2 - **Theme 1 - Meaningful Data Interaction for Families**. Subthemes & Participant Quotes.

| <a name="table-4.3">Subtheme</a> | Description & Quote | Status |
|:--------|:-------------------------------------------|:------:|
| People not Records|Support workers must always treat people like individuals, that are more than a data record. They should review family data before contact, but must always engage at a human level too, avoiding making any judgements based solely on data.<br/><br/>Worker A: _'You should never make a judgement on data… that data could be wrong.'_<br/>Worker B: _'It takes individuality, working with that person as well, doesn't it?'_ [SQ11]|Current / Emergent|
| Checking Data Together|Families should be explicitly invited to review, discuss, check, correct and approve data records. Data recording should be visible, and workers and families should check data together.<br/><br/>_'[The parent could] countersign. [The worker would] say, "I feel that we've talked about this today so I'm going to write that down. I'm going to show you. Can you sign and me sign if you're happy and I'm going to share this." That's a bit [better].'_ [Parent, FQ12]|Emergent / Imagined|
| Changing Lives Means Changing Data and Changing Consent|Recognising that families' lives are in constant flux, routine reviews of data should occur, and they should be invited to regularly review their choices regarding data collection, keeping and sharing. All systems and processes should treat data as fluid and flexible, not static unchanging facts. Feeds of recent changes should be available to both parties.<br/><br/>_'[There's] this perception of something sticking with you even after you've potentially reformed. […] That's something that happened a long time ago and that judgement is still there but [you'd be wondering] "Okay, is it [true]?"'_ [Worker, SQ61]|Imagined|
| Individual Agency & Family-sourced Data|Individuals should be able to create or contribute their own data to tell their own story and annotate particular datapoints with their own explanations.<br/><br/>Worker A: _'If you read information […] about me, you wouldn't expect to meet the person you meet.'_<br/>Worker B: _'That's it. It's the same for everybody.'_<br/>Worker A: _'[…] It just [has] basic things in most of the time, doesn't it […]? You're not a person [in the data record] are you really?'_<br/>Worker B: _'[I'd like it if you could] give your bit of personal data, your own story.'_<br/>Worker A: _'Yes, because everybody makes mistakes and there's probably thousands of people out there who have got a criminal record and have never done anything since. [They're] getting judged by having one thing [but they should be able to write] "Yes, I did this because of this situation but this is what I've done to make myself [better]…"'_ [FQ10]|Imagined|
| Granular Access Controls|Families should be given controls to manage access to their data and configure and change preferences at a fine-grained level.<br/><br/>_'[Families need to] feel they're being involved. […] [We need to be able to] sit together and say, "Right, that's the information I'll allow you to share. I don't want that bit shared. But this bit, because it will help me and the family […]". Say in this [scenario] family, she might have been married before and had domestic violence so she doesn't want that bit shared, that's in the past. So, it's [only] certain up-to-date information about the family [that would be shared] because this [the family suggested by the data] isn't her family.'_ [Parent, FQ16]|Imagined|

Table: Table 4.3 - **Theme 2 - Giving a Voice to the Family**. Subthemes & Participant Quotes.

| <a name="table-4.4">Subtheme</a> | Description & Quote | Status |
|:--------|:-------------------------------------------|:------:|
| Transparent, Respectful Data Handling|Support workers should treat families' data with the utmost respect, keeping it safe, ensuring it is not used beyond its intended purposes, shared without consent or put at risk. When talking to families about data, it is helpful to focus on positives and strengths and not use it as a means to criticise.<br/><br/>_'There was a time where I was at the doctors' and they asked how many units of alcohol I drank, and I said, probably about three bottles a week, at the time, not any more but later on [the support worker] pulled me up on it and they had it down as three bottles a day. That could have caused an issue was anyone ever to ask.'_ [Parent, CQ7]|Current|
| Always Seek and Demonstrate Greater Understanding|Support workers should always assume that their understanding from data is incomplete and should seek to learn about individuals and build a more complete picture of their lives. By showing this effort and their growing understanding, they will engender trust.<br/><br/>_'You don't want to reduce them to this number in a database. You want to understand their actual experiences and support them in getting better.'_ [Worker, SQ74]|Emergent|
| Pro-actively Challenge Data-centric Norms|Support workers and agencies can recognise that current systems and processes are data-centric and imbalanced, and can strive to change this through their actions: being as open as possible about how families' data will be handled, ensuring that proper oversight mechanisms exist for data handling especially in the sake of contentious issues, and that data is shared openly but consensually between authorities. <br/><br/>_'It hasn't been explained property to this [scenario] family that their information will be shared with other professionals. So, they've been left feeling really let down and probably quite angry about it. So, although that information does need to be shared, they [the support workers involved] ought to make the family properly aware that information will be shared.'_ [Worker, SQ18]|Imagined|

Table: Table 4.4 - **Theme 3 - Earning Families' Trust Through Transparency**. Subthemes & Participant Quotes.

### Theme 1: Meaningful Data Interaction for Families{#4.4.2}

Through discussions with families and support workers a deep understanding of what sort of families' ideal data interactions was obtained. Setting aside interface considerations, which were not the main focus of the inquiry, and focusing on the wider sociotechnical context around the data and its access, it seems that in order to maximise understanding for all parties, data interaction needs to be _meaningful_—the first theme of these findings. Encompassed within this concept are:

  - the need for understandable and effective summaries and visualisations,
  - the need for direct and ongoing data access with human support, and
  - the recommendation for families and support workers to interact with data together within the support interaction.

<a name="4.3.2.1">**Understandable Information Summaries**</a>

Written summaries of information were independently considered to be critical for both parents [SQ44] and support workers [SQ40]. These could also be used as a mechanism to protect privacy, by keeping sensitive details hidden:

_'In that example, depression, ten year ago, that shouldn't be on there for the support worker. All they should get is if Social Services have been involved and it should just be, "Please contact for more information." […] [The system should stop workers from] getting a list of all the kids who have ever missed dental appointments or when you were depressed ten years ago. […] There needs to be a thing where it's, sort of […] key trigger words, where if the word comes up a lot of times, it spots the patterns. Whereas, if [a problem] is mentioned once, it should only be [shown] at the highest level.'_ [Parent, CQ10]

Because the amassing of large volumes of historical data is expected, families expect (though are not happy about it [FQ6]) that any aspect of their past life may be _findable_: _'We go to them and say, "We're aware that you've got these issues going on" […] and not one family I've ever met has said, "How on earth have you got that information?"'_ [Worker, SQ42]. Managing expectations can be problematic [SQ40] and some workers felt they should not be given greater data access, fearing greater liability to _'trawl through data'_ so that they know everything.

This need for summaries can also be seen an echo of Gurstein's call for _effective data use for everyone_ (@gurstein2011). It is not sufficient to simply open up public sector databases to allow individual record access; families need not just the opportunity, but the technology, skills, formatting, interpretation and sensemaking to make the access effective. Some individuals may lack _'proper access to a computer'_ [Parent, CQ9]. Data tables are insufficient and may need to be supported by visualisations: _'Some families might not understand [a data viewing interface]. They might not be technical… I think sometimes it's easier to do it in pictures.'_ [Worker, SQ43]. Participants suggested pie charts, graphs, spider diagrams and timelines [SQ30, SQ31] or even an audio interface for the visually impaired [SQ45] to aid understanding. Visualisations also need verbal explanations [CQ11].

It is not clear who could or should do the skilled knowledge work of creating these representative and accurate tailored summaries and visualisations.

<a name="4.3.2.2">**Interact with Data Together**</a>

Directly using data together within a support conversation is seen as a key element of making data interaction meaningful for families. For support workers, the use of data can form _'a way in'_ or conversation starter:

> _'[Showing the data could be] an ice breaker [with] a new case. So, "We've got this information; can you tell me more about it?" That opens it up, like a can of worms and it all just comes out; you know what I mean? Then you're able to have that open and honest conversation with them to see what level of support that they need.'_—[Worker, SQ28]

The showing of data performs an additional important purpose, combatting the lack of _awareness_ of what data exists and who holds it [SQ39]. Currently, much of the data stored about families is invisible to them: _'Families really only see the data that we [support workers] want to present.'_ [Worker, SQ37] Regardless of families' legal rights to request copies of their data, it seems this right is rarely used [SQ38], and typically only when filing complaints. Lack of awareness can not only cause suspicion [SQ17], but also incorrect assumptions that support workers _'already know everything'_.

Participants particularly recognise the value of referencing data points over time (such as a record of welfare scores that support workers have previously given them), for example to track progress [SQ29, shown above in [Table 4.2](#table-4.2)]. This could motivate and reinforce progress [SQ6] by relating behaviours to consequences [SQ32]–essentially facilitating data-based decision making. Reviewing historical data is preferable to verbal description: _'Whenever you go through stuff like that [verbally], especially historic stuff, they can be quite remote so [having the data in front of you] would be good for that.'_ [Worker, SQ33].

<a name="4.3.2.3">**Direct and Unified Data Access**</a>

Despite the reality that families currently have no direct access to their civic data, family participants all eagerly described designs including apps, intranet terminals, online chat facilities, and self-service webpages, all offering individuals the ability to view their own data; there is a clear demand for _personal data interfaces_, which could empower families to use their own data:

> _'They could quickly tap onto the app […] and show somebody else where they're at.'_—[SQ54]

> _'Our first [idea] is the lovely [child's name] has made an app. [It's] free to download, you can make your own password and there's going to be a button on it so you can press it and then query the information that's held on you straight away.'_—[Parent, FQ7]

Workers and families shared a desire for one single point of access for data, useable by all parties [SQ25, SQ26], though families _'don't want to be responsible for looking after all our data'_[FQ17, S5].  Bringing together data from multiple sources would allow patterns to be spotted by correlating data from different sources, which workers perceived would help their preparation:

> _'[This imagined interface] would provide individual histories but you could also pull them all together so you can prepare, so for instance if mum was having some significant issues with mental health, you might be able to correlate the [child's] school attendance alongside that and find out why that's happening.'_—[SQ8]

<a name="4.3.2.4">**Ongoing Data Access and Support**</a>

Families, being accustomed to accessing information in other parts of their lives through smartphones and web interfaces, expect that any civic data interface would allow them to access data _'in their own time, at their own pace'_ [Parent, CQ12]. Currently access only possible via the support worker, functioning as a _gatekeeper_ within the support interaction, so opportunities to reflect upon the data are limited in time and coverage:

> _'[If conflict occurs,] I would need to go away and seek some advice on what can happen next, but it could be useful for the family, to spend that period of time, perhaps looking at all the information and identifying what it is that they feel they're being judged on.'_—[Worker, CQ13]

Timely access to data could be empowering, as families could track their own progress, enabling them to make plans outside of the support relationship, reducing dependency upon support, in line with the ultimate goals of the programme:

> _'If we were working with a family about school attendance, could we then link that in to [the families'] app so parents [would be] aware of what their attendance looks like at this point in time and they […][could] monitor it themselves and take accountability.'_ [Worker, SQ49]

As well as having ongoing access to data, families need human support to understand that data [SQ49, CQ11]. All participants agreed that _'Families should be able to talk to someone about their data'_ [S7]. Explanations are needed [CQ11] with language and vocabulary adjusted to individual literacy [SQ46] or age [SQ47]:

> _'No matter which [presentation of data is offered], you'd have verbal context for it as well, wouldn't you? You wouldn't just go, "There's your app" or "There's your piece of paper" and leave them. You'd just talk it through with them anyway.'_-[Worker, SQ49]

Key to meaningful involvement is the ability to start a conversation. Groups imagined families being able to send a message [SQ51] or record audio to raise an issue for discussion, letting their disagreement be known and empowering them to be part of a dialogue about what is recorded [SQ60].

### Theme 2: Giving a Voice to the Family{#4.4.3}

The second theme  systems and processes currently rely excessively upon the 'facts' within the data record, and they need to be updated to give the family an empowered role within their civic information ecosystem. The purposes of an EH intervention are to obtain more information for a better understanding of the family's situation and to make evidence-based plans and decisions to improve the situation. Seeking objective truth is clearly central. Impressions of that truth can be formed either by reading the data or by talking to the family. There are benefits and dangers of relying solely on either source. Families should become agents in the data ecosystem, and this involvement should lead to both greater empowerment and better evidence-based decisions.

<a name="4.3.3.1">**People not Records**</a>

It was evident, consistent with literature (@gitelman2013) and the pilot study [@bowyer2018family], that data can never represent absolute truth - it is often biased or incomplete, and this can mislead [SQ59, FQ11A]. For example, a lack of mental health information could make an individual look like a poor parent [SQ12]. Families may be less willing to 'open up' if they feel they may be judged unfairly [SQ14]. Therefore, developing a strong relationship between worker and all family members is key to understanding the full picture [FQ1]; to ensure fairness [SQ77], data must be current and complete [SQ13], but this state can only be achieved with the family's cooperation. Looking at data will never provide support workers with a complete understanding. Yet, workers often _'tend to just trust that everything that has been put down is right'_ [CQ1], allowing the data perspective to dominate. Such assumptions should be avoided [SQ10]; processes must recognise maintaining human face-to-face dialogue as a priority. Data should only provide  supplementary insight: _'You should never make a judgement on data… that data could be wrong. It takes individuality, working with that person as well, doesn't it?'_ [SQ11]. All participants presented with the sentence _'Public sector officials can make good decisions just by looking at a family's data'_ [S18] disagreed with it.

In spite of the warnings above, the data record is undeniably useful; over 80 comments from workers contend the current practice of reviewing a family's data prior to meeting in person is beneficial, because it provides useful background that will help them identify support needs. For example:

> _'I had a family where trying to unpick what had happened, over ten years, to the child, was really difficult. So, I went away, got the information and came back and if you have_ […] _that picture of how the family works_ [when you meet them]_,_ [that helps]_.'_—[SQ1]

Additional benefits identified included safeguarding workers [SQ3] or giving them an ability to _'check the family's claims'_ so that they might constructively challenge individuals [SQ4]. Supported families echoed the value of workers reviewing data [FQ1A], and saw benefits included _'not having to repeat your story'_ [SQ5].

The compromise that participants identified over the use of data is that workers should avoid making judgements based solely on data. While sometimes providing essential background to a worker [FQ11B, SQ62], historical data in particular often leads to inadvertent prejudice, especially where labels are used [SQ9]. No participant disagreed with the sentence _'Labels like "domestic abuse" are damaging to families and hard to shake off'_ [S15], and workers recounted experiences of being uncertain how to judge historical issues:

> _'[There's] this perception of something sticking with you even after you've potentially reformed. […] That's something that happened a long time ago and that judgement is still there but [you'd be wondering] "Okay, is it [still true]?"'_—[Worker, SQ61]

Many participants concluded that only _'relevant'_ information should be available, to those who _'need to know'_, but the wide range of opinions expressed suggest that this is a highly subjective judgement that would be difficult to determine. A cut-off period before which workers should have no right to look was suggested [Parent, CQ15], but the sentence _'Officials should be able to see historical records about families'_ [S17] was contentious. Some workers feared any restriction in access might mean they miss important background on an individual's past, such as sexual abuse or mental health issues [Worker, SQ76]. The solution to this dilemma is unclear, but transparency about what is in the data would seem to be a critical ingredient [[4.4.4](#4.4.4)].

<a name="4.3.3.2">**Checking Data Together**</a>

The idea of families and support workers reviewing data _together_ arose from many participants in workshops A and B, and this motivated an exploration of the concept of shared data interaction in more depth through the storyboarding exercise in workshop C [[4.3.4](#4.3.4)]. Families perceived value in having not just data representations as above, but also a data interface present within their care meeting, so they that they could see actual data and have it explained to them. One practice embodying the concept of transparency that is emerging in some care services is the use of '2-in-1' devices (laptop/tablet hybrids) within the care engagement. Workers can then visibly record data in front of families and then ask them to _'approve'_ the accuracy on screen [FQ12, SQ67]. Participants believed this would help to build trust between the support workers and families; if a family begins to feel powerless, they may disengage [SQ35], but even minor involvement, such as this emergent practice of signing off approval of data records [FQ12] or an imagined process of checking & correcting data records together (see next section) could make families feel more empowered which could make the support relationship more productive.

Family participants imagined going beyond just seeing and getting verbal explanations of their data to being able to review their data and be asked for their approval of accuracy [FQ3]. Maintaining accurate data is important because that data is used to decide care plans and support strategies. Families are thought to be better placed than anyone else to identify inaccuracies or gaps in their civic data. Participants believe family corrections would increase data accuracy. This does not mean free editing of records (as, for example, fears and/or self-interest could lead to families misrepresenting themselves in data [@bowyer2018family]). Instead, taking a role in reviewing, annotating, explaining, or requesting changes, through direct data-centred collaboration between involving workers and family members is desirable:

> _"_[There would be an] _individual view where each person within the family would have their own section_ […] _you could sit with them_ […] _and go through the data that we have got which would enable them to change anything that they want taken out."_—[Worker, SQ66]

Shared data interaction carries the potential to bring benefits in accountability, accuracy, simplicity [SQ25, SQ26] and consent.

<a name="4.3.3.3">**Changing Lives Means Changing Data and Changing Consent**</a>

One reason for reviewing historical data and for requiring dialogue with the family to gain an up-to-date picture, is that the truth changes over time. People are not static, and families' lives are always changing; given marriages, divorce, birth, death, house moves and other changes, data can become out-of-date simply through inaction. Given this, asking consent once at the start was considered insufficient [S3]. Data is inherently static – it does not change, but people do [SQ61, SQ63]. This was the basis for participants' desired practice that not only the content of the data, but the family's consent over what happens to that data that both need to be reviewed regularly [CQ16]. A process of regular reviews around data use could prevent unwelcome surprises about how family data is handled [CQ2, CQ17] which could damage trust and hinder co-operation. Participants imagined data systems issuing notifications or update feeds for families and support workers showing significant events or data updates [SQ64]. Support workers currently get notified of police incidents, safeguarding concerns and hospital admissions, but alerts of data changes across the care ecosystem could provide useful triggers for reviews or discussions:

> Worker A: _'We would get a report through to say…'"_
> Worker B: _'They've recorded something.'_
> Worker A: _'Yes. Then I suppose we would follow it up […] face to face.'_—[SQ65]

Regardless of the particular mechanism, it was ultimately felt that both data systems and support processes need to do a better job of supporting change.

<a name="4.3.3.4">**Individual Agency & Family-sourced Data**</a>

The idea of families reviewing data has significance not just for how it can help within the support interaction, but because it can give families an independent role in their data ecosystem. Both families and support workers imagined the family being able to interact with their civic data on their own, something that is currently not possible. This is a vital step for empowerment: if something goes wrong, families must be able to discover this and must be able to do something about it. Without a cycle of feedback involving individuals as stakeholders having the ability to review and correct data, data will quickly become inaccurate (Pollock, 2011). Thinking about data interaction at home unlocked additional thinking, such as families helping to fill gaps in data [SQ57] or contribute new data that may not otherwise be recorded [SQ58]. Giving families the ability to contribute new data would empower them to _'tell their own story'_ [FQ10]. Many participants saw this as-yet-unavailable capability as expected common sense:

> _'I just generally want to see [what is stored about me] just to know what people are saying and then obviously if it's wrong, I can correct them on it.'_ [Parent, CQ14]

Rather than solely relying on dialogue, families could provide new data more directly, e.g. through a 'family network app', which could also increase their sense of data ownership:

> _'It would [ask them] who [professionals the family is involved with] they could name outside of their family to create a network. […] But it would collect more than that, […] it would allow the family to be accountable for their data collection and making sure that it's accurate […] because we often go away and record it all on [our existing database] and it's our story rather than their story of how the events occurred.'_ [Worker, SQ36]

With new ways for self-expression, families could add context for support workers [FQ9, SQ55], unlocking new support topics [SQ56]. The overriding sense from both groups was that families having the ability to annotate or explain their data would allow them to hold authorities to account, and empower them to tell their story and _'show the real me'_, as illustrated in [FQ10, shown in [Table 4.3](#table-4.3) above].

<a name="4.3.3.5">**Granular Access Controls**</a>

Participants identified that it is important to consider that different individuals within the family would have different roles, access and summaries, in order to respect individual privacy [SQ52, SQ48]. Psychological harm could be caused through information leakage, for example an adopted child finding out their true parentage (@bowyer2018family). To avoid this, data should be managed carefully with consent being less binary and more fine-grained access controls being offered:

> Worker A: _'When a child turns 16, when they go to the doctors, is that confidential between me and my GP or can my parents see that?'_
> Worker B: _'I think it's confidential.'_
> Worker A: _'Exactly. So in this interface, I [would be] able to see that – [as the] 16 year old - you as my support worker could also, but not my mother.'_—[SQ53]

Once such capabilities are established, this could enable much more careful and deliberate forms of data-sharing which could support the creation of a personal data ecosystem [[2.3.4](#2.3.4)] beyond, but centred upon, the individual family member, all the while remaining under that individual family member's control:

> _'[I'm imagining an] online database of personal family info accessible [only] by people, practitioners that have permission […] I would say that it's only who you want [to give access to, that can see it]. You would have your private code which you could hand out, like the doctors give you appointments.'_—[Parent, FQ8]

Theme 2 shows see that giving families a role in the creation and stewardship of their data selves may unlock new capabilities and a sense of empowerment for families.

### Theme 3: Earning Trust through Transparency{#4.4.4}

The third theme looks at these imagined new data access capabilities and empowered role for data subjects in the wider sociotechnical context of how they could affect the support relationship. The topic of trust arose directly or indirectly in almost all participant conversations, and the findings show that transparent and open data handling and decision-making processes are key to support workers to earn the trust of supported families. Currently, families are mostly unaware of what data is held about them and what discussions about them are being had and have no choice but to trust both the support workers, and all the parties and technologies involved in the surrounding care ecosystem, which is very hard to do when they have little to no visibility of it. Without visibility, any error or surprise can be very damaging to this fragile trust and can harm the relationship, and conversely, increase transparency and explanation can avoid surprises and increase trust, improving the relationship.

<a name="4.3.4.1">**Transparent, Respectful Data Handling**</a>

The findings in Themes 1 and 2 above clearly suggest that in seeking the best possible understanding, families must be engaged in a fact-centric way, which requires trust in the support worker (to interpret and record data fairly and accurately) and in the system (to keep data safe and prevent misuse). A good relationship with the support worker is critical [FQ1] to the family's care. Workers recognise the importance of being transparent with families:

> _'I think that [families] have got a right to know what is held about them and what is said about them.'_—[Worker, SQ50]

Even for data that would itself would be considered uncontroversial, a lack of awareness to that data or a lack of transparency on how data is informing judgements can cause great worry to families:

> _'Some people that I've worked with, I think as soon as they know you're holding information about them they get really tight and [say], "What are you holding about me?" […] They don't like people knowing what's going on in their lives.'_—[Worker, SQ70]

The current approach, which relies on the support workers mentioning data that they consider relevant, can reassure families when they are kept thoroughly and regularly informed, but can result in expectations being broken by accidental sharing of information if its sensitivity is overlooked:

> _'That tends to be the biggest problem with this, these little bits of information that nobody ever thinks are relevant to bring up in everyday conversation and they're coming out.'_—[Parent, CQ3]

Data must be handled respectfully, with attention to family and individual privacy. A lack of transparency and trust can lead to an atmosphere of suspicion [SQ17] where families have _'a totally overwhelming feeling of people checking up on them'_ [SQ71] and apply extreme scrutiny to what they are told: _'You can get families who [no longer] believe what's being said about them.'_ [Worker, SQ73].
Fearful of consequences [SQ72], families may withhold information:

_'Well my thing would be who is [my data] going to be shared with? Which authorities? What is going to be shared? […] If I ask for help because my son has got massive behavioural issues and I've been trying for years to get help with him and […] if I go to social services, are they going to come in and think I can't cope because I'm on my own with five kids? Are they going to take all the kids away? That's my thing. So I'm terrified of Social Services, I really am.'_ [Parent, FQ14]

Respectful data handling also includes using tact and discretion when referencing data, and a common current practice is the use of a _strength-based approach_ [multiple workers in workshop B] when presenting or referencing data that could be perceived as particularly negative or judgemental; looking for the opportunities for growth rather than seeking to criticise.

An open and respectful approach is rooted not just in decency but in practicality as a co-operative family is easier to support: _'Because if someone is feeling judged or stressed or angry or whatever, then they can stop the conversation'_ [Parent, CQ5]. Being transparent with data can also help with accountability and accuracy, which can detect and prevent mistakes earlier:

> _'There was a time where I was at the doctors' and they asked how many units of alcohol I drank, and I said, probably about three bottles a week, at the time, not any more but later on [the support worker] pulled me up on it and they had it down [in the data record] as three bottles a day. That could have caused an issue was anyone ever to ask.'_—[Parent, CQ7]

In current practice, data handling *is* generally respectful - data mishandling and unexpected uses of data are currently mostly avoided; but transparency is low, making the perception of respectful handling quite fragile and entirely based upon trust rather than direct experience.

<a name="4.3.4.2">**Always Seek and Demonstrate Greater Understanding**</a>

In order to earn, build and maintain trust, support workers must always be seeking to form a more complete and up-to-date picture of the family, in line with the finding in [4.4.3](#4.4.3.1) that individuals are more than what is stored in their records. This requires human interaction to uncover. Demonstrating a deep understanding of the family, and that a family's lived reality has greater priority than what a database says can be a critical to trust-building:

> _'You don't want to reduce them to this number in a database. You want to understand their actual experiences and support them in getting better.'_–[Worker, SQ74]

It is important that families understand workers' good intentions when accessing data about them [FQ15]. However, if workers had to show all available data to families this could make it challenging to maintain good relations, _'because literally [the data we have] is like everything, isn't it? So I don't know how I would feel…'_ [Worker, SQ21]. In addition to avoiding breaches of expectations (see Theme 2 above), a transparent approach ensures that the privacy of families is respected, because data is not used in decisions without the chance for explanation:

> Parent: _'I don't want everybody knowing how rubbish I am with money.'_
> Child: _'That's my life.'_—[FQ2]

Participants also indicated that families' desire for transparency (as mentioned in the previous section) does not just imply reporting data usage, they need dialogue and human engagement to give them reassurance; trust and reassurance can is best achieved through a conversation [FQ1], not a data interface. Support processes need to change to better recognise the role of dialogue, rather than just consultation of a database, as the best way to achieve a rich and nuanced understanding.

<a name="4.3.4.3">**Pro-actively Challenge Data-centric Norms**</a>

Exploring this need for reassuring dialogue in more depth, it is clear that to avoid damaging negative spirals of emotion, deliberate openness is needed from support workers (and the entire care system) [SQ18] as to what information is held, and how it will be used and shared, in order to alleviate fears of data being used _'against'_ families that can arise without that transparency—giving them instead confidence that their interests are being protected, thus putting them at ease [SQ20]. Data handling processes appear to be only explained once in very loose terms during initial engagement, for the purposes of collecting informed consent, and are rarely revisited. Workers could easily imagine explaining data practices in greater detail than they currently do [SQ41] and clearly there is a need for proactive action by workers to counter the inherent knowledge imbalance of data being collected into systems that they are gatekeepers for.

Workers however lack control over the quality, coverage and timeliness of the family data and see this as a systemic issue they could not adequately address. From my experience with EH teams through the SILVER project [see [Section II Introduction](#section-ii-research-contexts)] it became clear that while support workers can see more data than most, they have far from the complete picture; in fact, there is no one organisation or individual with visibility of the entire family-information ecosystem, suggesting that greater openness with data would benefit not just the family, but other civic actors involved in the family's lives and in their care. Some participants suggested that openness about data handling needs to accompany data access, so for example if browsing information together [[4.4.2](#4.4.2.2); [4.4.3](#4.4.3.2)], it would be important to explain where the information has come from and why the support worker has it, rather than just reporting its content:

> Parent: _'[If the worker knew sensitive medical information] the family would be really annoyed, they would just want you [the worker] to go.'_
> Worker: _'I'm the same, me. I'd be like_ "I don't know how you got all this?". _That would be my first reaction but then if we [were to] discuss it and browse the information with the family [that would work better].'_—[CQ6]

As mentioned in [4.4.3](#4.4.3.3), there is a need to replace the current practice of treating consent as a one-off formality at the start of the support process with something better. This has previously been conceptualised as a need for _dynamic consent_ (@bowyer2018family; @kaye2015; @williams2015]. A common heuristic expressed by families here and in the earlier study is that data should only be seen by those that _'need to know'_, but this is very hard to achieve: first, because without transparency of data handling, a family cannot verify whether this is happening, so has to rely only on feelings and supposition to inform their trust. Second, the need for fair judgement over who should access families data is objectively important given that some support workers expressed a belief that their right to access families' data should overrule families' consent:

> Worker A: _'I think to enable us to work with families, we need to have as much information to give them the best possible service. So, I think we should be able to [access their information] regardless of what families say.'_
> Researcher: _'Regardless of what they say?'_
> Worker A: _'I do, yes.'_
> Researcher: _'Does everyone feel the same way then, that they don't get a say?'_
> Worker B: _'Yes, because you need as much information as what you can.'_—[SQ22]

This suggests that to ensure the 'need to know' is determined fairly and accountably, independent oversight might be needed; other situations that would benefit from this include deciding what parts of a medical history are _'relevant'_ [SQ23], arbitrating situations where legal duties may require the breaking of consent [SQ24], and being able to identify and address situations where recorded information may not tell the full story [CQ8].

These findings suggest that not just transparency but a progressive attitude to data practice, actively challenging current data centric norms, would enhance trust around data handling access and decision making as requirements and lead to a healthier support relationship. This could even include thinking about new ways of using data, for example at a collective community level [SQ78], to promote an open data-sharing culture.

Discussion{#4.5}
----------

The findings have provided a deeper understanding of families' experience of data RQ1 [[3.3.1](#RQ1)] and the role of data within EH relationships RQ2 [[3.3.2](#RQ2)]. This section discusses three implications:

- the value of involving people with their data [[4.5.1](#4.5.1)],
- the need for human interaction to make data access effective [[4.5.2](#4.5.2)], and
- the implications of a shared data interaction approach in terms of shifting the LDM closer to the supported family [[4.5.3](#4.5.3)].

### The Value of Involving People with Their Data{#4.5.1}

Data about supported individuals is integral to current care practice, improving decision making by providing a more complete picture of a family's life [[4.1.2](#4.1.2)]. This prevalent mindset reduces families' autonomy. Just as in the commercial sector [[2.1.2](#2.1.2)], families' civic data is considered a resource to be utilised. The implicit assumption is that data is a complete and objective source of truth [[4.1.2](#4.1.2)], yet participants agree it can never be [S14, S18'].

Families' lack of awareness of held data and its use leads to false expectations and surprises, and in the worst cases, fear and distrust which can harm the care relationship. Family civic data currently serves a _proxy for family involvement in decision making_. Families are cut out of the loop. They should be able to take a role in relation to their data [@bowyer2018family]. A lack of such involvement removes any possibility for data checking, increasing the chance that data can contain inaccuracies or errors of judgement due to out-of-date or missing data, which can cause harm [@bowyer2018family; @crossley2022].

<a name="4.4.1.1">**Trust**</a>

Participants' responses confirm prior findings [@vandijck2014] that trust in the independence and integrity of data holders is critical to an effective support relationship. Yet trust in EH is currently fragile, resting upon feelings and impressions.  The findings suggest that a support worker can build trust by continually striving to develop and show a deep understanding of the family as individuals, beyond 'what the computer says'. Trust—in the system and the worker—can be earned by treating them as people, not _'objects to be administered'_ [@cornford2013; S4], leading to more effective support.

Shared data interaction practices (such as checking data together, visible data recording, family sign-off, or contribution of individual perspectives as data) could give a family direct evidence that they are being listened to and that their viewpoint is important even when it contradicts the digital record. This would be powerful for trust-building. Transparency of processing—something that is currently near impossible—could empower families by giving them confidence through their ability to hold providers accountable by verifying that [as per the need established in @bowyer2018family] data is fair and accurate. It is evident from the findings that an EH system built upon strong trust would require direct involvement of the individual(s) being cared for. Shared data interaction as conceived by the participants suggests mechanisms for such involvement.

Shared data interaction would also align with the desire for evidence-based decisions [[4.1.2](#4.1.2)]. An earlier WHO study found that a similar approach lead to more effective collaboration and better decisions [@johnson2010]. Inefficiencies that could be avoided include spending time correcting misunderstandings, or 'damage control' following misjudgements. Participants described emergent practices of using data with families to track progress; these are apparently already effective, allowing families to see their own progress. If such data were available outside of the support engagement, this could empower families still further to be self sufficient.

A health innovation project in South Africa echoes these findings on the importance of trust, agency and involvement of the individual:

> _'The user must feel or experience trust, […] feel that they can control and increase their own access to a system. Their uptake and use are essential for such a [digital ecosystem] to work or be regarded as a sustainable solution.'_—[@herselman2016]

<a name="4.4.1.2">**Consent**</a>

Viewing data as a shared resource to be curated together could provide an effective alternative to EH's currently ineffective consent model [[4.3.2](#4.3.2)]. Currently consent collected as part of the EHA serves as a a _point of severance_ [@luger2013] that hands authorities _carte blanche_ powers to collect and use families' data. Ongoing access and direct use of data by families would offer practical _dynamic consent_ [@kaye2015; @williams2015].
If families were regularly 'talked through' their data, consent would become more reliable and less bureaucratic. Consent could shift from being seen as a formal permission to be certified and tracked, relying instead on the natural human instinct to speak up when you are shown something that seems amiss.
Families will be happier with the use of their data if they can see it, notice issues and speak up when they feel something is amiss.

If implemented in a robust manner, this could simplify consent processes and, by sharing responsibility for data stewardship, limit support workers' liability. Conversations centred upon data would allow mistakes to be spotted sooner, easing workers' fears of _'missing something important'_. Shifting the focus of the support relationship towards _discussions around data_ might help alleviate the inadequacies [@cornford2013] of the EH record to accurately represent families.

Giving the user a role in understanding and influencing the life of their own data is identified as a key ingredient of moving towards a more progressive model of digital citizenship:

> _'If, instead of disempowering users in the name of simplicity and ease of use, we acted to empower them and ourselves through increased literacy in the technologies employed, and constructed systems where data about behaviour can be more easily quantified and controlled by the user, then we would have the tools at our disposal for a more equitable negotiation with commercial and governmental forms of power.'_—[@bridle2016]

<a name="4.4.1.3">**Families as Agents of Self-Care**</a>

Shared data interaction could make supported families stakeholders in their own case. The care worker need take less of a position of authority, instead becoming an ally to the family member(s), now empowered as an agent in their own self-care. Individuals would be more able to act and improve their situation than previously [[4.4.3](#4.4.3)], approaching the HDI concept of _agency_ [@mortier2014]. Such a shift could serve as an antidote to data-centrism in the system and society at large [[2.1.2](#2.1.2)]. With control over and input into their _'data self'_—the representation of them that is seen by the state—families would have greater trust that their interests are being served. Through data, they could take part in informed decisions to could improve their own lives.

### Effective Data Access Requires Human Interaction{#4.5.2}

<a name="4.4.2.1">**The Need for Support**</a>

The findings shows that current data inequalities will not be solved simply by opening up databases to families and giving them access. They must be able to meaningfully comprehend the data and effect change based on what they learn. This involves the translation of raw data into meaningful information [[2.1.1](#2.1.1)]—through summaries, visualisations and explanations.

It is not clear who would have the access, skills and mandate to create such information representations. Participants' designs and desires echo prior claims that information available to must be _legible_ [[2.3.2](#2.3.2); @mortier2014] and that access must be _effective_ [[2.1.4](#2.1.4); @gurstein2011]. This includes providing suitable opportunities for access—for example via personal data interfaces not just within meetings—as well as addressing technology, literacy, mental or physical handicaps. Participant ideas around audio interfaces illustrate the extra steps that would be needed to provide effective access for all. To support varied needs, information access would need to be supported by a human relationship—one where someone can both explain the data as well as answer questions about it [[4.4.2](#4.4.2.4)].

It is the human-to-human interaction that can make data access meaningful. Data use necessitates an ongoing conversation. Systems need a human face or point of contact that individuals may put their trust in and to whom they can address questions. Access only to raw data would be inadequate and limiting [@cornford2013].

<a name="4.4.2.2">**Working Together**</a>

Explorations of human interactions around data within the support relationship suggest that shared data interaction could lead to more effective discussions.
The use of printouts, tablets or 2-in-1 devices to show data rather than verbally report it, can provide a focal point, optimising the discussion. The data representations would function as a _boundary object_ [@bowker2016; @star1989; @star2010], just as the data cards did [@bowyer2018family].
The families understand the data because it is _about_ them, and the support workers are familiar with the systems it came from. This could encourage
families to 'open up'. Many participants talked about how looking at data could serve as a conversation starter—echoing this study's use of stimuli [[3.4.2](#3.4.2)]. The ongoing use of such data representations as a metric to observe change from from meeting to meeting could bring a feeling of reward and accomplishment to the family and contribute to their future success.

Shared data interaction would also enable support workers to be less adversarial. They could position themselves as equals (_'Let's make sure this data is right.'_) and avoid appearing to side with the data (_'Our records say that you have…'_). As we see in this study, data representations serve as _'things to think with'_ [@bowyer2018family; [3.4.2](#3.4.2)]. Shared data interaction—played out in abstract through the use of storyboarding cards in Workshop C—helped participants to navigate scenarios and quickly imagine possible actions together.

<a name="4.4.2.3">**Agency & Negotiability**</a>

Yellow-bordered cards (for families) and blue-bordered cards (for staff) triggered both parties to take ownership of their piece of the puzzle, placing their 'own' actions without any direction having been given as to who should place which cards. Parents and staff had each taken a role in the scenario and felt ownership over the choice of options available to them. Similarly, green-bordered cards (actions involving both parties) usually resulted in both parties discussing and agreeing a view before the card was placed, showing that the way data is presented is key to how people respond to it. This gives some insight into how the dynamics of shared data interaction might work if implemented in practice. Feeling able to perfom actions such as commenting or correcting data would provide some _agency_ [@mortier2014] for family members;
The availability of capabilities over data, including the ability to raise a question or start a conversation would satisfy the second HDI requirement of _negotiability_. Conversely, an inability to act upon or influence shown data and its use would indicate a lack of negotiability, reinforcing the idea that simply viewing data is insufficient.

Efforts to deliver effective HDI capabilities in future should therefore focus upon the role of the human in the information system, as a data interface is limited by its operational context as to its ability to truly offer meaningful actions to users.

As our participants all strongly agreed, supported families _'should be treated like people, not database records.'_ [S4; [4.4.3](#4.4.3.1)]. Excessive focus upon the record can inadvertently become problematic in EH practice focusing upon child welfare:

> _'Children_ [can be seen as] _the objects of a variety of concerns which need to be acted upon rather than agents of their own lives'_—[@ec2014].

Analysis of the Child Index, an early warning child welfare system in the Netherlands, drew a similar conclusion on the importance of maintaining a compassionate human aspect in family-state relations:

> _"Taking into account that_ [care] _professionals' first love is the best interest of and care for a child,_ [policymakers should] _provide room for the 'love' between future technologies and their social actors to flourish."_—@lecluijze2015

### Shifting the Locus of Decision Making Through Shared Data Interaction{#4.5.3}

In pursuit of RQ2 [[3.3.2](#RQ2)], the workshops explored the role of data within the EH support relationship. Workshop C brought parents and workers together to explore the mechanics of shared data interaction at an interpersonal, sociotechnical level [[2.2.5](#2.2.5); [2.3.3](#2.3.3)] to explore the mutual benefits that might be offered by _shared data interaction_. The participants worked together to construct possible narratives expressed through human-human and human-data interactions. In doing so, they modelled how shared data interaction could rebalancing power over data. I conceptualise this as **shifting the Locus of Decision Making (LDM)**. LDM is a concept distinct from _locus of control_ [@spector1982] which normally refers to personal willpower, and _locus of power_, which refers to the concentration of power within an organisational hierarchy. The LDM is the the place where decisions are made. It may or may not coincide with existing authority structures. Accumulated understandings of EH practice, and more generally of data-centric service provision, suggest that decisions are typically made, germinated or championed close to where data is accessed. In an effect that has been expected since as early as 1970 [@klatzky1970] the increasing use of data in service provision [[2.1.2](#2.1.2)] has concentrated the LDM with data holders, who collect service users' data to serve their own purposes.

![Figure 4.2: Current Model of Data Interaction, <br/>and Proposed Model of Shared Data Interaction](./src/figs/fig4.2-shifting-locus.png)

<a name="4.4.3.1">**Removing the Gatekeeper**</a>

The current and imagined approaches are represented in [Figure 4.2](#figure-4.2).

In the current model (top), the only access to data by families is through the support worker as gatekeeper, who decides the scope, content and nature of their access. The LDM is 'back at the office', locked away from the family's participation.

In a more equitable model (bottom), support worker and family member are positioned as allies looking at the data together. This changes the nature of the support relationship. Some of the work that was previously done solely by the data holder (such as data maintenance and data-driven decision making) would now take place in the two-party context of the support meeting itself.

The removal of the gatekeeper role redistributes the power to interpret, select and judge data. Families would no longer be prevented from participating in data-based decision making. I theorise that shifting the data access from the domain of the support worker to the shared domain of the support meeting would move the LDM closer to the heart of the support relationship, creating a more balanced relationship and increasing families' agency and power.

Support for shifting the LDM through shared data interaction is seen in the findings: Both families and staff said they would value a shared data interaction approach. Multiple participants independently imagined benefits of reviewing data and consent together [[4.4.2](#4.4.2.2); [4.4.3](#4.4.3.2); [4.4.3](#4.4.3.3)]. Participants perceive shared data interaction as an improvement, but it has not been tested in practice, so the remainder of this subsection will consider the benefits and implications of such a shift.

<a name="4.4.3.2">**Individual/Family Benefits**</a>

Shared data interaction could empower families by giving them a role to play as agents in the life of their data, and a new ability to create and curate their own _data self_ so that it is as fair, accurate and representative as possible [@bowyer2018family; [4.5.1](#4.5.1.3)]. They would be further empowered by having access to view metrics by which their progress is judged, as they could
take steps to influence any poorer metrics, and then use the improved metrics as confidence-building evidence of growth—a positive feedback cycle that is hardly possible at present.

Shifting the LDM could enable families to take more responsibility, through an increased ability to reflect and make plans—an important element of harnessing one's personal data for self-improvement [[2.2.3](#2.2.3); @abiteboul2015], and through better accountability [SQ75]. Exposure to data is required for accountability [@crabtree2016]. The perceived benefit of individuals directly using data-based interfaces for health and wellbeing are already accepted; 93% of doctors believe apps can improve health outcomes [@kostkova2015].

<a name="4.4.3.3">**Care Provider Benefits**</a>

Benefits to supported individuals can be seen as benefits to the EH practitioner too, given their role to help improve the family's situation. But co-stewardship of family data can also reduce the burden and responsibility upon the authority to look after that data. Responsibility for ensuring completeness, accuracy and fairness is now shared. This could also reduce the likelihood of complaints or litigation, not least because families can shift from an 'us and them' mentality towards a more favourable perspective.

Provided the individual remains engaged, informed and understands the data and processes that exist, the scope for breaches of consent by workers is reduced because at every meeting (and, with personal data interfaces, outside those meetings) supported families are involved in a conversation that directly enables them to voice their approval or concerns for the ways their data is being used.

<a name="4.4.3.4">**Practical Challenges**</a>

<span class="editnote">add forward refs to limitations?</span>

Implementing shared data interaction would be challenging. Costs could be incurred if new equipment such as 2-in-1 devices were needed. New software interfaces would need to be commissioned, developed and purchased. Such interfaces would be technically difficult, given the fragmented care sector infrastructure [[4.1.2](#4.1.2); @copeland2015]. Identity management in this context is already challenging [@wilson2011], and child involvement requires special care [@tregeagle2008]. Support workers would need additional training both on software and hardware, this is already a current issue in the UK [@honeyman2016] and a critical one in Poland [@soja2015]. Training becomes particularly important in a system where the care workers must take on an educational role as sensemakers of digital records.

Involving individual members of the public as actors within systems previously targeted to staff would likely carry fresh considerations for access control, technical support and public liability insurance. Providing personal data interfaces to the public, and new communication channels for asking questions would carry a large human resource support cost.

The creation of a direct communication channel between supported individuals and support services offers potential savings for the state in terms of reducing the amount of costly [@kriisk2017] 'in the home' contact. However, broad human support for data access might change these savings into a net cost.

Dispute resolution procedures and additional legal and information governance support would be likely to be needed. New challenges might occur, such as individuals with destructive, manipulative or otherwise challenging intent, who might try to mislead workers for person gain.

It would be fair to criticise human-centred state interaction as something that would not be cheap or scalable. With more individual-state interactions, every case could take more worker time in a system that is already overburdened and underfunded [@copeland2015;@lga2017]. The state has adopted a data-centric approach to citizen interaction in part because it cannot manage to provide human relationships with every individual citizen. But now this approach has become ingrained into government approaches to citizen relations:

> _'_[Data-centric citizen interaction] _is no longer a technological necessity, but it has become a political intention.'_—[@bridle2016]

There is a need to reverse this trend, not only in practice but in political ambition, if people's interests are to be best served, and if a welfare state is to be truly _enabling_ [@miettinen2013]. By taking a more innovative approach to digital policy, it is possible that governments could be more effective in helping to involve those citizens that have become disadvantaged by the current system. A more human-centred approach could help to combat the digital divide [@kalvet2008; @steyaert2009].

My proposal for shifting the LDM is theoretical; it does not provide an implementable solution that could be rolled out at scale. Instead, it can serve as a mental model to stimulate discussions about potential change. Its value is in shining a light on the positive and negative impacts upon relationship effectiveness of current data practice in EH. These findings offer imagined practices that could be more efficient, and serve as a challenge to the status quo that should encourage EH providers to question their priorities when it comes to the use of people's civic data. The primary goal of EH is to empower families to help themselves as effectively as possible, and EH's focus on data arguably works against this.

Summation of Case Study One{#4.6}
---------------------------

<span class="editnote">make stronger references to Design in intro and elsewhere, and talk about what is feasible / implementable (maybe leading into that being explored in part two)</span>

Through four participatory co-design workshops with supported families and support workers in North-East England, this study highlighted five problem areas which participants perceive with current personal data practices:

1.	**A power imbalance** – Families' personal civic data is collected by care organisations who view it as a resource to be utilised, creating a structural power imbalance against families who are barely able to influence data values or practices.

2.	**A closed and opaque data ecosystem** – Families lack awareness of what data is held about them and how it is used, with support workers (who themselves have limited access) functioning as gatekeepers to what families will be told.

3.	**Ineffective, meaningless consent** – The current consent model, while legally satisfactorily, is ineffective. It is a one-time initial hurdle after which support workers can do whatever they deem necessary with families' data. Families are never again given any meaningful choices about what happens to their data.

4.	**No accountability and fragile, limited trust** – Without transparency or an ability to request or demand changes to data or data practices, families have no ability to hold data holders to account. This makes families' trust in the system hard to earn and fragile to maintain.

5.	**A lack of agency or true empowerment** – With families having no ability to shape the way they are seen in data, or even just to see how the state sees them, opportunities are missed to empower families for personal growth.

These explorations of shared data interaction and personal data interaction show there is both a need and a desire for a new approach. Deliberately openness with families' data and direct use within face-to-face consultations could address all five of these problems. The removal of the gatekeeper role over families' civic data would give families a role in the stewardship of their own data, shifting power in their favour. Clear visibility of data recording and usage would enable accountability (currently absent), engendering trust. With ongoing family involvement, the consent problem would be largely solved; families could immediately speak up at any point in the light of new developments or new information. Data-informed and support conversations could enable better decisions. With an ability to influence how they are represented and observe changes through data, families would be empowered to make changes in their own lives, acquiring a previously unattainable level of agency.

Data visualisations and summaries could serve as conversation starters and as boundary objects, enabling more effective conversations. A shift from verbal reporting to 'looking at data together' would change the dynamic of the support interaction away from 'us and them' towards an ally-based approach. Data accuracy should improve, given that for a full picture both data and dialogue is needed [@bowyer2018family]. Given the opportunity, individuals could contribute explanations, fill gaps or correct mistakes. Decision making would naturally improve through a greater focus on discussions around accurate evidence.

This chapter establishes that giving the family a role could be very powerful, because visible data processing would provide them with direct evidence that they are being listened to and that their perspective is seen to matter more than 'what the computer says'. The ability to ask questions about data treats the family with greater respect. Personal data interfaces, enabling families to act independently in their own time and in contexts outside of the support interaction, would allow individuals to alleviate concerns quickly and maintain confidence that their data selves remain fair and accurate. At the same time, new opportunities could arise for use of one's own data. The adoption of such measures could facilitate the emergence of a human-centred personal data ecosystem [[2.3.4](#2.3.4)] in a civic context.

Capabilities – or their absence – matter more than the on-screen technicalities of the data interaction. Data interfaces are limited by their operating context as to how much they can offer, but in this chapter data interaction is examined as a sociotechnical process [[2.3.3](#2.3.3)], looking beyond interface interaction to the human relationship between the individual and the state, which allows more holistic and human-centric solutions to be imagined, in line with the objectives of this thesis [[2.4](#2.4)].

The sociotechnical perspective allows deeper consideration of the purpose of EH interactions, refocusing attention on the core goals to empower individuals to better themselves. The human perspective on family civic data should be given the highest priority, so that professionals' flexibility is not limited, but also because data cannot adequately represent the complexities of human life [@bowyer2018family]. People are more than just data, and you have to talk to them to make sense of their lives and to avoid excluding them. Usage of data should always be supported with dialogue and engagement. It is this need to focus on the human aspect that explains why trust underpinned nearly every single problem imagined by participants. Without an open system that encourages dialogue and discussion, it is very hard not to close doors, create suspicion and harm trust.

[Figure 4.1](#figure-4.1) informs RQ1 [[3.3.1](#RQ1)], showing perspectives upon family civic data and practices. The thematic analysis [[4.4](#4.4)] of workshop transcripts identified positive and negative impacts on the support relationship of current civic data practices within EH, identifying best practices, seen in the subthemes and expressed as 38 specific practices for EH services [@bowyer2019]. Many of these are currently imagined or only just emerging. Participants believe these practices would improve families' engagement and the support they receive. These proposed practices (which inform RQ2 [[3.3.2](#RQ2)]), as well as the shared data interaction approach, challenge the status quo. They can inform policy, process and system design for all kinds of attempts to reform care services or digital citizenship offerings. Such changes carry significant challenges in cost, training, manpower and emergency planning, as with any systemic practice change in an organisation, but such an approach may get closer to the heart of the real issue of empowering _'left behind'_ (disempowered) families, perhaps moreso than a purely state-centred approach. Human-centred data use may offer a route to a more enabling welfare state. This work serves as a reminder that as we move into the data-driven age it is important that data should stay close to the people it is about, rather than to those that use the data to provide services.

The general principles expressed here could be equally applied to other domains including education, healthcare, democracy and commerce, and this emphasis upon individual capabilities over interface design is a mindset that could be applied to many human-computer interaction and design endeavours.

---
