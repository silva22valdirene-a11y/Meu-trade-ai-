name: Rodar Bot de Trade
on:
  schedule:
    - cron: '*/30 * * * *' # Isso faz o bot rodar a cada 30 minutos
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Instalar Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.9'
      - name: Instalar dependências
        run: pip install ccxt
      - name: Rodar bot
        run: python app.py
