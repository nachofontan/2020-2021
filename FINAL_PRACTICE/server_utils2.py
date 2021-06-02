import http.client
import json
import server_utils2 as su
from Seq02 import Seq


def species_name(limit_number):
    SERVER = "rest.ensembl.org"
    ENDPOINT = "/info/species/"
    PARAMS = "?content-type=application/json"

    connection = http.client.HTTPConnection(SERVER)
    connection.request("GET", ENDPOINT + PARAMS)

    response = connection.getresponse()
    print(response.status, response.reason)

    answer_decoded = response.read().decode()
    dict_response = json.loads(answer_decoded)
    species = (dict_response["species"])
    total = len(species)
    llist = []
    for n in range(0,limit_number):
        species_1 = species[n]
        name = species_1["display_name"]
        llist.append(name)
    names = llist


    context = {"number_of_species": limit_number,"species_name": names, "total_species": total}
    content = su.read_template_html_file("./html/list_species.html").render(context=context)
    return content

def karyotype(specie):
    SERVER = "rest.ensembl.org"
    ENDPOINT = "/info/assembly/"
    PARAMS = "?content-type=application/json"

    connection = http.client.HTTPConnection(SERVER)
    connection.request("GET", ENDPOINT + str(specie) + PARAMS)

    response = connection.getresponse()
    print(response.status, response.reason)

    answer_decoded = response.read().decode()
    dict_response = json.loads(answer_decoded)
    karyotype = dict_response["karyotype"]
    context = {"species_karyotype": karyotype, "specie_name": specie}
    content = su.read_template_html_file("./html/karyotype.html").render(context=context)
    return content
def chromosmes(specie, number):
    SERVER = "rest.ensembl.org"
    ENDPOINT = "/info/assembly/"
    PARAMS = "?content-type=application/json"

    connection = http.client.HTTPConnection(SERVER)
    connection.request("GET", ENDPOINT + str(specie) + PARAMS)

    response = connection.getresponse()
    print(response.status, response.reason)

    answer_decoded = response.read().decode()
    dict_response = json.loads(answer_decoded)
    karyotipe = dict_response["top_level_region"]
    for n in range(0, len(karyotipe)):
        dictt_chromosomes = (karyotipe[n])
        for key, values in dictt_chromosomes.items():
            listt = []
            if key == "name":
                listt.append(dictt_chromosomes)
                if values == number:
                    length = dictt_chromosomes["length"]

    context = {"specie": specie, "length_chromosome": length, "number": number}
    content = su.read_template_html_file("./html/chromosome.html").render(context=context)
    return content

def geneSeq(gene,genes_dict):
    SERVER = "rest.ensembl.org"
    ENDPOINT = "/sequence/id/"
    PARAMS = "?content-type=application/json"

    ID = genes_dict[gene]
    connection = http.client.HTTPConnection(SERVER)
    connection.request("GET", ENDPOINT + ID + PARAMS)

    response = connection.getresponse()
    print(response.status, response.reason)

    answer_decoded = response.read().decode()
    dict_response = json.loads(answer_decoded)

    sequence = dict_response["seq"]
    context = {"gene": gene, "sequence": sequence}
    content = su.read_template_html_file("./html/geneSeq.html").render(context=context)
    return content

def infoSeq(gene, genes_dict):
    SERVER = "rest.ensembl.org"
    ENDPOINT = "/sequence/id/"
    PARAMS = "?content-type=application/json"

    ID = genes_dict[gene]
    connection = http.client.HTTPConnection(SERVER)
    connection.request("GET", ENDPOINT + ID + PARAMS)

    response = connection.getresponse()
    print(response.status, response.reason)

    answer_decoded = response.read().decode()
    dict_response = json.loads(answer_decoded)
    idd = dict_response["id"]
    desc = dict_response["desc"]
    chromosome_name = desc.split(":")[1]
    start = desc.split(":")[3]
    end = desc.split(":")[4]
    lenght = (int(end) - int(start))


    context = {"gene": gene, "id": idd, "chromosome_name": chromosome_name, "start": start, "end": end, "lenght": lenght}
    content = su.read_template_html_file("./html/infoSeq.html").render(context=context)
    return content

def lengthSeq(gene, genes_dict):
    SERVER = "rest.ensembl.org"
    ENDPOINT = "/sequence/id/"
    PARAMS = "?content-type=application/json"

    ID = genes_dict[gene]
    connection = http.client.HTTPConnection(SERVER)
    connection.request("GET", ENDPOINT + ID + PARAMS)

    response = connection.getresponse()
    print(response.status, response.reason)

    answer_decoded = response.read().decode()
    dict_response = json.loads(answer_decoded)
    sequence = Seq(dict_response["seq"])
    length = sequence.len()

    context = {"length": length, "gene": gene}
    content = su.read_template_html_file("HTML/lengthCalc.html").render(context=context)
    return content
def percentageSeq(gene, genes_dict):
    SERVER = "rest.ensembl.org"
    ENDPOINT = "/sequence/id/"
    PARAMS = "?content-type=application/json"

    ID = genes_dict[gene]
    connection = http.client.HTTPConnection(SERVER)
    connection.request("GET", ENDPOINT + ID + PARAMS)

    response = connection.getresponse()
    print(response.status, response.reason)

    answer_decoded = response.read().decode()
    dict_response = json.loads(answer_decoded)
    sequence = Seq(dict_response["seq"])
    lenght = sequence.len()
    a, c, g, t = sequence.percentage(sequence.count_bases(), lenght)

    context = {"A": a, "C": c, "G": g, "T": t, "gene":gene}
    content = su.read_template_html_file("HTML/percentageCalc.html").render(context=context)
    return content







