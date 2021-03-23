## Grow Lab

I want to set up a automated grow system. You can follow the project on [hackaday.io](https://hackaday.io/project/177878-raspi-grow)

## Motivation

I'd rather program than garden and the thought of automating the process excites me. I also have a bunch of spare parts I need to find a use for so it feels like this was supposed to happen.

## Description and current status

This program lives on a raspberry pi and is accessible through ssh. If you run the main file you will be shown a menu with options to read from all sensors, the TSL2561, DHT22 or to quit the program. The high_low file is automated through a cronjob. This program is ran every 20 minutes and record the highest and lowest readings to data/data/json.

### Goals

<ul>
  <li>Track record highs and lows</li>
  <li>Graph information and figure out ways to visualize the data</li>
  <li>Watch out, notify, and correct environmental conditions.</li>
  <li>Automate watering => in the future this could mean a hydroponic system</li>
  <li>Set up a camera I can activate/deactivate through ssh and stream via VLC</li>
</ul>
