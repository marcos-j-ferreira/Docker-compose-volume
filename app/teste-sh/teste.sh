#!/bin/bash


URL="http://127.0.0.1:5000/"
V=2

for i in $(seq 1)
do 
    echo "-- Testando o GET -- Vez: $i "
    curl -s $URL
    echo " "
done


for i in $(seq 1 $V)
do 
    echo "-- Testando POSt itens - Vez: $i"
    curl -s -X POST "$URL/items/add" \
    -H "Content-Type: application/json" \
    -d '{"id": 10, "name": "coffe", "price": 9.20}'
done

for i in $(seq 1 $V)
do
    echo "-- Testando GET itens - Vez: $i "
    curl -s $URL/items
    echo " "
done