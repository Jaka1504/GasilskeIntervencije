import json
import requests
import time
from requests_html import HTMLSession

podatki_json_path = "podatki_test.json"

coerzId = [
    10014,
    10011,
    10012,
    10013,
    10015,
    10016,
    10017,
    10018,
    10019,
    10020,
    10021,
    10022,
    10023,
]
obcine = [
    11026516,
    24063526,
    21436437,
    11026524,
    21427624,
    21427632,
    11026532,
    21427659,
    11026559,
    11026567,
    11026575,
    21427667,
    11026583,
    11026591,
    11026605,
    21427675,
    11026621,
    11026630,
    11026648,
    11026656,
    21427683,
    21436445,
    11026664,
    11026672,
    11026699,
    11026702,
    11026729,
    21427691,
    11026737,
    21427705,
    11026745,
    21427713,
    11026753,
    21427721,
    11026761,
    11026770,
    11026788,
    11026796,
    11026800,
    11026818,
    24063461,
    11026826,
    11026834,
    11026842,
    21427730,
    11026869,
    21427748,
    21427756,
    21427764,
    21427772,
    11026885,
    11027709,
    11026893,
    11026907,
    11027717,
    11026915,
    11026923,
    11027725,
    21427799,
    11026931,
    11027733,
    11026940,
    11027741,
    11026958,
    11027750,
    11026966,
    11027768,
    21427802,
    11027776,
    21436453,
    21427829,
    11026974,
    11027784,
    11027792,
    21427837,
    11026982,
    11027008,
    11027806,
    11027814,
    11027016,
    11027822,
    11027024,
    11027849,
    11027032,
    11027857,
    11027059,
    24063470,
    11027865,
    11027067,
    21427845,
    11027075,
    11027873,
    11027083,
    21436461,
    11027881,
    21428019,
    11027890,
    11027091,
    11027903,
    11027105,
    21428027,
    11027911,
    24063518,
    21427853,
    11027113,
    21436470,
    11027121,
    11027130,
    11027920,
    11027148,
    11027938,
    11027946,
    11027954,
    11027156,
    11027962,
    11027164,
    21427861,
    11027172,
    11027989,
    11027199,
    11027997,
    11028004,
    11027202,
    21427870,
    11028012,
    21436488,
    21428035,
    11027229,
    21427888,
    11027237,
    21428043,
    11028039,
    11028047,
    11027245,
    11028055,
    11027253,
    11027261,
    11027270,
    11027288,
    21427896,
    24063488,
    24063453,
    11027296,
    21428051,
    11027326,
    11027318,
    11027300,
    11027334,
    21427900,
    11027342,
    11027369,
    11027377,
    11027385,
    11027393,
    11027407,
    21428060,
    21427918,
    21433632,
    11027415,
    21433659,
    21433667,
    21428078,
    21428086,
    11027423,
    24063496,
    21433675,
    11026877,
    21427926,
    11027431,
    11027440,
    11027458,
    11027466,
    24063500,
    11027474,
    11027482,
    11027504,
    11027512,
    21433683,
    11027539,
    21428264,
    11027547,
    11027555,
    21427934,
    11026613,
    11027563,
    11027571,
    11027580,
    21427942,
    21427969,
    11027598,
    11027601,
    11027610,
    21428094,
    11027628,
    21427977,
    11028063,
    11027636,
    11028071,
    11027644,
    11028080,
    21428108,
    11027652,
    11028098,
    11027679,
    11028101,
    11027687,
    21428124,
    11028128,
    21427985,
    11027695,
    21428116,
    21427993,
]
dogodekPodskupinaId = [
    10100,
    10200,
    10300,
    10400,
    10500,
    10600,
    10800,
    10900,
    11000,
    11100,
    11200,
    11300,
    11400,
    11500,
    11600,
    20100,
    20200,
    20300,
    20400,
    20500,
    20600,
    20700,
    20800,
    20900,
    30100,
    30200,
    30300,
    30400,
    40100,
    40200,
    40300,
    40400,
    40500,
    50100,
    50200,
    50300,
    60100,
    60200,
    60300,
    70100,
    70200,
    70300,
    80100,
    90100,
]
headers = {"content-type": "application/json"}
data = f'{{"limit":20000,"offset":0,"coezrId":{coerzId},"obcinaMID":{obcine},"dogodekPodskupinaId":{dogodekPodskupinaId},"datumOd":"2022-09-01T00:00:00","datumDo":"2022-10-19T00:00:00","corsBesedilo":null}}'


# To actually dela:
def pridobi_podatke(
    limit,
    offset,
    datumOd,
    datumDo,
    kategorije=coerzId,
    obcine=obcine,
    dogodki=dogodekPodskupinaId,
):
    data = f'{{"limit":{limit},"offset":{offset},"coezrId":{kategorije},"obcinaMID":{obcine},"dogodekPodskupinaId":{dogodki},"datumOd":"{datumOd}","datumDo":"{datumDo}","corsBesedilo":null}}'
    stran = requests.post(
        url="https://spin3.sos112.si/javno/PorociloApi/DnevniBilten",
        data=data,
        headers=headers,
    )
    slovar = stran.json()
    return slovar["value"]["data"]


def shrani_v_json(slovar, path):
    with open(path, "w", encoding="utf-8") as datoteka:
        json.dump(slovar, datoteka, ensure_ascii=False, indent=4)


def test():
    session = HTMLSession()
    res = session.get(
        url="https://spin3.sos112.si/javno/porocilo/dnevnibilten", headers=headers
    )
    res.html.render()

    get_urls = [
        "https://spin3.sos112.si/javno/PorociloApi/SifrantReCOObcina",
        "https://spin3.sos112.si/javno/PorociloApi/SifrantDogodek",
        "https://spin3.sos112.si/javno/PorociloApi/SifrantEZRObcina",
        "https://spin3.sos112.si/javno/PorociloApi/SifrantEZREZRVrsta",
        "https://spin3.sos112.si/javno/PorociloApi/SifrantPozarVzrok",
    ]
    for url in get_urls:
        print(f"Getting {url}...")
        session.get(url=url, headers=headers)
        time.sleep(2)
    print("Posting...")
    res = session.post(
        url="https://spin3.sos112.si/javno/PorociloApi/DnevniBilten",
        data=data,
        headers=headers,
    )
    time.sleep(5)
    print("Rendering...")
    res.html.render(reload=False)
    print("Rendering finished")

    print(res)
    print(res.html.html)
    print(len(res.html.html))


# test()
# shrani_v_json(
#     pridobi_podatke(
#         limit=20000,
#         offset=0,
#         datumOd="2010-01-01T00:00:00",
#         datumDo="2022-01-01T00:00:00",
#     ),
#     zajeti_podatki/podatki_json_path,
# )

with open(podatki_json_path, "r", encoding="utf-8") as dat:
    podatki = json.load(dat)


def ustvari_pomozni_seznam(
    ime_json_datoteke, ime_id, ime_opis, novo_ime_id, novo_ime_opis
):
    seznam_slovarjev = []
    for entry in podatki:
        if not entry[ime_id] in [
            kategorija[novo_ime_id] for kategorija in seznam_slovarjev
        ]:
            seznam_slovarjev.append(
                {novo_ime_id: entry[ime_id], novo_ime_opis: entry[ime_opis]}
            )
    shrani_v_json(
        sorted(seznam_slovarjev, key=lambda x: x[novo_ime_id]), ime_json_datoteke
    )


# ustvari_pomozni_seznam("zajeti_podatki/skupine.json", "dogodekSkupinaId", "dogodekSkupinaNaziv", "id", "ime skupine")
# ustvari_pomozni_seznam("zajeti_podatki/obcine.json", "obcinaMID", "obcinaNaziv", "id", "ime obcine")
# ustvari_pomozni_seznam("zajeti_podatki/podskupine.json", "dogodekPodskupinaId", "dogodekPodskupinaNaziv", "id", "ime podskupine")
# ustvari_pomozni_seznam("zajeti_podatki/dogodki.json", "dogodekId", "dogodekNaziv", "id", "ime dogodka")


def zajemi_vse_podatke(
    path,
    datumOd,
    datumDo,
    po_koliko_naenkrat=20000,
    offset=0,
    kategorije=coerzId,
    obcine=obcine,
    dogodki=dogodekPodskupinaId,
):
    seznam = []
    while True:
        time.sleep(10)
        seznamcek = pridobi_podatke(
            limit=po_koliko_naenkrat,
            offset=offset,
            datumOd=datumOd,
            datumDo=datumDo,
            kategorije=kategorije,
            obcine=obcine,
            dogodki=dogodki,
        )
        if not seznamcek:
            break
        seznam.extend(seznamcek)
        offset += po_koliko_naenkrat
        print(len(seznam))
    shrani_v_json(seznam, path)


# zajemi_vse_podatke(
#     path="surovi_podatki.json",
#     datumOd="2010-01-01T00:00:00",
#     datumDo="2022-01-01T00:00:00",
#     po_koliko_naenkrat=10000
# )