"""Guarda (ou repõe) a pasta de trabalho encriptada no repositório das páginas, para sobreviver ao fim do contentor.
  PAGE_PW=... python3 tools/snapshot.py save     -> /home/user/pedromja.github.io/_src/carros-work.tar.gz.enc
  PAGE_PW=... python3 snapshot.py restore <ficheiro.enc> <destino>"""
import os,sys,io,tarfile,base64
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
def key(pw,salt): return PBKDF2HMAC(hashes.SHA256(),32,salt,600000).derive(pw.encode())
pw=os.environ['PAGE_PW']
if sys.argv[1]=='save':
    W=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); out='/home/user/pedromja.github.io/_src/carros-work.tar.gz.enc'
    buf=io.BytesIO()
    with tarfile.open(fileobj=buf,mode='w:gz') as t: t.add(W,arcname='carros-work',filter=lambda ti: None if ti.name.endswith(('_full.html','.log')) else ti)
    salt=os.urandom(16); iv=os.urandom(12); os.makedirs(os.path.dirname(out),exist_ok=True)
    open(out,'wb').write(salt+iv+AESGCM(key(pw,salt)).encrypt(iv,buf.getvalue(),None)); print(out,os.path.getsize(out))
else:
    b=open(sys.argv[2],'rb').read(); salt,iv,ct=b[:16],b[16:28],b[28:]
    with tarfile.open(fileobj=io.BytesIO(AESGCM(key(pw,salt)).decrypt(iv,ct,None)),mode='r:gz') as t: t.extractall(sys.argv[3],filter='data')
    print('reposto em',sys.argv[3])
