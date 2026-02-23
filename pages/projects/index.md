---
layout: default
title: Projects
extra_css:
  - page_style.css
---

<div class="css-tabs-wrapper">
  {% assign sorted = site.projects | sort: 'date' | reverse %}
  
  {% for proj in sorted %}
    <input type="radio" name="project-tabs" id="proj-{{ forloop.index }}" class="tab-radio" {% if forloop.first %}checked{% endif %}>
  {% endfor %}

  <div class="split-view-container">
    
    <div class="project-list">
      {% for proj in sorted %}
        <label for="proj-{{ forloop.index }}" class="proj-label proj-label-{{ forloop.index }}">
          {{ proj.title }}
        </label>
      {% endfor %}
    </div>

    <div class="project-details">
      {% for proj in sorted %}
        <div class="proj-content proj-content-{{ forloop.index }}">
          <img src="{{ proj.image | relative_url }}" alt="{{ proj.title }}">
          <h2>{{ proj.title }}</h2>
          {{ proj.content }} 
        </div>
      {% endfor %}
    </div>

  </div>
</div>

<style>
  {% for proj in sorted %}
    #proj-{{ forloop.index }}:checked ~ .split-view-container .project-details .proj-content-{{ forloop.index }} {
      display: block;
    }
    #proj-{{ forloop.index }}:checked ~ .split-view-container .project-list .proj-label-{{ forloop.index }} {
      background: #0F1C2E;
      border-left: 4px solid var(--accent-aqua, #00E5FF);
      color: #FFFFFF;
    }
  {% endfor %}
</style>