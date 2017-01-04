[check in form](https://docs.google.com/forms/d/e/1FAIpQLSfMKPLhvomdGFEEMHcqA4scH0bqGtjskHV6v6wX0oOueicGIw/viewform?c=0&w=1)

### Wave 0: Lay the Groundwork
- [x] concept 
- [x] product plan
 - [x] problem statement
 - [x] market research
 - [x] user personas
 - [x] trello board
 - [x] to do list
 - [x] technology selections
 - [x] [wireframes] (https://gomockingbird.com/projects/6cisgvd/mFbWzQ)
    - [x] home page
    - [x] job results page
    - [x] details page 
    - [x] create account
    - [x] my account
- [x] create hello world django app
- [x] explore python machine learning
  - [x] watch Google Developers YouTube series about machine learning
  - [x] complete hello world
  - [x] complete simple tutorial
- [x] explore python web scraping
  - [x] complete simple scraping project
- [x] research indeed API
- [x] research React
  - [x] read [this](http://blog.andrewray.me/reactjs-for-stupid-people/)
  - [x] watch [this YouTube video](https://www.youtube.com/watch?v=BYbgopx44vo)


### Wave 1: Make it Viable (Make sure it is possible to do this)
- [ ] Goal: Get a score of similiarity given a user's experience level (int in years), resume (array of words), and job description (array of words)
  - [ ] manually classify 100+ jobs (qualified vs not qualified); get at least 50 qualified jobs. (Fill in [this spreadsheet](https://docs.google.com/spreadsheets/d/1rTUMT8Wog8TX1T5ayW4LNb4pKPfH6irpjDrhOnwz_j0/edit#gid=0)).
    - [x] manually classify 10 jobs [1/2/2017]
    - [x] manually classify 20 more jobs [1/3/2017]
    - [ ] manually classify 20 more jobs 
  - [x] research how to determine keywords [1/3/2017]
    - [x] talk to Aria about keyword approaches [1/3/2017]
    - [x] read/scan this [masters thesis] (http://digitalcommons.usu.edu/cgi/viewcontent.cgi?article=1343&context=gradreports) that has a similar topic to my app
        - [x] read chapter 4: skill finding algorithm [1/2/2017]
        - [x] scan the rest of paper [1/3/2017]
        - [x] experimentally apply concepts in this paper to my app [1/2/2017]
    - [x] research and play with Stanford's NLP toolkit [1/2/2017]
  - [x] count keywords in job description manually [1/2/2017]
  - [ ] Write a program to get keywords from 1000 job ads using TF-IDF approach
    - [x] manually create a text file by copy and pasting job ad 
    - [x] split text file into setences
    - [x] run job ad setences through TF-IDF
    - [ ] store in database of skill words
    - [ ] do this for three jobs
    - [ ] do this for 1000 jobs
      - [ ] access job url from Indeed API
      - [ ] get text from url; save as text file
      - [ ] send that file to TF-IDF method above
  - [ ] count keywords in a job ad (automatically)
  - [ ] count keywords in a resume (automatically)
  - [ ] compare keyword counts of both give that a numerical score/weight
   
  - [ ] make simple ML program that classifies qualified vs not (meets years of experience or not).
     - [ ] determine experience level needed in job description
     - [ ] compare that experience level with user's experience level and give that a score
     - [ ] do [this tutorial about text classification](http://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html)

- [ ] Goal: Create a skeleton of app
  - [ ] design app (MVC structure etc)
  - [ ] create Github repo
  - [ ] create file structure of Django app based on that
  
- [ ] deploy to Heroku
  
### Wave 2: Make it Work
*When stuck during this wave, work on Wave 3 stuff--CSS*
- [ ] Goal: create html/React version of webpages (minimal to no css)
  - [ ] homepage
  - [ ] jobs page
  - [ ] job page 
  - [ ] about page

**Homepage**
- [ ] input resume into a text box and it gets stored as data
- [ ] input search terms

**Qually jobs page**
- [ ] show jobs using search terms sent to Indeed API (not filtered for qualifications)
- [ ] show qualification score for each job
- [ ] ability to filter by qually score

- [ ] redeploy to Heroku

### Wave 3: Make it Beautiful
- [ ] add CSS to make it look like the wireframe
- [ ] ensure responsiveness (fix responsive bugs)
- [ ] redeploy to Heroku

### Wave 4: Optionals

