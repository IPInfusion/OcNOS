#!/usr/bin/python
#
# Copyright (C) 2016 IP Infusion, Inc. All Rights Reserved.
#

# Import required standard ansible modules #
import socket
import pickle
import subprocess
from distutils.version import LooseVersion
from ansible.module_utils.basic import *

# Documentation #
'''
Documentation
 This Ansible module prepares and executes 'ocsh' commands for given input tasks

Usage
 Inputs can be given in following formats:
  1)  Place commands to be executed with values
      e.g. bridge 1 protocol ieee vlan-aware

  2)  Using placeholders (?) instead of actual input values in command
      e.g bridge ? protocol ? ? | 1,ieee,vlan-aware; 2,mstp,ring; 3,rstp

       This is useful when same command needs to get executed with multiple values.
       | - Used to separate command and values
       , - Used to separate values for place-holders
       ; - Used to separate set of inputs for a command
       $ - Used to separate commands given in same line

Subtasks:
  ocnos_config supports following three types of subtasks:
  1) config_cmds : Input for this will be executed in ocsh's config mode
  2) exec_cmd : Input for this will be executed in ocsh's exec mode
  3) module_config_cmds : Input for this will be executed as a group in ocsh's config mode

Example playbook:

---
- hosts: OCNOS
  tasks:
    - ocnos_config:
          config_cmds:
               - 'bridge ? protocol ? ? | 1, ieee; 2,mstp,ring; 3,rstp $ interface eth3'
    - ocnos_config:
          config_cmds:
                - 'vlan ? protocol ? ? | 1,ieee; 2,mstp,ring; 3,rstp'
                - 'hostname {{ hostnameid }}'
          module_config_cmds:
                - 'interface ? $ bandwidth ? | eth1; 1g; $ eth2; 10g;'
    - ocnos_config:
             exec_cmds:
                     - 'write'

'''

# Function to fill input for placeholders '?' #
def fill_values_for_placeholders (string, comm):
 argv = comm.split(',')
 command = ''
 i = 0
 length = 0
 if '?' in string:
     if len(argv) >0 :
           for index,ch in enumerate(string):
              length +=1
              if ch == '?':
                  string=string.replace(ch,argv[i].strip(),1)
                  length += len(argv[i].strip())
                  i += 1
                  if i == len(argv):
                      if '?' in string:
                         sep_index = string.index('?')
                         last_index = string[:sep_index-1].rfind(' ')
                         command = string[:sep_index-1]
                      else:
                         command = string
                      break
 else:
   command = string
 return command

# Function to handle module_config_cmd #
def create_group_command (name):
     cstr = ''
     command_list = []
     playbook_com = name.split('|')
     playbook_argvs = playbook_com[1].split('$')
     for argv in playbook_argvs:
         playbook_command = playbook_com[0].split('$')
         command = argv.split(';')
         for index,last_cmd in enumerate(playbook_command):
             if index < len(command):
                string = fill_values_for_placeholders (last_cmd,command[index])
                command_list.append(string)
             else:
                if '?' in last_cmd:
                   sep_index = last_cmd.index('?')
                   string = last_cmd[:sep_index-1]
                   command_list.append(string)
                else:
                   command_list.append(last_cmd)
     for commd in command_list:
        cstr = cstr + " -e \"" + commd + "\""
     return cstr

# Function to convert playbook input to ocsh command #
def create_ocsh_cmd_from_playbook_task (module, input_task):
  command = []
  cstr = ''

  playbook_command = input_task.split('|')
  if len(playbook_command) > 1:
    argv_list = playbook_command[1].split(';')
    if len(argv_list) > 0:
      for comm in argv_list:
         string = fill_values_for_placeholders (playbook_command[0] ,comm)
         command.append(string)
  else:
    command.append(playbook_command[0].strip())
  for commd in command:
      cstr = cstr + " -e \"" + commd + "\""
  return cstr

# MAIN Function Definition #
def main():
    module = AnsibleModule(
        argument_spec = dict(
            config_cmds = dict (default=None, type='list'),
            exec_cmds = dict (default=None, type='list'),
            module_config_cmds = dict (default=None, type='list')
         )
    )

    # Prepare cmd #
    ocsh_cmd = '/usr/local/sbin/ocsh -k '

    # Get playbook inputs for tasks #
    config_cmd = module.params['config_cmds']
    exec_cmd = module.params['exec_cmds']
    group_cmd = module.params['module_config_cmds']

    # Handle Execution mode cmds #
    if exec_cmd != None and len(exec_cmd) > 0:
     for execCmd in exec_cmd:
      if execCmd is not None:
         ocsh_cmd += create_ocsh_cmd_from_playbook_task (module, execCmd.strip())

    # Handle Config mode commands #
    if config_cmd != None and len(config_cmd) > 0:
     ocsh_cmd += ' -e \"config terminal\" '
     for cmds in config_cmd:
      if cmds is not None:
         ocsh_cmd += create_ocsh_cmd_from_playbook_task (module, cmds.strip())

    # Handle group cmd #
    if group_cmd != None and len(group_cmd) > 0:
     ocsh_cmd += ' -e \"config terminal\" '
     for each_cmd in group_cmd:
       if each_cmd is not None:
         ocsh_cmd += create_group_command(each_cmd)

    # Dump Result #
    (rc, out, err) = module.run_command(ocsh_cmd)

    if out != None and out != '':
      #Suppress 'conf t' message
      out = out.replace ('Enter configuration commands, one per line.  End with CNTL/Z.\n','')

      #Format console output
      lines = out.splitlines()
      for line in lines:
        #Suppress 'enable' msg
        if 'OcNOS version ' in line and 'IPIRouter' in line:
          lines.remove(line)

    else:
      lines = None

    module.exit_json (OcNOS_Logs=lines,
                      changed=True,
                      rc=rc)

# Entry point #
main()
