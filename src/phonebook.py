class Phonebook:

    def __init__(self):
        self.entries = {'Ana': '061', 'POLICIA': '190', 'Si': '092', 'Carol': '013'}

    def add(self, name, number):
        """

        :param name: name of person in string
        :param number: number of person in string
        :return: 'Nome invalido' or 'Numero invalido' or 'Numero adicionado'
        """
        if '#' in name:
            return 'Nome invalido'
        if '@' in name:
            return 'Nome invalido'
        #ajustamos a mensagem de 'Nme invalido para Nome invalido'
        if '!' in name:
            return 'Nome invalido'
        if '$' in name:
            return 'Nome invalido'
        # ajustamos a mensagem de 'Nome invalio para Nome invalido'
        if '%' in name:
            return 'Nome invalido'

        if len(number) <= 0:
            #Adicionamos o = no if e ajustamos a mensagem retornada
            return 'Numero invalido'

        if name not in self.entries:
            self.entries[name] = number

        return 'Numero adicionado'

    def lookup(self, name):
        """
        :param name: name of person in string
        :return: return number of person with name
        """
        contactIsValid = self.valid_contact(name)
        if '#' in name:
            return 'Nome invalido'
        if '@' in name:
            return 'Nome invalido'
        if '!' in name:
            return 'Nome invalido'
        if '$' in name:
            return 'Nome invalido'
        if '%' in name:
            return 'Nome invalido'
        if contactIsValid:
            return self.entries[name]
        return "Contato não encontrado"

    def get_names(self):
        """

        :return: return all names in phonebook
        """
        return list(self.entries.keys())

    def get_numbers(self):
        """

        :return: return all numbers in phonebook
        """
        return list(self.entries.values())

    def clear(self):
        """
        Clear all phonebook
        :return: return 'Sua agenda foi apagada com Sucesso!!!'
        """
        self.entries = {}
        return 'Sua agenda foi apagada com Sucesso!!!'

    def search(self, search_name):
        """
        Search all substring with search_name
        :param search_name: string with name for search
        :return: return list with results of search
        """
        result = []
        for name, number in self.entries.items():
            if search_name in name:
                result.append({name, number})
        if len(result) == 0:
            return None
        return result

    def get_phonebook_sorted(self):
        """

        :return: return phonebook in sorted order
        """
        return self.entries

    def get_phonebook_reverse(self):
        """

        :return: return phonebook in reverse sorted order
        """
        reversed_entries = {key: value for key, value in reversed(self.entries.items())}
        return reversed_entries

    def delete(self, name):
        """
        Delete person with name
        :param name: String with name
        :return: return 'Numero deletado'
        """

        try:
            self.entries.pop(name)
            return 'Numero deletado'
        except KeyError:
            return 'Contato não encontrado na agenda'

    def valid_contact(self, name):
        contact = list(self.entries.keys())
        return name in contact

    def edit(self, name, new_number):
        """
        Edit the number of a person
        :param name: String with the name of the person
        :param new_number: String with the new number
        :return: 'Contato não encontrado' or 'Número editado'
        """
        if name in self.entries:
            self.entries[name] = new_number
            return 'Número editado'
        else:
            return 'Contato não encontrado na agenda'


