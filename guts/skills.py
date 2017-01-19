# _*_ coding:utf-8 _*_
from __future__ import unicode_literals

import sys
reload(sys)  
sys.setdefaultencoding('utf8')

import mechanize
from BeautifulSoup import BeautifulSoup
import urllib2 
import cookielib
import requests
import random
import time
import os

from qually_dj.qually_dj.jobs.models import Keyword
from qually_dj.qually_dj.jobs.models import JobAd

resume = """"QUAI LOREN WENTT
845-825-0101||quai.wentt@gmail.com

EXPERIENCE
Software Development Student, Ada Developers Academy (August 2016 - August 2017) 
•	Intensive training in full stack software development, with exposure to and implementation of a wide variety of languages, frameworks, and methodologies.
•	Emphasis on collaboration, leadership, Agile practices, and computer science fundamentals.

Research Assistant, Veterans Affairs Health Care System (April 2015 – June 2016)
•	Assisted in database management
•	Wrote VBA macro that extracts patient data from database and outputs a personalized report

Technical Writer Associate (Intern), Qualcomm (October 2014 – December 2014)
•	Edited internal documents for proper format, legal statements, and language mechanics according to style guide
•	Edited engineering white papers for content, structure, and spelling/grammar
•	Distinguished performance at internship; (Read recommendation on LinkedIn)

Freelance Writer/Editor, Independent Contractor (January 2014 – August 2016)
•	Wrote marketing copy, website content, and white papers
•	Edited academic papers in various writing styles (APA, MLA, Chicago, AMA) for submission to peer-reviewed journals

Chemical Defense Program Manager/Platoon Leader, US Army (October 2012 – January 2014)
•	Ensured unit preparation for a chemical, biological, or nuclear attack by:
o	planning and executing training exercises
o	ordering and ensuring maintenance of $40K worth of equipment
o	inspecting lower level units and assisting them with meeting standards
o	giving biweekly presentations regarding status of program
•	Rebuilt a failing program into most improved program in the organization in a matter of months
•	Managed of a platoon of 25 soldiers in preparation for overseas deployment

EDUCATION
United States Military Academy at West Point (2012)
Bachelor of Science in Psychology, with a concentration in Computer Science (GPA: 3.4)

SKILLS
Experience with and affinity for learning programming languages
•	Ruby on Rails, DJango/Python, Java
Exposure to tools/languages for front-end development
•	HTML/CSS, Javascript, Backbone JS
Familiarity with database design/implementation
•	Access, MS SQL Server, MySQL, SQLite, Postgres

ACCOMPLISHMENTS
•	Qualcomm Coin of Distinguished Achievement for performance during internship in 2014
•	Basic Parachutist (Certified to safely exit an airplane at 1250ft by static line parachute)
"""

job1="""Software Engineer--Networking stack 
Adara Networks - San Jose, CA 95131
Indeed Hire is in partnership with ADARA Networks. ADARA Networks is an industry leading developer of production-ready and vendor-neutral Software Defined Networking, Virtual Computing, and Networking solutions.

The engineering team at ADARA Networks is responsible for developing and maintaining a Networking Stack System. Tasks include but not limited to design, develop, and troubleshoot proprietary code and open standards code in the IP stack and other areas as deemed necessary. Ensure rapid high quality delivery of high availability systems.

General Requirements:

Results driven, motivated to succeed in fast paced intensive agile development environment; not seeking a set hours waterfall development position
Ability to be creative, efficient, and productive with minimal supervision or guidance.
Must be able to work both alone and as an efficient, cooperative member of a team.
Must be able to give and receive constructive criticism.
Experience Requirements:

Hands on direct development for 3+ years of networking product development experience in the development based upon deep knowledge of Routing and Switching Protocols including the algorithms underlying these protocols.
Good knowledge of packet forwarding in Control and Data Path (RIB and FIB).
Expert understanding of layer-3 and layer-2 network protocols and technologies required; specifically OSPF, BGP, RIP, EIGRP IS-IS, IGMP, PIM, STP; including debugging, analysis and extensions
Good understanding or MPLS, RSVP and extensions (e.g. TE)
Good understanding of ECMP, Multi-Path Networking, Solid understanding of TCP/IP networking; socket programming.
Good Knowledge of RTP, RTSP and Streaming Multimedia Protocols
Solid knowledge of SDN:
Open v Switch and Controllers
OpenFlow OVSDB and other SouthBound APIs
REST and other NorthBound APIs
Good knowledge of concurrency and synchronization issues/techniques in a multi-threaded and multiprocessor environment.
Knowledge of kernel-bypass frameworks (such as netmap, DPDK, libzero) is a plus.
Knowledge of Single Root I/O Virtualization (SR-IOV) is a plus.
Free BSD and Linux kernel knowledge is a plus.
Knowledge of Storage Protocols a plus.
Good oral and written communication skills.
3+ years of industry experience.
Education:

BS/MS in CS, EE, or related area.
Job Type: Full-time

Job Location:

San Jose, CA
Required education:

Bachelor's
Required experience:

Software Engineering: 3 years
Software Defined Networking (SDN): 3 years"""

job2="""Veritas enables organizations to harness the power of their information, with solutions designed to serve the world’s largest and most complex heterogeneous environments. Veritas NetBackup is the world's leading backup and recovery solution for enterprise data centers and hybrid clouds. With its vast array of hardware, operating system, virtualization, database, application, and storage-related technologies, the modern data center is a complicated place. That’s why NetBackup has long been the trusted choice for enterprises seeking to reduce that complexity and make data protection as manageable as possible for their limited staff. NetBackup is a single solution for the entire enterprise, available on a converged platform, and instrumented to require minimal administration in even the largest, most dynamic environments.
Joining the globally distributed Engineering team, you will be working with highly skilled engineers on one of Veritas’s leading and highest revenue earning flagship software product.
We’re looking for software engineers with the ideas and innovative approach to take us into the future. You will need to have degree in Computer Science or a related discipline with a focus on Software Engineering such as IT, Computer Studies or Sciences. You’ll have the confidence to speak up, suggest new ways of doing things and give our business a fresh impetus. Full of enthusiasm, creative and naturally curious, you’ll have a real talent for solving problems.
Responsibilities:
Be a part of a development team following the AGILE development process, responsible for delivering feature content including test automation for product releases
Develop cross-platform (Unix, Linux, and Windows) software
Design and develop the test automation infrastructure needed
Be point of contact in team for quality related aspects – includes test plan, collaboration with system test engineers, other test process’s
Planning and commitment of sprint goals to meet the definition of done.
You will be accountable for high quality and timely delivery of feature and sprint commitments to meet the definition of done for areas you own
Participate in reviews of requirements, design, source code, and supporting documentation
Troubleshoot and resolve product issues through teamwork
Participate in improvement of existing development and testing procedures and processes 
Skills:
Strong QA test automation knowledge including hands on experience with couple of test frameworks
Strong coding and debugging skills in Java, JUnit, Perl, any other scripting languages. Working knowledge of C/C++
Strong analytical thinking and ability to analyze and optimize existing software applications for purpose of maintenance or redesign.
Demonstrable understanding of UNIX/Windows system components and their interactions a plus, including file systems.
Strong background in OO concepts, and multi-threaded programming.
Knowledge of enterprise level software deployment
Nice to have working knowledge of REST based API development
Education and Experience:
Masters degree and/or 2-4 years of experience
Experience in an Agile environment"""

job3 = """Job Description
 
Software Developer 2 - 73642
Description
 
The Department of Biomedical Data Science (DBDS) is recruiting a Software Developer to support key production projects in the Department of Radiology and the Stanford Cancer Institute (SCI). Radiology and SCI focus the world-class expertise of researchers and clinicians on the most critical issues in research and medicine today. Multidisciplinary teams work to transform detection, diagnosis, treatment and prevention discoveries into the most advanced patient care available. These aspects make this a particularly exciting opportunity for candidates seeking stimulating technological challenges, expansion of software development skills including use of cutting edge software technologies, and a leading role in producing applications that will have real-world impact on patient care and scientific advancement. 

DBDS was started in order to create an integrated field of biomedical data science provide and cultivate an intellectual home for collaborative research. As a basic science department, DBDS is devoted to the development of novel computational and statistical methods for acquiring, representing, storing, and analyzing biological and clinical data at all scales. 

This purpose of this position is to design, build and implement robust and innovative web-based applications for Cancer informatics and Radiology research, including a system to mine clinical and imaging data to personalize patient care. Experience with SQL, relational databases and web application frameworks is expected.

Duties include:
Conceptualize design, implement, and develop solutions for complex system/programs independently.
Work with a variety of users to gain information, and develop intra-system tradeoffs between different users, as necessary; interact with a diverse client base and outside vendor contacts.
Document system builds and application configurations; maintain and update documentation as needed.
Provide technical analysis, design, development, conversion, and implementation work.
Work as a project leader, as needed, for projects of moderate complexity.
Serve as a technical resource for applications.
Compare, evaluate, and implement new features and technologies, and integrate them into the computing environment.
Follow team software development methodology.
Collaborate closely with other software developers. 
* - Other duties may also be assigned.
Qualifications
 
DESIRED QUALIFICATIONS:
Demonstrated ability to develop web applications using open source tools, languages, libraries, and current standards-compliant code.
Expert level knowledge of front-end development languages and ability to hand code HTML, CSS, and JavaScript functions/libraries and link them to backend services and functions.
Familiarity with AngularJS, JQuery and mechanisms of AJAX services
Demonstrated ability in Java/J2EE programming techniques and be familiar with JDBC, JSP, Servlets, MVC Frameworks including Struts2, Spring, Hibernate ORM, REST, JSON, Database Design and SQL optimization techniques 
Solid understanding of web standards and usability methods.
Demonstrated ability to test, debug, and deploy software on Linux platforms and web servers.
Ability to use an Integrated Development Environment (IDE) such as Eclipse to develop, debug, and re-factor existing applications and functional modules 
EDUCATION & EXPERIENCE (REQUIRED):
Bachelor's degree and five years of relevant experience, or a combination of education and relevant experience. 

KNOWLEDGE, SKILLS AND ABILITIES (REQUIRED):
Expertise in designing, developing, testing, and deploying applications.
Proficiency with application design and data modeling.
Ability to define and solve logical problems for highly technical applications.
Strong communication skills with both technical and non-technical clients.
Ability to lead activities on structured team development projects.
Ability to select, adapt, and effectively use a variety of programming methods.
Knowledge of application domain. 
PHYSICAL REQUIREMENTS*:
Constantly perform desk-based computer tasks, grasp lightly/fine manipulation.
Frequently sitting.
Occasionally stand/walk, use a telephone. 
Rarely writing by hand, lift/carry/push/pull objects that weigh up to 10 pounds.
Strong visual acuity.
* - Consistent with its obligations under the law, the University will provide reasonable accommodation to any employee with a disability who requires accommodation to perform the essential functions of his or her job."""
job_descriptions = [job1,job2,job3]

cj = cookielib.CookieJar()
br = mechanize.Browser()

br.set_cookiejar(cj)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)




user_agents=['Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A',
			'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3',
			'Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/20110201',
			'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko'
			]

#pick a random user-agent to try to pretend not to be a bot
br.addheaders = [('user-agent',  random.choice(user_agents)),
('accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')]

#log in
br.open('https://www.jobscan.co/login')
 
br.select_form(name='reg')

br.form['email']= 'quai.wentt@gmail.com'

br.form['password']= 'qually123'

br.submit()

# go to job/resume scan page
br.open('https://www.jobscan.co/')

br.select_form(name='form')
br.form['cv']= resume
br.form['jd']= job_desc
# for f in br.forms():
# 	print f
br.submit()


soup = BeautifulSoup(br.response())

# get skills
skills=soup.findAll("span", attrs={"data-skillkey":True})

# get categories
categories = soup.findAll(attrs={"data-skill":True})


keywords =[]
for skill in skills:
	keywords.append(skill.getText())
for cat in categories:
	keywords.append(cat.getText())
	
# get unique values by chaging it to a set
keywords = set(keywords)

# for all keywords, put it in keyword database
# if it is not in there already
for kyword in keywords
	try:
		Keyword.get(name=kyword)
	except Keyword.DoesNotExist: 
		Keyword.create(name=kyword, category='none')




