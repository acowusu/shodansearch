#!/bin/bash


PS3='Please enter a number to select your choice: '
options=("get my ip address" "search shodan" "scan host" "Quit")
select opt in "${options[@]}"
do
    case $opt in
        "get my ip address")
            
            echo "your ip address is "
            shodan myip

            ;;
        "search shodan")
            echo "Enter Query"
            read query
            shodan search --fields ip_str,port,org,hostnames $query
            ;;
        "scan host")
            echo "enter an ip address or host name"
            read ip
            shodan  host $ip
            ;;
        "Quit")
            break
            ;;
        *) echo "invalid option $REPLY";;
    esac
done