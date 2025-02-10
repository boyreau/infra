#!/bin/sh

if [ ! -f /usr/bin/gitea ]
then
	# Binary download
	wget -O gitea https://dl.gitea.com/gitea/1.23.1/gitea-1.23.1-linux-amd64
	chmod +x gitea
	
	# Binary signature check
	gpg --keyserver keys.openpgp.org --recv 7C9E68152594688862D62AF62D9AE806EC1592E2
	gpg --verify gitea-1.23.1-linux-amd64.asc gitea-1.23.1-linux-amd64
	
	cp gitea /usr/bin/gitea
fi

# Expected directory structure
if [ ! -d /var/lib/gitea ]
then
	mkdir -p /var/lib/gitea/{custom,data,log}
	chown -R git:git /var/lib/gitea/
	chmod -R 750 /var/lib/gitea/
fi

if [ ! -d /etc/gitea ]
then
	mkdir -p /etc/gitea
	chown root:git /etc/gitea
	chmod 770 /etc/gitea
fi

