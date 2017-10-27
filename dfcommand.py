#!/usr/bin/python
import subprocess
partition_threshold_usage = 10
df_cmd = subprocess.check_output(['df','-h'])
lines = df_cmd.splitlines()
for line in lines[1:]:
   columns = line.split()
   used_percentage = columns[4]
   used_percentage = used_percentage.replace('%','')
   if int(used_percentage) > partition_threshold_usage:
     print "partition %s usage is beyond threshold at %s" % (columns[0],columns[4])

