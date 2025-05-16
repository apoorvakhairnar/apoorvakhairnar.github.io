---
layout: default
title: Projects
extra_css:
  - page_style.css
---
<div class="content_desktop">
  <div class="projects">
    {% assign sorted = site.projects | sort: 'date' | reverse %}
    {% for proj in sorted %}
      <figure>
        <a href="{{ proj.url | relative_url }}">
          <img src="{{ proj.image | relative_url }}" alt="{{ proj.title }}">
        </a>
      </figure>
    {% endfor %}
  </div>
</div>

<div class="content_mobile">
  <div class="projects_mobile">
    {% assign sorted = site.projects | sort: 'date' | reverse %}
    {% for proj in sorted %}
      <figure>
        <a href="{{ proj.url | relative_url }}">
          <img src="{{ proj.image | relative_url }}" alt="{{ proj.title }}">
        </a>
      </figure>
    {% endfor %}
  </div>
</div>