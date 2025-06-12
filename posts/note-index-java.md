---
layout: page
title: Java Notes
permalink: /posts/note-index-java/
---

# 📒 Java Notes

{% assign java_notes = site.posts | where_exp: "item", "item.path contains 'Java_Notes'" | sort: "path" | reverse %}
<ul>
  {% for post in java_notes %}
    <li><a href="{{ post.url }}">{{ post.title }}</a></li>
  {% endfor %}
</ul>

<p><a href="/posts/">⬅ Back to Notes Index</a></p>
