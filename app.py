from logging import NullHandler
from operator import itemgetter
from os import link
from re import template
from flask import Flask,request
from flask.helpers import url_for
from flask.sessions import NullSession
from flask.templating import render_template
import requests
from werkzeug.utils import redirect
from flask_bootstrap import Bootstrap

app = Flask(__name__)


bs = Bootstrap(app)

global item 
item='google'

#This block of code was used for creating a new page and then transfering the data to the next webpage

# -------*-------*-------*-------*-------*-------*-------*-------*-------*-------*-------*-------*-------*-------*-------*-------*
# @app.route('/',methods=['GET','POST'])
# def word_entry():
#     item = request.form.get('word')
#     if item!=NullHandler:
#         return redirect(url_for('index'))
#     else:
#         return render_template('homepage.html',item=item)
# -------*-------*-------*-------*-------*-------*-------*-------*-------*-------*-------*-------*-------*-------*-------*-------*

@app.route('/')
def index():
    
    return render_template('index.html')



# -----------------**-----------------**-----------------**SEARCH ENGINE STARTING-----------------**-----------------**-----------------**
@app.route('/search', methods=['GET','POST'])
def search():

    
    item = request.form.get('word')


    url = 'https://www.googleapis.com/customsearch/v1?key=AIzaSyDqTWLRP7QJJWFPzJHCXzswbe4AZO0oLU8&cx=017576662512468239146:omuauf_lfve&q={}'

    
    if(item==NullSession):
        return("<h1> No Result was found with this word </h1>")
    else:
        r = requests.get(url.format(item)).json()
        # print(r)
        links=[]
        ll = {}

        l= len(r['items'])
        
        for x in range(l):
            ll={ 
                'title':r['items'][x]['title'],
                'lin':r['items'][x]['link'],
                'displin':r['items'][x]['displayLink'],
                'snipp':r['items'][x]['snippet'],
            }
            links.append(ll)

        # print(links)

        # links = {
        #     'title': r['items'][0]['title'],
        #     'linkk': r['items'][0]['link']

        # }
        # print(r['items'][0]['title'])
        


        return render_template('search.html',links=links,l=l)

# -----------------**-----------------**-----------------**SEARCH ENGINE ENDING-----------------**-----------------**-----------------**



# ----------**----------------------------HARYANA EDUCATIONAL REPORT-----------------**-----------------**-----------------**-----------------**

@app.route('/haryana')
def haryana():
    url = 'https://api.data.gov.in/resource/bdcf1dbe-e426-4ede-9a56-35f769078b73?api-key=579b464db66ec23bdd000001ce9223c326b94b9a514bf351f7c0fa46&format=json&offset=0'
    r = requests.get(url.format()).json()
    

    l = len(r['records'])
    
    ll=[]

    for x in range(l):
        info = {
            'title': r['title'],
        'indname': r['index_name'],
        'ins': r['records'][x]['type_of_institutions'],
        'yr66_67':r['records'][x]['_1966_67'],
        'yr70_71':r['records'][x]['_1970_71'],
        'yr75_76':r['records'][x]['_1975_76'],

        'yr80_81':r['records'][x]['_1980_81'],
        'yr85_86':r['records'][x]['_1985_86'],
        'yr90_91':r['records'][x]['_1990_91'],
        'yr95_96':r['records'][x]['_1995_96'],
        
        'yr00_01':r['records'][x]['_2000_01'],
        'yr05_06':r['records'][x]['__2005_06'],
        'yr10_11':r['records'][x]['__2010_11'],
        'yr12_13':r['records'][x]['_2012_13_r_'],

        }
        
        
        

        
        ll.append(info)

    
    


    return render_template("haryana_edu_rep.html",ll=ll,info=info)
# -----------------**-----------------**-----------------**END OF HARYANA EDUCATIONAL REPORT-----------------**-----------------**-----------------**


if (__name__)=='__main__':
    app.run(debug=True)