from fabric.api import *
import os
import fabric.contrib.project as project

def clean():
    local('rm -rf ./deploy')

def generate():
    local('hyde gen -r')

def regen():
    clean()
    generate()

def serve():
    local('hyde serve')

def reserve():
    regen()
    serve()
