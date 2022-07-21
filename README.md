# medicar

## Descrição do projeto
  API para gerenciamento de uma clinica médica (apenas Backend)

  A descrição, especificações e regra de negócios desse projeto estão neste [link](https://github.com/Intmed-Software/desafio).

### Executando o projeto localmente

#### Requisitos

 - Python 3.10 instalado.
 
#### Instruções

  Após baixar o projeto, entre na pasta e execute os seguintes comandos:

    #Cria o ambiente virtual
    python3 -m backend/venv env
    
    #Ativa o ambiente virtual
    source backend/venv/bin/activate
    
    #Instale as dependências
    python3 -m pip install -r requirements.txt
    
    #Django - Executa as migrations 
    python3 backend/manage.py migrate
	
	  #Opcional - Populando o banco
    python3 backend/manage.py loaddata fixtures/dbPopulate.json
    
    #Django - Roda o servidor
    python3 backend/manage.py runserver
    
> Caso utilize o comando opcional de popular o banco com dados iniciais, a fixture já cria um super usuário, 4 especialidades, 4 médicos, 4 agendas (uma para cada médico) e 3 horários para cada agenda.
> As credenciais do superusuário são:  "Username": "gestor"; "Senha": "gestao2435".

### Estrutura 

  O projeto é dividido em módulos, sendo cada módulo responsável pelas funções referentes ao nome do módulo sendo eles:
  - agenda;
  - consulta;
  - medico;
  - usuario.
  
### Rotas (Endpoints)
   As rotas e seus parâmetros estão de acordo com o especificado no [projeto](https://github.com/Intmed-Software/desafio/tree/master/backend) com as seguintes modificações:

   - Os campos no retorno das requisições estão organizados em ordem alfabética;
   - Foi adicionado o campo especialidade para cada médico;
   - Foi adicionado token de acesso, gerado ao realizar cadastro;
   - Esse token de acesso faz parte do cabeçalho das requisições;
   - Esse token de acesso é utilizado para registrar para qual usuário será marcada a consulta.
   > Parti do pressuposto que não ter autenticação era uma pegadinha, pois se assim fosse seria possivel para um usuário marcar consultas para outro usuário. Caso fosse para de fato não ter autenticação, bastaria comentar as linhas que exigem autenticação e reescrever a função que armazena a consulta para usar o id ou login ao invés do token (não poderia ser o nome pois ele pode ser duplicado).

### Observações
  Os seguintes problemas foram encontrados durante a realização da tarefa, o que ocasionaram não conformidades com as regras de negócio definidas no escopo do projeto:

  - Dificuldade de trabalhar com arrays (não consegui declarar o campo horários na agenda como um array, sendo necessário criar um model de horários, o que acabou diminuindo a eficiencia do preenchimento da agenda)
  - Dificuldades de trabalhar com filtros (Ao sobrescrever o queryfilter com um filtro customizado acabou inviabilizando os filtros padrões, o que impede algumas pesquisas (especialidade e crm por exemplo))
  - Dificuldade em deploy na nuvem (mesmo sabendo que é opcional, tentei o caminho mais indicado nos tutoriais (heroku), mas o buildpack persiste em conflitos que inviabilizam o build)

### Considerações Finais
  Considerando que só usei metade do tempo disponibilizado para realização da tarefa, os requisitos mínimos foram atingidos, embora tenha plena consciencia do espaço para melhorias no projeto. Aguardo apontamentos e novas instruções para melhoria do mesmo.

