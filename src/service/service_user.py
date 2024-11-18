from src.models.store import Store
from src.models.user import User

# Criar uma instância global de Store que será compartilhada
shared_store = Store()


class ServiceUser:
    # Se não for fornecido um valor ao criar a instância, o valor padrão será None
    def __init__(self, store=None):
        self.store = store if store else Store()
    #Se store tiver um valor válido, será atribuído a self.store
    #Se store for None (ou seja, o parâmetro não foi passado),
    #uma nova instância de Store será criada com Store() e atribuída a self.store
    def search_user(self, name):
        for user in self.store.bd:
            if user.name == name:
                return user
        return None

    def add_user(self, name, job):
        if name is not None and job is not None:
            if isinstance(name, str) and isinstance(job, str):
                if self.search_user(name) is None:
                    user = User(name, job)
                    self.store.bd.append(user)
                    return "Usuário Adicionado com sucesso!"
                else:
                    return f"Erro: Usuário com nome '{name}' já existe!"
            else:
                return "Erro: 'name' e 'job' devem ser strings."
        else:
            return "Erro: 'name' e 'job' não podem ser nulos."

    def remove_user(self, name):
        if name is not None:
            if isinstance(name, str):
                user = self.search_user(name)
                if user is not None:
                    self.store.bd.remove(user)
                    return f"Usuário '{name}' removido com sucesso!"
                else:
                    return f"Erro: Usuário com nome '{name}' não encontrado."
            else:
                return "Erro: 'name' deve ser uma string."
        else:
            return "Erro: 'name' não pode ser nulo."

    def update_user(self, name, new_job):
        print(f"Lista antes de atualizar: {self.store.bd}")
        if name is not None and new_job is not None:
            if isinstance(name, str) and isinstance(new_job, str):
                user = self.search_user(name)
                if user is not None:
                    user.job = new_job
                    print(f"Lista depois de atualizar: {self.store.bd}")
                    return f"Trabalho do usuário '{name}' atualizado para '{new_job}'."
                else:
                    return f"Erro: Usuário com nome '{name}' não encontrado."
            else:
                return "Erro: 'name' e 'new_job' devem ser strings."
        else:
            return "Erro: 'name' e 'new_job' não podem ser nulos."

    def get_user_by_name(self, name):
        print(f"Buscando usuário: {name}")
        if name is not None:
            if isinstance(name, str):
                user = self.search_user(name)
                if user is not None:
                    print(f"Usuário encontrado: {user}")
                    return user
                else:
                    return f"Erro: Usuário com nome '{name}' não encontrado."
            else:
                return "Erro: 'name' deve ser uma string."
        else:
            return "Erro: 'name' não pode ser nulo."