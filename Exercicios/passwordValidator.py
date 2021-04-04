import re


# Usar o website https://regex101.com para construir expressões

regex = r"[a-zA-Z0-9$%&@]{8,}\d"

string = "sfsdlfksdn%90"

padrao = re.compile(r"[a-zA-Z0-9$%&@]{8,}\d")

match = padrao.fullmatch(string)


if match:
    print("ok")
