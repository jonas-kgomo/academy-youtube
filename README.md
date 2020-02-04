# Coding Youtube

> Langauge choices 
Youtube is coded with Python, C and Java for uts backend. HTML 5 for front-end

1. Python: runs using Django and GraphQL. UI not friendly
   [github-api tutorial](https://raybesiga.com/basic-django-app-github-api/)
2. Why I used Django  
   Django : Fast and not bloated. Security and tools. Admin portal.


## Resources 

**Coding Youtube** uses the following resources: 

- Youtube API
- Primer CSS kit
- Octicons
- [Shape](https://shape.so/app)


# Theme

- Uses Github Aesthetics
- Hover-[card](https://github.com/Justineo/github-hovercard)
- https://github.com/StylishThemes/GitHub-Feed-Icons

![](https://tonsky.me/blog/github-redesign/200_new_look.png)


# Instruction

Django Install 

`py -m pip install virtualenvwrapper-win`

Create a virtual project `cd codeyoutube`

start virtual environment `mkvirtualenv myproject`, and activate with `workon myproject`, to check the version, run `django-admin --version ` 


.
├── codeyoutube~
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py


## Google Youtube API with [Python](https://github.com/youtube/api-samples/tree/master/python)

`pip install --upgrade google-api-python-client`

`pip install --upgrade google-auth google-auth-oauthlib google-auth-httplib2`

### Youtube Features ToDo

- 