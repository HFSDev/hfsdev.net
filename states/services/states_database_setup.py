from states.models import State
from states.models import Region

def setup_database():
    """
    Sets the states app database ready. It creates all states and regions, but
    leaves cities blank.
    """
    State.objects.all().delete()
    Region.objects.all().delete()

    regionN = Region()
    regionN.name = "Norte"
    regionN.abbreviation = "N"
    regionN.save()
    regionNE = Region()
    regionNE.name = "Nordeste"
    regionNE.abbreviation = "NE"
    regionNE.save()
    regionS = Region()
    regionS.name = "Sul"
    regionS.abbreviation = "S"
    regionS.save()
    regionCO = Region()
    regionCO.name = "Centro-Oeste"
    regionCO.abbreviation = "CO"
    regionCO.save()
    regionSE = Region()
    regionSE.name = "Sudeste"
    regionSE.abbreviation = "SE"
    regionSE.save()


    state = State()
    state.name = "Amazonas ".strip()
    state.region = regionN
    state.abbreviation = "AM"
    state.save()

    state = State()
    state.name = "Roraima  ".strip()
    state.region = regionN
    state.abbreviation = "RR"
    state.save()

    state = State()
    state.name = "Amapá    ".strip()
    state.region = regionN
    state.abbreviation = "AP"
    state.save()

    state = State()
    state.name = "Pará     ".strip()
    state.region = regionN
    state.abbreviation = "PA"
    state.save()

    state = State()
    state.name = "Tocantins".strip()
    state.region = regionN
    state.abbreviation = "TO"
    state.save()

    state = State()
    state.name = "Rondônia ".strip()
    state.region = regionN
    state.abbreviation = "RO"
    state.save()

    state = State()
    state.name = "Acre     ".strip()
    state.region = regionN
    state.abbreviation = "AC"
    state.save()


    state = State()
    state.name = "Maranhão           ".strip()
    state.abbreviation = "MA"
    state.region = regionNE
    state.save()

    state = State()
    state.name = "Piauí              ".strip()
    state.abbreviation = "PI"
    state.region = regionNE
    state.save()

    state = State()
    state.name = "Ceará              ".strip()
    state.abbreviation = "CE"
    state.region = regionNE
    state.save()

    state = State()
    state.name = "Rio Grande do Norte".strip()
    state.abbreviation = "RN"
    state.region = regionNE
    state.save()

    state = State()
    state.name = "Pernambuco         ".strip()
    state.abbreviation = "PE"
    state.region = regionNE
    state.save()

    state = State()
    state.name = "Paraíba            ".strip()
    state.abbreviation = "PB"
    state.region = regionNE
    state.save()

    state = State()
    state.name = "Sergipe            ".strip()
    state.abbreviation = "SE"
    state.region = regionNE
    state.save()

    state = State()
    state.name = "Alagoas            ".strip()
    state.abbreviation = "AL"
    state.region = regionNE
    state.save()

    state = State()
    state.name = "Bahia              ".strip()
    state.abbreviation = "BA"
    state.region = regionNE
    state.save()


    state = State()
    state.name = "Mato Grosso       ".strip()
    state.abbreviation = "MT"
    state.region = regionCO
    state.save()

    state = State()
    state.name = "Mato Grosso do Sul".strip()
    state.abbreviation = "MS"
    state.region = regionCO
    state.save()

    state = State()
    state.name = "Goiás             ".strip()
    state.abbreviation = "GO"
    state.region = regionCO
    state.save()

    state = State()
    state.name = "Distrito Federal  ".strip()
    state.abbreviation = "DF"
    state.region = regionCO
    state.save()

    state = State()
    state.name = "São Paulo         ".strip()
    state.abbreviation = "SP"
    state.region = regionSE
    state.save()

    state = State()
    state.name = "Rio de Janeiro    ".strip()
    state.abbreviation = "RJ"
    state.region = regionSE
    state.save()

    state = State()
    state.name = "Espírito Santo    ".strip()
    state.abbreviation = "ES"
    state.region = regionSE
    state.save()

    state = State()
    state.name = "Minas Gerais      ".strip()
    state.abbreviation = "MG"
    state.region = regionSE
    state.save()

    state = State()
    state.name = "Paraná            ".strip()
    state.abbreviation = "PR"
    state.region = regionS
    state.save()

    state = State()
    state.name = "Rio Grande do Sul ".strip()
    state.abbreviation = "RS"
    state.region = regionS
    state.save()

    state = State()
    state.name = "Santa Catarina    ".strip()
    state.abbreviation = "SC"
    state.region = regionS
    state.save()