Django-utilities
================

Vários utilitários para o Django

* Widgets:
  * _TelefoneWidget_ (Widget de Telefone)
  * HTML 5
    * _EmailInput_
    * _NumberInput_
    * _TelephoneInput_
    * _DateInput_
    * _DateTimeInput_
    * _TimeInput_
* HTTP
  * HttpResponseNotAuthorized (Response 401)
  * InstanceJsonResponse (Response json de uma instância)
  * JsonResponse (Response Json de um objeto)
* Managers
  * _BaseManager_
    * _get_or_none_
    * _get_or_404_

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
* TemplateTags
  * _float_format_br_ (Retorna número formatado com ',' para casas decimais (duas por padrão) e com '.' para cada 'passo decimal')
  * _integer_format_br_ (Retorna número formatado com '.' para cada 'passo decimal' e sem casas Decimais)
  * _monetary_format_br_ (Retorna número formatado com ',' para casas decimais (duas casas) e com '.' para cada 'passo decimal')
  * _numero_extenso_ (Retorna número escrito por extenso)
  * _ordering_link_ (Retorna link para ordenação por colunas)
  * _markdown_ (Retorna HTML de um Markdown)
  * _instance_to_json_filter_ (Retorna um json apartir de uma instância, aceita parâmetro exclude)
  * _json_dumps_ (Retorna json.dumps para um objeto)
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
