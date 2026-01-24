class Aluno():
	def __init__(self, nome, matricula, turma):
		self.nome = nome
		self.matricula = matricula
		self.turma = turma

class Sistema():
	def __init__(self):
		self.matricula = 0
		self.turma_132 = []
		self.turma_133 = []
		self.turmas = [self.turma_132, self.turma_133]
		
	def criar_aluno(self):
		nome = input("Digite o nome do aluno: ").strip().title()
		self.matricula += 1
		if self.matricula <= 25:
			nome_turma = "turma_132"
			turma_escolhida = self.turma_132
		else:
			nome_turma = "turma_133"
			turma_escolhida = self.turma_133
		aluno = Aluno(nome, self.matricula, nome_turma)
		turma_escolhida.append(aluno)
		
		print(f"Nome: {aluno.nome}, Matricula: {aluno.matricula}, Turma: {aluno.turma}")
		
	def ver_turmas(self):
		print("1 - Turma 132\n2 - Turma 133") 
		controle = True
		while controle:
			resposta = int(input("Qual turma deseja ver? "))
			if resposta == 1:
				print(f"{'Nome':<20}Matricula")
				for aluno in self.turma_132:
					print(f"{aluno.nome:20}{aluno.matricula}")
				controle = False
			elif resposta == 2:
				print(f"{'Nome':<20}Matricula")
				for aluno in self.turma_133:
					print(f"{aluno.nome:20}{aluno.matricula}")
				controle = False
			else:
				print("opcao invalida")
				
	def ver_todos_alunos(self):
		nomes_ordernar = []
		for turma in self.turmas:
			for aluno in turma:
				nomes_ordernar.append(aluno.nome)
		nomes_ordernar.sort()
		for nomes in nomes_ordernar:
			print(nomes)
	
	def editar_aluno(self):
		matricula_aluno = int(input("Digite a matricula do aluno que você quer editar: "))
		for turma in self.turmas :
			for aluno in turma:
				if aluno.matricula == matricula_aluno:
					print(f"Nome: {aluno.nome:10}Turma:{aluno.turma:10}CPF: xxxxx")
					resposta = input("Qual informacao deseja alterar? ").lower().strip()
					if resposta == "nome":
						nome_novo = input("Insira o novo nome: ").strip().title()
						aluno.nome = nome_novo
						return
					elif resposta == "cpf":
						print("Ainda em desenvolvimento")
						return
					elif resposta == "turma":
						turma_nova = input("Insira o numero da nova turma: ").strip()
						if aluno in self.turma_132 and turma_nova == "133":
								self.turma_132.remove(aluno)
								aluno.turma = "turma_133"
								self.turma_133.append(aluno)
								print(f"Tranferencia para turma {turma_nova} concluida com sucesso")
								return
						elif aluno in self.turma_133 and turma_nova == "132":
								self.turma_133.remove(aluno)
								aluno.turma = "turma_132"
								self.turma_132.append(aluno)
								print(f"Tranferencia para turma {turma_nova} concluida com sucesso")
								return
						elif turma_nova in aluno.turma:
							print("Impossivel fazer transferencia para mesma turma")
						else:
								print("Turma inexistente")
					else:
						print("Opcao inexistente")		
					
	
	def popular_testes(self):
		zeca = Aluno("Zecaaaa", 1, "turma_132")
		self.turma_132.append(zeca)
		peca = Aluno("Peca", 2, "turma_133")
		self.turma_133.append(peca)
		leca = Aluno("Leca", 3, "turma_132")
		self.turma_132.append(leca)
		self.matricula = 3
		
	def menu(self):
		while True:
			print("1 - Cadastrar Aluno")
			print("2 - Ver turmas")
			print("3 - Ver todos os alunos")
			print("4 - Editar Aluno")
			print("5 - Excluir aluno")
			op = int(input("Digite o numero da opção do que deseja fazer: "))
			if op == 1:
				self.criar_aluno()
			elif op == 2:
				self.ver_turmas()
			elif op == 3:
				self.ver_todos_alunos()
			elif op == 4:
				self.editar_aluno()
			elif op == 5:
				pass
			else:
				print("opcao invalida")

respostas_positivas = {"sim", "s", "yes", "y", "presente", "positivo"}
respostas_negativas = {"n", "nao", "no", "negativo"}

escola = Sistema()
escola.popular_testes()
escola.menu()
	

