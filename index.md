---
---

{% include section.html %}
## About Me

{% capture text %}

I'm a first-year PhD student in Computer Science at Georgia Tech, where I'm advised by [Anand Iyer](https://www.anand-iyer.com/) in the NetSys Lab. My research interests lie at the intersection of systems and machine learning, with a current focus on building efficient and reliable agentic LLM systems for complex, distributed tasks.

Before joining Georgia Tech, I was an undergraduate research intern on several systems projects. At Carnegie Mellon’s Parallel Data Lab, I worked with [Greg Ganger](https://www.ece.cmu.edu/directory/bios/ganger-greg.html) and [Rashmi Vinayak](https://www.cs.cmu.edu/~rvinayak/) on a theory-enhanced system for efficiently transitioning data across redundancy schemes. At Microsoft Research, I collaborated with Sid Sen, Chetan Bansal, and Gagan Somashekar to develop synthetic application request traces via AI behavior mimicry for system reliability testing.

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
