```
superset-fork/               # твой репозиторий
│
├── superset_plugin_form/    # каталог плагина
│   ├── __init__.py
│   ├── views.py             # кастомные FlaskAppBuilder views
│   ├── forms.py             # твоя форма (WTForms / Flask-WTF)
│   ├── config.py            # конфиг плагина
│   └── assets/              # фронтовая часть (если надо)
│
├── setup.py                 # описание пакета
└── README.md
```
# Superset Plugin Form
```
superset-extension/
│
├── docker-compose.yml
├── Dockerfile
├── superset_config.py
│
├── superset_plugin_form/
│   ├── __init__.py
│   ├── config.py
│   ├── views.py
│   ├── forms.py
│   └── templates/
│       ├── form.html
│       └── form_success.html
│
└── setup.py
```

```python
from setuptools import setup, find_packages

setup(
    name="superset_plugin_form",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        "superset.app": [
            "superset_plugin_form = superset_plugin_form"
        ],
    },
)
```