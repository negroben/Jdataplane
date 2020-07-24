import requests,base64,json
puerto="5555"
usuario="dataplane"
passwd="negro2004"
haproxy="161.35.60.108"
frontend="http-in"
aplicacion = "aplicacion"




#PASO 1: Obtengo version y genero un id de transaccion

#obtengo nueva version
uri = "http://" + haproxy+ ":" + puerto + "/v2/services/haproxy/configuration/global"
response = requests.get(uri,auth=(usuario, passwd))
json_data = response.json()
version=str(json_data['_version'])

#Obtengo nuevo id de transaccion
uri_id = "http://" + haproxy+ ":" + puerto + "/v2/services/haproxy/transactions?version=" + version
response_id = requests.post(uri_id,auth=(usuario, passwd))
json_data_id = response_id.json()
id=str(json_data_id['id'])

#genero acl para cambiar estado sitio "Actualizando"
url_acl = "http://" + haproxy+ ":" + puerto + "/v2/services/haproxy/configuration/http_request_rules?parent_type=frontend&parent_name=" + frontend+ "transaction_id=" + id

datos = {
    "cond_test":  "{ path_beg / " + aplicacion + " }",
    "deny_status":  400,
    "type":  "deny",
    "cond":  "if",
    "index":  0
}
acls = requests.post(uri_id,auth=(usuario, passwd),json=(datos))

#Hago Commit de la ACL

url_commit = "http://" + haproxy+ ":" + puerto + "/v2/services/haproxy/transactions/" + id
commit = requests.put(url_commit,auth=(usuario, passwd))

print(version)
print(id)
print(url_acl)
print(datos)
print(acls)
print(commit)

