Defining a New Field: Human Data Relations {#chapter-7}
=======================================================

> _"What drives and drags the world are not machines, but ideas."_
>—Victor Hugo (19th century poet)

Introduction to Part Two{#7.1}
------------------------

[Chapter 6](#chapter-6) concluded the academic inquiry part of this thesis. We now know, backed up by the insights from the Case Studies' participants, what people want from direct RQ1 [[3.3.1](#RQ1)] and indirect RQ2 [[3.3.2](#RQ2)] data relations. That is, however, not the end of the story. Bringing to bear my experience as a designer and software developer, I can advance the exploration of this problem space further, turning from theory to practice, from what is needed to what is possible. It has been my good fortune to have been involved throughout the duration of this PhD with peripheral activities that also can be seen, in the context of this thesis' findings, to relate very much to the pursuit of personal empowerment and human-centric data use. For Part Two, therefore, I expand the original research question, going beyond the initial RQ [[2.4](#RQ)] which asks what relationship people want with their personal data, and explore how those desires could be met in practice:

> <a name="exRQ"></a>**"Having understood what relationship people want with their personal data, how might these better data relations be achieved?"**

Methodologically, Part Two is distinct from the main academic enquiry. The Case Studies prioritised a participatory and investigatory approach, but there is a need for specialist design innovation that cannot always arise from working with everyday users. The approach now, therefore, is more UCD than PD [[3.2.1](#3.2.1)]. Part One's findings become material for myself as an adversarial designer, informing ideas for technical and societal changes that can bring about better data relations. [7.2](#7.2) describes the peripheral R&D activities I undertook, which form the basis of learning for Part Two.

The wide-reaching objective of achieving better data relations in practice has many facets: technical, design, commercial, legal, moral, social and political. These will not all be covered. Collectively, Chapter 7, 8 and 9 present an understanding of the multi-faceted realities of today's PDE landscape _sufficient to inform the design_ of PDE processes and systems in pursuit of better relationships with data. This understanding is synthesised from my real-world practical designs and insights, as well as from the work of other innovators and activists, and is contextualised relative to existing literature and the thesis's earlier contributions. As such, it will be necessary to introduce some new literature and external references throughout Part Two,. This is because it is only through reflection upon the findings of Part One from this new perspective that the particular practical and activist avenues that Part Two will need to explore become evident.

In this chapter, I position the topic of this thesis as a field of study in its own right, _Human Data Relations (HDR)_, formally defined in [7.3](#7.3). Additional insights into how people relate to data are identified [[7.4](#7.4)], as well an important dichotomy of people's needs for better relations with their data [[7.6](#7.6)]. The six wants [[Chapter 6](#chapter-6)] are repurposed as four core objectives for a landscape of better HDR [[7.7](#7.7)]. I conceptualise those who pursue these objectives as _HDR reformers_ and reflect on the researcher-turned-activist stance that drives this chapter, recognising a nascent _recursive public_ [[7.8](#7.8)].

Peripheral Research & Design Settings{#7.2}
------------------------

As established earlier [[3.6](#3.6)], Part Two explores the wider action research [[3.2.2](#3.2.2)] cycle that has contributed to my evolving learning about HDR, looking beyond direct academic investigation and drawing upon both self-experimentation and my embedded work in in the PDE space [[2.3.4](#2.3.4)] as both developer and researcher. Through field experience, I have understood constraints and opportunities that affect data interaction system and process design. Concurrently,I have fed research learnings back into those projects, creating practical impact. Instead of conducting formal studies, I have undergone a process of acculturation to the world of practical system building and project operation in the PDE. Through design, technical prototyping and pushing boundaries of existing systems, I have developed knowledge and gained expertise which allows me to draw conclusions with confidence about how the discipline of Human Data Relations (which I define below) should proceed in its future R&D to best serve individual and societal interests.

Concurrent to this PhD, I took a major role in two industrial research projects (1 & 2), and two academic research projects (3 & 4):

  1. **BBC R&D's Cornmarket Project** [@sharp2021], which explored through user experience design, technical prototyping and participatory research, how individuals might interact with data through a Personal Data Store interface [see [ARI7.1](#ari-bbc)];
  2. **Sitra/Hestia.ai's _digipower_ Investigation** [@härkönen2022project], a successor to Case Study Two, in which European politicians examined companies' data practices through exercising data rights and conducting technical audits [see [ARI7.2](#ari-digipower)];
  3. **Connected Health Cities (CHC)'s SILVER Project** [@ConnectedHealthCities2017silver], where I, along with a backend developer and a team of researchers, developed a prototype health data viewing interface for Early Help support workers [see [3.4.1](#3.4.1.1)]; and
  4. **Digital Economy Research Centre (DERC)'s Healthy Eating Web Augmentation Project**, which explored the use of web augmentation techniques to modify the user interface of takeaway service _Just Eat_ to include health information, in support of healthy eating [see [ARI7.3](#ari-derc)].

For additional details about these projects and my involvement in them, see the linked sections. See also [ARI7.4](#ari-attribution) for a note about the attribution and origin of the ideas presented within this chapter.

'Human Data Relations': A Definition{#7.3}
------------------------------------

Chapter 6 established six 'wants' that people have in their relationships with data: _visible_, _understandable_ and _useable data_; _process transparency_, _individual oversight_ and _decision-making involvement_.

The major contribution of this thesis, beyond evidencing these wants in chapters 4 to 6, is to transform these desires into a clearly defined field for future research and innovation. Repurposing concepts of 'human-technology relations' and later 'human-data relations' which have been the subject of some study in the contexts of philosophy, embodied interaction and the performing arts [@ihde1990; @hogan2012; @windeyer2021], I have chosen to name this field **Human Data Relations**, or **HDR** for short. I propose this field as a successor to Mortier _et al._'s Human Data Interaction (HDI) [@mortier2014].

HDR builds upon HDI but takes a broader sociotechnical stance. HDR encompasses all the ways people and organisations can and should relate to data, not just direct data interaction. Through its greater focus on relationships and ecosystems, and approaches that address today's data-centric power-imbalanced reality, it offers a more actionable research agenda for the world of the 2020s. HDR's definition draws upon three distinct connotations or readings of its name:

| <a name="hdr-definition">A Definition of Human Data Relations (HDR)</a> |
| :---------------------------------- |
| The field of HDR encompasses all the ways in which humans and human organisations relate to, and with, data, specifically: |
|   1. _Human-Data Relations_: users' direct interaction with data to understand and use it, similar to HDI, in service of the direct data wants [[6.1](#6.1)] of visible, understandable and useable data. |
|   2. _Human "Data Relations"_: individuals' relationships with organisations that hold data about them, in service of the indirect data wants [[6.2](#6.2)] of transparency, individual oversight and involvement. |
|   3. _Human/Data Relations_: how organisations manage their customers with respect to personal data. Similar to _public relations_ or _customer relations_, organisations choose how present their data practices (so as to build trust), and whether they will involve users with data, and provide support to understand data to their users. Organisations can empower individuals and build more effective customer relationships through HDR [[4.4.1](#4.4.1); [5.5.2](#5.5.2); [6.1.2](#6.1.2)]. |

Having scoped HDR, we see that 'better' HDR can be achieved by working to empower individuals [[6.3](#6.3)] through pursuit of the identified six wants for data relations. However, as this section will explain, HDR is motivated in two distinct ways, to which those wants apply differently. As background understanding, the next section will examine more closely what role data plays in people's lives.

The Role of Personal Data {#7.4}
-------------------------

Today, almost anything can be encoded as data. Many previously analogue objects and activities now have digital equivalents, so the concept of data has become broad and hard to pin down. Underlying HDR is a need to recognise what roles data can play in people's lives—what it _is_ to people. I have so far identified eight distinct lenses to explain how people might relate to data—including as property, as memory and as creative work. These are modelled in [Table ARI5.2](#table-ari5.2).

People may think of their personal data through any or all of these _lenses_ [@karger2005; [2.2.2](#2.2.2.5)] at any given time. Any data interaction process or interface design should take these into account. Different informational representations might be needed at different times [@lindley2018], bringing different aspects of the data to the forefront. Looking across these lenses, I identify four specific _roles_ that data can serve:

1. Data has a role as an **artefact of value** to your life;
2. Data has a role in **informing** you about yourself, the world, and the prior or recent actions of others that may affect you;
3. Data has a role as **a useable<sup>[10](#fn10)</sup> material with which to effect change** in your life;
4. Data has a role as **a means to monitor changes** in data holders' behaviours, in digital influences upon you, or within your life.

Human Data Interaction or Human Information Interaction?{#7.5}
--------------------------------------------------------

To unpack HDR further, we must differentiate between humans relating to data, and humans relating to information. HDI concerns the way people interact with data. Mortier _et al._ [@mortier2013; @mortier2014] defined the field of HDI without making the important distinction between data (the digital artefact stored on computer) and information (the facts or assertions available from that data). This is an important distinction. _Human Information Interaction (HII)_ originated in library sciences to consider how humans relate to information without regard to the technologies involved [@marchionini2008]. Jones _et al._ called for a new sub-field of HII in an HCI context[^11], highlighting the need to focus on information interaction:

> _"_[HCI can] _unduly focus attention on the computer when, for most people, the computer is a means to an end—the effective use of information."_—@jones2006

DIKW theory [[2.1.1](#2.1.1)] highlights that interpretation of data to obtain information is a discrete activity. This was borne out in the findings of Case Study Two, where it became clear that participants have distinct wants from data, and from information [[5.4.3](#5.4.3.2)]. Access to data _and_ information is critical to both understanding and useability [[6.1.2](#6.1.2); [6.1.3](#6.1.3)].

[^11]: The HCI panelists involved (excepting Fidel) were seemingly unaware of the existing HII field in library sciences, as they positioned the publication as a call for a 'new field'.

Drawing on DIKW theory, allows the identification of three distinct artefacts people can have relations with:

  1. **data** - the stored digital artefacts held by organisations for algorithmic processing and human reference, copies of some of which can be obtained using data rights;
  2. **information about individuals** (a.k.a. _life information_) - facts and assertions about the individual and their life, obtained through human or algorithmic interpretation of stored data or analytical inference; and
  3. **information about data** (a.k.a. _metadata_ [[Table 5.2](#table-5.2); [5.3.1](#5.3.1)] or _ecosystem information_) - stored facts about data, such as storage location, access history, means of collection, contextual meaning, or sharing records.

The Two Distinct Motivations for Better Data Relations{#7.6}
------------------------------------------------------

Considering these two types of information in the context of the six wants [[Chapter 6](#chapter-6)] reveals two very different reasons why people might want better data relations:

(i) to acquire _information about your data_, so that you might exert control over where the data is held and how it is used, in order to be treated fairly and make informed choices about personal data. I call this **Personal Data Ecosystem Control (PDEC)**.

(ii) to acquire _information about yourself_, so that you might gain insights into your own behaviour, and gain personal benefits from those insights or make changes in your life. I call this **Life Information Utilisation (LIU)**.

[Figure 7.1](#figure-7.1) shows processes individuals might go through in pursuit of these motives. PDEC is a process of holding organisations to account and managing _what happens_ to personal data, often regardless of what it means. LIU is more concerned with _what the data means_ and its inherent personal value, regardless of where it is stored and how it is used[^12]. This novel motivational model was first proposed in [@bowyer2021twopurposes].

![Figure 7.1: The Two Motivations for HDR: Controlling Your Personal Data Ecosystem and Utilising Your Information About Your Life<br/>(with 'idealised'[^13] processes illustrated)](./src/figs/fig7.1-the-two-motivations-for-hdr.jpg){#figure-7.1}

[^12]: There is some overlap. Organisations hold data to enable interpretation (usually algorithmic) to inform decision making. In this way, organisations are doing LIU for _their_ benefit. This grey area is situated as part of PDEC, because from the individual's perspective, how organisations understand you through information informs decisions that affect your life. As such, it is more likely to enable you to exert control over use of your data than to pursue personal LIU goals.

[^13]: The illustrated processes incorporate existing data access processes such as GDPR, where the only access is through provision of a copy of one's data. This is _not_ ideal, as it creates divergent versions and will quickly become out-of-sync, however for the sake of simplicity that inefficiency is ignored [see [5.5.1](#5.5.1) for improvements to copy-based access].

### Life Information Utilisation (LIU){#7.6.1}

_Life Information Utilisation_ is a superset of _Self Informatics (SI)_ [[2.2.3](#2.2.3)], including all purposes relating to self-monitoring and self-improvement through personal data, but also other uses including creative expression, evidence gathering, nostalgia, keeping, and sharing. Many such desires were expressed in Case Study Two [[Table 5.4](#table-5.4)], and also hinted at in the Early Help context [[4.4.1](#4.4.1)]. While the existence of digitally-encoded information clearly unlocks new possibilities, LIU has existed in some form throughout human civilisation, as seen through analogue processes such as storytelling, journaling and scrapbooking.

The most relevant of the six wants to LIU are _data understandability_ [[6.1.2](#6.1.2)] and _data useability<sup>[10](#fn10)</sup>_ [[6.1.3](#6.1.3)], which relate closely to the HDI concepts of _legibility_ and _agency_ respectively.

### Personal Data Ecosystem Control (PDEC){#7.6.2}

Unlike LIU, _Personal Data Ecosystem Control_ is a _new_ individual need, arising as a result of the emergence of the data-centric world [[2.1](#2.1); [2.2.4](#2.2.4)]. Only when organisations began to collect and store facts about people as a substitute for direct communication and involvement did it become necessary. The more data is collected about individuals, and the more parties doing so, the greater the need for individuals to understand these acts so that they might influence them (or risk their lives being affected in unexpected or unfair ways). PDEC is a direct response to the power imbalance between data holders and individuals [@wef2014lens; [2.1.2](#2.1.2)].

Several of the six wants are important to PDEC: visible data and transparent processes (referred to collectively as _data ecosystem transparency_), and individual oversight and involvement (referred to collectively as _data ecosystem negotiability_, drawing on the HDI concept of _negotiability_). These grouped terms are used below.

Four Objectives for Human Data Relations{#7.7}
----------------------------------------

![Figure 7.2: Mapping the Six Wants into Objectives for the HDR Opportunity Landscape](./src/figs/fig7.2-landscape-objectives.jpg){#figure-7.2}

To offer future value to future researchers, activists and innovators, this chapter contributes a map of the HDR opportunity landscape. This map is expressed in abstract here, and explored in more depth in Chapters [8](#chapter-8) and [9](#chapter-9). First, the six wants [[Chapter 6](#chapter-6)] are transformed into four simple _landscape objectives_ which shape the ultimate goals for effective HDR in this landscape of opportunity:

  1. Data Awareness & Understanding;
  2. Data Useability<sup>[10](#fn10)</sup>;
  3. Data Ecosystem Awareness & Understanding[^14] and
  4. Data Ecosystem Negotiability<sup>[14](#fn14)</sup>.

[^14]: To avoid overly cumbersome wording, subsequent sections will drop the 'Data' prefix from 'Data Ecosystem Awareness & Understanding' and 'Data Ecosystem Negotiability'.

As [Figure 7.2](#figure-7.2) shows, the need for data to be understandable, visible and useable applies to all types of data, whether that data is interpretable as _life information_ (information within the data, that says something about the individual) or _ecosystem information_ (information _about_ the data, where it is held and how it is used). These two types of information will collectively be referred to as **human information**. These terms are used in subsequent sections.

Better Human Data Relations as a Recursive Public{#7.8}
-------------------------------------------------

Let us revisit the stance from which we approach this change. This PhD is grounded in participatory action research and experience-centred design [[3.2](#3.2)]. Using a _Digital Civics_ [@vlachokyriakos2016] approach to understand people's unmet needs, we can model how the world should change. Such research is political [[3.2.1](#3.2.1)], seeking to correct an imbalance in the world through _adversarial design_ [@disalvo2012]. Where Part One embraced participatory investigation, Part Two steps forward in the role of activist researcher, exploring how individuals and groups can actually change their world to meet the established understanding of what should change.

In this, we can consider ourselves (those who pursue better HDR, or _HDR reformers_ as a shorthand) as a nascent _recursive public_ [@p2pwikiRecursivePublic]. This term originates in the free software movement to describe:

> _'a collective, independent of other forms of constituted power, capable of speaking to existing forms of power through the production of actually existing alternatives'_–@kelty2008

Being a recursive public means using various means at our disposal to seek to modify the systems and practices we live within in pursuit of our goals. These methods might include participatory research, experience-centred design, software prototyping, rights exertion and campaigning.

This idea of reconfiguring society in this way has been conceived as _civic hacking_ [@crabtree2007; @levitas2013; @tauberer2014]. The collective around HDR reform does not yet exist as a named and identifiable _public_ [@ledantec2016] but its members congregate around interconnected and overlapping movements such as:

- the _MyData_ community [@mydata2017declaration; [2.3.4](#2.3.4)];
- personal data lockers [@digime2021; @citizenme2021; @sharp2021];
- digital rights [@openRightsGroup];
- gig economy worker rights [@kirven2018; @wie2022];
- privacy by design [@cavoukian2010];
- privacy activism [@davies1990; @bits2000];
- data justice [@taylor2017; @crivellaro2019];
- critical algorithm studies [@gillespie2016];
- adversarial interoperability [@doctorow2019];
- 'makers' [@altsitsiadis2021];
- humane technology [@harris2013]; and
- explainable AI [@explainableAI].

Summation: HDR—A Landscape Ready to Explore{#7.9}
---------------------------------

The commonality to so many groups [[7.8](#7.8)] suggests HDR reform is an emergent cultural phenomenon, whether or not a single identifiable public coalesces. Time will tell whether _Human Data Relations_ as laid out in this thesis is sufficient to give form to that phenomenon. At the least, HDR offers a descriptive umbrella term. The breadth of research, innovation and activism validates the need _and_ the desire for such a recursive public around HDR reform to exist. In fact, it already does exist, whether named or not. Therefore, Part Two takes an unashamedly critical view of the status quo, favouring the disruptive societal changes these movements seek. Part Two aspires to provide actionable approaches for all HDR reform practitioners, by asking:

> **_"How can we change the world into the one we want?"_**

This chapter has established a clear scope, motivation and research question for the new field of Human Data Relations. This sets the stage for the next two chapters, where I will take the reader on a journey of exploration through the HDR landscape to consider that question in more detail, taking note of the pitfalls and opportunities that exist.

What follows in Chapters [8](#chapter-8) and [9](#chapter-9) is deliberately broad and open-ended[^15]. It does not provide a complete answer to this question or the expanded research question [[7.1](#exRQ)], nor could it. I do not pretend to be complete or definitive in my interpretation of the outlook for HDR. Alternative interpretations and schools of thought than HDR exist. What follows is not a roadmap, but rather a snapshot of ongoing work, identified challenges and known opportunities, that can be understood through Part Two of this thesis and subsequently exploited by HDR reformers and practitioners.

[^15]: Some of the challenges and opportunities described in the next two chapters are covered in greater detail than others. This corresponds only to my proximity and depth of engagement with those ideas, rather than their relative merit, complexity or impact potential. Given the broad aim to chart a new field, I consider it is more useful to introduce a range of applicable ideas even if some are only lightly detailed than to document just a few.

---
