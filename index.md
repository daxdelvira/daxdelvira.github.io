---
---

{% include section.html %}
## About Me

{% capture text %}

I'm a third-year PhD student in Computer Science at Georgia Tech, advised by [Ada Gavrilovska](https://sites.cc.gatech.edu/home/ada/) in the Kernel Lab. I work at the two-way intersection of systems and machine learning — building **systems for AI** and bringing **AI into systems** — with a throughline of storage and memory hierarchies.

My current work builds AI runtime systems that let multi-agent LLM workflows for scientific computing run efficiently on high-performance computing platforms. Earlier, at Carnegie Mellon’s Parallel Data Lab, I worked with [Greg Ganger](https://www.ece.cmu.edu/directory/bios/ganger-greg.html) and [Rashmi Vinayak](https://www.cs.cmu.edu/~rvinayak/) on efficiently managing data across redundancy schemes in cluster storage. At Microsoft Research, I collaborated with Sid Sen, Chetan Bansal, and Gagan Somashekar on AI-driven methods for cloud reliability testing.

I always enjoy learning from other students and researchers, and can be reached by emailing dax [at] gatech [dot] edu.

{% endcapture %}

{%
  include feature.html
  image="images/dax_rectangle_profile_photo.jpeg"
  link="research"
  title=""
  text=text
%}

{% include section.html %}

## Highlights

{% capture text %}


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
  image="images/Screenshot From 2024-10-02 14-53-37.png"
  link="research"
  title="Publications"
  text=text
%}

{% capture text %}


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

{%
  include button.html
  link="team"
  text="See community involvement"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

{% endcapture %}

{%
  include feature.html
  image="images/photo.jpg"
  link="team"
  title="Community"
  flip=true
  style="bare"
  text=text
%}
