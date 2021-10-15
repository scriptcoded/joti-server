#!/usr/bin/env bash

commands="$(awk NF "$1")"
commands="$(echo "$commands" | sed -z 's/\n/ ~ /g;s/ ~ $/\n/')"

rshell repl "~ $commands ~"
