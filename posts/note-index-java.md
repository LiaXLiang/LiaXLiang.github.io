---
layout: page
title: Java Notes
permalink: /posts/note-index-os/
---

# 📒 Java Notes

{% assign os_notes = site.posts | where_exp: "item", "item.path contains 'Java_Notes'" | sort: "date" | reverse %}
<ul>
  {% for post in os_notes %}
    <li><a href="{{ post.url }}">{{ post.title }}</a></li>
  {% endfor %}
</ul>

<p><a href="/posts/">⬅ Back to Notes Index</a></p>
