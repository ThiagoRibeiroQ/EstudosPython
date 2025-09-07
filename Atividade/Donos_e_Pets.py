class Pet:

    def __init__(self, nome, especie, idade):
        self.nome = nome
        self.especie = especie
        self.idade = idade

    def __str__(self):
        return f"{self.nome} ({self.especie}, {self.idade} anos)"

    def emitir_som(self):
        if self.especie.lower() == "cachorro":
            print(f"{self.nome} diz: Au au!")
        elif self.especie.lower() == "gato":
            print(f"{self.nome} diz: Miau!")
        else:
            print(f"{self.nome} faz um som: ...")

    def fazer_aniversario(self):
        self.idade += 1
        print(f"🎉 Parabéns, {self.nome}! Agora você tem {self.idade} anos.")


class Dono:
    def __init__(self, nome):
        self.nome = nome
        self.pets = []

    def __str__(self):
        return self.nome

    def adotar_pet(self, pet_novo):
        self.pets.append(pet_novo)
        print(f"{self.nome} adotou um novo amigo: {pet_novo.nome}!")

    def listar_pets(self):
        print(f"\n--- Pets de {self.nome} ---")
        if not self.pets:
            print("Ainda não possui pets.")
        else:
            for pet in self.pets:
                print(f"- {pet}")
    
    def chamar_pets(self):
        for pet in self.pets:
            pet.emitir_som()


if __name__ == "__main__":
    pet1 = Pet("Rex", "Cachorro", 3)
    pet2 = Pet("Mimi", "Gato", 5)
    pet3 = Pet("Piu", "Pássaro", 1)

    dono1 = Dono("Carlos")
    print(f"Dono criado: {dono1}")
    print("-" * 20)

    dono1.adotar_pet(pet1)
    dono1.adotar_pet(pet2)
    
    dono1.listar_pets()
    print("-" * 20)
    
    print(f"{dono1.nome} está chamando seus pets:")
    dono1.chamar_pets()
    print("-" * 20)

    pet1.fazer_aniversario()
    
    print("\nDepois do aniversário do Rex:")
    dono1.listar_pets()