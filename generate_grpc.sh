#!/bin/bash

# Script para gerar os arquivos Python a partir dos arquivos .proto

cd grpc_services/protos

# Gerar os arquivos Python
python -m grpc_tools.protoc --python_out=.. --grpc_python_out=.. -I. services.proto

echo "Arquivos gRPC gerados com sucesso!"