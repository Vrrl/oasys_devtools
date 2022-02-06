# Oasys Devtools Library


## Installing

```bash
$ pip install git+https://git.pti.org.br/equipe-propria-de-desenvolvimento/oasys-devtools.git
```

## Example



```python
from oasysdevtools import oasys

o = oasys(debug=True, report_url='localhost:8000')
```

Get video connection

```python
vid = o.video()

ret, frame = vid.read() # Get Frame

```

Send result

```python
# fake result
result = {'Warning': 'Object detected','Object': 'thief', 'proba': 80}

o.report(data=result, endpoint='homesecurity') # http request

```

