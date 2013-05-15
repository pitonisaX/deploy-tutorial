from fabric.api import env, run, cd, sudo, put, require, settings, hide, puts

def hello(name="World") :
    print("Hello %s" % name)

env.user = ['pitonisax']
env.hosts = ['pycourse.com']

def deploy():
    cd('~/blog')
    run('git pull')
    run('bin/pelican -s mysite.py')

def check_distro():
    run('cat /etc/*release*')