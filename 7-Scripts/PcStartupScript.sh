#!/usr/bin/bash

AgentPid="$(mktemp)/AGENT.PID"

if [[ -s $AgentPid ]]; then
  source $AgentPid
else
  eval $(ssh-agent -s)
  env | grep -i ssh > $AgentPid
fi

echo "+++ LOAD KEY FOR GIT +++"
ssh-add $HOME/.ssh/id_ed25519
echo "+++ LOAD KEY FOR DFS BASTION HOSTS +++"
ssh-add $HOME/.ssh/ssh-pri

# Port forwarding for AS400 Server Monitoring Web App
ssh -L 8989:10.242.0.38:3389 t.le@172.21.198.39 -N -f
# Dynamic port forwarding for other Application at DFS.
ssh -C -D 8888 t.le@172.21.198.39 -N -f

