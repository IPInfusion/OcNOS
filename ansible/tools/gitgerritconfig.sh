#!/bin/bash
# Setup script for the gerrit environment at IPI 

SCRIPTDIR=$( cd "$( dirname "$0" )" && pwd ) ; 
pwd | grep " "
if [ $? -eq 0 ]; then
  echo "Current working directory path contains whitespace; keep git repo in a path without whitespaces. Exiting."
  exit -1
fi

# Search, assign the .git directory
# Search maximum of 10 subdirectories for the .git directory
COUNTER=0
while [  $COUNTER -lt 10 ]; do
  if [ -d .git ]; then
    GIT_WORKINGDIR=`pwd`
    break
  fi
let COUNTER=COUNTER+1
cd ..
done

if [ $COUNTER -ge 10 ]; then
  echo "Unable to find .git directory. This does not seems to be a git repo."
  echo "Please execute this script under a git working directory"
  exit -1
fi

# Moving to place where .git directory is available
cd ${GIT_WORKINGDIR}

which wget > /dev/null 2>&1
if [ $? -ne 0 ]; then
  echo "ERROR: Unable to find wget program. Unable to set environment"
  echo "Exiting."
  exit 1
fi


echo -ne "1. Getting hooks from remote server...";
# Commit message validation and Gerrit change id management
wget -q "http://10.12.3.45/ipi/git/hooks/generic/commit-msg" -O .git/hooks/commit-msg > /dev/null 2>&1
if [ $? -eq 0 ]; then
  echo "Done."
else
  echo "Failed"
fi
chmod +x .git/hooks/commit-msg

# Gerrit configuration to push to the temporary branch
echo -ne "2. Setting push destination to be Gerrit friendly remote branch..."
git config remote.origin.push refs/heads/*:refs/for/*
echo "Done."

echo -ne "3. Configure git pull to always rebase for all branches..."
# http://www.kernel.org/pub/software/scm/git/docs/git-rebase.html
git config branch.autosetuprebase always
echo "Done."

# Commmit template
echo -ne "4. Setting Commit template..."
wget -q "http://10.12.3.45/ipi/git/templates/generic/commit-template" -O .git/info/commit-template > /dev/null 2>&1
if [ $? -eq 0 ]; then
  git config commit.template ${GIT_WORKINGDIR}/.git/info/commit-template
  echo "Done."
else
  echo "Failed"
fi

##
