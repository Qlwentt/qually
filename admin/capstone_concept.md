## Concept Components
### Problem Statement: 
  
Job searching can be a time-consuming process. The average unemployed job-seeker spends 191 hours looking for a job before getting one. Much of this time is spent online sifting through job annoucements. Job annoucement aggregators like Indeed.com offer great prospects, but people have to manually read each job annoucement to see if they qualify. That takes time. 

I propose a web application that, when given a person's resume, shows a user only jobs they likely qualify for (using machine learning).

### Draft Feature Set:

User: My target user is an entry/mid level professional who normally looks for jobs on Indeed and uses the brute force method to apply for jobs. That is, they tend to scour the internet looking for jobs they qualify for and then apply for as many jobs as possible. This person has an idea of what kind of job they are looking for, but might not have the experience to qualify for any job they happen to find.

__As a user....__

1. I can input my resume and it gets stored as data
  - MVP: can copy and paste resume text into an input box
  - Optional: can upload resume as word document
  
2. I can input search parameters (job title, experience level, location)
  - MVP: pure input
  - Optional: program guesses parameters from resume and user confirms or updates them
 
3. I can get a paginated list of jobs that the program thinks I'm qualified for
  - MVP: uses web scraping or Indeed API to get jobs from Indeed using job title and location
  - Optional: support for other sites besides Indeed
  
  - MVP: uses keyword comparison to generate a score of how similar the job announcement is to my resume
  - MVP: shows annoucements that meet a certain default threshold. For example, show to the user if score is 75 or more
  - MVP: default threshold is chosen based on human feedback during the test stage (I have the computer give me recomendations then  manually decide whether or not I qualify; take the average score of the announcements I qualify for).
  
  - Optional: I can specify how conservative or liberal I want the app to be (make it favor false positives or false negatives)
   - Sets threshold for showing a job accordingly
  
4. I can click on a job to see its details
  - MVP: title, description, salary if available, etc. 
  - MVP: link back to original Indeed listing

**Important Optional (I really really want to get to this)**

1. I can create an account using my gmail
  - Would save my resume, my history of qualified vs. not qualified jobs, and search parameters
  - Super Optional: support for creating an account without using Oauth

2. I can give feedback (yes I'm qualified, no I'm not) to improve quality of job suggestions

**Super Optional**

3. I can save jobs and mark jobs as applied. 

5. Jobs saved and applied for would be accounted for in the job recommendation algorithm

6. I can get suggestions on skills or wording that will improve my resume (for example a pop up that says "A lot of the jobs in your area are looking for programmers who know C++. Do you know C++? Y/N. If yes, "You should add that to your resume" If no "maybe you should consider learning it". 
  
  - Crazy Idea/Spinoff Project: It could also find (with API or web scraping) open source courses with the skills you need and tell you about them (ex., "do you know C++"? Y/N. If no, "there's a Coursera course starting in two weeks called "C++ Basics and Stuff." You should consider signing up"
  
7. Iphone/Android app version

### Draft Technology Choices 

  - Python (because of the machine learning and possible web scraping components)
  - DJango (because it works with python).
  - PostgresSQL for the database
  - Heroku for deployment
  - Indeed API
  - HTML/CSS/JS for frontend
  - Oauth for user authentication (optional)
  - Open to suggestions

Sources 

https://www.bls.gov/news.release/empsit.t12.htm

http://cep.lse.ac.uk/conference_papers/25_06_2009/mueller1.pdf