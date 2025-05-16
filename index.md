---
layout: default
title: Home
---

<!-- paste your entire index.html body here, inside Markdown -->
{% raw %}
{%- capture homepage -%}
<!-- Original content_desktop and content_mobile divs -->
<div class="content_desktop">
      <div class="about">
        <h1>Apoorva Khairnar</h1>
        <p>
          Hi! I am Apoorva, a Ph.D. student at the Department of Mechanical Engineering, <a href="https://vt.edu">Virginia Tech</a>. 
          I completed my Bachelor's in Mechanical Engineering (2021) with Honors in Thermal Engineering from <a href="https://www.coep.org.in/">COEP Technological Univeristy</a> (formerly College of Engineering Pune).
          Currently, I am working as a Graduate Research Assistant at the <a href="https://naughtonlab.org/">Biomechanical Systems Lab</a> at VT under the guidance of <a href="https://me.vt.edu/people/faculty/naughton-noel.html">Dr. Noel Naughton</a>. My research
          focuses on the control of soft robots such as octopus arms and snakes using Neuromorphic Computing. Additionally, my work involves integrating artificial and physical reservoir computers to enable embedded sensing in soft robots.
        </p>
      </div>
      <div class="profile-photo">
        <img src="/assets/images/apoorva2.jpg" alt="apoorvakhairnar">
      </div>
    </div>
    <!-- Page content for mobile -->
    <div class="content_mobile">
      <div class="about">
        <h1>Apoorva Khairnar</h1>
        <p>
          Hi! I am Apoorva, a Ph.D. student at the Department of Mechanical Engineering, <a href="https://vt.edu">Virginia Tech</a>. 
          I completed my Bachelor's in Mechanical Engineering (2021) with Honors in Thermal Engineering from <a href="https://www.coep.org.in/">COEP Technological Univeristy</a> (formerly College of Engineering Pune).
          Currently, I am working as a Graduate Research Assistant at the <a href="https://naughtonlab.org/">Biomechanical Systems Lab</a> at VT under the guidance of <a href="https://me.vt.edu/people/faculty/naughton-noel.html">Dr. Noel Naughton</a>. My research
          focuses on the control of soft robots such as octopus arms and snakes using Neuromorphic Computing. Additionally, my work involves integrating artificial and physical reservoir computers to enable embedded sensing in soft robots.
        </p>
      </div>
      <div class="profile-photo">
        <img src="/assets/images/apoorva2.jpg" alt="apoorvakhairnar">
      </div>
    </div>
    <!-- Buttons for desktop -->
    <div class="buttons_desktop">
      <div class="button"><a href="mailto:apoorvak@vt.edu">Email</a></div>
      <div class="button"><a href="https://github.com/apoorvakhairnar">Github</a></div>
      <div class="button"><a href="https://www.linkedin.com/in/apoorva-khairnar-6b381a1a0/">LinkedIn</a></div>
    </div>
    <!-- Buttons for mobile -->
    <div class="buttons_mobile">
      <div class="button"><a href="mailto:apoorvak@vt.edu">Email</a></div>
      <div class="button"><a href="https://github.com/apoorvakhairnar">Github</a></div>
      <div class="button"><a href="https://www.linkedin.com/in/apoorva-khairnar-6b381a1a0/">LinkedIn</a></div>
    </div>
{%- endcapture -%}
{{ homepage | markdownify }}
{% endraw %}