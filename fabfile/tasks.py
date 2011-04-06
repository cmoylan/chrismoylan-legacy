from fabric.api import *

WEBAPP = 'chrismoylan'

# Tasks
def deploy():
    #checkout()

    local('tar czf /tmp/chrismoylan.tar.gz ../chrismoylan')
    put('/tmp/chrismoylan.tar.gz', '/tmp/chrismoylan.tar.gz')

    stop()

    # Copy and clean the files, removing git metadata and old cache
    with cd(env.site_dir):
        run('tar xzf /tmp/chrismoylan.tar.gz')
        run('rm -rf chrismoylan/.git')
        run('rm -r chrismoylan/data/*')

    start()

    # Clean up
    run('rm /tmp/chrismoylan.tar.gz')
    local('rm /tmp/chrismoylan.tar.gz')
    #local('rm -rf /tmp/chrismoylan')

def bounce():
    stop()
    start()

def stop():
    with cd(env.site_dir + WEBAPP):
        run('''
if [ -a paster.pid ];
  then
    %s/paster serve --stop-daemon;
  else
    echo "paste server was not running";
fi;
        ''' % env.virtualenv)

def start():
    with cd(env.site_dir + WEBAPP):
        run('%s/paster serve --daemon --log-file=production.log production.ini' % env.virtualenv)

def checkout():
    with cd('/tmp'):
        local("git clone %s" % env.git)

