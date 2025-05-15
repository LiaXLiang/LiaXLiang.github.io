---
layout: page
title: Operating System Cheatsheet
permalink: /posts/note-index-os/
---

# 📘 Operating System Cheatsheet

{% assign os_notes = site.posts | where_exp: "item", "item.path contains 'Operating_System_Cheatsheet'" | sort: "date" | reverse %}
<ul>
  {% for post in os_notes %}
    <li><a href="{{ post.url }}">{{ post.title }}</a></li>
  {% endfor %}
</ul>

<p><a href="/posts/">⬅ Back to Notes Index</a></p>
