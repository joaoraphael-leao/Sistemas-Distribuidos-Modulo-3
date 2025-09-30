#!/usr/bin/env python3

import subprocess
import os
import sys

def generate_grpc_files():
    """Gera os arquivos Python a partir dos arquivos .proto"""
    
    # Muda para o diretório dos protos
    proto_dir = os.path.join("grpc_services", "protos")
    output_dir = "grpc_services"
    
    if not os.path.exists(proto_dir):
        print(f"Erro: Diretório {proto_dir} não encontrado!")
        return False
    
    # Comando para gerar os arquivos
    cmd = [
        sys.executable, "-m", "grpc_tools.protoc",
        f"--python_out={output_dir}",
        f"--grpc_python_out={output_dir}",
        f"-I{proto_dir}",
        os.path.join(proto_dir, "services.proto")
    ]
    
    try:
        print("Gerando arquivos gRPC...")
        subprocess.run(cmd, check=True)
        print("Arquivos gRPC gerados com sucesso!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Erro ao gerar arquivos gRPC: {e}")
        return False

if __name__ == "__main__":
    generate_grpc_files()