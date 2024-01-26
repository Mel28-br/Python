cid = input("Nome da Cidade(s): ").lower

if any(religious_name in cid for religious_name in ["João", "lucas", "mateus","santos","santo","são"]):
    print("Essa Cidade contém SANTO no nome")

else:
    print("Essa Cidade não contém SANTOS no nome")