#!/usr/bin/env bash
echo "$(date) - Hello, World! from a script"

NUMBER=1

if [[ "$OSTYPE" == "darwin"* ]]; then
  echo "You are running on a Mac"
fi
 
if [[ "$NUMBER" -eq 1 ]]; then 
  echo "The number is 1"
fi

gpu_info=$(lspci 2>/dev/null | grep -E "VGA|Display")
echo "GPU Info: $gpu_info"
export PATH="$HOME/.pyenv/shims:$PATH"