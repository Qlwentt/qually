[markdown helper](http://dillinger.io/)

### Problem Statement


Job searching can be a time-consuming process. The average unemployed job-seeker spends 191 hours  looking for a job before getting one.<sup>[1](https://www.bls.gov/news.release/empsit.t12.htm)	</sup> <sup>[2] (http://cep.lse.ac.uk/conference_papers/25_06_2009/mueller1.pdf) </sup> Much of this time is spent online sifting through job annoucements. Job annoucement aggregators like Indeed.com offer great prospects, but people have to manually read each job annoucement to see if they qualify. That takes time.


I propose a web application that, when given a person's resume, shows a user only jobs they likely qualify for (using machine learning).

### Market Research
#### Competition

**[Career Builders' Recommender](http://www.careerbuilder.com/recommendations)**

This site's main purpose is to be a job search engine. Using a user's resume to recommend jobs is one aspect of its job recommender feature. It also uses other things like search history, jobs applied to, and other user behavior.

Its job recommender using just a resume is buggy and often cannot give any recommendations at all.

**[Jobscan](https://www.jobscan.co/)**

This site's main purpose is to evaluate how well your resume matches *a particular job* annoucement. You copy and paste your resume and copy and paste the job description. It gives you a matching percentage of how well your resume meets the job description. 

A feature of this site is that its "job matcher" shows you jobs from Indeed based on 3-6 skills taken from your resume (which you can adjust). The job matcher does not give its recommendations based on matching percentages for your resume, only 3-6 skills/keywords.

**[Indeed](https://www.indeed.com/)**

Lets you filter jobs by experience level. It is not super-successful(shows you jobs where you need 5 years of experience when you select "entry-level."

#### User Feedback
The biggest critque of Jobscan (my most comparable competitor) is that it is trying to solve the wrong problem. [In this PBS review](http://www.pbs.org/newshour/making-sense/ask-headhunter-scam-employer-interviewing/), headhunter Nick Corcodilos complains that Jobscan just helps job-seekers "beat algorithms with more algorithms." The argument is that using an automated process won't tell applicants if they are truly qualifed, only if they are properly keyword-stuffing their resumes. 

#### Differentiation
What will separate my product from what is currently available is that it will scan every job annoucement from your Indeed search results and show you the ones that you have a higher matching percentage for.

### User Persona: Jenny the Jobseeker

Jenny is an entry/mid level professional who normally looks for jobs on Indeed and uses the brute force method to apply for jobs. She tends to scour the internet looking for jobs she qualifies for and then applies for as many jobs as possible. She has an idea of what kind of job she is looking for, but doesn't have the experience to qualify for any job she happens to find.

### Progress Trackers
* [to-do list](https://gist.github.com/Qlwentt/6aa3f06676e730c39cb402cafab2000f)
* [Trello board](https://trello.com/b/GQ4r0upu/qually)

### Technology Stack
* Python (because of the machine learning and possible web scraping components)
* DJango (because it works with python).
* PostgresSQL for the database
* Heroku for deployment
* Indeed API
* HTML/CSS for frontend
* JS/React for frotend
* Oauth for user authentication (optional)

#Wireframes
click image for link to the rest of the wireframes
[<img src="https://s-media-cache-ak0.pinimg.com/originals/bc/80/4a/bc804a592dcb51f10ac410b27fff0ba2.png">](https://gomockingbird.com/projects/6cisgvd/4gXVnCu/)
