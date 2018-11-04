#!/bin/sh
cd src/smart_knife/bluest/src/;g++ blerun.cpp -o blerun && sudo chown root:root blerun && sudo chmod u+s blerun
