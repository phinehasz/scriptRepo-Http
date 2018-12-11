#!/usr/bin/env python
# coding=UTF-8
import sys, getopt, os, subprocess


def main(argv):
    branch = ''
    prefix = ''
    try:
        opts, args = getopt.getopt(argv, "hb:p:", ["prefix="])
    except getopt.GetoptError:
        print('xxx.py -b <name> -prefix <pwd>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('sonarScan.py -b <name> -prefix <pwd>')
            sys.exit()
        elif opt == "-b":
            branch = arg
        elif opt in ("-p", "--prefix"):
            prefix = arg
    if (branch == '' or prefix == ''):
        print('xxx.py -b <name> -prefix <pwd>')
        sys.exit(2)

   
    # dir = '/home/admin/tomcat/xxx'
    dir = 'xxx'
    listdir = os.listdir(dir)
    mvncmd = ["mvn", "xxxx"]
    with open('/home/adminn/zxxxxcan.log', 'w+') as logfile:
        for project in listdir:
            if (project.startswith(prefix)):   
                mvncmd.append("xxx" + xxx)
                print "cd " + dir + os.sep + project
                os.chdir(dir + os.sep + project)
                print (" ".join(mvncmd))
                print "cd " + dir + os.sep + project >> logfile
                subprocess.Popen(" ".join(mvncmd), shell=True, stdout=logfile, stderr=logfile).communicate()
                print '\r\n' >> logfile


if __name__ == "__main__":
    main(sys.argv[1:])
