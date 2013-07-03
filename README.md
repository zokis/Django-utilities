Django-utilities
================

Vários utilitários para o Django

* Widgets:
  * _TelefoneWidget_ (Widget de Telefone)
* Views
  * _SearchFormListView_ (View Genérica para listagem com Filtro)
* Models
  * _UserDateAdd_ (Modelo que guarda o usuário que Adicionou e a Data)
  * _UserDateUpd_ (Modelo que guarda o usuário que Atualizou e a Data)
* ModelFields
  * _TelefoneField_ (ModelField de Telefone)
* Middlewares
  * _FirstLoginMiddleware_ (Verifica se é o primeiro login do usuário)
  * _CachedTemplateMiddleware_
* Forms
  * _GenericRelationsForm_ (ModelForm para Gerneric Relations)
* FormFields
  * _BRPhoneNumberField_ (FormField para telefone BR)
* _autodiscover_ (Registra Todos os Modelos no Admin)
* _password_generator_ (Retorna um password randômico)
* _get_paginator_context_ (Devolde Dicionário com todos os objetos necessários para Paginação (object_list, is_paginated, page_obj, paginator))
* _get_next_or_previous_ (Retorna a próxima instância baseado no ordering do Model)
* Choices (PAIS, ESTADO, SEXO)
* _EmailBackend_ (Backend que utiliza username ou email para o login)
* _parse_date_ (Retorna Data Formatada)
* _get_years_ (Retorna range do ano x até o atual)
* _converte_unicode_ (Converte string para unicode)
* _instance_to_dict_ (Retorna um dicionário baseado na instância, com a opção de escolher os campos (fields ou exclude))
* _instance_to_json_ (Retorna um json baseado na instância, com a opção de escolher os campos (fields ou exclude))
