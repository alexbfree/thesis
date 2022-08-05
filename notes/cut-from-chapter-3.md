### Context Three: The Practical Pursuit of Better Human Data Relations
[TODO move / reposition this to be external to the thesis, maybe omit entirely]

The third context for this PhD, which has remained a parallel focus throughout, is a more practical one; to go beyond just understanding people's perspectives but to look, in the context of what we learn about people's desires for their data and their relationships, at what is currently possible in practice. The goal is to find out what factors shape the design and implementation of real world data interaction systems and processes, to understand what legal, social, economic, technical or political factors come into play and importantly, to explore what technologies or techniques might be able to pursue human-centric design goals in a data-centric world. In scope, this context is a broad one, encompassing all forms of personal data interaction; as such it is able to draw on the findings of RQ1 and RQ2 from the first two contexts, viewing those as "needs" or "requirements" that would ideally be met through the design and pursuit of new interfaces, policies and practices.

In total four separate research activities beginning in 2017 and continuing through to 2022 and beyond have taken place within this practical research context, outside of the Case Studies but very much drawing upon and feeding insights back into the developing findings, and thus part of the action research cycle of this thesis [[3.2.2](#3.2.2)].

These activities relate to this thesis not as case studies but as exemplars to illustrate possible avenues for bringing about better Human Data Relations in practice (RQ3) [TODO deformalise RQ3]. Chapter 7 examines the practicalities of bringing about the desired changes.

#### Health Data Interface Development: CHC's SILVER project

The embedded role I took in the SILVER project described in section 3.4.1.1 contributes also to this context, as part of my role was as a front-end software developer for a personal data health interface intended for use by support workers in the Early Help context. Learnings from that experience also helped to serve RQ3 [TODO deformalise / remove RQ3]. This aspect of the SILVER project is considered out of scope for this thesis, though reference is made to it in Chapter 7.

#### Obtaining Data and Reconfiguring Data Interfaces through Web Augmentation

[TODO update this section with new paper, possibly shorten a bit too]

As a software developer I have been aware for a long time that one of the biggest challenges in building new data interfaces is to gain programmatic access to the necessary data. As part of the trend towards cloud-based services and data-centric business practices, it has become increasingly difficult to access all of the data held about users by service providers. Application Programming Interfaces (APIs) are a technical means for programmers to access a user's data so that third party applications may be built using that data. Unfortunately, as a result of commercial incentives to lock users in and keep data trapped [@abiteboul2015; @bowyer2018freedata], much of users' data can no longer be accessed via APIs. While GDPR data portability requests do open up a new option for the use of one's provider-collected data in third party applications, this is an awkward and time-consuming route for both users and developers. _Web augmentation_ provides a third possible technical avenue for obtaining data from online service providers. It relies on the fact that a users data is loaded to the user's local machine and displayed within their web browser everytime a website is used, and therefore it is possible to extract that data from the browser using a browser extension. Similarly, once loaded into the browser, a provider's webpage can be modified to display additional data or useful human-centric functionality that the provider failed to provide.

In order to better understand what is and is not possible using this technique, I participated from 2018 to 2020 as a part time web developer in a project which was using the web augmentation technique to improve the information given to users of Just Eat, a takeaway food ordering platform in the UK. While this particular use case does not concern personal data, the technology being used by the project were considered highly relevant, and the goals of the research project were also human-centric, and consistent with our own research goals - tackling power imbalance of service providers in order to better serve individual needs. This research project is not detailed within this thesis, and is not considered a primary study for this PhD, but is referenced within Chapter 7. The paper which published the study is [ADD REF goffe _ET AL_], which is included in [ADD APPENDIX REFERENCE TO GOFFE ET AL PAPER HERE].

#### Personal Data Store Research: The BBC R&D Cornmarket Project

[TODO: Diminish this so it is no longer a case study just a contributing piece of work]

Within the personal data interface design context, I undertook my second embedded research activity within the PhD. For an eight month period (three months full time and five months part time) beginning in early summer of 2020, I was a research intern in the British Broadcasting Corporation's Research and Development department. The BBC has a public remit to carry out research and development in the broadcast, media and information space, including HDI [@bbcrd2017], and has over 200 researchers. I was assigned to a project codenamed Cornmarket, a collaboration between user experience designers, researchers and developers which aimed to explore a new role for the BBC in extending its public service role beyond broadcasting into personal data stewardship. The main task was to develop a prototype personal data locker into which people could store everyday data including TV and music media streaming data, health data, and financial data. This provided an excellent opportunity to put all of my learnings acquired thus far for all three RQs into practice, and further deepen my understanding of RQ3 - the barriers and opportunities to actually building new human-centric data interfaces in the real world. [TODO deformalise RQ3] Throughout the internship I was able to explore the problem space from many different angles - sharing my own research expertise, doing competitor analysis and background research, information architecture, data modelling, user experience and user-centred design, technology prototyping and supporting participatory research activities. This embedded research provided numerous new insights and an opportunity to iterate and develop my theories and models with BBC colleagues.

#### Understanding the Power of Data: Sitra's #digipower Project with Hestia.ai

[TODO add details here]


### Practical Data Experiments, Interface Design and Prototyping{#3.5.4}

![Figure 14: Visual Design Mockup for Life Partitioning in a PDS -- A visual design mockup collaboratively created with BBC Research colleague Jasmine Cox](./src/figs/fig14-pds-partititioning.png)

![Figure 15: Prototype interface for GDPR Data Viewing -- A working prototype that I developed during a hack week at BBC R&D](./src/figs/fig15-prototype-gdpr-interface.png)

![Figure 16: SILVER Health Data Viewing Interface -- A working health data viewing interface for Early Help support workers that I developed as part of the SILVER project](./src/figs/fig16-silver-data-interface.png)

In the BBC placement in particular, and also in the Self GDPR Experiments of Context Two and the development aspects of the embedded SILVER placement in Context One, the focus was not on uncovering individual perspectives, but on direct experimentation in the world to discover constraints and possibilities -- in line with the philosophy of Deweyan pragmatism referenced in 3.1. To design a better future, we must understand the world at it is, not just as people perceive it. Another justification is that as a designer or software developer, we need not only user requirements but knowledge of actual constraints and possibilities for implementation if we are to create something that is realistic and feasible for use in the real world. With this in mind, I conducted many practical explorations of data interaction throughout this thesis. Loosely these could be divided into design activities, prototyping, and interface development.

As part of my placement at BBC R&D, I co-designed a conceptual personal data locker interface for unifying a user's data from different sources and then partitioning it into different 'areas of life'. Our design was mocked up visually by BBC colleague Jasmine Cox and is shown in Figure 14. Imagining and iterating on possible interface designs and user flows is an important part of the process of prototyping possibilities - some ideas seem viable until you actually try to detail them.

As mentioned in 3.4.2.3, I had been gathering my own data from GDPR requests since 2018. This 'testing what is possible' of GDPR processes provided valuable insights to inform both RQ2 and RQ3 [TODO deformalise RQ3], but also provided me with copies of my own personal data. At BBC R&D, I participated in 'hack week' as part of which explored possibilities for personal data locker interface designs. I used the data I had retrieved via GDPR and built a prototype user interface in JavaScript, shown in Figure 15, that would import data files from different parts of life and extract information that could then be used to categorise and display my own data. Doing this activity heightened my understanding of what is possible with real GDPR-retrieved data, and the complexities of dealing with it and analysing it in practice.

As a front-end developer embedded within the SILVER project, I was responsible to build a functional user interface for support workers to explore health data, illustrated in Figure 16. This provided an opportunity to put the ideas of timelines and Temporal PIM (see section 2.2.2) into practice and explore which features are most useful; the SILVER project ran an evaluation workshop of this software with support workers at a local council which provided further insights into which features are most valuable when interacting with personal data.


![Figure 19: A Model for Personal Data -- Developing a common model for personal data imported into a PDS a part of BBC Cornmarket R&D work](./src/figs/fig19-life-modelling.jpg)



----


### Thesis structure approach

[TODO CUT THIS SECTION AND COVER IT IN INTRO]

In writing up this thesis, I made a choice to foreground my two most major research activities as Case Studies, and not to detail the other activities carried out beyond the high level summaries included in this chapter. Case Study One and Two both span research questions RQ1 and RQ2 (see [Figure 3.2](#figure-3.2) in section 3.4) as they explore both people's direct relationship with data _and_ the relationships people have that indirectly involve data. The learnings that allow me to explore and draw conclusions that serve RQ3 [TODO deformalise RQ3] come from a variett of practical activities, described in 3.4.3 above, all focused on designing and bringing about better human data relations in practice.

Because of the overlapping of RQs 1 and 2 in Case Study One and Two, I have structured the subsequent chapters as follows:

* Chapter 4 details Case Study One in the context of both RQ1 & RQ2.
* Chapter 5 details Case Study Two in the context of both RQ1 & RQ2.
* Chapter 6 is the first discussion chapter, which separately unifies RQ1 findings and RQ2 findings, so that they can be referenced in general terms as distinct understanding of people's wants in their direct relationships to data (RQ1) and their wants in relationships with those who hold data about (i.e. their indirect relationships to data) (RQ2), drawing from insights that span both case studies.
* Chapter 7 is the concluding discussion chapter, which examines how those needs identified in Chapters 4, 5 and 6 might be achieved in practice, through software development, education and civic action. This covers all three research subquestions and draws these together to address the main research question.



----

and how they want it to be used, and how could people's desires for the role data plays in their lives be brought closer to reality


----

In this thesis, and its title I use the term _'human data relations'_ to encompass both of these aspects - human-data relations (the individual's relationship to their data, as imagined by HDI), but also human data relations, i.e. human relationships that involve data.

----

In parallel to this, I was began to conduct my own experiments using GDPR to see and explore my own data. This allowed me to sensitise myself to the research space, and to enhance my understanding of RQ3 (finding out more about what is and is not possible in practice when it comes to everyday personal data access) [TODO deformalise RQ3] but also crucially it enabled me to become a participant in my own research, enabling a deeper understanding of this research context.

----

In chapter 7, a similar approach was used, although in this case as this was not a participatory engagement, the source text was my own captured field notes informed by design materials and other digital files created as part of the research placement.

-----

cut from epistemology section:





 but are constantly tested and re-evaluated by their practical experiences of the world. In particular

To me this is an overriding truth about reality and this focus on understanding change, as perceived by individuals, is a key research motivation. Where constructivists may focus more upon deeply understanding an individual's reality at a moment in time, .

I also look to



 At this point we must consider the individual's motivation for constructing and pragmatically changing their concepts of the world, and to understand this we can look to _objectivism_ [@peikoff1993], the philosophy put forward by Ayn Rand, which is a belief that the mind, informed by the senses, is the means by which we discover truths about the world, and it does so by forming concepts and using _inductive reasoning_ [@smith2011] (in essence, "if these things are true then what else must be true?") to acquire knowledge).

Objectivism also states As a final philosophical element to incorporate,
