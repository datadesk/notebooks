# datadesk/notebooks

All of our computational notebooks.

| date  | slug | description |
|---|---|---|{% for obj in object_list %}
|  `{{ obj.date }}` | [{{ obj.slug }}]({{ obj.url }}) | {{ obj.description }} |{% endfor %}