# datadesk/notebooks

All of our computational notebooks. Also available as [a CSV file](notebooks.csv).

| date | slug | description |
|:--|:--|:--|{% for obj in object_list %}
|  {{ obj.date }} | [{{ obj.slug }}]({{ obj.url }}) | {{ obj.description }} |{% endfor %}
