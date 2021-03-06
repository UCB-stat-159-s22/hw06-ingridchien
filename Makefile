.ONESHELL:

.PHONY: env
env:
	mamba env create -f environment.yml

.PHONY: html
html:
	jupyterbook build .

.PHONY: html-hub
html-hub:
	cd ligobook
	jupyter-book config sphinx .
	sphinx-build  . _build/html -D html_baseurl=${JUPYTERHUB_SERVICE_PREFIX}/proxy/absolute/8000
	cd _build/html
	python -m http.server

.PHONY: clean
clean:
	rm figures/*.png
	rm audio/*wav
	rm -rf _build
	rm -rf ligobook/_build