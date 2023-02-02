TAG=$(shell date +%Y.%m.%d)
DESC=$(shell echo $1)

add:	
	git add .
commit: add
	git commit -m "$(DESC) -> Enviado no dia $(TAG) para o repositório online."
push: 	commit
	git push