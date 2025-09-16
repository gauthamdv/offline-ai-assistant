#!/bin/bash

sync
sh -c "echo 3 > /proc/sys/vm/drop_caches"

apt clean

rm -rf ~/.cache/thumbnails/*

rm -rf /tmp/*
rm -rf /var/tmp/*

rm -rf ~/.nv

