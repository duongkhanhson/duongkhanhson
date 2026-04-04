---
title: "Debug Categories"
permalink: /debug-categories/
layout: single
---

<h2>Categories</h2>
<ul>
{% for category in site.categories %}
  <li>{{ category[0] }}: {{ category[1].size }} posts</li>
{% endfor %}
</ul>

<h2>Tutorials Posts</h2>
<ul>
{% for post in site.categories.Tutorials %}
  <li>{{ post.title }} ({{ post.path }})</li>
{% endfor %}
</ul>
