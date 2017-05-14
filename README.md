# Qually

Qually is a web application that shows users jobs that match their qualifications. There are two ways qually determines what jobs a user is quallyfied for *years of experience* and *resume keywords*

## Desktop View
![Desktop screen shots](/desktop_view.png?raw=true "Desktop screen shots")


## Mobile View

![Mobile screen shots](/qually_mobile.png?raw=true "Mobile screen shots")


## Main Features
- Search for jobs
- Create a profile
- Save jobs

## Architecture
![ERD Diagram](/my_project_visualized.png?raw=true "ERD Diagram")

## Demo
| [Live Site](https://qually.herokuapp.com/) | [Video Demo](https://cl.ly/3m0j0o3w203F) |

## Technologies
 - Indeed API - communicates with Indeed to get a raw list of jobs for the user's job title and location
 - Python/Django
 - Postgresql
 - Bootstrap
 - AWS Elastic Beanstalk
 - Heroku

## What I Learned
**Big O isn't just for whiteboarding**: 
An earlier version of this project was VERY slow. It took over 5 minutes to show the jobs list view after clicking "See My Jobs." The performance issues stemmed from the way I was finding the common keywords between the user's resume and each job description. The initial algorithm I used was very inefficient. For every word in a resume and every word in a job description, I checked every keyword from a database of keywords. If that word was a keyword and was in both the resume and job description, I saved it in a list of common keywords. These are the keywords that are displayed under a job blurb on the job list view. This algorithm is O(n^2), and it turned out to be very, very slow in practice. 

To improve performance, I used a different approach. I constructed a dictionary of the words in a resume where the key was the word and the value was True. In python, keys that do not exist return a value of "None." Therefore, instead of looping through all of the words in a resume and checking them against words in a job description, I could just loop through the words in the job description, use each word as a key for the resume dictionary, and see if the value was true or None. That way I had the common words between a resume and a job description. I used a similiar approach and put all keywords from my database into a dictionary and checked the common words against the dictionary. Thus I reduced the time complexity of finding common keywords from O(n^2) to O(n). That ended up making a huge difference in practice, brining the time to see the job list view down to about 7 seconds.

**Take Time to Understand AWS Pricing/Database space isn't cheap**:
I had to take my site off of AWS because within 10 days of deployment it racked up a bill of over $200. I honestly didn't understand what I was being charged for (because I thought I was using the "Free Tier") and I didn't know how to reduce my bill, so I just shut it down. In the future, when I want to deploy a personal project using AWS, I'm going to make an effort to educate myself better on the costs so that I won't be caught off guard.

After I shut down my site, I looked into it and realized that my database size was driving the high costs. I had a large database because I was trying to increase performance by saving each job that Qually had seen already so that displaying the job list view could be faster. This is an example of the classic conflict between memory and time. 

## Improvements 
**Performance**:
Although I recently implemented some changes that have drastically reduced runtime, there is still much to be desired when it comes to performance. Most users expect an immediate result when they click a button, so in comparison 7 seconds seems VERY slow. To further improve performance, I'd like to experiment with Redis as a caching layer.

**Better Experience Filter**:
The experience filter uses a regular expression to identify both digits and numbers in word form and if a number is in the same sentence as the word "experience," then it assumes that this number represents how many years of experience the job requires. This crude approximation can be improved. Perhaps instead of looking at the entire sentence, it could only look three or four words after a number for the word experience. This would reduce the number of incorrect experience classifications.

**Resume Upload**:
I really wanted to look into being able to upload your resume (instead of copying and pasting it) but I didn't have time. It seems like Django has support for this already, and it would simply involve creating a model and view for Files.

**Asthetics**:
There are some visual things that I'd like to fix. 
- footer with indeed credit should be flush to the bottom of the window
- profile view could look better on mobile
- some margin issues on job list view on some screens

