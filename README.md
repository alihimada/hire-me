Hire me!
========

Do you really want to join Willet? If so, you're in the right place! This project was created to give applicants more opportunities to showcase their talent. While it isn't required to complete this exercise, it is useful if you do not have a lot of other projects to showcase.

Background
----------
In this project you will find two folders:

- `job_descriptions`
- `src`

For more details regarding what positions are available, look at the individual job descriptions (in particular, the **tl;dr** sections) in the `job_descriptions` folder.

If you want to show us your skills, do the following:

Setup
-----
- fork this repository
- install the [Google App Engine SDK for Python](https://developers.google.com/appengine/docs/python/gettingstartedpython27/devenvironment)
- create an `app.yaml` file in the `src` directory, like this:
        application: your-appspot-name
        version: 1
        runtime: python27
        api_version: 1
        threadsafe: true
        
        libraries:
        - name: jinja2
        version: "2.6"
        
        handlers:
        - url: /static
        static_dir: static
        
        - url: /stylesheets
        static_dir: static/stylesheets
        
        - url: /images
        static_dir: static/images
        
        - url: /.*
        script: main.app

- Get things started by running your project using `dev_appserver.py` or the **Google App Engine Launcher**
- make something cool with the code in the `src` directory
- send us a pull request when you are done so we can see what you made (also, make sure it includes a link to your appspot domain so we can see what you did live)

What should you make? That's up to you. We've listed a few ideas below.

**Ideas for developers**:
- Make it possible for users to submit data via a form
- Dynamically create the resume from a different source
- Add unit tests, or get things running in a different framework
- ...Get creative!

**Ideas for designers**:
- Make different designs for different goals (e.g. designer, developers, etc)
- Make the page more interactive: what are other ways that resume can communicate information to someone?
- Make the page adapt to different formats (e.g. mobile, tablet, etc.)
- ... Get creative!
