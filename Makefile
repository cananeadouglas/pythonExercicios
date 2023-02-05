TAG=$(shell date +%Y.%m.%d)

add:	
	git add .
commit: add
	git commit -m " -> Enviado no dia $(TAG) para o repositório online."
push: 	commit
	git push