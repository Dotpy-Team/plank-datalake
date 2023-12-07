import os 
import shutil

def delete_pycache(root_dir):
    for root, dirs, files in os.walk(root_dir):
        for dir in dirs:
            if dir in ('__pycache__','migrations'):
                pycache_path = os.path.join(root, dir)
                shutil.rmtree(pycache_path)
                print(f'Deleted: {pycache_path}')

        for file in files:
            if file.endswith('.sqlite3') or file.endswith('.db'):
                db_path = os.path.join(root, file)
                os.remove(db_path)
                print(f'Deleted: {db_path}')

if __name__ == "__main__":
    projeto_django_path = os.getcwd()    
    delete_pycache(projeto_django_path)
