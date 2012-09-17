import webapp2
import jinja2
import os

from datetime import datetime

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__))
)

class ResumePage(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'author' : 'Your name',
            'contact': {
                'phone'  : ['555-555-5555'],
                'email'  : ['you@some-website.com'],
                'address': {
                    'street1' : '200 University Ave. W.',
                    'street2' : '',
                    'city'    : 'Waterloo',
                    'province': 'Ontario',
                    'postal_code': 'N2L 3G1',
                }
            },
            'education': [{
                'title'      : '(Candidate for) Bachelor of X',
                'business'   : 'University of Waterloo',
                'department' : 'Faculty of X',
                'location'   : 'Waterloo, Ontario',
                'start'      : datetime(2012,1,1),
                'end'        : None, #optional, assumed to be 'Present day'
                'notes'      : [ #optional
                    'I did really well in [some course]!'
                ],
            }],
            'experience': [{
                'title'      : 'Your Title',
                'business'   : 'Business Name',
                'department' : 'Deparment', # optional
                'location'   : 'City, Provice/State/etc, [Country]',
                'start'      : datetime(2012,1,1),
                'end'        : None, #optional, assumed to be 'Present day'
                'notes'      : [ #optional
                    'I was their first co-op, and accomplished X'
                ],
            }, {
                'title'      : 'Your Other Job',
                'business'   : 'Business Name',
                'department' : 'Deparment', # optional
                'location'   : 'City, Provice/State/etc, [Country]',
                'start'      : datetime(2010,1,1),
                'end'        : datetime(2011,12,31), #optional, assumed to be 'Present day'
                'notes'      : [ #optional
                    'I was their first co-op, and accomplished X'
                ],
            }]
        }

        template = jinja_environment.get_template('templates/resume.html')
        self.response.out.write(template.render(template_values))

app = webapp2.WSGIApplication([
    ("/", ResumePage),
    # Add other pages by creating new URL handlers
    # e.g. ("/regex", PageHandler)
], debug=True)
