---
---

{% include section.html %}
## About Me
I am a first year PhD student broadly interested in the intersection of systems and ML. I'm fortunate to be part of NetSys Lab @ GATech, advised by Anand Iyer. Prior to joining NetSys, I was an undergraduate research intern for various systems projects. I worked with Greg Ganger and Rashmi Vinayak at the CMU Parallel Data Lab, implementing a new theory-enhanced  system to make transitioning data between redundancy schemes more efficient,and with Sid Sen, Chetan Bansal, and Gagan Somashekar at Microsoft Research Labs using AI behavior mimicry techniques to generate synthetic application request traces for system reliability.

I always enjoy learning from other students and researchers, and can be reached by emailing dax [at] gatech [dot] edu.


{% include section.html %}

## Highlights

{% capture text %}
My published work.

{%
  include button.html
  link="research"
  text="See publications"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

{% endcapture %}

{%
  include feature.html
  image="images/photo.jpg"
  link="research"
  title="Publications"
  text=text
%}

{% capture text %}

Under construction. Check back later for open source projects :smile:

{%
  include button.html
  link="projects"
  text="Browse projects"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

{% endcapture %}

{%
  include feature.html
  image="images/photo.jpg"
  link="projects"
  title="Projects"
  flip=true
  style="bare"
  text=text
%}

{% capture text %}

A bit about my lab, my service contributions, etc.

{%
  include button.html
  link="community"
  text="See community involvement"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

{% endcapture %}

{%
  include feature.html
  image="images/photo.jpg"
  link="community"
  title="Community"
  flip=true
  style="bare"
  text=text
%}