Defining a New Research Agenda: Human Data Relations {#chapter-7}
=======================================================

<span class="editnote">Clarify Data/Information labelling in 7.5 and chapter 8)</span>

> _"What drives and drags the world are not machines, but ideas."_
>—Victor Hugo (19th century poet)

Foundations for Practical Exploration of Data Wants{#7.1}
------------------------------------------------------------

The participatory research track of this PhD research [[3.2.2](#3.2.2)], which has been the focus of the last three chapters of this thesis, sought to discover what people want from data, and from relations that involve or use their data. We now know, from findings common to both Case Studies, six 'wants' that people have in their relationships with data: _visible_, _understandable_ and _useable data_; _process transparency_, _individual oversight_ and _decision-making involvement_ [[Chapter 6](#chapter-6)].

It is clear, given the complex sociotechnical and power-imbalanced reality of today's data-centric world [[2.1.2](#2.1.2); [2.3.3](#2.3.3)], that if positive change towards these wants is to be pursued, there is more to understand. We need to learn how people can design pragmatic, viable approaches to effect change. There is an opportunity to move from qualitative research into activist research and adversarial design [[3.2](#3.2); @disalvo2012]. This has been the focus of the parallel, embedded research track of this PhD—to go beyond the RQs [[3.3.3](#3.3.3)] and explore how people's relationships with data might be changed in practice.

The Case Studies prioritised a participatory and investigatory approach, but there is a need for specialist design innovation that cannot always arise from working with everyday users. The approach for this track, therefore, is more UCD than PD [[3.2.1](#3.2.1)]. The established findings become material for myself as an activist researcher and adversarial designer, informing ideas for technical and societal changes that can bring about better data relations. Bringing to bear my experience as a designer and software developer, I can advance the exploration of this problem space farther than a participatory researcher could. It has been my good fortune to have been embedded, over the duration of this PhD, in various research, design and development capacities, on four practical projects, that can be seen to relate very much to the pursuit of personal empowerment and human-centric data that I and the participants have envisaged.

Before explaining the different projects undertaken (which will be done in [Section IV](#section-iv)), it is important to establish a more precise framing for this track of the research. In short, the RQ for the practical track of the PhD can be considered as:

> <a name="exRQ"></a>**"Having understood what relationship people want with their personal data, how might these better data relations be achieved?"**

When looking for an existing discipline around which to frame the exploration of this question, Mortier <em>et al.</em>'s Human-Data Interaction (HDI) [@mortier2013; @mortier2014] is an obvious place to start; its principles relate closely to the wants uncovered in Chapter 6:

- HDI's _legibility_ is very similar to the want for _understandable data_, and in part highlights the want for _process transparency_.
- HDI's _negotiability_ could be seen to imply both the want for _individual oversight_ and _decision making involvement_.
- Along with that want for involvement, the want for _useable data_ could also be mapped onto HDI's concept of _agency_ (and to Gurstein's _effective access_ as well).

While HDI is clearly a foundational school of thought that underpins this work [[2.3.2](#2.3.2)] and aligns with its findings about what people need from data, its value in finding out how we might pursue those goals is limited. To explain why this is the case, it is useful to consider again the perspective of information theory introduced in 2.1.1, specifically the difference between data and information.

HDI focuses on the way people interact with data, in a very general sense. Mortier _et al._ defined the field of HDI without making the important distinction between data (the digital artefact stored on computer) and information (the facts or assertions available by interpreting that data, or facts about the artefact of data), and their conception of data interaction seems to encompass both. This was a significant oversight. As further evidence for the importance of making that distinction, it should be noted that _Human Information Interaction (HII)_ originated in library sciences to consider how humans relate to information without regard to the technologies involved [@marchionini2008]. Coincidentally, Jones _et al._ had around the same time called for a new sub-field of HII in an HCI context[^12], highlighting the need to focus on information interaction:

> _"_[HCI can] _unduly focus attention on the computer when, for most people, the computer is a means to an end—the effective use of information."_—@jones2006

[^12]: The HCI panelists involved (excepting Fidel) were seemingly unaware of the existing HII field in library sciences, as they positioned the publication as a call for a 'new field'.

DIKW theory [[2.1.1](#2.1.1)] highlights that interpretation of data to obtain information is a discrete activity. This was borne out in the findings of Case Study Two, where it became clear that participants have distinct wants from data, and from information [[5.5.4.2](#5.5.4.2)]. Access to data _and_ information is critical to both understanding and useability<sup>[11](#fn11)</sup> [[6.1.2](#6.1.2); [6.1.3](#6.1.3)].

Drawing on DIKW theory with consideration to these findings allows the identification of three distinct things that people can have relations with:

  1. **data** - the stored digital artefacts held by organisations for algorithmic processing and human reference, copies of some of which can be obtained using data rights;
  2. **information about individuals** (which I will call _life information_) - facts and assertions about the individual and their life, obtained through human or algorithmic interpretation of stored data or analytical inference; and
  3. **information about data** (a.k.a. _metadata_ [[Table 5.2](#table-5.2); [5.4.1](#5.4.1)] or what I will call _ecosystem information_) - stored facts about data, such as storage location, access history, means of collection, contextual meaning, or sharing records.

These new terms introduced here of _life information_ (information within the data, that says something about the individual) and _ecoystem information_ (information _about_ the data, where it is held and how it is used) are critical to the subsequent sections of this thesis, as each must be considered separately. These concepts are unpacked more in [ADD FORWARD REF].

By differentiating and highlighting the different wants around these concepts, this thesis enriches existing understandings of HDI. There is however another aspect of HDI that makes it insufficient for our needs: it offers understanding of the problems of today's data relations, but it does not go far enough in exploring, accepting and confronting the real-world barriers to agency, legibility and negotiability that exist. A number of researchers within the HDI field have identified the need to develop HDI into something broader: Crabtree and Mortier wrote about the need to examine HDI in a relational sense in 2015 [@crabtree2015], and in 2016 identified the need to examine the issues of diminishing user control as being worthy of multidisciplinary study [@crabtree2016]. Deborah Lupton acknowledges the social entangled nature of personal data in [@lupton2016] which begins to explore HDI more through a societal lens [@lupton2016]. Sailaja _et al._ outlined the need to embrace HDI from a practical and grounded designerly stance, asserting that _"the emergent nature of [HDI] calls for refinement of the theoretical tenets [of legibility, agency and negotiability] to help them translate into practical and tangible responses that are embedded in the technologies we create"_ [@sailaja2021workshop].

As a response to and a formalisation of these calls to extend HDI, this thesis proposes a new research agenda to elevate HDI to the sociotechnical level. From the individual data needs of HDI and of the Case Studies it defines a clear, actionable model against which efforts to operationalise HDI and other data wants can be aligned. It advances the field of HDI to the sociotechnical level, by providing a framing that embraces and confronts the practical realities of pursuing better data interaction capabilities and better relationships that involve data. This new research agenda is named _Human Data Relations (HDR)_ and is explained below.

'Human Data Relations': A Definition{#7.2}
------------------------------------

The section above shows there is a need to distinguish this wider focus from HDI as conceived such that design and research work can be appropriately focused. The world of humans and machines can in effect be designed for at three levels, each with a broader and more human focus than the last:

1. _Human-Computer Interaction (HCI)_ focuses on the interaction between people and machines.
2. _Human-Data Interaction (HDI)_ focuses on the interaction between people and the data stored within those machines.
3. _Human Data Relations (HDR)_ focuses on the _relationships_ that people have with data and the relationships people have with those who hold data about them.

Building upon HDI but embracing the sociotechnical, HDR encompasses all the ways people and organisations can and should relate to and through data, not just direct data interaction. Through its greater focus on relationships and ecosystems, and approaches that address today's data-centric power-imbalanced reality, it offers a more actionable research agenda for the world of the 2020s. This different focus also highlights why HDI cannot just be expanded by adding new tenets; the tenets are quite similar to the data wants identified in this thesis, but the lens through which we view them is different, being as it is more practical and more sociotechnical. This makes HDR something fundamentally different than HDI, and justifies the expression of a new named research agenda.

In naming this new research agenda, concepts of 'human-technology relations' and later 'human-data relations' which have been the subject of some minor study in the contexts of philosophy, embodied interaction and the performing arts [@ihde1990; @hogan2012; @windeyer2021] were repurposed, to produce the name of **Human Data Relations** (without a hyphen), or **HDR** for short.

HDR's definition draws upon three distinct connotations or readings of its name:

| <a name="hdr-definition">A Definition of Human Data Relations (HDR)</a> |
| :---------------------------------- |
| The research agenda for better data relations encompasses all the ways in which humans and human organisations relate to, and with, data, specifically: |
|   1. _Human-Data Relations_: users' direct relationships with data, interacting with it to understand and use it, similar to HDI, in service of the direct data wants [[6.1](#6.1)] of visible, understandable and useable data. |
|   2. _Human "Data Relations"_: individuals' relationships with organisations that hold data about them, in service of the indirect data wants [[6.2](#6.2)] of transparency, individual oversight and involvement. |
|   3. _Human/Data Relations_: how organisations manage their customers with respect to personal data. Similar to _public relations_ or _customer relations_, organisations choose how present their data practices (so as to build trust), and whether they will involve users with data, and provide support to understand data to their users. Organisations can empower individuals and build more effective customer relationships through HDR [[4.5.1](#4.5.1); [5.6.2](#5.6.2); [6.1.2](#6.1.2)]. |

<span class="editnote">add ref to https://dl.acm.org/doi/fullHtml/10.1145/2751314 Verbeek unpacking the nature of relations such as hybridity, influence, points of contact.</span>

Having scoped HDR, we see that 'better' HDR can be achieved by working to empower individuals [[6.3](#6.3)] through pursuit of the identified six wants for data relations. However, as the next section will explain, HDR is motivated in two distinct ways, to which those wants apply differently. As background understanding, let us examine more closely what role data plays in people's lives.

The Role of Personal Data {#7.3}
-------------------------

Today, almost anything can be encoded as data. Many previously analogue objects and activities now have digital equivalents, so the concept of data has become broad and hard to pin down. Underlying HDR is a need to recognise what roles data can play in people's lives—what it _is_ to people. This research has identified eight distinct lenses to explain how people might relate to data—including as property, as memory and as creative work. These are modelled in [Table 7.1](#table-7.1).

<a name="table-7.1">Way of thinking about data</a> | Explanation & Implications |
|:--------|:---------------------------------------------------|
| Data as property|Data can be considered as a possession. This highlights issues of ownership, responsibility, liability and theft.|
| Data as a source of information about you|Knowing that data contains encoded assertions about you and can be used to derive further conjectures enables thinking about how it might be exploited by others, but also how you can explore and use it yourself for reflection, asking questions, self-improvement and planning. It invites consideration of the right to access, data protection, and issues around accuracy, fairness and misinterpretation / misuse.|
| Data as part of oneself|A photo or recording of you, or a typed note or search that popped into your head could be deeply personal. This lens on data highlights issues around emotional attachment/impact, privacy, and ethics.|
| Data as memory|Data can be considered as an augmentation to one's memory, a digital record of your life. This lens facilitates design thinking around search and recall, browsing, summarising, cognitive offloading, significance/relevance, and the personal value of data.|
| Data as creative work|Some of the data we produce (e.g. writing, videos, images) can be considered as an artistic creation. This lens enables thinking about attribution, derivation, copying, legacy and cultural value to others.|
| Data as new information about the world|Data created by others can inform us about previously unknown occurrences in our immediate digital life or the wider world. This lens is useful for thinking about discovery, recommendations, bias, censorship, filter bubbles, and who controls the information sources we use, as well as who will see and interpret data that we generate and what effects our data has on others.|
| Data as currency|Many data-centric services require data to be sacrificed in exchange for access to functionality, and some businesses now explicitly enable you to sell your own data. This lens highlights that data can be thought of as a tradable asset, and invites consideration of issues of data's worth, individual privacy, exploitation and loss of control.|
| Data as a medium for thinking, communicating and expression|Some people collect and organise data into curated collections, or use it to convey facts and ideas, to persuade or to evoke an emotional impact. This lens is useful to consider data uses such as lists, annotation, curation, editing, remixing, visualisation and producing different views of data for different audiences.|

Table: Table 7.1 - Eight Lenses on Personal Data.

People may think of their personal data through any or all of these _lenses_ [@karger2005; [2.2.2](#2.2.2.5)] at any given time. Any data interaction process or interface design should take these into account. Different informational representations might be needed at different times [@lindley2018], bringing different aspects of the data to the forefront. Looking across these lenses, there are four specific _roles_ that data can serve:

1. Data has a role as an **artefact of value** to your life;
2. Data has a role in **informing** you about yourself, the world, and the prior or recent actions of others that may affect you;
3. Data has a role as **a useable<sup>[11](#fn11)</sup> material with which to effect change** in your life;
4. Data has a role as **a means to monitor changes** in data holders' behaviours, in digital influences upon you, or within your life.

The Two Distinct Motivations for Better Data Relations{#7.4}
------------------------------------------------------

Considering these two types of information in the context of the six wants [[Chapter 6](#chapter-6)] reveals two very different reasons why people might want better data relations:

(i) to acquire _information about your data_, so that you might exert control over where the data is held and how it is used, in order to be treated fairly and make informed choices about personal data. This will be called **Personal Data Ecosystem Control (PDEC)**.

(ii) to acquire _information about yourself_, so that you might gain insights into your own behaviour, and gain personal benefits from those insights or make changes in your life. This will be called **Life Information Utilisation (LIU)**.

[Figure 7.1](#figure-7.1) shows processes individuals might go through in pursuit of these motives. PDEC is a process of holding organisations to account and managing _what happens_ to personal data, often regardless of what it means. LIU is more concerned with _what the data means_ and its inherent personal value, regardless of where it is stored and how it is used[^13]. This novel motivational model was first proposed in [@bowyer2021twopurposes].

![Figure 7.1: The Two Motivations for HDR: Controlling Your Personal Data Ecosystem and Utilising Your Information About Your Life<br/>(with 'idealised'[^14] processes illustrated)](./src/figs/fig7.1-the-two-motivations-for-hdr.jpg){#figure-7.1}

[^13]: There is some overlap. Organisations hold data to enable interpretation (usually algorithmic) to inform decision making. In this way, organisations are doing LIU for _their_ benefit. This grey area is situated as part of PDEC, because from the individual's perspective, how organisations understand you through information informs decisions that affect your life. As such, it is more likely to enable you to exert control over use of your data than to pursue personal LIU goals.

[^14]: The illustrated processes incorporate existing data access processes such as GDPR, where the only access is through provision of a copy of one's data. This is _not_ ideal, as it creates divergent versions and will quickly become out-of-sync, however for the sake of simplicity that inefficiency is ignored [see [5.6.1](#5.6.1) for improvements to copy-based access].

### Life Information Utilisation (LIU){#7.4.1}

_Life Information Utilisation_ is a superset of _Self Informatics (SI)_ [[2.2.3](#2.2.3)], including all purposes relating to self-monitoring and self-improvement through personal data, but also other uses including creative expression, evidence gathering, nostalgia, keeping, and sharing. Many such desires were expressed in Case Study Two [[Table 5.4](#table-5.4)], and also hinted at in the Early Help context [[4.5.1](#4.5.1)]. While the existence of digitally-encoded information clearly unlocks new possibilities, LIU has existed in some form throughout human civilisation, as seen through analogue processes such as storytelling, journaling and scrapbooking.

The most relevant of the six wants to LIU are _data understandability_ [[6.1.2](#6.1.2)] and _data useability<sup>[11](#fn11)</sup>_ [[6.1.3](#6.1.3)], which relate closely to the HDI concepts of _legibility_ and _agency_ respectively.

### Personal Data Ecosystem Control (PDEC){#7.4.2}

Unlike LIU, _Personal Data Ecosystem Control_ is a _new_ individual need, arising as a result of the emergence of the data-centric world [[2.1](#2.1); [2.2.4](#2.2.4)]. Only when organisations began to collect and store facts about people as a substitute for direct communication and involvement did it become necessary. The more data is collected about individuals, and the more parties doing so, the greater the need for individuals to understand these acts so that they might influence them (or risk their lives being affected in unexpected or unfair ways). PDEC is a direct response to the power imbalance between data holders and individuals [@wef2014lens; [2.1.2](#2.1.2)].

Several of the six wants are important to PDEC: visible data and transparent processes (referred to collectively as _data ecosystem transparency_), and individual oversight and involvement (referred to collectively as _data ecosystem negotiability_, drawing on the HDI concept of _negotiability_). These grouped terms are used below.

Four Objectives for Human Data Relations{#7.5}
----------------------------------------

![Figure 7.2: Mapping the Six Wants into Objectives for the HDR Opportunity Landscape](./src/figs/fig7.2-landscape-objectives.jpg){#figure-7.2}

To offer future value to future researchers, activists and innovators, this chapter contributes a map of the HDR opportunity landscape. This map is expressed in abstract here, and explored in more depth in Chapters [8](#chapter-8) and [9](#chapter-9). First, the six wants [[Chapter 6](#chapter-6)] are transformed into four simple _landscape objectives_ which shape the ultimate goals for effective HDR in this landscape of opportunity:

  1. Data Awareness & Understanding;
  2. Data Useability<sup>[11](#fn11)</sup>;
  3. Data Ecosystem Awareness & Understanding[^15] and
  4. Data Ecosystem Negotiability<sup>[14](#fn14)</sup>.

[^15]: To avoid overly cumbersome wording, subsequent sections will drop the 'Data' prefix from 'Data Ecosystem Awareness & Understanding' and 'Data Ecosystem Negotiability'.

As [Figure 7.2](#figure-7.2) shows, the need for data to be understandable, visible and useable applies to all types of data, whether it is interpretable as _life information_ or _ecosystem information_.

Better Human Data Relations as a Recursive Public{#7.6}
-------------------------------------------------

Let us revisit the stance from which we approach the goals of better HDR. This PhD is grounded in participatory action research and experience-centred design [[3.2](#3.2)]. Using a _Digital Civics_ [@vlachokyriakos2016] approach to understand people's unmet needs, we can model how the world should change. Such research is political [[3.2.1](#3.2.1)], seeking to correct an imbalance in the world through _adversarial design_ [@disalvo2012]. Where the Case Studies' track embraced participatory investigation, the embedded research track moves forward from the perspective of an activist researcher, exploring how individuals and groups can actually change their world to meet the established understanding of what should change. By taking this role, we can consider ourselves (those who pursue better HDR, or _HDR reformers_ as a shorthand) as a nascent _recursive public_ [@p2pwikiRecursivePublic]. This term originates in the free software movement to describe:

> _'a collective, independent of other forms of constituted power, capable of speaking to existing forms of power through the production of actually existing alternatives'_–@kelty2008

Being a recursive public means using various means at our disposal to seek to modify the systems and practices we live within in pursuit of our goals. These methods might include participatory research, experience-centred design, software prototyping, rights exertion and campaigning.

This idea of reconfiguring society in this way has been conceived as _civic hacking_ [@crabtree2007; @levitas2013; @tauberer2014]. The collective around HDR reform does not yet exist as single named and identifiable _public_ [@ledantec2016] but there is an emergent trend towards better HDR. HDR reformers today congregate around interconnected and overlapping movements including (but not limited to):

- the _MyData_ community [@mydata2017declaration; [2.3.4](#2.3.4)];
- personal data lockers [@digime2021; @citizenme2021; @sharp2021];
- digital rights campaigners [@openRightsGroup];
- gig economy worker rights [@kirven2018; @wie2022];
- privacy by design [@cavoukian2010];
- privacy activism [@davies1990; @bits2000];
- data justice [@taylor2017; @crivellaro2019];
- critical algorithm studies [@gillespie2016];
- adversarial interoperability [@doctorow2019];
- the 'right to repair' movement [@svensson2018];
- 'makers' and digital DIY enthusiasts [@altsitsiadis2021; @gauntlett2015];
- humane technology [@harris2013];
- self-sovereign identity [@satoru2021];
- user liberation [@edwards2004];
- explainable AI [@explainableAI]; and
- responsible AI [@osullivan2021].

Summation: HDR—A Landscape Ready to Explore{#7.7}
---------------------------------

The commonality to so many groups [[7.6](#7.6)] suggests HDR reform is an emergent cultural phenomenon, whether or not a single identifiable public coalesces. Time will tell whether _Human Data Relations_ as laid out in this thesis is sufficient to give form to that phenomenon. At the least, HDR offers a descriptive umbrella term. The breadth of research, innovation and activism validates the need _and_ the desire for such a recursive public around HDR reform to exist. In fact, it already does exist, whether named and unified or not. There is a growing desire to take back control of technology for the betterment of humankind. Therefore, in the next chapters this thesis takes an unashamedly critical view of the status quo, favouring the disruptive societal changes these movements seek. The HDR research agenda poses (from a data-oriented design standpoint) an important question of society:

> **_"How can we change the world into the one we want?"_**

This chapter has established a clear scope and motivation for the new research agenda of Human Data Relations. This sets the stage for the next two chapters, which describe this researcher's efforts to pursue the HDR agenda in practice as part of his role in embedded academic and industrial project work. The next chapters will take the reader on a journey of exploration through the HDR landscape, recognising the design implications of law and the commercial realities of design and considering the above question in more detail. By highlighting the pitfalls and opportunities that exist, the objective is for this thesis to provide actionable principles and approaches for HDR reform practitioners that can help nascent movements toward HDR reform to flourish.

It is important to note that the Human Data Relations research agenda, while it views a change from the data-centric status quo as positive, does not imply that to be an HDR reformer one must be an activist. While adversarial design [ADD FORWARD REF] and collective activism [ADD FORWARD REF] are clearly useful approaches to progress HDR, systems can also be changed from within. Designers and thought leaders within data-centric organisations and governments could embrace HDR's objectives themselves. The fact that so many of the HDR reform communities mentioned in the previous section are somewhat activist in nature, is more of a reflection of the reality that the goals of HDR cannot easily surface within the dominant digital commerce paradigms of today, and so people - pursuing both individualist [ADD BACK REF] and collective agendas [ADD FORWARD REF], operate at the grassroots level, and may seem to many to be activists. While this thesis leans more into the activist angle of HDR research, motivated by the researcher's background [ADD REF TO BACKGROUND], balance is sought through the fact that the embedded project work track has included work in projects both inside [ADD REF TO BBC, SILVER] and outside [ADD REF TO HESTIA, DERC] of the system.

What follows in Chapters [8](#chapter-8) and [9](#chapter-9) is deliberately broad and open-ended[^16]. It does not provide a complete answer to this question or the extended research question [[7.1](#exRQ)], nor could it. This thesis does not pretend to be complete or definitive in its interpretation of the outlook for HDR. Alternative interpretations and schools of thought than HDR exist. What follows is not a strict roadmap, but rather a preliminary model based on a sampling of ongoing work, identified challenges and known opportunities, that can be understood through the remainder of this thesis, leading to the major contribution of this thesis as an actionable research agenda and useful reference material for the pursuit of better human data relations.

[^16]: Some of the challenges and opportunities described in the next two chapters are covered in greater detail than others. This corresponds only to this researcher's proximity and depth of engagement with those ideas, rather than their relative merit, complexity or impact potential. Given the broad aim to chart a new area of research, it is considered to be more useful to introduce a range of applicable ideas, even if some are only lightly detailed, than to document just a few.

---
