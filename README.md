# Vacinação

Mesmo diante desse cenário de pandemia, a população, principalmente as crianças, não devem 

deixar de se imunizar e manter a vacinação de rotina em dia. Essa é a recomendação das 

principais instituições mundiais de saúde.




----------------------------------------------------------------



# POST /vaccinations - Esta rota fará o cadastro do cartão de vacina:


  ### Corpo da requisição:

    {
        "cpf": "01234567891",
        "name": "Chrystian",
        "vaccine_name": "Pfizer",
        "health_unit_name": "Santa Rita"
    }


  ### Resposta da requisição:

    {
        "cpf": "01234567891",
        "name": "Chrystian",
        "first_shot_date": "Tue, 26 Apr 2022 18:31:33 GMT",
        "second_shot_date": "Mon, 25 Jul 2022 18:31:33 GMT",
        "vaccine_name": "Pfizer",
        "health_unit_name": "Santa Rita"
    }



----------------------------------------------------------------


# GET /vaccinations - Esta rota retornará todos os cartões de vacina:

### Resposta da requisição:

    [
        {
            "cpf": "01234567891",
            "name": "Chrystian",
            "first_shot_date": "Fri, 29 Oct 2021 16:30:31 GMT",
            "second_shot_date": "Thu, 27 Jan 2022 16:30:31 GMT",
            "vaccine_name": "Pfizer",
            "health_unit_name": "Santa Rita"
        },
        {
            "cpf": "19876543210",
            "name": "Cauan",
            "first_shot_date": "Fri, 29 Oct 2021 16:31:30 GMT",
            "second_shot_date": "Thu, 27 Jan 2022 16:31:30 GMT",
            "vaccine_name": "Coronavac",
            "health_unit_name": "Santa Rita"
        },
        {
            "cpf": "54221194161",
            "name": "Eduardo",
            "first_shot_date": "Fri, 29 Oct 2021 16:35:24 GMT",
            "second_shot_date": "Thu, 27 Jan 2022 16:35:24 GMT",
            "vaccine_name": "Coronavac",
            "health_unit_name": "Santa Rita"
        }
    ]