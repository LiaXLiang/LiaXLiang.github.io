---
layout: page
title: Leetcode Notes
permalink: /posts/note-index-leetcode/
---

# 📗 Leetcode Notes

{% assign lc_notes = site.posts | where_exp: "item", "item.path contains 'Leetcode_Notes'" | sort: "date" | reverse %}
{% assign grouped = lc_notes | group_by_exp: "post", "post.path | split: '/' | slice: 2, 1 | first" %}

{% for group in grouped %}
  <details>
    <summary>{{ group.name }}</summary>
    <ul>
      {% for post in group.items %}
        <li><a href="{{ post.url }}">{{ post.title }}</a></li>
      {% endfor %}
    </ul>
  </details>
{% endfor %}

<p><a href="/posts/">⬅ Back to Notes Index</a></p>