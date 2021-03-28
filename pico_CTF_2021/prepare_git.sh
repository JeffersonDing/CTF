#!/bin/bash
find . -size +100M |sed 's|^./||' | cat >> .gitignore