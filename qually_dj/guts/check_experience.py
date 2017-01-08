# _*_ coding:utf-8 _*_
# encoding=utf8  
import sys  
import unidecode
import re
from textblob import TextBlob as tb
reload(sys)  
sys.setdefaultencoding('utf8')



def correct_spacing(text):
  return re.sub(r'([a-z:.)])([A-Z])', r'\1 \2', text)
# print correct_spacing
# print tb(correct_spacing)
def to_s(tb):
	return ('\t' + str(tb))

def hasNumbers(inputString):
    # has_digits=bool(re.search(r'\d', inputString))
    answer = "none"
    # numbers=["one","two","three","four","five","six","seven","eight","nine","ten","1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    get_digits={"one": 1, "1" : 1,"two": 2, "2": 2, "three": 3, "3": 3, "four": 4, "4": 4, "five": 5,"5": 5, "six": 6,"6": 6, "seven": 7,"7": 7,"eight": 8,"8": 8,"nine": 9,"9": 9,"ten": 10,"10": 10, "none": False}
    for number in get_digits:
    	if number in inputString:
    		answer=number
    		break
    return get_digits[answer]

def experience_requirement(job_desc):
  sentences=tb(job_desc).sentences
  for sentence in sentences: 
  	if ("experience" in sentence.lower()):
  			has_num=hasNumbers(to_s(sentence))
  			if has_num:
  				return has_num
  		
def meets_requirement(exp_int,job_desc):
  if exp_int >= experience_requirement(job_desc):
    return True
  else:
    return False
    
job_desc="Must have 5+ years' experience. You:You are a software engineer who strives for excellence in the user’s experience as well as in your technical solutions. You have a curious mind and a passion for continuous improvement. You thrive in an agile and fast-paced environment.Us:We are a high-performing cross-functional team of developers, product managers, and designers. We are passionate about delivering elegant solutions to complex business problems and we have a proven track record of delivering successful v1 applications that delight our customers.What we want you to do:You will work with your scrum team to deliver impactful and valuable features bi-weekly. You will work on end-to-end features from concept to design to production, and partner with product managers, user experience designers, and other engineers to achieve high-quality solutions.Basic Qualifications:Ability to handle multiple competing priorities in a fast-paced environmentStrong knowledge of data structures, algorithms, enterprise systems, asynchronous architectures, and object oriented programmingDemonstrated experience with best SDLC practices: coding standards, reviews, code management, build processes, and testingProfessional experience building REST APIsExperience with relational databases, schema design, SQLB.S. in Computer Science or equivalent experiencePreferred Qualifications:Experience with backend web based Java development and Linux-based integrated development environments, or equivalent (e.g. NodeJS w/ Express or ASP.NET MVC)Experience developing Software as a Service (SaaS) applications and understanding the impact of this architecture in a deployment environmentDatabase implementations (query optimization, index generation, caching) or NoSQL DBs a plusExperience developing JS, CSS, HTML sitesExperience developing Single Page Web Applications and frameworks like Boostrap, AngularJS, or equivalent.The CompanyApptio is the CIO’s business management system. We build advanced data and analytics applications that help all IT leaders understand and make informed decisions about their technology investments, capitalize on the cloud transformation and drive innovation within their organization. We call it Technology Business Management. Our applications help companies align technology spending to business outcomes and automate IT processes like cost transparency, benchmarking, chargeback and planning. Hundreds of customers, including more than 40 percent of the Fortune 100, choose Apptio as their business system of record for IT. For more information, please visit www.Apptio.com ( http://www.Apptio.com ).Apptio Inc. is not open to 3rd party solicitation or resumes for our posted FTE positions. Resumes received from 3rd party agencies that are unsolicited will be considered complimentary.Apptio, Inc. provides equal employment opportunities (EEO) to all employees and applicants for employment without regard to race, color, religion, gender, sexual orientation, national origin, age, disability, genetic information, marital status, amnesty, or status as a covered veteran in accordance with applicable federal, state and local laws. Apptio, Inc. complies with applicable state and local laws governing non-discrimination in employment in every location in which the company has facilities."
job_desc=correct_spacing(job_desc)
print meets_requirement(5,job_desc)




