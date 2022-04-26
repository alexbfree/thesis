Discussion II: Designing and Pursuing Better Human Data Relations {#chapter-7}
=======================

> _"Civilizations advance not by the technology they know about, but by the technology they don't have to know about."_ -- Anonymous proverb

Chapter Overview
----------------

Through the Case Studies (Chapter 4 & 5) and the discussion in Chapter 6, a clear understanding of what people want from direct and indirect data relations (RQ1 & RQ2) has been established. In this chapter, we turn our attention from theory to practice, from what is needed to *what is possible*. Specifically, this chapter will answer RQ3, which asks the practical question _'What challenges and opportunities are relevant when pursuing better Human Data Relations?'_. Throughout Context Three (3.4.3), which consists of my embedded work in four industrial and academic research projects during the course of my PhD, I have been able to explore how better Human Data Relations (HDR) can be pursued in practice. This chapter aims to provide a roadmap, illustrated with real world insights and activities, and building upon the theoretical insights from the Case Studies, to inform the design of future research, innovation and policy.

In section 7.2, the concept of HDR is expanded to identify its two key purposes, which are used in section 7.3 as a framing to present identified obstacles and opportunities. Section 7.4 summarises the roadmap in a Theory of Change context, and section 7.5 concludes the thesis, summarising its contributions and answering the overall research question.

### Practical Research Settings

The majority of examples and learnings shared in this chapter come from my participation as an expert researcher in two industrial research projects:

1. **BBC R&D's Cornmarket Project**, which explored through UX design and participatory research, how individuals might interact with data through a Personal Data Store interface (see 3.4.3.3)
2. **Sitra/Hestia.ai's #digipower Project**, a successor to Case Study Two, in which European politicians examined companies' data practices through data rights and technical audits (see 3.4.3.4)

In addition, my participation as an interface designer and front-end software developer in the following two academic research projects contributes secondarily to this chapter:

3. **Connected Health Cities (CHC)'s SILVER Project**, where I, along with a backend developer and a team of researchers, developed a health data viewing interface for Early Help support workers (see 3.4.3.1).
4. **Digital Economy Research Centre (DERC)'s Healthy Eating Web Augmentation Project**, which explored the use of web augmentation techniques to modify the user interface of takeaway service Just Eat in support of healthy eating (see 3.4.3.2).

### Attribution of Insights

While this thesis is my own original work, some of the specific details, theories and ideas presented in this chapter arose or were developed through close collaboration, discussion and ideation with other researchers, including:

 - Jasmine Cox, Suzanne Clarke, Tim Broom and Alex Ballantyne at BBC R&D;
 - Paul-Olivier Dehaye and Jessica Pidoux at Hestia.ai;
 - Stuart Wheater of Arjuna Technologies and Kyle Montague of Open Lab during the SILVER project; and
 - Louis Goffe of Open Lab on the DERC Healthy Eating project

Due to these collaborations and the ongoing and parallel nature of all of these projects to my PhD research, it is impossible to precisely delineate the origin of each idea or insight. In practice, ideas from my developing thesis and own thinking informed each project's trajectory and thinking, and vice-versa. These ideas would not have emerged in this form without my participation, so they are not the sole intellectual property of others, but equally I would not have reached the same conclusions alone, so the ideas are not solely my own either. All diagrams and illustrations were produced by me, except where specified, and the overall synthesis and framing presented in this chapter is my own original work. Where this chapter includes material from the four projects, that material is either already public, or permission has been obtained from the corresponding project teams.

Expanding the Concept of Human Data Relations
---------------------------------------------

Chapter 6 established six 'wants' in HDR: visible, understandable and usable data; process transparency and individual oversight and involvement. At a simplistic level therefore 'better' HDR can be achieved by working to improve upon those six aspects of data interaction. However, as this section will explain, HDR can be conceptually split into two distinct purposes, to which those six wants apply differently, therefore it is worth spending the time to develop the concept of HDR further. As background understanding for this duality of purpose, it is first necessary to examine more closely what role data plays in people's lives.

### The Role of Personal Data

In the modern world, where almost anything can be encoded as data, and many previously analogue objects and activities now have digital equivalents, the concept of data has become broad and hard to pin down. Key to Human Data Relations (and indeed part of this thesis's main RQ) is to explain what role data plays in people's lives. Through the Case Studies and Research Settings and my prior learning, I have identified 8 distinct ways to consider what data *is* to people and how they might relate to it. These are modelled in Table 15.

Table: Table 15. **Eight lenses on data**.

| Way of thinking about data | Explanation & Implications |
|:--------|:---------------------------------------------------|
|Data as property|Data can be considered as a possession. This highlights issues of ownership, responsibility, liability and theft.|
|Data as a source of knowledge about you|Knowing that data contains encoded assertions about you and can be used to derive further conjectures, enables thinking about how it might be exploited by others, but also how you can use it yourself for reflection, self-improvement and planning. It invites consideration of the right to access, data protection, and issues around accuracy, fairness and misinterpretation / misuse.|
|Data as part of oneself|A photo or recording of you, or a typed note or search that popped into your head could be deeply personal. This lens on data highlights issues around emotional attachment/impact, privacy, and ethics.|
|Data as memory|Data can be considered as an augmentation to one's memory, a digital record of your life. This lens facilitates design thinking around search and recall, browsing, summarising, significance/relevance, and the personal value of data.|
|Data as creative work|Some of the data we produce (e.g. writing, videos, images) can be considered as an artistic creation. This lens enables thinking about attribution, derivation, copying, legacy and cultural value to others.|
|Data as new information about the world|Data created by others can inform us about previously unknown occurrences in our immediate digital life or the wider world. This lens is useful for thinking about discovery, recommendations, bias, censorship, filter bubbles, and who controls the information sources we use.|
|Data as currency|Many data-centric services require data to be sacrificed in exchange for access to functionality, and some businesses now explicitly enable you to sell your own data. This lens highlights that data can be thought of as a tradable asset, and invites consideration of issues of data's worth, individual privacy, exploitation and loss of control.|
|Data as a medium for thinking, communicating and expression|Some people collect and organise their data into curated collections, or use it to convey facts, ideas or to evoke an emotional impact. This lens is useful to consider data uses such as lists, annotation, curation, editing, remixing, and producing different views of data for different audiences.|

When considering HDR, it is important to recognise that people may think of their personal data through any or all of these _'lenses'_ [@karger2005;2.2.2] at any given time, and any process or system design involving data interaction should take these into account.

Looking across this set of lenses, it is possible to identify four specific roles that data can serve:

1. Data has a role as an **artifact of value** to your life;
2. Data has a role in **informing** you about yourself, the world, and the actions of others that may affect you;
3. Data has a role as **a usable material with which to effect change** in your life;
4. Data has a role as **a means to monitor** data holders' behaviours, digital influences upon you and changes within your life.

### Human Data Interaction or Human Information Interaction?

To unpack HDR further, we next need to highlight the difference between humans relating to data, and humans relating to information. Human Data Interaction (HDI) concerns the way people interact with data. Mortier _et al._  [@mortier2013;@mortier2014] defined the field of HDI without distinguishing data (the digital artifact stored on computer) from information (the facts or assertions that said data can provide when interpreted). This is an important distinction. Originating in library sciences, the parallel field of Human Information Interaction (HII) is well established, and considers the way humans relate to information without regard to the technologies involved [@marchionini2008]. As William Jones observes, these two fields should be examined together [@jones2006]. As DIKW theory highlights (see 2.1), **interpretation of data to obtain information** is a discrete activity. This was borne out in the findings of Case Study Two, where it became clear that participants need to relate both to data, and to information (5.4.3.2). Access to data and information is critical to both understanding and useability, as detailed in section 6.1.2 and 6.1.3.

In considering Human Data Relations, there are in fact three distinct aspects to consider:

1. _data_ - the stored digital artifacts pertaining to users held by organisations for algorithmic processing, copies of which can be obtained using individual data rights.
2. _information about individuals_ - the collection of facts and assertions about the individual and their life, which are obtained through interpretation (or in some organisations' case, through analytical inference).
3. _information about data_ (also identified in Table 9 / 5.3.1 as _metadata_) - facts about the data, such as where it has been stored, who has accessed it, how it was collected, or when it has been shared externally.

### The Two Distinct Purposes of Human Data Relations

By making this distinction between the two types of information which people might interact with and considering the six wants in Chapter 6, it becomes clear that there are two very different reasons why people might want better HDR:

(i) to acquire _information about one's data_, so that one might exert control over and make informed choices about where _the data_ is held and how it is used in order to be treated fairly and gain more control over the use of personal data. This is *Personal Data Ecosystem Control (PDEC)*.

(ii) to acquire _information about oneself_, so that one might gain insights into one's own behaviour and gain personal benefits from those insights or them to make changes in one's life. This is *Life Information Utilisation (LIU)*.

The two distinct processes that individuals might go through in pursuit of these purposes are exemplified in Figure 29. PDEC is a process of holding organisations to account over and managing _what happens to personal data_, often regardless of what it means, whereas LIU is more concerned with _what the data means_, regardless of where it is stored and how it is used[^13]. The two purposes of HDR are further detailed in [@bowyer2021].

[INSERT DIAGRAM - Figure 29]

[^13]: Of course, there is some overlap; the reason that organisations hold data is so that they can interpret it (usually algorithmically) to inform decision making. In this way, organisations could be seen to be doing LIU for their own benefit. From a human-centric perspective, this grey area is situated as part of PDEC, as from the individual perspective, how organisations understand you through information will inform decisions that affect your life and so is part of the reason why one might want to exert control over data use rather than being part of exploiting data to gain self-insights and personal benefits.

#### Life Information Utilisation

Life Information Utilisation is a superset of Self Informatics (SI), as defined in 2.2.3. It includes all purposes relating to self-monitoring and self-improvement through data, but also includes all other uses of personal data including creative expression, evidence gathering, nostalgia, keeping, and sharing. Many of these desires were expressed in Case Study Two (see Table 12 in 5.3.3), and also hinted at in the Early Help context (4.4.1). While the existence of digitally-encoded information clearly unlocks new possibilities, LIU has existed in some form throughout modern civilisation, as seen through analogue processes such as storytelling, journalling, scrapbooking, arts and crafts.

In the LIU context, the most important wants to focus on improving are Understandability of data (6.1.2) and Useability of data (6.1.3), which relate closely to the HDI concepts of _legibility_ and _agency_ respectively. Obstacles and opportunities for Understandability and Useability will be explored in 7.3.1.1 and 7.3.1.2 respectively.

#### Personal Data Ecosystem Control

Unlike LIU, Personal Data Ecosystem Control is an individual need that is new; arising as a result of the emergence of the data-centric world (2.1, 2.2.4). It was only when organisations began to collect and store facts about people as a substitute for direct communication and involvement that it became necessary. The more data is collected about individuals, and the more parties collect and share that data, the greater the need for individuals to learn about that data so that they might influence its use (or risk their lives being affected in unexpected or potentially unfair ways). PDEC is a direct response to the power imbalance the World Economic Forum described in 2014 [2.1.2;@wef2014lens].

In the PDEC context, multiple data wants are important: visible data and transparent processes, as well as individual oversight and involvement. For simplicity, the former two wants will be handled collectively as _"Ecosystem Transparency"_, and the latter two as _"Ecosystem Negotiability"_ (drawing on the HDI concept of _negotiability_). Obstacles and opportunities for improving HDR in these two grouped areas will be explored in 7.3.2.1 and 7.3.2.2 respectively.

Answering RQ3: What are the challenges and opportunities?
---------------------------------------------------------

In this section, the third RQ will be addressed: _What challenges and opportunities are relevant when attempting to meet the six wants of human data relations?_ The answers to this question are represented as discretely named ideas: either practical obstacles observed and practical opportunities identified. Within the simplified groupings of wants detailed above, these are conveyed as follows:

- _Obstacles_ are illustrated through learnings and insights from the projects (7.3.1.1.1, 7.3.1.2.1, 7.3.2.1.1, 7.3.2.2.1)
- _Opportunities_ are illustrated using conceptual models and design ideas from the projects (7.3.1.1.2, 7.3.1.2.2, 7.3.2.1.2, 7.3.2.2.2)

### Challenges and Opportunities in Life Information Utilisation

#### Understandable Data

##### Obstacles to Data Understandability

**Unrelatable data**.
[Meaningfulness / relatability -> relate it to people/places/events] [Context - Life - > need life interfaces]

**Lack of Legibility**.
[Information within Data -> Lack of Visualisations and Tools] [Complexity -> common formats/abstractions/summarisations]

**The Personal Data Diaspora**.
[Scatteredness -> holistic/unification, place to centralise] [My data is everywhere I am nowhere]

##### Improving Data Understandability

**Unified Life Information Storage**.
[Use standards & semantics to convert data to life information]. [Personal data Stores as place to put stuff] [Data Trusts]

**Meaning Extraction Software**.
[Build systems to extract meaning - interpreting and combining signals] [Semantic/content analytics]

**Life Information Interfaces**.
[presenting and visualising life information]
[Alternative Perspectives: temporal, entity-based/relational and geographical exploration] [relate to subjectivity]

#### Useable[^14] Data

[^14]: The words _'usability'_ and _'usable'_ (spelt without an 'e') most commonly refer to a judgement of the degree to which a website or user interface is easy to use [@nielsen2012]. Throughout this thesis, I deliberately use the alternative word spellings of _'useability'_ and _'useable'_ [@dictUseability; @dictUseable] respectively, to clearly distinguish from this ease-of-use concept and to denote that I am referring a different meaning: the more literal definition, i.e. _"the quality or state of being convenient and practicable for use"_ [@dictUsability; @dictUsable]. Any usages without an 'e' can be taken to refer to the interface ease-of-use concept.

##### Obstacles to Data Useability

**Trapped Data**.
[Trapped Data -> Force unlocking of data through technical means or regulatory influence]

**Integration Challenges**.
[Integration challenges -> Need to be able to bring data together and connect and combine]

**Lack of Malleability**.
[Lack of malleability -> need to be able to slice/group/view from different perspectives]

**Inability to Investigate**.
[inability to investigate -> enable questions, comparisons, investigations etc]

##### Improving Data Useability

**Exploratory Actions & Asking Tools**.
[supporting useful actions on data - filtering, referencing, cross referencing, conjecturing/whatiffing - data action verbs]
[asking tools rather than answers or insights]

**Life Information as Material**.
[data as material, interface features as tools to use that material] [an information operating system]

**PIM & SI capabilities**.
[supporting appropriation, annotation, organisation, curation, use & re-use] [reference 2.2.2 , including adaptability, re-use, etc]
[Reflection & Goals] [support goal setting, tracking and reflection]

#### Other Factors in Life Information Utilisation

**Motivation**.
[Motivation -> Showing the potential]

**Effort**.
[Effort -> doing as much as possible automatically, conjecture and assertion over blank pages. training rather than meticulous instructution.]

**Ecosystem Transparency**.
[how the other wants fit in, visibility as it pertains to Life info, transparency/oversight/involvement etc]

**Agency & Ecosystem Negotiability**.
[agency over trapped data (by tech or by companies (lead into next)]

### Challenges and Opportunities in Personal Data Ecosystem Control

#### Ecosystem Transparency

##### Obstacles to Ecosystem Transparency

**Introspective Practices**.
[hidden data and closed processes -> closed by default thinking -> encourage or legislate for openness.. e.g. data portability/access rights, rights to explanatione etc, but more needed]

**Proprietary, Incompatible Silos**.
[silos and motives towards closed proprietary systems -> highlight the pains]. [lack of standards, motivations against interoperability -> motivate standards and unconver opportunities for interoperability]

**Ecosystem Complexity**.
[complex data ecosystems, adtech]

**A Lack of Metadata**.
[lack of information *about* our data -> awareness and accountability even where access is difficult -> ] [show metadata diagram]

##### Improving Ecosystem Transparency

**Transparency through Regulation**.
[regulation - forcing openness transparency and interop. DSA ? ] [standards for data access - technical standards could make compliance easier to judge too]

**Ecosystem Mapping & Visualisation**.
[ecosystem visualisation and overviews]

**Collective Investigations**.
[collectives - as a means to compare and see more]

**Tap the Seams**.
[exploiting the seams - the battle for the seams]

**Bootstrap 'Data Understanding' Innovation**.
[standards creation and the benefits of enabling a 'data understanding' industry]

#### Ecosystem Negotiability

##### Obstacles to Ecosystem Negotiability

**The Datafication of the Self**.
[data self affects you but cannot see (proxy for involvement, unseen inferences etc)- > find a way to produce better digital selves]. [brings in LDM etc].

**The Technological Hegemony**.
[structural power, resource control, centralisation etc -> uneven landscape -> awareness as first step and systemic change needed to change. ]

**Digital Landscape Manipulation**.
[the four levers of infrastructural power. accumulation of info/surveillance as power. changing available information/actions as power]
[Controlling the landscape of what is knowable, and what is do-able -> recognise the importance of free information landscapes, and make them happen through tech or through regulation]

##### Improving Ecosystem Negotiability

**Regulating the Information Landscape**.
[-> better policies to protect the information landscape? DSA.]

**Unionisation**.
[collectives, as a means to ask collectively /demand change, supported by policy (uber, ref GDPR guidelines?)]

**Self-Profiling**
[better digital selves -> people as source of data. profiles and curated as better representation of self, ref past calls in C4&5 for stewardship, user-contributed data etc] [Can also hint at VRM style declarations] [Better data, which you control; but also less uncontrollable effects]

**Taking Back Power in the Browser**.
[-> exploiting the seams in order to produce new information presentations... ref JE paper (+colin?) -> web aug, firefox containers. Taking Back Power In The Browser, resist moves to apps]

**Free Information Landscapes**.
[the battle for landscape control - RSS, API, 3P interfaces, etc, Defending The Seams And Protecting Interface Freedom]. [information surfaces]. [reclamation and repurposing]

#### Other Factors in Personal Data Ecosystem Control

**Inclusive Information Flows**.
[Feeds and flows that loop in the data subject (default not opt in)] [Delay] [Lack of up to date insights / delay]. [Rivers of Information]

**Data Literacy**.
[data literacy and rights awareness - you should teach this in schools]. [Rights Inconsistencies]. [Inconsistent and difficult data rights offerings]

A Theory Of Change Perspective on Better Human Data Relations
-------------------------------------------------------------

[the four change quadrants for each of the two purposes. diagrams to work out].

Thesis Conclusion
-----------------

[reiterate the answer to the question - the key 4 roles, 3 capabilities and N approaches needed for better human data relations]

[clarify the contribution of the thesis, with backreferences - 2 case studies, RQ answers, and the HDR roadmap]

[highlight future value/societal implications of the work]
