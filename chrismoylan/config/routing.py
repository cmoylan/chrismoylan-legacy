"""Routes configuration

The more specific and detailed routes should be defined first so they
may take precedent over the more generic routes. For more information
refer to the routes manual at http://routes.groovie.org/docs/
"""
from routes import Mapper

def make_map(config):
    """Create, configure and return the routes Mapper"""
    map = Mapper(directory=config['pylons.paths']['controllers'],
                 always_scan=config['debug'])
    map.minimization = False
    map.explicit = False

    # The ErrorController route (handles 404/500 error pages); it should
    # likely stay at the top, ensuring it can always be resolved
    map.connect('/error/{action}', controller='error')
    map.connect('/error/{action}/{id}', controller='error')

    # CUSTOM ROUTES HERE
    # User functions
    map.connect('login', '/login', controller='users', action='login')
    map.connect('logout', '/logout', controller='users', action='logout')

    # Named pages
    map.connect('home', '/', controller='pages', action="show", id="1")
    map.connect('about', '/about', controller='pages', action="show", id="3")
    map.connect('professional', '/about/professional', controller='pages', action="show", id="8")
    map.connect('programming', '/about/programming', controller='pages', action="show", id="4")
    map.connect('music', '/about/music', controller='pages', action="show", id="7")

    # Journal/Blog
    map.connect('journal', '/journal', controller='blogs', action='index')
    map.connect('journal_categories', '/journal/categories/{id}', controller='blogs', action='categories')
    map.connect('/journal/{id}', controller='blogs', action='show',
        requirements=dict(id='\d+')
    )
    map.connect('/journal/{action}/{id}', controller='blogs')
    # Post comments on blog
    map.connect('/journal/{blogid}/{controller}/{action}',
        requirements=dict(blogid='\d+', id='\d+')
    )
    map.connect('/journal/{blogid}/{controller}/{action}/{id}',
        requirements=dict(blogid='\d+', id='\d+')
    )

    # Project section
    map.connect('projects', '/projects', controller='projects', action='index')

    # TODO add legacy routes so you don't fuck up google ranking

    map.connect('/{controller}/{action}')
    map.connect('/{controller}/{action}/{id}')

    return map
