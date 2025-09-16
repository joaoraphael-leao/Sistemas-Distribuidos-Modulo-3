from flask import Flask, request, jsonify
import requests

# Configuração base do Flask
def create_app():
    app = Flask(__name__)
    return app

# Imports comuns que podem ser reutilizados
__all__ = ['Flask', 'request', 'jsonify', 'requests', 'create_app']