#!/usr/bin/bash

while IFS='' read -r line || [[ -n "$line" ]]; do
    echo "processing: $line"
    cd /home/sumitkhanna/applift/publisherid/
    split -l $[ $(wc -l $line |cut -d" " -f1) * 70 / 100 ] $line
    mv xaa ../"train"$line
    mv xab ../"test"$line      
    cd ..
    python SGD.py "train"$line "WC_publisherid" "test"$line "submit"$line
done < "/home/sumitkhanna/applift/publisherid/listoffiles.txt"

while IFS='' read -r line || [[ -n "$line" ]]; do
    echo "processing: $line"
    cd /home/sumitkhanna/applift/traffictype/
    split -l $[ $(wc -l $line |cut -d" " -f1) * 70 / 100 ] $line
    mv xaa ../"train"$line
    mv xab ../"test"$line
    cd ..
    python SGD.py "train"$line "WC_traffictype" "test"$line "submit"$line   
done < "/home/sumitkhanna/applift/traffictype/listoffiles.txt"

while IFS='' read -r line || [[ -n "$line" ]]; do
    echo "processing: $line"
    cd /home/sumitkhanna/applift/campaignid/
    split -l $[ $(wc -l $line |cut -d" " -f1) * 70 / 100 ] $line
    mv xaa ../"train"$line
    mv xab ../"test"$line
    cd ..      
    python SGD.py "train"$line "WC_campaignid" "test"$line "submit"$line
done < "/home/sumitkhanna/applift/campaignid/listoffiles.txt"

while IFS='' read -r line || [[ -n "$line" ]]; do
    echo "processing: $line"
    cd /home/sumitkhanna/applift/appsitecategory/
    split -l $[ $(wc -l $line |cut -d" " -f1) * 70 / 100 ] $line
    mv xaa ../"train"$line
    mv xab ../"test"$line
    cd ..
    python SGD.py "train"$line "WC_appsitecategory" "test"$line "submit"$line
done < "/home/sumitkhanna/applift/appsitecategory/listoffiles.txt"

while IFS='' read -r line || [[ -n "$line" ]]; do
    echo "Text read from file: $line"
    cd /home/sumitkhanna/applift/appsiteid/
    split -l $[ $(wc -l $line |cut -d" " -f1) * 70 / 100 ] $line
    mv xaa ../"train"$line
    mv xab ../"test"$line
    cd ..
    python SGD.py "train"$line "WC_appsiteid" "test"$line "submit"$line
done < "/home/sumitkhanna/applift/appsiteid/listoffiles.txt"

while IFS='' read -r line || [[ -n "$line" ]]; do
    echo "processing: $line"
    cd /home/sumitkhanna/applift/traffictype/
    split -l $[ $(wc -l $line |cut -d" " -f1) * 70 / 100 ] $line
    mv xaa ../"train"$line
    mv xab ../"test"$line
    cd ..
    python SGD.py "train"$line "WC_traffictype" "test"$line "submit"$line   
done < "/home/sumitkhanna/applift/traffictype/listoffiles.txt"

while IFS='' read -r line || [[ -n "$line" ]]; do
    echo "processing: $line"
    cd /home/sumitkhanna/applift/publisherid/
    split -l $[ $(wc -l $line |cut -d" " -f1) * 70 / 100 ] $line
    mv xaa ../"train"$line
    mv xab ../"test"$line   
    cd ..   
    python SGD.py "train"$line "OW_publisherid" "test"$line "submit"$line
done < "/home/sumitkhanna/applift/publisherid/listoffiles.txt"

while IFS='' read -r line || [[ -n "$line" ]]; do
    echo "processing: $line"
    cd /home/sumitkhanna/applift/campaignid/
    split -l $[ $(wc -l $line |cut -d" " -f1) * 70 / 100 ] $line
    mv xaa ../"train"$line
    mv xab ../"test"$line  
    cd ..    
    python SGD.py "train"$line "OW_campaignid" "test"$line "submit"$line
done < "/home/sumitkhanna/applift/campaignid/listoffiles.txt"

while IFS='' read -r line || [[ -n "$line" ]]; do
    echo "processing: $line"
    cd /home/sumitkhanna/applift/appsitecategory/
    split -l $[ $(wc -l $line |cut -d" " -f1) * 70 / 100 ] $line
    mv xaa ../"train"$line
    mv xab ../"test"$line
    cd ..
    python SGD.py "train"$line "OW_appsitecategory" "test"$line "submit"$line
done < "/home/sumitkhanna/applift/appsitecategory/listoffiles.txt"

while IFS='' read -r line || [[ -n "$line" ]]; do
    echo "Text read from file: $line"
    cd /home/sumitkhanna/applift/appsiteid/
    split -l $[ $(wc -l $line |cut -d" " -f1) * 70 / 100 ] $line
    mv xaa ../"train"$line
    mv xab ../"test"$line
    cd ..
    python SGD.py "train"$line "OW_appsiteid" "test"$line "submit"$line
done < "/home/sumitkhanna/applift/appsiteid/listoffiles.txt"

