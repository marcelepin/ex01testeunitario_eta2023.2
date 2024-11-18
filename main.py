from src.service.service_user import ServiceUser

service = ServiceUser()

resultado_add = service.add_user("Marcele", "QA")
print(resultado_add)  # Deve imprimir "Usuário Adicionado com sucesso!"
"""
# Remover o mesmo usuário
resultado_remove = service.remove_user("Marcele")
print(resultado_remove)  # Deve imprimir "Usuário 'Marcele' removido com sucesso!"

resultado_update = service.update_user("Marcele", "Senior QA")
print(resultado_update)  # Deve imprimir "Trabalho do usuário 'Marcele' atualizado para 'Senior QA'."

# Verificar se o trabalho foi atualizado
print(service.store.bd)  # Deve mostrar a lista com o job atualizado.
"""
resultado_get = service.get_user_by_name("Marcele")
if isinstance(resultado_get, str):
    print(resultado_get)  # Caso seja uma mensagem de erro
else:
    print(f"Usuário encontrado: Nome={resultado_get.name}, Job={resultado_get.job}")