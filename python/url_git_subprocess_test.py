#!/usr/bin/env python
# coding=UTF-8
import os, subprocess
import urllib2, json, time

aa= '..'


siteMsg = dict(zip([aa], ['111']))
master = '...'
log_file = open('/home/admin....log')
project_repo = '/home/admin/...'
repo_set = set(os.listdir(project_repo ))


def get_json(url):
    return urllib2.urlopen(urllib2.Request(url)).read()


def parse_to_str(parsed_json):
    return json.dumps(parsed_json, ensure_ascii=False)


def parse_site(site):
    parsed_json = json.loads(get_json(url))['json子项']
    for domain in parsed_json:
        for appMsg in domain['json子项']:
            application_url = appMsg['applicationUrl'].encode('utf-8') #处理unicode
            if parse_to_str(appMsg['applicationStatusValue']) == u'\"check\"':  #处理unicode
       


def check_url(url):
    return '.git' in url or master in url


def get_git_url(url):
    if master in url:
        return url[0:url.find(master) - 1] + '.git'
    return url


def A():
    print  >> log_file,time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
    
    for git_url in online_url_list:      
        if repo_set.__contains__(trunk_name):
        project_name, trunk_name = get_trunk_name(git_url, site)
            os.chdir(open_grok_project_repo)
            get_err_process_cmd(' '.join(['rm', '-rf', trunk_name]))
            print  >> log_file,'delete'


def D(err): return 'a' in err or 'b' in err


def B(cmd):
    stdout, stderr = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
                                      stderr=subprocess.PIPE).communicate()
    err = stderr.decode('utf-8')
    return err


def C(git_url, site):
    project_name = git_url[git_url.rfind('/') + 1:git_url.find('.git')]
    trunk_name = siteMsg[site] + project_name
    return project_name, trunk_name


