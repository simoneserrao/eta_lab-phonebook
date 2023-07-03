from src.phonebook import Phonebook

class TestPhonebook:

    def test_add_contact_with_sucess(self):
        # Setup
        name = "Samu"
        number = "192"
        resultado_esperado = "Numero adicionado"

        service = Phonebook()

        # Chamada
        resultado = service.add(name=name, number=number)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_add_contact_invalid_name_hashtag(self):
        # Setup
        name = "#Samu"
        number = "192"
        resultado_esperado = "Nome invalido"

        service = Phonebook()

        # Chamada
        resultado = service.add(name=name, number=number)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_add_contact_invalid_name_arroba(self):
        # Setup
        name = "@Samu"
        number = "192"
        resultado_esperado = "Nome invalido"

        service = Phonebook()

        # Chamada
        resultado = service.add(name=name, number=number)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_add_contact_invalid_name_exclamacao(self):
        # Setup
        name = "!Samu"
        number = "192"
        resultado_esperado = "Nome invalido"

        service = Phonebook()

        # Chamada
        resultado = service.add(name=name, number=number)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_add_contact_invalid_name_sifrao(self):
        # Setup
        name = "$Samu"
        number = "192"
        resultado_esperado = "Nome invalido"

        service = Phonebook()

        # Chamada
        resultado = service.add(name=name, number=number)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_add_contact_invalid_name_porcento(self):
        # Setup
        name = "%Samu"
        number = "192"
        resultado_esperado = "Nome invalido"

        service = Phonebook()

        # Chamada
        resultado = service.add(name=name, number=number)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_add_contact_invalid_number_zero(self):
        # Setup
        name = "Samu"
        number = ""
        resultado_esperado = "Numero invalido"

        service = Phonebook()

        # Chamada
        resultado = service.add(name=name, number=number)

        # Avaliacao
        print(len(number))
        assert resultado_esperado == resultado

    def test_lookup_contact_with_success(self):
        # Setup
        self.entries = {'Ana': '061', 'POLICIA': '190', 'Bia': '013'}
        name = "Ana"
        resultado_esperado = self.entries[name]

        service = Phonebook()

        # Chamada
        resultado = service.lookup(name=name)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_lookup_contact_not_found(self):
        # Setup
        name = "Samu"
        resultado_esperado = "Contato não encontrado"

        service = Phonebook()

        # Chamada
        resultado = service.lookup(name=name)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_lookup_contact_invalid_name_hashtag(self):
        # Setup
        name = "#Ana"
        resultado_esperado = "Nome invalido"

        service = Phonebook()

        # Chamada
        resultado = service.lookup(name=name)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_lookup_contact_invalid_name_arroba(self):
        # Setup
        name = "@Ana"
        resultado_esperado = "Nome invalido"

        service = Phonebook()

        # Chamada
        resultado = service.lookup(name=name)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_lookup_contact_invalid_name_exclamacao(self):
        # Setup
        name = "!Ana"
        resultado_esperado = "Nome invalido"

        service = Phonebook()

        # Chamada
        resultado = service.lookup(name=name)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_lookup_contact_invalid_name_sifrao(self):
        # Setup
        name = "$Ana"
        resultado_esperado = "Nome invalido"

        service = Phonebook()

        # Chamada
        resultado = service.lookup(name=name)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_lookup_contact_invalid_name_porcento(self):
        # Setup
        name = "%Ana"
        resultado_esperado = "Nome invalido"

        service = Phonebook()

        # Chamada
        resultado = service.lookup(name=name)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_get_names_with_success(self):
        # Setup
        self.entries =  {'Ana': '061', 'POLICIA': '190', 'Si': '092', 'Carol': '013'}
        resultado_esperado = list(self.entries.keys())

        service = Phonebook()

        # Chamada
        resultado = service.get_names()

        # Avaliacao
        assert resultado_esperado == resultado

    def test_get_numbers_with_success(self):
        # Setup
        self.entries =  {'Ana': '061', 'POLICIA': '190', 'Si': '092', 'Carol': '013'}
        resultado_esperado = list(self.entries.values())

        service = Phonebook()

        # Chamada
        resultado = service.get_numbers()

        # Avaliacao
        assert resultado_esperado == resultado

    def test_clear_phonebook_with_success(self):
        # Setup
        resultado_esperado = "Sua agenda foi apagada com Sucesso!!!"

        service = Phonebook()

        # Chamada
        resultado = service.clear()

        # Avaliacao
        assert resultado_esperado == resultado

    def test_search_contact_with_success(self):
        # Setup
        self.entries = {'Ana': '061', 'POLICIA': '190', 'Si': '092', 'Carol': '013'}
        search_name = "Si"
        resultado_esperado = [{'Si', '092'}]

        service = Phonebook()

        # Chamada
        resultado = service.search(search_name)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_search_contact_not_found(self):
        # Setup
        self.entries = {'Ana': '061', 'POLICIA': '190', 'Si': '092', 'Carol': '013'}
        search_name = "Bia"
        resultado_esperado = None

        service = Phonebook()

        # Chamada
        resultado = service.search(search_name)

        # Avaliação
        assert resultado_esperado == resultado

    def test_get_phone_sorted(self):
        # Setup
        self.entries = {'Ana': '061', 'POLICIA': '190', 'Si': '092', 'Carol': '013'}
        resultado_esperado = self.entries

        service = Phonebook()

        # Chamada
        resultado = service.get_phonebook_sorted()

        # Avaliacao
        assert resultado_esperado == resultado

    def test_get_phone_reverse(self):
        # Setup
        self.entries = {'Carol': '013', 'Si': '092', 'POLICIA': '190', 'Ana': '061'}
        resultado_esperado = {'Ana': '061', 'Carol': '013', 'POLICIA': '190', 'Si': '092'}

        service = Phonebook()

        # Chamada
        resultado = service.get_phonebook_reverse()

        # Avaliação
        assert resultado_esperado == resultado

    def test_delete_with_success(self):
        # Setup
        name = "Si"
        resultado_esperado = 'Numero deletado'

        service = Phonebook()

        # Chamada
        resultado = service.delete(name)

        # Avaliacao

        assert resultado_esperado == resultado

    def test_delete_name_not_found(self):
        # Setup
        name = "Bia"
        resultado_esperado = 'Contato não encontrado na agenda'

        service = Phonebook()

        # Chamada
        resultado = service.delete(name)

        # Avaliação
        assert resultado_esperado == resultado

    def test_edit_contact_with_success(self):
        # Setup
        name = 'Ana'
        new_number = '123'
        resultado_esperado = 'Número editado'

        service = Phonebook()

        # Chamada
        resultado = service.edit(name, new_number)

        # Avaliação
        assert resultado_esperado == resultado

    def test_edit_name_not_found(self):
        # Setup
        name = "Bia"
        new_number = "123"
        resultado_esperado = 'Contato não encontrado na agenda'

        service = Phonebook()

        # Chamada
        resultado = service.edit(name, new_number)

        # Avaliação
        assert resultado_esperado == resultado


