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
  /* Hide radios and all content by default */
  .tab-radio { display: none; }
  .proj-content { display: none; }

  /* Desktop App Layout */
  .css-tabs-wrapper {
    width: 100%;
    height: 80vh;
    overflow: hidden;
    margin-top: 20px;
  }
  .split-view-container {
    display: flex;
    gap: 30px;
    max-width: 1200px;
    height: 100%;
    margin: 0 auto;
    padding: 0 20px;
  }
  .project-list {
    width: 35%;
    height: 100%;
    overflow-y: auto;
    display: flex;
    flex-direction: column;
    gap: 10px;
    padding-right: 10px;
  }
  .project-list::-webkit-scrollbar { display: none; } /* Hide scrollbar for sleekness */
  
  .proj-label {
    padding: 15px 20px;
    cursor: pointer;
    background: rgba(15, 28, 46, 0.4);
    border-radius: 8px;
    color: #8DA3B5;
    font-weight: 600;
    transition: all 0.2s ease;
  }
  .proj-label:hover { background: #0F1C2E; color: #FFFFFF; }
  
  .project-details {
    width: 65%;
    height: 100%;
    overflow-y: auto;
    background: #0F1C2E;
    border-radius: 12px;
    padding: 40px;
  }
  .project-details img {
    width: 100%;
    max-height: 400px;
    object-fit: cover;
    border-radius: 8px;
    margin-bottom: 25px;
  }
  .project-details h2 { color: #FFFFFF; }
  .project-details p { color: #8DA3B5; line-height: 1.6; }

  /* Mobile Layout */
  @media (max-width: 768px) {
    .split-view-container { flex-direction: column; }
    .project-list { width: 100%; max-height: 25vh; }
    .project-details { width: 100%; height: 55vh; padding: 20px; }
  }

  /* Magic Loop to connect Radios to Content */
  {% for proj in sorted %}
    /* Show content when radio is checked */
    #proj-{{ forloop.index }}:checked ~ .split-view-container .project-details .proj-content-{{ forloop.index }} {
      display: block;
    }
    /* Highlight the active label on the left */
    #proj-{{ forloop.index }}:checked ~ .split-view-container .project-list .proj-label-{{ forloop.index }} {
      background: #0F1C2E;
      border-left: 4px solid #FF6B6B; /* Coral accent */
      color: #FFFFFF;
    }
  {% endfor %}
</style>