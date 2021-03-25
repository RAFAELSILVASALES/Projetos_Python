import speedtest
r= speedtest.Speedtest()
servers = r.get_servers() 
r.get_best_server() 
r.download(threads=None)
r.upload(threads=None, pre_allocate=True)
print(r.results.share())







# servers = r.get_servers().  essa linha vai pegar 49 servidores no speedtest.

# r.get_best_server(). essa linha vai Retorna o servidor mais próximo,
# aquele com a menor distância.

# r.download(threads=None).  essa é a função que  executam os testes de download
#| O argumento
# threads=None determina o número de threads a serem usados ​​para o teste.
# Por padrão, é Nenhum, o que significa que o servidor speedtest.net
#decide quantos threads usar.

# threads= linha ou encadeamento de execução.

#r.upload(threads=None, pre_allocate=True). teste de upload.
# pre_allocate=True vai alocar os dados na memoria. para não alocar basta troca
# True por False.

# r.results.share(). vai requisitar o resutado do teste para o speedtest.


