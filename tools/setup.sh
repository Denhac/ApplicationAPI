mkdir /etc/systemd/system/httpd.service.d
echo -e "[Service]\nPrivateTmp=no" > /etc/systemd/system/httpd.service.d/privatetmp.conf
systemctl daemon-reload
apachectl restart
systemctl show httpd | grep PrivateTmp



pip install aws
pip install --upgrade aws
