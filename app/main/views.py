from . import main
from flask import render_template

@main.route('/')
def index():
    return render_template('main/index.html')


@main.route('/deploy')
def deploy():
    return render_template('main/deploy.html')


@main.route('/project')
def project():
    return render_template('main/project/project.html')


@main.route('/project/add', methods=['GET', 'POST'])
def project_add():
    return render_template('main/project/add.html')