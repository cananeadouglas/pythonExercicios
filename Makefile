TAG=$(shell date +%Y.%m.%d-%A)

name:
	git config --global user.name "Douglas Cananéa"
email:	name
	git config --global user.email "cananeadouglas@gmail.com"
add:	email	
	git add .
commit: add
	git commit -m "Enviado em $(TAG)."
push: 	commit
	git push