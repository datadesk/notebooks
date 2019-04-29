# datadesk/notebooks

All {{ count }} of our computational notebooks. Also available as [a CSV file](notebooks.csv). Elsewhere you can find our open-source [software packages](https://github.com/datadesk/packages) and [tutorials](https://github.com/datadesk/tutorials).

| date | slug | description |
|:--|:--|:--|{% for obj in object_list %}
|  {{ obj.date }} | [{{ obj.slug }}]({{ obj.url }}) | {{ obj.description }} |{% endfor %}
