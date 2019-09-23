# ansible-subprocess

## Demo

```python
from ansible_subprocess import run_playbook
status = run_playbook('playbooks/sample.yml', 'web')
status = run_playbook('playbooks/sample2.yml',
                        ['127.0.0.1', '127.0.0.2'],
                        extra_vars={'var1': 'hoge', 'var2': 'fuga'},
                        extra_options=['--syntax-check'])
```

## Installation

```bash
pip install ansible-subprocess
```
