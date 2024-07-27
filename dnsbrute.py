import dns.resolver

res = dns.resolver.Resolver()
res.timeout = 0.1  
res.lifetime = 0.1
with open("/home/kali/solyd_pentest/subdomains-top1mil-20000.txt", "r") as arq:
    sub_domain = arq.read().splitlines() 

alvo = "bancocn.com"

for subdomains in sub_domain:
    try:
        sub_alvo = subdomains + "." + alvo
        result = res.resolve(sub_alvo, "A")  
        for ip in result:
            print("IP do alvo: {} é: {} ".format(sub_alvo, ip))
    except:
        pass

 