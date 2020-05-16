#!/bin/bash
#sudo /etc/init.d/odooRockscripts-server restart
sudo /etc/init.d/odoo_rockscripts-server restart
sudo /etc/init.d/postgresql stop
sudo /etc/init.d/postgresql restart
#sudo mv /home/rockscripts/.local/lib/python3.6/site-packages/xmlsec* /usr/local/lib/python3.6/dist-packages
#sudo /etc/init.d/odoo restart

##{"numero": "00000001", "tipoMoneda": "PEN", "receptor": {"tipo": 6, "direccion": "JR. MONTEROSA NRO. 233 INT. 904 (CHACARILLA DEL ESTANQUE)  LIMA", "nombre": "SALLY PERU HOLDINGS S.A.C.", "nro": "20549473301"}, "totalVenta": 7.6464, "emisor": {"ciudad": "LIMA", "tipo": 6, "direccion": "BENJAMIN FRANKLIN MZ. M LOT. 13", "departamento": "Chorrillos", "codigoPais": "PE", "codigoPostal": "15054","nombre": "Nekade", "nro": "20603408111"}, "serie": "F001", "sumatoriaIgv": "1.17", "fechaVencimiento": "2019-01-08", "totalVentaGravada": 6.48, "fechaEmision": "2019-01-08", "items": [{"cantidad":"1.0", "montoAfectacionIgv": 0.972, "tipoPrecioVentaUnitario": "01", "unidadMedidaCantidad": "ZZ", "valorUnitario": 5.4, "valorVenta": 5.4, "tipoAfectacionIgv": "10", "descripcion": "Ajos", "precioVentaUnitario": 6.372}, {"cantidad": "1.0", "montoAfectacionIgv": 0.19440000000000002, "tipoPrecioVentaUnitario": "01", "unidadMedidaCantidad": "ZZ", "valorUnitario": 1.08, "valorVenta": 1.08, "tipoAfectacionIgv": "10", "descripcion": "Apio", "precioVentaUnitario": 1.2744}], "horaEmision": "00:11:30"}

#CHANGE PASSWORD
#update res_users set password='$pbkdf2-sha512$25000$2RsD4Px/751zztkbY.y9Nw$pTUBP3dLAlcqsffuLW5L9o7f5fILTYPwVdaGlRQqYuhIydXnNYJSiTMfH0VhBAFWvbw026uJNjX9o.YLnmPHRQ' where login = 'vcgroup01@gmail.com';
#update res_users set create_uid = 2 where login = 'elmervr14@gmail.com';
#select login , password, active from res_users;
#select login, create_ui from res_users;
#PGPASSWORD=Productoresonline1 psql -U odoo -d ecomerce

# git config --global user.email "rockscripts@gmail.com"
# git config --global user.name "rockscripts"
# git pull
# git add .
# git commit -m 'init'
# git push

# sudo systemctl stop nginx 
# sudo service apache2 start
# https://parikshitvaghasiya.blogspot.com/2018/08/change-to-port-80-instead-of-8069-odoo.html

#pingf(){
#    if ping -w 2 -q -c 1 192.168.1."$1" > /dev/null ;
#    then 
#        printf "IP %s is up\n" 192.168.1."$1"
#    fi
#}
#
#main(){
#
#    NUM=1
#    while [ $NUM -lt 255  ];do 
#        pingf "$NUM" &
#        NUM=$(expr "$NUM" + 1)
#    done
#    wait
#}
#
#main