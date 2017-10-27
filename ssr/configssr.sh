Test() {
    if [ $? != 0 ]
    then
        echo "Error !"
        exit 0
    fi
}

wget http://www.djangoz.com/linux_setup_ssr/ssr
Test
sudo mv ssr /usr/local/bin
Test
sudo chmod 766 /usr/local/bin/ssr
Test
ssr install
Test
ssr config
Test
