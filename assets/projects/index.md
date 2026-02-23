---
layout: default
title: Projects
extra_css:
  - project_style.css
---
{% assign sorted_projects = site.projects | sort: 'date' | reverse %}

<style>
  /* Hide the radio buttons and all content by default */
  input[type="radio"].tab-radio { display: none; }
  .project-content { display: none; }

  /* Jekyll loop to generate dynamic states */
  {% for proj in sorted_projects %}
    /* 1. Show content when radio is checked */
    #proj-{{ forloop.index }}:checked ~ .split-view-container .project-details .proj-content-{{ forloop.index }} {
      display: block;
      animation: fadeIn 0.4s ease;
    }
    /* 2. Highlight the active label on the left */
    #proj-{{ forloop.index }}:checked ~ .split-view-container .project-list .proj-label-{{ forloop.index }} {
      background: var(--color-card);
      border-left: 4px solid var(--color-accent);
      color: var(--color-text-primary);
    }
  {% endfor %}

  @keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
  }
</style>

<div class="css-tabs-wrapper">
  
  {% for proj in sorted_projects %}
    <input type="radio" class="tab-radio" name="project-tabs" id="proj-{{ forloop.index }}" {% if forloop.first %}checked{% endif %}>
  {% endfor %}

  <div class="split-view-container">
    
    <div class="project-list">
      {% for proj in sorted_projects %}
        <label for="proj-{{ forloop.index }}" class="proj-label proj-label-{{ forloop.index }}">
          <h3>{{ proj.title }}</h3>
          <span class="proj-date">{{ proj.date | date: "%B %Y" }}</span>
        </label>
      {% endfor %}
    </div>

    <div class="project-details">
      {% for proj in sorted_projects %}
        <div class="project-content proj-content-{{ forloop.index }}">
          <img src="{{ proj.image | relative_url }}" alt="{{ proj.title }}">
          <h2>{{ proj.title }}</h2>
          {{ proj.content }}
        </div>
      {% endfor %}
    </div>
    
  </div>
</div>