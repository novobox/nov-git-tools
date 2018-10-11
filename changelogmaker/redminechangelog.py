#!/usr/bin/env python

# -------------------
# TODO : everything !
# -------------------

from redmine import Redmine
from pdb import set_trace

sredmine = Redmine('https://{redmineurl}/', username='XXX', password='XXX')

project = sredmine.project.get('myprojectslug')

versions = project.versions[0:]
versions = reversed(sorted(versions, key=lambda dct: dct['name']))

#Collect versions issues
collected_issues = []
issues = sredmine.issue.filter(project_id='myprojectslug', status_id='*')
for issue in issues:
    if issue.version:
        if issue.version.id not in collected_issues:
            set_trace()
            collected_issues[issue.version.id] = 4
        #collected_issues[issue.version.id].append(issue)


for version in versions:
    print u"[%s]" % version
    print "\n"
    
#print verion.id

#versionissues = sredmine.issue.filter(project_id='newhotel', fixed_version=verion)



set_trace()

#print dir(project.versions[1])


#versions = sredmine.version.filter(project_id='newhotel')
#print versions[0]
