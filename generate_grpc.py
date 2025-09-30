#!/usr/bin/env python3

import subprocess
import os
import sys

def generate_grpc_files():
    """Gera os arquivos Python a partir dos arquivos .proto"""
    
    # Muda para o diretório dos protos
    proto_dir = os.path.join("grpc_services", "protos")
    output_dir = "grpc_services"
    proto_file = os.path.join(proto_dir, "services.proto")
    
    if not os.path.exists(proto_dir):
        print(f"ERRO: Diretório {proto_dir} não encontrado!")
        return False
    
    if not os.path.exists(proto_file):
        print(f"ERRO: Arquivo {proto_file} não encontrado!")
        return False
    
    # Comando para gerar os arquivos
    cmd = [
        sys.executable, "-m", "grpc_tools.protoc",
        f"--python_out={output_dir}",
        f"--grpc_python_out={output_dir}",
        f"--proto_path={proto_dir}",
        proto_file
    ]
    
    try:
        print("Gerando arquivos gRPC...")
        print(f"   Proto: {proto_file}")
        print(f"   Output: {output_dir}")
        
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        
        print("SUCCESS: Arquivos gRPC gerados com sucesso!")
        print("   - services_pb2.py")
        print("   - services_pb2_grpc.py")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"ERRO ao gerar arquivos gRPC: {e}")
        if e.stderr:
            print(f"   Detalhes: {e.stderr}")
        return False

if __name__ == "__main__":
    generate_grpc_files()