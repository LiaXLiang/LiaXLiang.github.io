---
layout: page
title: Notes Index
permalink: /posts/
---

# 🗂️ Notes Index

## 📗 Leetcode Notes
{% assign lc_notes = site.posts | where_exp: "item", "item.path contains 'Leetcode_Notes'" | sort: "date" | reverse %}
<ul>
  {% for post in lc_notes %}
    <li><a href="{{ post.url }}">{{ post.title }}</a></li>
  {% endfor %}
</ul>

## 📘 Operating System Cheatsheet
{% assign os_notes = site.posts | where_exp: "item", "item.path contains 'Operating_System_Cheatsheet'" | sort: "date" | reverse %}
<ul>
  {% for post in os_notes %}
    <li><a href="{{ post.url }}">{{ post.title }}</a></li>
  {% endfor %}
</ul>


