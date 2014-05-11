import os
import urllib

import jinja2
import webapp2

from urllib2 import urlopen
from json import load 


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
    
DEFAULT_TOPIC_NAME = 'all things considered'


    
    
class MainPage(webapp2.RequestHandler):

    def get(self):
        topic_name = self.request.get('topic_name', DEFAULT_TOPIC_NAME)
        url = 'http://api.npr.org/query?apiKey=' 
        key = 'MDEzNzM3MjgyMDEzOTk3MjI4MjQ1YmIwYg001'
        url = url + key
        url += '&numResults=3&format=json&id='
        url1 = url
                                                
        if topic_name == "science":
            url+= '1007'
        elif topic_name == "movies":
            url+= '1045'
        elif topic_name == "news":
            url+= '1001'
        elif topic_name == "economy":
            url+= '1032'
        elif topic_name == "music":
            url+= '1039'
        elif topic_name == "all things considered":
            url+= '2'
            
        response = urlopen(url)
        json_obj = load(response)
        
        template_values = {
            'topic_name': topic_name,
            'json_obj': json_obj,
            'url': url1,
        }

        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))


class npr(webapp2.RequestHandler):

    def post(self):
        
        topic_name = self.request.get('topic_name')
            
        query_params = {'topic_name': topic_name}
        self.redirect('/?' + urllib.urlencode(query_params))
        
        
        
"""class npr_story(webapp2.RequestHandler):
    
    def post(self):
        
        story = self.request.get('story['id'])
        
        query_params = {'story': story}
        self.redirect('/?' + urllib.urlencode(query_params))"""
        
    
        

    







"""response = urlopen(url)
json_obj = load(response)
array = []
i = 1

print "Top 5 news in" +' ' + a +' '+ "field are : " + '\n'

for story in json_obj['list']['story']:
	print i
	print story['title']['$text'] + '\n'
	array.append(story['id'])
	i = i+1
	

print '\n'
b = input("Enter 1 or 2 or 3 or 4 or 5 for details of corresponding story" + '\n')

url = 'http://api.npr.org/query?apiKey=MDEzNzM3MjgyMDEzOTk1MzgzNjYyZWJmZA001&numResults=1&format=json&id='
url += array[b-1]
response = urlopen(url)
json_obj = load(response)


for story in json_obj['list']['story']:
    print "TITLE: " + story['title']['$text'] + "\n"
    print "DATE: "  + story['storyDate']['$text'] + "\n"
    print "NPR URL: " + story['link'][0]['$text'] + "\n"

    if 'teaser'in story:
        print "TEASER:" + story['teaser']['$text'] + "\n"
        
    if 'byline' in story:
	    print "BYLINE: " + story['byline'][0]['name']['$text'] + "\n"
	
    if 'show' in story:
	    print "PROGRAM: " + story['show'][0]['program']['$text'] + "\n"
    
    if 'image' in story:
        print "IMAGE: " + story['image'][0]['src'] + "\n"
	
    if 'caption' in story:
	    print "IMAGE CAPTION: ", story['image'][0]['caption']['$text'] + "\n"
	
    if 'producer' in story:
	    print "IMAGE CREDIT: " + story['image'][0]['producer']['$text'] + "\n"
	
    if 'audio' in story:
        print "MP3 AUDIO: " + story['audio'][0]['format']['mp3'][0]['$text'] + "\n"	
	
    for paragraph in story['textWithHtml']['paragraph']:
	    print paragraph['$text'].encode('ascii', 'replace') + " \n"
"""

application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/sign', npr),
   # ('/sign2',npr_story),
], debug=True)