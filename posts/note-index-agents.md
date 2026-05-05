---
layout: page
title: AI Agent Cheatsheet
permalink: /posts/note-index-agents/
---

<style>
/* 控制 summary 的折叠箭头与字体大小 */
details > summary {
  font-size: 1.0rem;
  font-weight: bold;
  cursor: pointer;
  list-style: none;
  display: flex;
  align-items: center;
  margin: 1rem 0;
}

details > summary::before {
  content: "▶";
  margin-right: 0.5rem;
  transform: rotate(0deg);
  transition: transform 0.2s ease;
}

details[open] > summary::before {
  transform: rotate(90deg);
}

/* 链接样式 */
.agent-link a {
  font-size: 1.0rem;
  text-decoration: underline;
  color: #333;
  transition: color 0.2s ease;
}

.agent-link a:hover {
  color: #007acc;
}
</style>

# 🤖 AI Agent Cheatsheet

{% assign agent_notes = site.posts | where_exp: "item", "item.categories contains 'Agent_Notes'" | sort: "date" | reverse %}
{% assign grouped = agent_notes | group_by_exp: "post", "post.categories[1]" %}

{% for group in grouped %}
  <details>
    <summary>{{ group.name }}</summary>
    <ul>
      {% for post in group.items %}
        <li class="agent-link"><a href="{{ post.url }}">{{ post.title }}</a></li>
      {% endfor %}
    </ul>
  </details>
{% endfor %}

{% if page.categories contains 'Agent_Notes' %}
  <a href="/posts/note-index-agent/">
    ⬅ Back to AI Agent Cheatsheet
  </a>
{% else %}
  <a href="/posts/">
    ⬅ Back to Notes Index
  </a>
{% endif %}