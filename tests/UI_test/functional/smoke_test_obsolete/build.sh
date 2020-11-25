#!/usr/bin/env bash

set -ex

export PROJ_HOME=$(dirname $0)
export PATH=$PATH:$PROJ_HOME/node_modules/.bin

# npm install mermaid.cli

# mmdc -i happy_flow_1.mmd -o happy_flow_1.png
# mmdc -i happy_flow_1.mmd -o happy_flow_1.png

mmdc -i test_network.mmd -w 1920 0h 1920 -o test_network.png
