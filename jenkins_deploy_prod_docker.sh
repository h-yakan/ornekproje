#!/bin/sh

ssh -i /home/user/.ssh/UrlshortenerV1.pem ubuntu@ec2-13-48-190-187.eu-north-1.compute.amazonaws.com <<EOF
  cd /repo/ornekproje
  git pull
  docker-compose -f docker-compose.prod.yml up --build -d
  exit
EOF
