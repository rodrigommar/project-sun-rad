from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from  dotenv import load_dotenv
from urllib.parse import quote_plus
import os
import json



def connect_mongodb():
    
    load_dotenv()
    
    username = os.getenv('USER_NAME')
    password = os.getenv('PASSWORD')
    cluster_name = os.getenv('CLUSTER_NAME')
    id_host = os.getenv('ID_HOST')
    schema = os.getenv('SCHEMA')


    escaped_username = quote_plus(username)
    escaped_password = quote_plus(password)

    uri =  f"{schema}://{escaped_username}:{escaped_password}@{cluster_name}.{id_host}"


    try:
        client = MongoClient(uri, server_api=ServerApi('1'))
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        return client
    
    except Exception as e:
        print(e)



def verifica_se_db_existe(client, db_name):
    
    try:      
        db_list = client.list_database_names()
        
        if db_name in db_list:
            print('Banco de Dados existe')
            return True
        else:    
            print('Banco de Dados NÃO Existe')
            return False
    
    except Exception as e:       
        print(f"Erro ao verificar a existência do banco de dados: {e}")



def create_db(client, db_name):
    
    try:
        
        if not verifica_se_db_existe(client, db_name):
            db = client[db_name]
            print(f"Banco de dados '{db_name}' criado com sucesso.")
            return db
        
        else:
            return client[db_name]
        
    except Exception as e:     
        print(f"Erro ao criar banco de dados: {e}")
        return None
     
    


def verifica_se_collection_existe(db, collection_name):
    
    try:
        
        collections = db.list_collection_names()
    
        if collection_name in collections:
            print(f"A coleção '{collection_name}' existe.")
            return True
        else:
            print(f"A coleção '{collection_name}' NÃO existe.")
            return False
        
    except Exception as e:
        print(f"Erro ao verificar existência da coleção de documentos: {e}")
        return None
        
    
    

def create_collection(db, collection_name):
    
    try:
        if not verifica_se_collection_existe(db, collection_name):
            db.create_collection(collection_name)
            print(f"Coleção '{collection_name}' criada com sucesso.")
        
        return db[collection_name]
        
    except Exception as e:
        print(f'Erro ao criar uma coleção de documentos: {e}')
        return None
    



def ler_dados_de_arquivo_json(path_file):
    
    try:
        with open(path_file, 'r') as f:
            dados_json = json.load(f)
            print('Leitura Concluída!')
        return dados_json
    
    except FileNotFoundError:
        print(f"Erro: O arquivo '{path_file}' não foi encontrado.")
        return None
    
    except json.JSONDecodeError as e:
        print(f"Erro de decodificação JSON em '{path_file}': {e}")
        return None
    
    except Exception as e:
        print(f"Erro ao ler o arquivo '{path_file}': {e}")
        return None
        
        

    
def salvar_dados_no_mongodb(data_json, db_nome, colecao_nome, client):
    
    if client:
        
        try:
            if verifica_se_db_existe(client, db_nome) and verifica_se_collection_existe(client[db_nome], colecao_nome):               
                db = client[db_nome]
                colecao = db[colecao_nome]
                resultado = colecao.insert_many(data_json)
                num_docs_inseridos = len(resultado.inserted_ids)
                print(f'Total de Documentos salvos na coleção {colecao_nome}: {num_docs_inseridos}.')
        
        except Exception as e:
            print(f'Erro ao salvar dados no MongoDB: {e}')



if __name__ ==  '__main__':
    
    connection = connect_mongodb()
    
    #dados_json = ler_dados_de_arquivo_json('/home/noah/Documentos/project-sun-rad/data_raw/estacoes_automaticas.json')
    #verifica_se_collection_existe(connection['db-climate'], 'stations')
    #salvar_dados_no_mongodb(dados_json, 'db-climate', 'stations', connection)
    
    #verifica_se_db_existe(connection, 'db-climate')
    #create_db(connection, 'db-climate')
    #verifica_se_collection_existe(connection['db-climate'], 'stations')
    #create_collection(connection['db-climate'], 'stations')
    